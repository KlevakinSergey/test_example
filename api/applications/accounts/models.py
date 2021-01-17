import jwt

from django.conf import settings
from django.template.loader import render_to_string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

from .managers import UserManager
from .agents import EmailAgent


class User(AbstractBaseUser, PermissionsMixin):
    last_login = None
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField('Created at', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    def send_activation_email(self, host):
        code = jwt.encode({'id': self.id}, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        context = {
            'email': self.email,
            'confirm_url': f'https://{host}/?activate={code}',
        }
        email_html_message = render_to_string('email/email_verification.html', context)
        email_plaintext_message = render_to_string('email/email_verification.txt', context)

        agent = EmailAgent(
            from_email='test@gmail.com',
            to_emails=[self.email],
            subject='Email verification',
            html_content=email_html_message,
            message=email_plaintext_message,
        )
        return agent.send_email()

    def save(self, *args, **kwargs):
        if not self.email:
            raise ValueError('User must have an email')

        super(User, self).save(*args, **kwargs)


class Profile(models.Model):

    GENDER_CHOICES = (

        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, 'Prefer not to say (default option)'),

    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=4)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.full_name}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

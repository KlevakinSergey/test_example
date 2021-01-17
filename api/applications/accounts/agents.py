from django.core.mail import send_mail


class EmailAgent:
    def __init__(self, from_email, to_emails, subject, html_content, message):
        self.from_email = from_email
        self.to_emails = to_emails
        self.subject = subject
        self.html_content = html_content
        self.message = message

    def send_email(self):

            send_mail(
                self.subject,
                self.message,
                self.from_email,
                self.to_emails,
                html_message=self.html_content,
                fail_silently=False,
            )
            return True

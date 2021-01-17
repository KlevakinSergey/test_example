from django.shortcuts import render
from django.conf import settings

from .forms import ApplicationForm
from .tasks import send_email_contact
from .models import Layout


def index(request):
    layouts = Layout.objects.all()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            text = form.cleaned_data['text']
            data = f'Имя: {name}\n\nНомер телефона: {phone_number}\n\nКомментарий: {text}'
            send_email_contact.delay('Заявка на звонок', data, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            form.save()
    else:
        form = ApplicationForm()

    return render(request, 'index.html', locals())

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def send_contact_mail(contact):

    context = {
        'name': contact.name,
        'message': contact.text
    }

    template = get_template('email.html')
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject='formular contact',
        body=content,
        to=[contact.email],
    )
    mail.content_subtype = 'html'
    mail.send()
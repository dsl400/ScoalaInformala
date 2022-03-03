

from django import forms

from contact.models import Contact
from utils.email import send_contact_mail


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    text = forms.CharField(
        max_length=1000,
        widget=forms.Textarea,
    )

    def save(self,*args, **kwargs):
        contact = super(ContactForm, self).save(*args,**kwargs)
        send_contact_mail(contact)
        return contact
    
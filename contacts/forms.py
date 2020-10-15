from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('last_name', 'first_name', 'patronymic', 'date_of_birth', 'phone', 'email', 'social_page_networks',
                  'deck')
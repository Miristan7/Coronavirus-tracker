from django.db import models

from django.forms import ModelForm, Textarea, TextInput

class Contact(models.Model):
    STATUS = {
        (1, 'Now'),
        (2, 'Read'),
    }
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сообщение из контактной формы"
        verbose_name_plural = "Сообщения из контактной формы"

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Ваше имя'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Тема'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Ваше сообщение'})
        }


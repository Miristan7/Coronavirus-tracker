from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import ContactForm, Contact


def contact(request):
    return render(request, 'main/contactPage.html')


def contact_form(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contactdata = Contact()
			contactdata.name = form.cleaned_data['name']
			contactdata.email = form.cleaned_data['email']
			contactdata.subject = form.cleaned_data['subject']
			contactdata.message = form.cleaned_data['message']
			contactdata.save()

			messages.success(request, "Спасибо, ваше сообщение было отправлено.")
			return HttpResponseRedirect('/contact/')
	else:
		form = ContactForm()
	return render(request, 'main/contactPage.html', {'form': form})


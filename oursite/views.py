from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(request.POST)
            print (form.cleaned_data['email'])
            form.save()
            # redirect to a new URL:
            return render(request, 'oursite/thanks.html')
    else:
        form = RegisterForm()
        context = {'form' : form}
        template = 'oursite/contact.html'
        return render(request, template, context)
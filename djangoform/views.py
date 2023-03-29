from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
            form = ContactForm()
    return render(request, 'contact.html', {'form': form})

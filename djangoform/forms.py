from django import forms

class ContactForm(forms.Form):
    Name=forms.CharField(max_length=100,help_text="Enter your name")
    Email=forms.EmailField(help_text="Enter your email")
    file=forms.FileField()
    Message=forms.CharField(widget=forms.Textarea,help_text="Enter your message")

from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Type something"}))

def clean_email(self):
    email = self.cleaned_data.get("email")
    if not "gmail.com" in email:
        raise forms.ValidationException("Email must be gmail")
    return email

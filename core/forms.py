from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=255, required=True)
    email = forms.EmailField(label='Your email', required=True)
    phone = forms.CharField(label='Your Phone', required=False, max_length=255)
    message = forms.CharField(widget=forms.Textarea, required=True)


class SubscriberForm(forms.Form):
    unsubscribe_key = forms.UUIDField(required=True)


class NewSubscriberForm(forms.Form):
    email = forms.EmailField(label='Your email', required=True)

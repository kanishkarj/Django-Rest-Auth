from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from .models import User
from django.http import HttpResponse
import time

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp)) +  six.text_type(user.is_active)

account_activation_token = AccountActivationTokenGenerator()

def sendActivationMail(user):
    message = render_to_string('acc_active_email.html', {
                    'user':user, 
                    'domain':"localhost:8000",
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
    mail_subject = 'Activate your account.'
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send() 

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()        
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
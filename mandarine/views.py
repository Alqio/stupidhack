from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mandarine.models import UserProfile
from django.db import IntegrityError
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.core import mail


def login_user(request):
    """
    Takes care of logging users in with Django's own login functionalities.
    """
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')

    print("Login failed!")    
    return render(request, 'mandarine/login.html')


def signup_user(request):
    """
    Creates a new user to the database, using UserProfile model and the form found in
    templates/webstore/signup.html.
    """
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'mandarine/signup.html',
                          {"message": "Username '" +
                           username + "' is already taken"})
        user.is_active = False
        user.save()
        mail_subject = 'Activate your account'
        message = render_to_string('webstore/email.html', {
            'user': user,
            'domain': get_current_site(request).domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        connection = mail.get_connection()
        connection.open()

        email_message = mail.EmailMessage(
            mail_subject, message, 'support@webstore.com',
            [email, ], connection=connection)
        email_message.send()
        connection.close()

        profile = UserProfile.objects.create(user=user)
        if request.POST.get('admin', False):
            profile.is_admin = True
        else:
            profile.is_admin = False
        profile.save()
        return render(request, 'mandarine/verify.html')
    return render(request, 'mandarine/signup.html')


@login_required(login_url='/login')
def logout_user(request):
    """
    Logs the user out with Django's default logout functionality.
    """
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    """
    Activates an account, and sends a verification mail.
    """
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')


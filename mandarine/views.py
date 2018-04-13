from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mandarine.models import (UserProfile, Mandarin)
import random
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


def generate_data_from_values(values):
    """
    generates a list of random values from a list of pairs that contain
    lowest possible roll and highest possible roll
    """

    def rand(b, t):
        return round(random.uniform(b, t), 2)

    return list(map(lambda x: rand(x[0], x[1]), values))


def generate_good_data(sample_count):
    """
    Creates as many arrays containing generated values of data as mentioned in sample_count.
    This method creates data that could be considered "good"
    """
    m = Mandarin()
    fields = list(m.__dict__.keys())[2:]
    values = \
        [(1.75, 4), (2, 4), (1.75, 3.25), (2, 4), (3, 4), (4, 5),
         (2, 4), (2, 3), (4.5, 5), (1, 1.5), (1, 1.25),
         (1, 1), (3, 4), (4, 5), (1, 2), (1, 1.5), (1, 4),
         (1, 1.05), (3, 5), (3, 5), (3, 5), (2.5, 3.5),
         (1, 2.5), (1, 2), (1, 2), (4, 5)]
    data = []
    for i in range(sample_count):
        sample_data = generate_data_from_values(values)
        data.append(dict(list(zip(fields, sample_data))))
    return data


def generate_bad_data(sample_count):
    """
    Creates as many arrays containing generated values of data as mentioned in sample_count.
    This method creates data that could be considered "bad"
    """
    m = Mandarin()
    fields = list(m.__dict__.keys())[2:]
    values = \
        [(1, 5), (1, 3.5), (1, 3.25), (2, 5), (1, 4), (1, 3),
         (3, 5), (1, 5), (1, 4.5), (1, 5), (3, 5),
         (1.5, 5), (1, 3.5), (2.5, 4), (1, 3), (3, 5), (1, 4),
         (1.05, 4), (2, 4), (2, 4), (2, 4), (2.5, 4),
         (2, 5), (1, 5), (3, 5), (0, 2)]
    data = []
    for i in range(sample_count):
        sample_data = generate_data_from_values(values)
        data.append(dict(list(zip(fields, sample_data))))
    return data


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

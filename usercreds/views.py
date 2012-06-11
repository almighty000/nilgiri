# Software License Agreement (BSD License)
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Imran Hossain Shaon mdshaonimran@gmail.com

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from usercreds.models import Credentials
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django import http

def submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if (username == None):
        return HttpResponseRedirect('/')

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return HttpResponseRedirect('/dashboard/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def sign_up(request):
    return render(request, 'usercreds/sign_up.html')

def create_user(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.create_user(username, email, password)
    user.save()
    creds = Credentials(access_key='', secret_key='', uid=user.id)
    creds.save()
    ## only send mail with proper email settings or activating the dummy server
    #send_mail('Subject here', 'Here is the message.', 'from@example.com',
    #            ['mdshaonimran@gmail.com'], fail_silently=False)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def edit_view(request):
    userid = request.user.id
    creds = Credentials.objects.get(uid=userid)
    c = { 'uid': userid, 'access_key': creds.access_key, 'secret_key': creds.secret_key, 'region': creds.region, 'endpoint': creds.endpoint }
    return render(request, 'usercreds/edit_view.html', c)

def update_view(request):
    access = request.POST.get('accesskey')
    secret = request.POST.get('secretkey')
    region = request.POST.get('region')
    endpoint = request.POST.get('endpoint')
    userid = request.user.id
    creds = Credentials.objects.get(uid=userid)
    creds.access_key = access
    creds.secret_key = secret
    creds.region = region
    creds.endpoint = endpoint
    creds.save()

    return HttpResponseRedirect('/edit/')




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

# file: callbacks/keypairs/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.shortcuts import render_to_response, render

import dashboard.api.euca.describekeypairs
import dashboard.api.euca.addkeypair
import dashboard.api.euca.deletekeypair

def keypairs(request):
    context = { }
    template = 'keypairs/keypairs.html'
    return render(request, template, context)

def describeKeypairs(request):
    nilCmd = dashboard.api.euca.describekeypairs.DescribeKeyPairs()
    keypairs = nilCmd.main_cli(request.user.id)
    context = { 'keypairs': keypairs }
    template = 'keypairs/describe_keypairs.html'
    return render(request, template, context)


def createKeypair(request):
    query = request.POST.get('key_name', '')
    nilCmd = dashboard.api.euca.addkeypair.AddKeyPair()
    keypair = nilCmd.main_cli(request.user.id, query)
    context = { 'keypair': keypair }
    if keypair == "KeyPair":
        return HttpResponse(keypair)
    else:
        template = 'keypairs/create_keypair.html'
        return render(request, template, context)

def deleteKeypair(request):
    query = request.POST.get('key_name', '')
    nilCmd = dashboard.api.euca.deletekeypair.DeleteKeyPair()
    keypair = nilCmd.main_cli(request.user.id, query)
    return HttpResponse(keypair)

# modal
def modalKeypairs(request):
    context = { }
    template = 'keypairs/keypairs_modal.html'
    return render(request, template, context)

def describeModal(request):
    nilCmd = dashboard.api.euca.describekeypairs.DescribeKeyPairs()
    keypairs = nilCmd.main_cli(request.user.id)
    context = { 'keypairs': keypairs }
    template = 'keypairs/describe_modal.html'
    return render(request, template, context)


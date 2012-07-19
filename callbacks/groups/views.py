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

# file: callbacks/groups/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

import dashboard.api.euca.describegroups
import dashboard.api.euca.addgroup
import dashboard.api.euca.deletegroup
import dashboard.api.euca.editgroup
import dashboard.api.euca.authorize
import dashboard.api.euca.revoke

def groups(request):
    context = { }
    template = 'groups/groups.html'
    return render(request, template, context)

def describeGroups(request):
    nilCmd = dashboard.api.euca.describegroups.DescribeGroups()
    groups = nilCmd.main_cli(request.user.id)
    context = { 'groups': groups }
    template = 'groups/describe_groups.html'
    return render(request, template, context)

def editGroup(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.api.euca.editgroup.EditGroup()
    groups = nilCmd.main_cli(request.user.id, query)
    context = { 'groups': groups }
    template = 'groups/edit_group.html'
    return render(request, template, context)

def describeGroup(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.api.euca.editgroup.EditGroup()
    groups = nilCmd.main_cli(request.user.id, query)
    context = { 'groups': groups }
    template = 'groups/describe_group.html'
    return render(request, template, context)

def createGroup(request):
    query_name = request.POST.get('group_name', '')
    query_description = request.POST.get('group_description', '')
    nilCmd = dashboard.api.euca.addgroup.AddGroup()
    status = nilCmd.main_cli(request.user.id, query_name, query_description)
    return HttpResponse(status)

def deleteGroup(request):
    query = request.POST.get('group_name', '')
    nilCmd = dashboard.api.euca.deletegroup.DeleteGroup()
    status = nilCmd.main_cli(request.user.id, query)
    return HttpResponse(status)


def authorize_group(request):
    query_group_name = request.POST.get('group_name', '')
    query_ip_protocol = request.POST.get('ip_protocol', '')
    query_from_port = request.POST.get('from_port', '')
    query_to_port = request.POST.get('to_port', '')
    query_cidr_ip = request.POST.get('cidr_ip', '')
    nilCmd = dashboard.api.euca.authorize.Authorize()
    status = nilCmd.main_cli(request.user.id, query_group_name, query_ip_protocol, query_from_port, query_to_port, query_cidr_ip)
    return HttpResponse(status)


def revoke_rules(request):
    query_group_name = request.POST.get('group_name', '')
    query_ip_protocol = request.POST.get('ip_protocol', '')
    query_from_port = request.POST.get('from_port', '')
    query_to_port = request.POST.get('to_port', '')
    query_cidr_ip = request.POST.get('cidr_ip', '')
    
    nilCmd = dashboard.api.euca.revoke.Revoke()
    status = nilCmd.main_cli(request.user.id, query_group_name, query_ip_protocol, query_from_port, query_to_port, query_cidr_ip)
    return HttpResponse(status)

# modal
def modalGroups(request):
    context = { }
    template = 'groups/groups_modal.html'
    return render(request, template, context)

def describeModal(request):
    nilCmd = dashboard.api.euca.describegroups.DescribeGroups()
    groups = nilCmd.main_cli(request.user.id)
    context = { 'groups': groups }
    template = 'groups/describe_modal.html'
    return render(request, template, context)


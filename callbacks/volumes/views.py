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

# file: callbacks/volumes/views.py

from django import shortcuts
from django.template.context import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

import dashboard.api.euca.describevolumes
import dashboard.api.euca.createvolume
import dashboard.api.euca.createvolumefromsnapshot
import dashboard.api.euca.deletevolume
import dashboard.api.euca.attachvolume
import dashboard.api.euca.detachvolume

def volumes(request):
    context = { }
    template = 'volumes/volumes.html'
    return render(request, template, context)

def describeVolumes(request):
    nilCmd = dashboard.api.euca.describevolumes.DescribeVolumes()
    volumes = nilCmd.main_cli(request.user.id)
    context = { 'volumes': volumes }
    template = 'volumes/describe_volumes.html'
    return render(request, template, context)

#def create_volume_view(request):
#    context = { }
#    template = 'volumes/create_volume.html'
#    return render(request, template, context)

def createVolume(request):
    query_vol_size = request.POST.get('vol_size', '')
    query_vol_zone = request.POST.get('vol_zone', '')
    nilCmd = dashboard.api.euca.createvolume.CreateVolume()
    status = nilCmd.main_cli(request.user.id, query_vol_size, query_vol_zone)
    return HttpResponse(status)

def snapCreateVolume(request):
    query_snapshot_id = request.POST.get('snapshot_id', '')
    query_zone = request.POST.get('zone', '')
    nilCmd = dashboard.api.euca.createvolumefromsnapshot.CreateVolumeFromSnapshot()
    status = nilCmd.main_cli(request.user.id, query_snapshot_id, query_zone)
    return HttpResponse(status)

def deleteVolume(request):
    query_vol_id = request.POST.get('vol_id', '')
    nilCmd = dashboard.api.euca.deletevolume.DeleteVolume()
    status = nilCmd.main_cli(request.user.id, query_vol_id)
    return HttpResponse(status)

def volumeModal(request):
    context = { }
    template = 'volumes/volume_modal.html'
    return render(request, template, context)

def attachVolume(request):
    query_vol_id = request.POST.get('vol_id', '')
    query_instance_id = request.POST.get('instance_id', '')
    query_device_name = request.POST.get('device_name', '')
    nilCmd = dashboard.api.euca.attachvolume.AttachVolume()
    status = nilCmd.main_cli(request.user.id, query_vol_id, query_instance_id, query_device_name)
    return HttpResponse(status)

def detachVolume(request):
    query_volume_id = request.POST.get('vol_id', '')
    nilCmd = dashboard.api.euca.detachvolume.DetachVolume()
    status = nilCmd.main_cli(request.user.id, query_volume_id)
    return HttpResponse(status)

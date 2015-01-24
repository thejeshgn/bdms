from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404
import json,csv,re
from tracking.utils import get_ip_address
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template import RequestContext
import logging,requests
from django.contrib import messages
from django.conf import settings
import urllib
from django.views.decorators.csrf import csrf_exempt
import md5
import requests
from .models import *
from .forms import *

logger = logging.getLogger(__name__)
HEADER_FORM_URLENCODED = {'content-type':'application/x-www-form-urlencoded'}


def home(request):
    return render_to_response('home.html',{'request':request}, context_instance = RequestContext(request))



from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import (login as auth_login,  authenticate)
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Mucluc

from django.template import loader
from django.db.models import Q
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.utils.encoding import force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic

def home(request):
    return render(request, 'hocbai/menu.html')
def nguphap(request):
    
        date1=datetime.date
        
        isname=request.POST.get("searchmucluc", "")
        muclucv =Mucluc.mucluc1.all()
        
        context = {
            'muclucv': muclucv,
            'date1': date1,
            'isname': isname,
            
        }
        
        return render(request, 'hocbai/nguphap.html')
def cumtu(request):
    return render(request, 'hocbai/cumtu.html')
def video(request):
    return render(request, 'hocbai/video.html')

from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import Company,Employee
# Create your views here.
def index(request):
	company = Company.objects.all()
	return render_to_response('kevin/data.html', locals())

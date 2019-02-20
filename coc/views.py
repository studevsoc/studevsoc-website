

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import coc
from django.shortcuts import render

# Create your views here.
def coc_list(request):
    cocs = coc.objects.filter(coc_date__lte=timezone.now()).order_by('coc_date')
    return render(request,'coc/coc_list.html',{'cocs': cocs})

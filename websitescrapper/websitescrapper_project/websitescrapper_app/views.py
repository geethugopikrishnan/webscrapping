# from django.contrib.sites import requests
import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from .models import Links
# Create your views here.


def home(request):
    if request.method == 'POST':
        link_new = request.POST.get('page','')
        urls = requests.get(link_new)
        beautisoup = BeautifulSoup(urls.text, 'html.parser')
        # address = []
        for link in beautisoup.find_all('a'):
            # address.append(link.get('href'))
            li_address = link.get('href')
            li_string = link.string
            Links.objects.create(address=li_address,stringname=li_string)


        return redirect('/')
    data = Links.objects.all()
    return render(request, 'home.html', {'data': data})



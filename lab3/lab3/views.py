from django.views import View
from django.shortcuts import render, redirect

class HomePageView(View):
    def get(self, request):
     
        return render(request, 'lab3/index.html',{'hi':'hello world!'})




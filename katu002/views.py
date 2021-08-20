from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    #index.htmlwをレンダリングする
    template_name = 'index.html'
    

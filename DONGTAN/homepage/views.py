from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from homepage.models import Menu

class IntroTV(TemplateView):
	template_name='homepage/intro.html'

class DishLV(ListView):
	model=Menu
	template_name='homepage/menu_all.html'
	context_object_name='menus'


class DishDV(DetailView):
	model=Menu
	template_name='homepage/menu_detail.html'

class PhotoTV(TemplateView):
	template_name='homepage/photo.html'
from django.urls import path, re_path
from homepage.views import *

app_name='homepage'

urlpatterns= [
	path('intro/',IntroTV.as_view(),name='intro'),
	path('dish/',DishLV.as_view(),name='dish'),
	re_path(r'^dish/(?P<pk>\d+)/$',DishDV.as_view(),name='dish_detail'),
	path('photo/',PhotoTV.as_view(),name='photo'),



]
from django.urls import *

from . import views
urlpatterns = [
 path('index/',views.index,name="home"),
 path('portfolio/',views.portfolio,name="portfolio"),
 path('contact/',views.contact,name="contact"),
]
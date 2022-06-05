from django.urls import path
from . import views
"""
path =('',views.index,name = 'index')-This means https://website.com we can enter into the page.


But

path =('/downloads',views.downloads,name = 'downloads')--This means https://website.com/downloads we can enter into the page.
whatever written in the brackets is or should be written in the url while typed by the user.

"""

urlpatterns = [
    path('',views.index,name = "index"),
    path('counter',views.counter,name = 'counter')
]

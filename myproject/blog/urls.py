# This is the simplest view possible in Django.
# To call the view, we need to map it to
# a URL - and for this we need a URLconf.
# To create a URLconf in the polls directory, 
#create a file called urls.py.
#Your app directory should now look like:

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

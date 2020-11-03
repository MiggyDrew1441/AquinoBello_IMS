from django.conf.urls import url
from .views import *

# setup the links here to be access

urlpatterns = [
	url(r'^$', 
		index, # function 
		name="index" 
	),

	url(r'^display_laptop', 
		display_laptops, # views.py function 
		name='display_laptops'
	),

	url(r'^display_desktop', display_desktops, name='display_desktops'),
	url(r'^display_mobile', display_mobiles, name='display_mobiles')
]
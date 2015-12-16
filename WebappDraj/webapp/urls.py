from django.conf.urls import include, url
from . import views

urlpatterns = [
	# url(r'^$', views.inf_estad_list, name='first-view'),

	url(r'^$', views.search, name='search'),
]
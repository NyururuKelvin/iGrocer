from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
	#Leave as empty string for base url
	url(r'^$', views.home, name="home"),
	url(r'^store$', views.store, name="store"),
	url(r'^signup', views.signup, name='signup'),
    url(r'^login', LoginView.as_view(), name='login_url'),
    url(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
	url(r'^sub/$', views.subscription, name="sub"),
	url(r'^cart/$', views.cart, name="cart"),
	url(r'^checkout/$', views.checkout, name="checkout"),
	url(r'^update_item/$', views.updateItem, name="update_item"),
	url(r'^process_order/$', views.processOrder, name="process_order"),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
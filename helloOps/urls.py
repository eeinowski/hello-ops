from django.conf.urls import url
from django.views.decorators.cache import cache_page
from helloOps.views import HomePageView


urlpatterns = [
    url(r'^$', cache_page(60*60)(HomePageView.as_view()), name='home'),
]

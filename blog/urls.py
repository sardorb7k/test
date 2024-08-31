from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='home'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', PostDetail, name='post_detail'),
    path('signup/', SingupPage, name='signup'),
    path('logout/', LogoutUser, name='logout'),
    path('login/', LoginPage, name='login'),
    path('contact/', ContactPage, name='contact'),
    path('about/', AboutPage, name='about'),
    path('category/<slug:slug>/', CategoryPost, name='category_post'),
]


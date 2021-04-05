"""routerProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from router_app import views as appview
from restapi_router import views as restview
#from rest_framework import routers  # add this

#router = routers.DefaultRouter()  # add this
#router.register(r'posts', restview.PostView, 'Crud')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', appview.create),
    path('show/',appview.show),
    path('edit/<int:id>/', appview.edit),
    path('update/<int:id>/', appview.update),
    path('delete/<int:id>/', appview.delete),
path('new_router/', restview.CreateNewRouter.as_view()),
path('update_ip/', restview.UpdateRouterIP.as_view()),
path('router_sapid/', restview.ListRouterUsingsapId.as_view()),
path('delete_based_ip/', restview.DeleteBasedonIP.as_view()),
path('list_router_in_range/', restview.ListRouterIPRange.as_view()),
path('hello/', restview.HelloView.as_view(), name='hello'),

]
#5375019688c2e4bd7db1d99d71ba293d067b4aa2  authtoken for user reshma to view hello and resapi_router rest apis
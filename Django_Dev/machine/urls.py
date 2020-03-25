
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',  views.find_machine,name="index"),
    path('test/',  views.test1,name="test"),
    path('test1/',  views.test2,name="test1"),
]


from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machine/',  views.find_machine,name="machine"),
    path('index/',  views.index,name="index"),
    path('dashboard/',  views.dashboard,name="dashboard"),
    path('detail/',  views.detail,name="detail"),
]

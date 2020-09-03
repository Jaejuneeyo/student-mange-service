from django.contrib import admin
from django.urls import path 
from original import views
from .views import create,detail,update,delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('create/',views.create,name="create"),
    path('login/',views.login, name="login"),
    path('update/<int:student_id>', update, name='update'),
    path('delete/<int:student_id>', delete, name='delete'),
]

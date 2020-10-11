from django.contrib import admin  
from django.urls import path  
from appointments import views  
urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', views.show) ,
    path('appform', views.appform , name="appform"),  
    path('show',views.show, name="show"),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('calender', views.calender, name="calender") ,
    path('fullreport/<int:id>' , views.fullreport , name = "fullreport"),
    path('sendmail/<int:id>' , views.sendmail , name = "sendmail"),
    path('fullrecords' , views.fullrecords , name="fullrecords"),
]  
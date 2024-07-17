
from django.urls import path
from blog import views
urlpatterns = [
   
    path("",views.user),
    
    
    path("edit/<id>",views.edit,name="edit"),
    path("delete/<id>",views.delete,name="delete")

]
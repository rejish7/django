
from django.urls import path
from blog import views
urlpatterns = [
    # path("index",views.index),
    path("",views.user),
    
    # path("gallery",views.gallery),
    path("edit/<id>",views.edit,name="edit"),
    path("delete/<id>",views.delete,name="delete")
#     path("faq",views.faq),
#     path("travel",views.travel),
]
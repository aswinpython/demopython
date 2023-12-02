from.import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:cheat_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvlistview/',views.Cheatlistview.as_view(),name='cbvlistview'),
    path('cbvdetail/<int:pk>/',views.Cheatdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Cheatupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Cheatdeleteview.as_view(),name='cbvdelete'),
]

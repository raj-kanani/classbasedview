from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [



]



# classbasedview, templateview, redirectview
# path('home/', views.Home.as_view(), name='Home'),
# # path('', views.Home.as_view(name='home'), name='rk'),
# path('newform/', views.Newform.as_view(), name='Newform'),
# path('new/', views.New.as_view(), name='New'),
# path('child/', views.Child.as_view(), name='Child'),
# path('', views.TemplateView.as_view(template_name='home.html'), name='home')
# path('', views.Home.as_view(extra_context={'sub': 'python'}), name='home'),
# path('home/', views.Home.as_view(), name='home'), # kwargs data check in used..
# path('home1/', views.RedirectView.as_view(url='/'), name='home1'),
# path('home2/', views.RedirectView.as_view(url='https://www.google.com'), name='home2'),
# path('index/', views.Index.as_view(), name='index'),

# path('index1/', views.Index1.as_view(), name='index1'),#pattern_name='index'


# path('raj/<int:pk>/', views.Raj.as_view(), name='raj'),
# path('roll/<int:pk>/', views.TemplateView.as_view(template_name='home.html'), name='raj1'),
#
# path('raj/<slug:post>/', views.Raj.as_view(), name='raj'),
# path('<slug:post>/', views.TemplateView.as_view(template_name='home.html'), name='raj1'), # reverse url 2 ma name us in 1st url run


####### CRUD operation
    # path('todo/', views.Todoview.as_view(), name='todo'),
    # path('tododetail/', views.Tododetailview.as_view(), name='tododetail'),
    # path('delete/<int:id>/', views.Deleteview.as_view(), name='delete'),
    # path('update/<int:id>/', views.Updateview.as_view(), name='update'),
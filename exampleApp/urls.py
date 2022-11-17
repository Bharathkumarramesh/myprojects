from rest_framework import routers

from exampleApp.views import UserViewset
# from exampleApp.views import UserList, UserDetail

#
# from exampleApp import views
# from exampleApp.views import UserList, UserDetail
#
router = routers.DefaultRouter()
router.register(r'users', UserViewset, basename='user')
# router.register(r'users', UserList, basename='user')
# router.register(r'users/<int:pk>', UserDetail, basename='user')

#
# from django.urls import path, include
#
# urlpatterns = [
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view()),
# ]

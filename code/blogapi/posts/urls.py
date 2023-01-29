from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import * 

""" router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls """

urlpatterns = [

    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('venue_pdf/<int:pk>', venue_pdf, name = 'venue_pdf'),

]
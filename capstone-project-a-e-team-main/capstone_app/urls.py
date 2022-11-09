
from django.urls import path
from.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView
)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/',views.about,name='aboutas'),
    path('log/',views.log,name='log'),
    path('document/',views.document,name='document'),
    path('series',views.series,name='series'),
    path('test2/',views.test2,name='test2')
    
    ]
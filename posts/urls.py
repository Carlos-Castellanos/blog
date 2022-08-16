from django.urls import path
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from django.conf import settings


urlpatterns = [
    path('',PostListView.as_view() , name="post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('new/', PostCreateView.as_view(), name="post_new"),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name="post_edit"),
    path('register/', views.register, name='register'),
	path('login/', LoginView.as_view(template_name='posts/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='posts/logout.html'), name='logout'),
    


]
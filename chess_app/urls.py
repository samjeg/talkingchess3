from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chess_app'


urlpatterns = [
	url(r'^$', auth_views.LoginView.as_view(
            template_name="chess_app/login.html",
        ), name='login'),
	url(r"^logout/$", auth_views.LogoutView.as_view(
    		template_name="chess_app/index.html"
    	), name="logout"),
    url(r'^register/$', views.Register.as_view(), name='register'),
	url(r'^create_profile/$', views.UserProfileCreateView.as_view(), name='create_profile'),
	url(r'^profile/(?P<pk>\d+)/$', views.UserProfileDetailView.as_view(), name='profile_detail'),
	url(r'^profile/(?P<pk>\d+)/update_profile/$', views.UserProfileUpdateView.as_view(), name='update_profile'),
	url(r'^chessboard/(?P<pk>\d+)/$', views.ChessboardDetailView.as_view(), name='chess_detail'),
]
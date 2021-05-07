from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'responses'
urlpatterns = [
    path('', views.form_view, name='my_responses'),
    # path('accounts/login', LoginView.as_view(), name='login'),
    path('dash/', views.admin_view, name='dashboard'),
    path('team/', views.team_view, name='team'),
    path('team/<int:pk>', views.team_member, name='team_single'),
    path('all_resp/', views.all_responses, name='all_resp'),
    path('people_analytics/', views.analytics, name='analytics'),
    path('highlights/', views.top_highlights, name='highlights'),
]

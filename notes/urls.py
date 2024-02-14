from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from . import views

urlpatterns = [
    #Authentication
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),

    #Profile
    path('profile/', views.getProfile, name='profile'),
    path('profile/update/', views.updateProfile, name='update-profile'),
    
    path('notes',views.getNoteListView_or_createNote.as_view()),
    path('note/<int:pk>',views.NoteView.as_view())
]
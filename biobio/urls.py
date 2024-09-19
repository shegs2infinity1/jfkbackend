from django.http import JsonResponse
from django.urls import path
from django.conf.urls import handler500
from .views import CustomTokenObtainPairView,BiodataListView,BiodataCreateView,CreateUserView,UserVerficationView,UserProfileDetailView
from .views import OrderCreateView, OrderListView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('biodata/', BiodataListView.as_view(), name='biodata-list'),  # Admin route
    path('biodata/', BiodataCreateView.as_view(), name='biodata-create'),  # Biodata submission route for clients
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('verify/', UserVerficationView.as_view(), name='verify'),
    path('profile/<str:username>/', UserProfileDetailView.as_view(), name='user-profile-detail'),  # Profile detail endpoint
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/new/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<str:username>/', OrderListView.as_view(), name='order-list-username'),  # Use URL parameter


]

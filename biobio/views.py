from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework import serializers
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAdminUser
from .models import Biodata
from .models import UserProfile , Order
from .serializers import BiodataSerializer
from .serializers import UserProfileSerializer , OrderSerializer
import pdb

from rest_framework.permissions import IsAuthenticated


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer

class BiodataListView(generics.ListAPIView):
    queryset = Biodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this
# Create your views here.
class BiodataCreateView(generics.CreateAPIView):
    queryset = Biodata.objects.all()
    serializer_class = BiodataSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can submit

    def perform_create(self, serializer):
        # Attach the currently logged-in user to the biodata entry
        serializer.save(user=self.request.user)

class CreateUserView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserVerficationView(APIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        # serializer = UserProfileSerializer(data=request.data)
        try:

            username = request.data['username']
            password = request.data['password']
        except KeyError:
            return Response({'error': 'Missing username or password'}, status=status.HTTP_400_BAD_REQUEST)

        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user_profile = UserProfile.objects.get(username=username)
            if user_profile.password == password:
                return Response({"role": user_profile.role}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Username and password do not match"}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({"error": "Username and password do not match"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Log the exception here (optional)
            print(f"Internal server error: {e}")
            return Response({"error": "Internal server error. Please try again later."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UserProfileDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.AllowAny]


    def get(self, request, username,*args, **kwargs):
        try:
            user_profile = UserProfile.objects.get(username=username)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)
    def put(self, request, *args, **kwargs):
        try:
            user_profile = UserProfile.objects.get(username=request.user.username)
            serializer = UserProfileSerializer(user_profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({"error": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

class OrderCreateView(generics.CreateAPIView):
    #pdb.set_trace()
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    print("Reached perform_create method1")  # Temporary print statement for debugging
    def perform_create(self, serializer):
        #pdb.set_trace()
        print("Reached perform_create method2")  # Temporary print statement for debugging
        username = self.request.data.get('username')

        try:
            user_profile = UserProfile.objects.get(username=username)
            print("Reached perform_create method3")  # Temporary print statement for debugging
            serializer.save(client=user_profile.username)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError({"error": "User with the provided username does not exist."})

        except Exception as e:

            print(f"Error creating order: {e}")
            # Return a generic error response
            return Response({"error": "An error occurred while placing the order."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        username = self.request.query_params.get('username')
        try:
            user = UserProfile.objects.get(username=username)
            Orderlist = Order.objects.filter(client=username)
            return Orderlist
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "User with the provided username does not exist."})
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return Order.objects.none()
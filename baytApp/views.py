from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class UserRegistrationView(generics.CreateAPIView):
   
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        # {'username': user.username, 'email': user.email},
        return Response({}, status=status.HTTP_201_CREATED)
class UsersView(APIView):    

    def get(self, request):
        
        users = User.objects.filter(is_staff=False)
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def perform_create(self, serializer):
        return serializer.save()
class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
       
        user = request.user

        currentUser = User.objects.get(user=request.user)

        serializer = UserSerializer(currentUser)

       
        return Response(serializer.data)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
       
        request.auth.delete()  
        
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
class CreateJobView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = PremiumJobSerializer
    # permission_classes = [IsAuthenticated]

class UpdateJobView(generics.UpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = PremiumJobSerializer
    # permission_classes = [IsAuthenticated]

class DeleteJobView(generics.DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = PremiumJobSerializer
    # permission_classes = [IsAuthenticated]
class PremiumJobView(APIView):
    # permission_classes = [IsAuthenticated]    

    def get(self, request):
        
        jobs = Job.objects.all()
        serializer = PremiumJobSerializer(jobs, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
class JobView(APIView):    

    def get(self, request):
        
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many= True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
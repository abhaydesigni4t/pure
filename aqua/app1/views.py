from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SignupForm
from django.contrib.auth import login, authenticate, get_user_model


User = get_user_model()

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email  # Set username to the email
            user.save()
            login(request, user, backend='app1.auth_backends.EmailBackend')  # Specify backend here
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'app1/signup.html', {'form': form})


from .forms import SignupForm, EmailAuthenticationForm  # Import the new form

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired URL name
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'app1/login.html', {'form': form})


def home(request):
    return render(request,'app1/home.html')


from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created successfully'}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({'access': str(refresh.access_token), 'refresh': str(refresh)})
    
    
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import Model1Serializer,GetModel1Serializer
from .models import Model1

class Model1View(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = Model1Serializer(data=request.data, partial=True)  # Ensure partial=True for partial updates
        if serializer.is_valid():
            instance = serializer.save()  
        
            response_serializer = Model1Serializer(instance, fields=request.data.keys())
            return Response(response_serializer.data, status=201)
        return Response(serializer.errors, status=400)



class GetModel1View(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, device_id, *args, **kwargs):
        
        try:
            model_instance = Model1.objects.get(device_id=device_id)
            serializer = GetModel1Serializer(model_instance)
            return Response(serializer.data, status=200)
        except Model1.DoesNotExist:
            return Response({"error": "Device not found"}, status=404)

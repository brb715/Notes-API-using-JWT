from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Note, CustomUser
from .serializers import NoteSerializer, MyTokenObtainPairSerializer, RegisterSerializer, ProfileSerializer

class getNoteListView_or_createNote(ListCreateAPIView):
    queryset=Note.objects.all().order_by('-updated')
    serializer_class=NoteSerializer

class NoteView(RetrieveUpdateDestroyAPIView):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#api/notes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    public_notes = Note.objects.filter(is_public=True).order_by('-updated')[:10]
    user_notes = request.user.notes.all().order_by('-updated')[:10]
    notes = public_notes | user_notes
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)
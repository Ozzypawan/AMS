from rest_framework import viewsets
from .models import Rank, Profile, Document, BankDetail, Device
from .serializers import RankSerializer, ProfileSerializer, DocumentSerializer, BankDetailSerializer, DeviceSerializer

class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all()
    serializer_class = RankSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_admin:
            queryset = queryset.filter(user=self.request.user)
        return queryset

class BankDetailViewSet(viewsets.ModelViewSet):
    queryset = BankDetail.objects.all()
    serializer_class = BankDetailSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_admin:
            queryset = queryset.filter(user=self.request.user)
        return queryset

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    
    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_admin:
            queryset = queryset.filter(user=self.request.user)
        return queryset

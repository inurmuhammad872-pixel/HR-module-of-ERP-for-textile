
# Create your views here.
from rest_framework import generics, status, viewsets
from .serializers import XodimlarSerializer, CustomRegisterSerializer,TatilUpdateSerializer
from .models import User, Xodimlar
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Count
from rest_framework.decorators import action
from django_filters.views import FilterView
from .filters import XodimlarFilter
from django.views.generic import ListView
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import XodimlarFilter
from django.shortcuts import render




class XodimlarViewSet(viewsets.ModelViewSet):
    queryset = Xodimlar.objects.all()
    serializer_class = XodimlarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = XodimlarFilter

    @action(detail=True, methods=['post'])
    def tatilga_chiqish(self, request, pk=None):
        xodim = self.get_object()
        serializer = TatilUpdateSerializer(xodim, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(tatil_holati=True)
            return Response({'status': 'xodim tatilga chiqarildi'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def tatildan_qaytish(self, request, pk=None):
        xodim = self.get_object()
        serializer = TatilUpdateSerializer(xodim, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(tatil_holati=False, tatil_boshlanish_sana=None, tatil_tugash_sana=None)
            return Response({'status': 'xodim tatildan qaytdi'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
       
        if q:
            qs = qs.filter(
                Q(ism__icontains=q) |
                Q(familiya__icontains=q) |
                Q(lavozim__icontains=q) |
                Q(bolim__icontains=q)
            )
        return qs





class XodimlarStatisticsAPIView(APIView):
    def get(self, request):
        today = timezone.now().date()

        total = Xodimlar.objects.count()
        today_added = Xodimlar.objects.filter(created_at__date=today).count()

        return Response({
            "total_employees": total,
            "today_added_employees": today_added
        })
    



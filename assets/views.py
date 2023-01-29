from django.shortcuts import render
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer
from rest_framework import permissions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from utils.response_wrapper import ResponseWrapper
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Company created',
                    status=status.HTTP_201_CREATED
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def list(self, request):
        try:
            companies = Company.objects.all()
            serializer = self.get_serializer(companies, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Company list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(company)
            return ResponseWrapper(
                data=serializer.data,
                message='Company retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Company updated',
                    status=status.HTTP_200_OK
                )
            else:
                return ResponseWrapper(
                    message=serializer.errors,
                    error_code=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def destroy(self, request, *args, **kwargs):
        try:
            company = Company.objects.filter(id=kwargs['pk']).first()
            company.delete()
            return ResponseWrapper(
                message='Company deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


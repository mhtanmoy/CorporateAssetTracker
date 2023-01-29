from django.shortcuts import render
from .models import Company, Employee, Device, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer, DeviceCheckoutSerializer, DeviceCheckinSerializer
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


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Employee created',
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
            employees = Employee.objects.all()
            serializer = self.get_serializer(employees, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Employee list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(employee)
            return ResponseWrapper(
                data=serializer.data,
                message='Employee retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, *args, **kwargs):
        try:
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Employee updated',
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
            employee = Employee.objects.filter(id=kwargs['pk']).first()
            employee.delete()
            return ResponseWrapper(
                message='Employee deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device created',
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
            devices = Device.objects.all()
            serializer = self.get_serializer(devices, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Device list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, *args, **kwargs):
        try:
            device = Device.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device)
            return ResponseWrapper(
                data=serializer.data,
                message='Device retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


    def update(self, request, *args, **kwargs):
        try:
            device = Device.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device updated',
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
            device = Device.objects.filter(id=kwargs['pk']).first()
            device.delete()
            return ResponseWrapper(
                message='Device deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )


class DeviceLogViewSet(viewsets.ModelViewSet):
    queryset = DeviceLog.objects.all()
    #serializer_class = DeviceLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


    def get_serializer_class(self):
        if self.action == 'checkout':
            return DeviceCheckoutSerializer
        elif self.action == 'checkin':
            return DeviceCheckinSerializer
        else:
            return DeviceLogSerializer


    def checkout(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device checked out',
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

    def checkin(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device_log, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return ResponseWrapper(
                    data=serializer.data,
                    message='Device checked in',
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

    def list(self, request):
        try:
            device_logs = DeviceLog.objects.all()
            serializer = self.get_serializer(device_logs, many=True)
            return ResponseWrapper(
                data=serializer.data,
                message='Device log list',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            serializer = self.get_serializer(device_log)
            return ResponseWrapper(
                data=serializer.data,
                message='Device log retrieved',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, *args, **kwargs):
        try:
            device_log = DeviceLog.objects.filter(id=kwargs['pk']).first()
            device_log.delete()
            return ResponseWrapper(
                message='Device log deleted',
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return ResponseWrapper(
                message=str(e),
                error_code=status.HTTP_400_BAD_REQUEST
            )



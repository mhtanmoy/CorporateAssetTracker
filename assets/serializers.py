from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog
from authentications.models import UserAccount as User
from authentications.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'address', 'company_license']
        read_only_fields = ['id']
        

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Employee
        fields = ['id', 'user', 'company', 'address']
        read_only_fields = ['id']

    def get_user(self, obj):
        user = User.objects.get(id=obj.user.id)
        return UserSerializer(user).data

class DeviceSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Device
        fields = ['id', 'name', 'company', 'model', 'brand', 'serial_number']
        read_only_fields = ['id']

    def get_company(self, obj):
        return CompanySerializer(obj.company).data


class DeviceLogSerializer(serializers.ModelSerializer):
    device = DeviceSerializer()
    employee = EmployeeSerializer()
    class Meta:
        model = DeviceLog
        fields = ['id', 'device', 'employee', 'checkout_date', 'checkout_condition', 'checkin_date', 'checkin_condition']
        read_only_fields = ['id']

    def get_device(self, obj):
        return DeviceSerializer(obj.device).data

    def get_employee(self, obj):
        return EmployeeSerializer(obj.employee).data
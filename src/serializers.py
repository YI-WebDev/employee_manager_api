from rest_framework import serializers
from .models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'gender', 'birth_date', 'department', 'joined_date', 'termination_date']
        extra_kwargs = {
            'name': {'error_messages': {'blank': '名前は必須項目です。'}},
            'gender': {'error_messages': {'blank': '性別は必須項目です。', 'invalid_choice': '性別は必須項目です。'}},
            'birth_date': {'error_messages': {'blank': '生年月日は必須項目です。', 'invalid': '生年月日は必須項目です。'}},
            'department': {'error_messages': {'blank': '所属部署は必須項目です。', 'invalid_choice': '所属部署は必須項目です。'}},
            'joined_date': {'error_messages': {'blank': '入社年月日は必須項目です。', 'invalid': '入社年月日は必須項目です。'}},
            'termination_date': {'error_messages': {'blank': '退社年月日は必須項目です。', 'invalid': '退社年月日は必須項目です。'}},
        }
    
    def validate(self, data):
        errors = {}

        if data.get('termination_date') and data.get('joined_date') and data['termination_date'] < data['joined_date']:
            errors['termination_date'] = "退職日が入社日より早い日付で指定されています。"
        if data.get('joined_date') and data.get('birth_date') and data['joined_date'] < data['birth_date']:
            errors['joined_date'] = "入社日が生年月日より早い日付で指定されています。"
        
        required_fields = ['name', 'gender', 'birth_date', 'department', 'joined_date']
        for field in required_fields:
            if not data.get(field):
                errors[field] = f"{field}は必須項目です。"
        
        if errors:
            raise serializers.ValidationError(errors)
        return data
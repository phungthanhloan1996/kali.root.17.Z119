from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import WorkerInfo, AttendanceRecord, CustomUser
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'z119group',
            'is_leader', 'is_director', 'group_name')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username', 'z119group',
            'is_leader', 'is_director', 'group_name')
class WorkerInfoForm(forms.ModelForm):
    class Meta:
        model = WorkerInfo
        fields = ['name', 'rank', 'position','phone_number']

class AttendanceRecordForm(forms.ModelForm):
    class Meta:
        model = AttendanceRecord
        fields = ['status', 'note']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'placeholder': 'Nhập lý do', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        note = cleaned_data.get('note')

        if status and not note:
            raise forms.ValidationError("Lý do là bắt buộc khi có trạng thái.")
        return cleaned_data


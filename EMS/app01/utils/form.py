from django import forms
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class EmployeeModelForm(BootStrapModelForm):
    name = forms.CharField(
        min_length=3,
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = models.Employee
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]


class PrettyModelForm(BootStrapModelForm):
    """新建靓号"""
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        txt_mobile = self.cleaned_data.get("mobile")
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


class PrettyEditModelForm(BootStrapModelForm):
    """编辑靓号"""
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile", "price", "level", "status"]

    def clean_mobile(self):
        txt_mobile = self.cleaned_data.get("mobile")
        # 排除自己以外，判断其他数据是否手机号重复
        exists = (models.PrettyNum.objects.exclude(id=self.instance.pk)
                  .filter(mobile=txt_mobile).exists())
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile

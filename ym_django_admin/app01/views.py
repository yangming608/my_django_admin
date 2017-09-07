from django.shortcuts import render, HttpResponse, redirect
from django.forms import ModelForm
from django.forms import fields as ffields
from app01 import models
# from django.forms import fields as ffields
import time
# Create your views here.
def test(request):
    # time.sleep(10)
    return HttpResponse("...")


class TestModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        error_messages = {
            'user': {'required': '用户名不能为空'},
            'email': {'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
        }
        labels = {
            'user': '用户名',
            'email': "邮箱",
            "age": "年龄"
        }

def xxx(request):
    form_obj = TestModelForm()
    if request.method == "GET":
        com_dic = {"form_obj": form_obj}
        return render(request, "xxx.html", com_dic)
    else:
        form_obj = TestModelForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("http://www.baidu.com")
        com_dic = {"form_obj": form_obj}
        return render(request, "xxx.html", com_dic)



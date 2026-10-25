from django.shortcuts import render, redirect
from app01.models import Department, Employee
from app01.utils.form import EmployeeModelForm


def user_list(request):
    """用户列表"""
    queryset = Employee.objects.all()
    return render(request, "app01/user_list.html", {"queryset": queryset})


def user_add(request):
    """普通表单新建用户"""
    if request.method == "GET":
        depart_list = Department.objects.all()
        return render(request, "app01/user_add.html", {"depart_list": depart_list})
    Employee.objects.create(
        name=request.POST.get("name"),
        password=request.POST.get("password"),
        age=request.POST.get("age"),
        account=request.POST.get("account"),
        gender=request.POST.get("gender"),
        depart_id=request.POST.get("depart"),
    )
    return redirect("/user/list/")


def user_add_modelform(request):
    """ModelForm 新建用户"""
    if request.method == "GET":
        form = EmployeeModelForm()
        return render(request, "app01/user_add_modelform.html", {"form": form})
    form = EmployeeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "app01/user_add_modelform.html", {"form": form})


def user_edit(request, nid):
    """编辑用户（ModelForm）"""
    row_object = Employee.objects.filter(id=nid).first()
    if request.method == "GET":
        form = EmployeeModelForm(instance=row_object)
        return render(request, "app01/user_edit.html", {"form": form})
    form = EmployeeModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "app01/user_edit.html", {"form": form})


def user_delete(request, nid):
    """删除用户"""
    Employee.objects.filter(id=nid).delete()
    return redirect("/user/list/")

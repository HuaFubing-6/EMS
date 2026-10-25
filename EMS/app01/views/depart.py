from django.shortcuts import render, redirect
from app01.models import Department


def depart_list(request):
    """部门列表：读取数据库全部部门"""
    queryset = Department.objects.all()
    return render(request, "app01/depart_list1.html", {"queryset": queryset})


def depart_add(request):
    """新建部门"""
    if request.method == "GET":
        return render(request, "app01/depart_add1.html")
    title = request.POST.get("title")
    Department.objects.create(title=title)
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """编辑部门"""
    if request.method == "GET":
        row_object = Department.objects.filter(id=nid).first()
        return render(request, "app01/depart_edit1.html", {"row_object": row_object})
    title = request.POST.get("title")
    Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")

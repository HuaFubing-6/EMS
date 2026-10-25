from django.shortcuts import render, redirect
from app01 import models
from app01.utils.form import PrettyModelForm, PrettyEditModelForm
from app01.utils.pagination import Pagination


def pretty_list(request):
    """靓号列表 + 搜索手机号 + 分页"""
    data_dict = {}
    search_data = request.GET.get("q", "")
    if search_data:
        data_dict["mobile__contains"] = search_data

    queryset = models.PrettyNum.objects.filter(**data_dict)

    # 分页：自动切片并生成分页组件 HTML
    page_object = Pagination(request, queryset)

    return render(request, "app01/prettynum_list.html", {
        "queryset": page_object.queryset,
        "search_data": search_data,
        "page_string": page_object.page_html(),
    })


def pretty_add(request):
    """新建靓号"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, "app01/prettynum_add.html", {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "app01/prettynum_add.html", {"form": form})


def pretty_edit(request, nid):
    """编辑靓号"""
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        return render(request, "app01/prettynum_edit.html", {"form": form})
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty/list/")
    return render(request, "app01/prettynum_edit.html", {"form": form})


def pretty_delete(request, nid):
    """删除靓号"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty/list/")

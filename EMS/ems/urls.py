"""
URL configuration for ems project.
"""

from django.contrib import admin
from django.urls import path
from app01.views import depart, user, pretty

urlpatterns = [
    path("admin/", admin.site.urls),

    # 部门管理
    path("depart/list/", depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/delete/', depart.depart_delete),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/add/modelform/', user.user_add_modelform),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('pretty/list/', pretty.pretty_list),
    path('pretty/add/', pretty.pretty_add),
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),
]

from django.db import models

class Employee(models.Model):
    """员工表"""
    # 性别选择
    GENDER_CHOICES = (
        (1, "男"),
        (2, "女"),
    )

    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.CharField(verbose_name="账号", max_length=32)
    create_time = models.DateTimeField(verbose_name="入职时间", null=True, blank=True)

    depart = models.ForeignKey(
        to="Department",
        verbose_name="部门",
        on_delete=models.CASCADE,
    )


    gender = models.SmallIntegerField(verbose_name="性别", choices=GENDER_CHOICES, default=1)

    def __str__(self):
        return self.name

class Department(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="部门名称", max_length=32)

    def __str__(self):
        return self.title


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号", max_length=11)

    price = models.IntegerField(verbose_name="价格", default=0)

    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未使用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)

    def __str__(self):
        return self.mobile


class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


# EMS 联通用户管理系统

基于 Django 4.2 + Bootstrap 3 开发的后台管理系统，包含部门管理、用户管理、靓号管理三大模块。

---

## 一、技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Django 4.2 |
| 数据库 | MySQL 8.0 |
| 前端 | Bootstrap 3.4.1 + jQuery 3.6.0 |
| 时间选择插件 | bootstrap-datepicker 1.9.0 |
| 模板引擎 | Django Template |
| Python | 3.x（解释器路径 `D:\python\python.exe`） |

---

## 二、环境要求

1. Python 3.x（已安装 Django 4.2、pymysql）
2. MySQL 8.0，已创建数据库 `ems`
3. 依赖包：
   ```
   django==4.2
   pymysql
   ```

---

## 三、快速启动

```bash
# 1. 进入项目目录
cd D:\pycham-studyproject\EMS

# 2. 确保 MySQL 已启动，数据库 ems 已创建

# 3. 执行数据库迁移（首次）
D:\python\python.exe manage.py makemigrations
D:\python\python.exe manage.py migrate

# 4. 启动开发服务器
D:\python\python.exe manage.py runserver
```

浏览器访问：`http://127.0.0.1:8000/`

---

## 四、项目结构

```
EMS/
├── manage.py                  # Django 命令行入口
├── ems/                       # 项目配置目录
│   ├── settings.py            # 配置文件（数据库、APP、模板等）
│   ├── urls.py                # 总路由（按模块分发）
│   └── wsgi.py
└── app01/                     # 业务 APP
    ├── models.py              # 数据模型（3张表）
    ├── admin.py
    ├── migrations/            # 数据库迁移记录
    │   ├── 0001_initial.py
    │   ├── 0002_alter_employee_depart.py
    │   ├── 0003_prettynum.py
    │   └── 0004_alter_employee_create_time.py
    ├── utils/                 # 公共组件（可复用）
    │   ├── bootstrap.py       # BootStrap 样式基类
    │   ├── form.py            # 所有 ModelForm 表单类
    │   └── pagination.py       # 分页组件类
    ├── views/                 # 视图（按模块拆分）
    │   ├── depart.py          # 部门视图
    │   ├── user.py            # 用户视图
    │   └── pretty.py          # 靓号视图
    ├── templates/             # HTML 模板
    │   └── app01/
    │       ├── layout.html               # 母版（顶部导航栏）
    │       ├── depart_list1.html        # 部门列表
    │       ├── depart_add1.html          # 新建部门
    │       ├── depart_edit1.html         # 编辑部门
    │       ├── user_list.html            # 用户列表
    │       ├── user_add.html             # 用户新建（原始方式）
    │       ├── user_add_modelform.html   # 用户新建（ModelForm）
    │       ├── user_edit.html            # 编辑用户
    │       ├── prettynum_list.html      # 靓号列表
    │       ├── prettynum_add.html       # 新建靓号
    │       └── prettynum_edit.html      # 编辑靓号
    └── static/                # 静态资源
        ├── css/
        ├── js/jquery-3.6.0.min.js
        ├── img/
        └── plugins/
            ├── bootstrap-3.4.1/        # Bootstrap 框架
            └── bootstrap-datepicker/    # 日期选择插件
```

---

## 五、数据表设计

### 1. Department（部门表）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BigAutoField | 主键 |
| title | CharField(32) | 部门名称 |

### 2. Employee（员工/用户表）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BigAutoField | 主键 |
| name | CharField(32) | 姓名 |
| password | CharField(64) | 密码 |
| age | IntegerField | 年龄 |
| account | CharField(32) | 账号 |
| create_time | DateTimeField | 入职时间（可空，日期选择插件） |
| gender | SmallIntegerField | 性别（1=男，2=女） |
| depart | ForeignKey(Department) | 所属部门（外键，级联删除） |

### 3. PrettyNum（靓号表）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | BigAutoField | 主键 |
| mobile | CharField(11) | 手机号 |
| price | IntegerField | 价格（默认0） |
| level | SmallIntegerField | 级别（1级~4级） |
| status | SmallIntegerField | 状态（1=已占用，2=未使用） |

---

## 六、功能模块

### 6.1 部门管理

| 功能 | 路由 | 视图函数 |
|------|------|----------|
| 部门列表 | `/depart/list/` | `depart_list` |
| 新建部门 | `/depart/add/` | `depart_add` |
| 编辑部门 | `/depart/<nid>/edit/` | `depart_edit` |
| 删除部门 | `/depart/delete/?nid=x` | `depart_delete` |

### 6.2 用户管理

| 功能 | 路由 | 视图函数 |
|------|------|----------|
| 用户列表 | `/user/list/` | `user_list` |
| 新建用户（原始） | `/user/add/` | `user_add` |
| 新建用户（ModelForm） | `/user/add/modelform/` | `user_add_modelform` |
| 编辑用户 | `/user/<nid>/edit/` | `user_edit` |
| 删除用户 | `/user/<nid>/delete/` | `user_delete` |

### 6.3 靓号管理

| 功能 | 路由 | 视图函数 |
|------|------|----------|
| 靓号列表（搜索+分页） | `/pretty/list/` | `pretty_list` |
| 新建靓号 | `/pretty/add/` | `pretty_add` |
| 编辑靓号 | `/pretty/<nid>/edit/` | `pretty_edit` |
| 删除靓号 | `/pretty/<nid>/delete/` | `pretty_delete` |

---

## 七、核心代码讲解

### 7.1 `utils/bootstrap.py` —— Bootstrap 样式基类

**作用：** 自动给 ModelForm 生成的每个输入框加上 `form-control` 样式和 `placeholder`，避免每个表单重复写 `__init__`。

```python
class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}

class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass   # 业务表单继承这个

class BootStrapForm(BootStrap, forms.Form):
    pass   # 普通 Form 继承这个
```

**设计思路：** `BootStrap` 是一个 mixin（混入类），只负责加样式。通过多继承同时复用给 ModelForm 和 Form。

### 7.2 `utils/form.py` —— 所有表单类

| 类 | 用途 | 校验规则 |
|----|------|----------|
| `EmployeeModelForm` | 用户新建/编辑 | name 最少 3 位 |
| `PrettyModelForm` | 新建靓号 | 手机号正则 `^1[3-9]\d{9}$`，查重 |
| `PrettyEditModelForm` | 编辑靓号 | 同上，但排除自身查重 |

**手机号查重原理：**
```python
# 新建：判断所有记录是否有重复
exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()

# 编辑：排除自己这一行再判断
exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
```

### 7.3 `utils/pagination.py` —— 分页组件

**作用：** 自动对查询集切片，并生成分页按钮 HTML（首页/上一页/页码/下一页/尾页/跳转框）。

**使用方式：**
```python
page_object = Pagination(request, queryset, per_page=10)
context = {
    "queryset": page_object.queryset,      # 当前页数据
    "page_string": page_object.page_html()  # 分页按钮 HTML
}
```

**关键特性：**
- 每页 10 条，最多显示 11 个页码按钮（当前页居中）
- **保留搜索条件**：翻页时自动带上 `?q=xxx`，解决搜索+分页冲突
- 页码跳转框（输入页码→跳转）

### 7.4 日期选择插件

在用户新建/编辑页面引入 `bootstrap-datepicker`：
```html
<link rel="stylesheet" href="{% static 'plugins/bootstrap-datepicker/css/bootstrap-datepicker.min.css' %}">
<script src="{% static 'plugins/bootstrap-datepicker/js/bootstrap-datepicker.min.js' %}"></script>
<script src="{% static 'plugins/bootstrap-datepicker/locales/bootstrap-datepicker.zh-CN.min.js' %}"></script>
```
```javascript
$('#id_create_time').datepicker({
    format: 'yyyy-mm-dd',
    language: 'zh-CN',
    autoclose: true
});
```

---

## 八、关键设计决策

1. **视图按模块拆分**：`views/depart.py`、`user.py`、`pretty.py`，不堆在一个文件里
2. **表单抽公共基类**：避免每个 ModelForm 重复写 `__init__` 加样式
3. **分页组件化**：`Pagination` 类可复用到任何列表页
4. **搜索条件保留**：翻页不丢失关键词（`?q=888&page=2`）
5. **新建/编辑表单分开**：`PrettyModelForm` 和 `PrettyEditModelForm`，编辑时排除自身查重

---

## 九、数据库配置

`ems/settings.py`：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ems',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

> 注意：使用 pymysql 连接 MySQL，需在 `ems/__init__.py` 中初始化：
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

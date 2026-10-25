from django.utils.safestring import mark_safe


class Pagination:
    """公共分页组件：接收当前页/总数据，自动切片并生成分页按钮 HTML"""

    def __init__(self, request, queryset, per_page=10, max_show=11):
        """
        :param request:    HttpRequest 对象（用来读取 GET 参数、保留搜索条件）
        :param queryset:   已过滤好（含搜索条件）的完整查询集
        :param per_page:   每页显示条数
        :param max_show:   页面上最多显示的页码按钮个数
        """
        # 1. 当前页码（非法数字时默认第1页）
        try:
            page = int(request.GET.get("page", 1))
        except (ValueError, TypeError):
            page = 1
        self.page = page

        # 2. 总条数 & 总页数
        self.total_count = queryset.count()
        self.per_page = per_page
        total_page, remainder = divmod(self.total_count, per_page)
        if remainder:
            total_page += 1
        self.total_page = total_page

        # 3. 切片区间：第1页[0:10] 第2页[10:20] ...
        self.start = (page - 1) * per_page
        self.end = page * per_page
        self.queryset = queryset[self.start:self.end]   # 给模板用：只取当前页数据

        # 4. 页码按钮显示范围（最多 max_show 个，当前页居中）
        half_show = max_show // 2
        page_start = page - half_show
        page_end = page + half_show
        if page_start <= 1:
            page_start = 1
            page_end = max_show
        if page_end >= total_page:
            page_end = total_page
            page_start = total_page - max_show + 1
            if page_start <= 1:
                page_start = 1
        self.page_start = page_start
        self.page_end = page_end

        # 5. 拷贝 GET 参数（保留搜索条件，解决 ?q=888&page=23 的小bug）
        import copy
        self.query_dict = copy.deepcopy(request.GET)

    def _page_url(self, page_num):
        """生成带搜索条件的分页链接，如 ?q=888&page=2"""
        self.query_dict["page"] = page_num
        return "?" + self.query_dict.urlencode()

    def _hidden_fields(self):
        """除 page 外的 GET 参数生成 hidden 输入框，让跳转框也保留搜索条件"""
        items = ""
        for k, v in self.query_dict.items():
            if k == "page":
                continue
            items += '<input type="hidden" name="%s" value="%s">' % (k, v)
        return items

    def page_html(self):
        """生成分页组件 HTML（首页/上一页/页码/下一页/尾页/跳转）"""
        if self.total_count == 0:
            return ""

        html_list = []

        # 首页
        if self.page <= 1:
            html_list.append('<li class="disabled"><span>首页</span></li>')
        else:
            html_list.append('<li><a href="%s">首页</a></li>' % self._page_url(1))

        # 上一页
        if self.page <= 1:
            html_list.append('<li class="disabled"><span>上一页</span></li>')
        else:
            html_list.append('<li><a href="%s">上一页</a></li>' % self._page_url(self.page - 1))

        # 中间页码按钮
        for p in range(self.page_start, self.page_end + 1):
            if p == self.page:
                html_list.append('<li class="active"><a href="%s">%d</a></li>' % (self._page_url(p), p))
            else:
                html_list.append('<li><a href="%s">%d</a></li>' % (self._page_url(p), p))

        # 下一页
        if self.page >= self.total_page:
            html_list.append('<li class="disabled"><span>下一页</span></li>')
        else:
            html_list.append('<li><a href="%s">下一页</a></li>' % self._page_url(self.page + 1))

        # 尾页
        if self.page >= self.total_page:
            html_list.append('<li class="disabled"><span>尾页</span></li>')
        else:
            html_list.append('<li><a href="%s">尾页</a></li>' % self._page_url(self.total_page))

        # 页码跳转框（form提交，hidden字段保留搜索条件）
        jump = (
            '<li style="margin-left:8px;vertical-align:middle;">'
            '<form method="get" style="display:inline;margin:0;">'
            + self._hidden_fields() +
            '<input type="text" name="page" class="form-control" '
            'style="width:60px;height:32px;display:inline-block;padding:4px 6px;">'
            '<button type="submit" class="btn btn-default" style="height:32px;">跳转</button>'
            '</form>'
            '</li>'
        )
        html_list.append(jump)

        return mark_safe('<ul class="pagination" style="margin:0;">' + "".join(html_list) + '</ul>')

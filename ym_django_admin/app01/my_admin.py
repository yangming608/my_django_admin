from my_admin_plugin.service import v1
from app01 import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class UserInfoAdmin(v1.BaseMyAdmin):
    def edit(self,obj):  # 这个函数都是在templatetags中的my_admin_list内中调用，self传递的是v1中BaseMyAdmin对象，不是类的方法，此处的self还可以封装request
        # 反向生成url name='%s_%s_changelist'%(app_label，model_name)
        # 获取app名字和模块名,下面这种也可以
        # type(obj)._meta.app_label  这样也能够拿得到app_name
        # v1.site.namespace           这样也能够拿得到namespace
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        name_space = self.site.namespace        # 获取name_space

        url_name  = f"{name_space}:{app_label}_{model_name}_change"
        now_url = reverse(url_name,args=(obj.pk,))
        return mark_safe(f"<a href='{now_url}'>编辑</a>")

    def checkbox(self,obj):
        tag = "<input type='checkbox' />"
        return mark_safe(tag)

    list_display = [checkbox, "user", "email", edit]


v1.site.register(models.UserInfo, UserInfoAdmin)

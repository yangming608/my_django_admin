from django.shortcuts import HttpResponse, render, redirect
# from django.contrib import admin


class BaseMyAdmin(object):
    list_display = "__all__"

    def __init__(self,model_class, site):
        self.model_class = model_class
        self.site = site

    def get_urls(self):
        from django.conf.urls import url
        info = self.model_class._meta.app_label, self.model_class._meta.model_name
        urlpatterns = [
            url(r'^$', self.changelist_view, name='%s_%s_changelist' % info),
            url(r'^add/$', self.add_view, name='%s_%s_add' % info),
            url(r'^(.+)/history/$',self.history_view, name='%s_%s_history' % info),
            url(r'^(.+)/delete/$',self.delete_view, name='%s_%s_delete' % info),
            url(r'^(.+)/change/$',self.change_view, name='%s_%s_change' % info),
        ]
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls()

    # def changelist_view(self, request):
    #     data = self.model_class._meta.app_label, self.model_class._meta.model_name
    #     info = f"{data}-changelist_view"
    #     return HttpResponse(info)
    def changelist_view(self, request):
        # data = self.model_class._meta.app_label, self.model_class._meta.model_name
        result_list = self.model_class.objects.all()
        context = {
            "result_list": result_list,
            "list_display": self.list_display,
            "my_admin_obj": self
        }
        return render(request, "my_admin/change_list.html", context)

    def add_view(self,request):
        data = self.model_class._meta.app_label, self.model_class._meta.model_name
        info = f"{data}-add_view"
        return HttpResponse(info)

    def history_view(self,request,pk):
        data = self.model_class._meta.app_label, self.model_class._meta.model_name
        info = f"{data}-history_view"
        return HttpResponse(info)

    def delete_view(self,request,pk):
        data = self.model_class._meta.app_label, self.model_class._meta.model_name
        info = f"{data}-delete_view"
        return HttpResponse(info)

    def change_view(self,request,pk):
        data = self.model_class._meta.app_label, self.model_class._meta.model_name
        info = f"{data}-change_view"
        return HttpResponse(info)


class MyAdminSite(object):
    def __init__(self):
        self._registry = {}  # model_class class -> admin_class instance
        self.namespace = "my_admin_plugin"
        self.app_name = "my_admin_plugin"

    def register(self, model_class, xxx=BaseMyAdmin):
        self._registry[model_class] = xxx(model_class, self)
        """
        {
            UserInfo类：BaseMyAdmin(UserInfo类,MyAdminSite对象)
        }
        """

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace

    def get_urls(self):
        from django.conf.urls import include,url
        ret = [
            url(r'^login/$', self.login, name='login'),
            url(r'^logout/$', self.logout, name='logout'),
        ]

        for model, model_admin in self._registry.items():
            print(model._meta.app_label, model._meta.model_name)
            ret += [
                url(r'^%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]

        return ret

    def login(self, request):
        return HttpResponse("login")

    def logout(self, request):
        return HttpResponse("logout")


site = MyAdminSite()
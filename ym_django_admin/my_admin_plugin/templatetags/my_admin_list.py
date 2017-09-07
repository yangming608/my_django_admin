from django.template import Library
from types import FunctionType
from django.urls import reverse
register = Library()

def table_body(result_list, list_display, my_admin_obj):
    for row in result_list:   # row 是每一行的数据对象
        yield [name(my_admin_obj,row) if isinstance(name,FunctionType) else getattr(row, name) for name in list_display]  # 前端for循环驱动生成器

def table_head(list_display):
    for name in list_display:
        yield name.__name__.title() if isinstance(name,FunctionType) else name # 前端for循环驱动生成器

@register.inclusion_tag("my_admin/md.html")
def func(result_list, list_display, my_admin_obj):
    v = table_body(result_list, list_display, my_admin_obj)
    w = table_head(list_display)
    # for item in list_display:
    #     # print(item,ygadmin_obj.model_class)
    #     if isinstance(item,FunctionType):
    #         print(item.__name__.title())
    #     else:
    #         print(item)

    return {"xxx": v, "ooo":w}


# @register.simple_tag
# def func(result_list, list_display):
#     return "vvv"
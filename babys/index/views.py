from django.shortcuts import render
from commodity.models import *
from index.models import PersonInfo
from django.views.generic.base import TemplateView
# Create your views here.


# def indexView(request):
#     title = '首页'
#     classContent = ''
#     commodityInfos =CommodityInfos.objects.oerder_by('-sold').all()[:8]

#     types = Types.objects.all()
#     # 宝宝服饰dfdsfk
#     c1 = [x.seconds for x in types if x.firsts == '儿童服饰']
  
#     clothes = CommodityInfos.objects.filter(types_in=c1).order_by('-sold')[:5]
    
#     # 奶粉辅食
#     f1 = [x.seconds for x in types if x.firsts == '奶粉辅食']
#     food = CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[0:5]

#     # 宝宝用品
#     g1 = [x.seconds for x in types if x.firsts == '儿童用品']
#     goods = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]
     
#     return render(request, 'index.html', locals())


# def indexView(request):
#     # 使用method属性判断请求方式
#     if request.method == 'GET':
#         # 类方法的使用
#         print(request.is_secure())
#         print(request.is_ajax())
#         print(request.get_host())
#         print(request.get_full_path())
#         print(request.get_raw_url())
#         # 属性的使用
#         print(request.COOKIES)
#         print(request.content_type)
#         print(request.content_params)
#         print(request.scheme)
#         # 获取get请求的请求参数
#         print(request.GET.get('user',''))

#         return render(request, 'index.html')

#     elif request.method == 'POST':
#         # 获取post请求的请求参数
#         print(request.POST.get('user',''))
#         return render(request, 'index.html')

class indexClassView(TemplateView):
    template_name = 'index.html'
    template_engine = None
    content_type = {'title':'首页', 'classContent':''}

    # 重新定义模板上下文的获取方式
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['commodityInfos'] = CommodityInfos.objects.order_by('-sold').all()[:8]
        types = Types.objects.all()
        
        # 宝宝服饰
        c1 = [x.seconds for x in types if x in x.firsts == '儿童服饰']
        context['clothes'] = CommodityInfos.objects.filter(types__in=c1).order_by('-sold')[:5]

        # 奶粉辅食
        f1 = [x.seconds for x in types if x in x.firsts == '奶粉辅食']
        context['food'] =  CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]

        # 宝宝用品
        g1 = [x.seconds for x in types if x in x.firsts == '儿童用品']
        context['goods'] = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]

        return context
    
    def get(self, request, *args, **kwargs):
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


        


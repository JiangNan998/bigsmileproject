from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from bigsmile.models import SiteInfo,Classes,Productinfo,Product
# Create your views here.
def index(request):
    # 在这里写业务逻辑
    # 在这里读取数据库
    
    print('开始读取数据')
    # 站点基础信息
    siteInfo = SiteInfo.objects.all()[0]
    # 产品分类
    classes = Classes.objects.all()
    #全部产品
    productlist = Productinfo.objects.all()

    data = {
        "siteInfo": siteInfo,
        "classes": classes,
        "productlist": productlist
    }
    return render(request,'index.html',data)

def classes(request):
    # 站点基础信息
    siteInfo = SiteInfo.objects.all()[0]
    # 产品分类
    classes = Classes.objects.all()
    #产品列表
    try:
        choosed_id = request.GET['id']
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id)
    except:
        return redirect('/')

    if choosed:
        productlist = Productinfo.objects.filter(belong=choosed[0])
    else:
        productlist = []
    

    data = {
        "siteInfo": siteInfo,
        "classes": classes,
        "productlist": productlist
    }
    return render(request,'classes.html',data)

def product_view(request):
    return render(request,'product.html')

#product详情页
def product_detail(request, product_id):
    product = get_object_or_404(Productinfo, id=product_id)
    return render(request,'product_detail.html',{'product': product})
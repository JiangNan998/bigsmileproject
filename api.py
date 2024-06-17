from rest_framework.decorators import api_view
from rest_framework.response import Response
from bigsmile.models import Classes,Productinfo
from bigsmile.toJson import Classes_data,Productinfo_data

@api_view(['GET','POST'])
def api_test (request):
    classes = Classes.objects.all()
    classes_data = Classes_data(classes, many=True)
    productlist = Productinfo.objects.all()
    productlist_data = Productinfo_data(productlist,many=True)

    data = {
        'classes':classes_data.data,
        'productlist':productlist_data.data
    }
    return Response({'data':data})
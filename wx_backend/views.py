from django.shortcuts import render
from rest_framework.response import Response

from .models import Welcome
from django.http import JsonResponse
def welcome(request):
    # 1 查出order最大的一张图片，返回给前端
    res=Welcome.objects.all().order_by('-order').first()
    img='http://192.168.1.100:8000/media/'+str(res.img)
    return JsonResponse({'code':100,'msg':'成功','result':img})
#2 轮播图接口

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .models import Banner,Notice
from .serializer import BannerSerializer, NoticeSerializer,CollectionSerializer


class BannerView(GenericViewSet, ListModelMixin):
    queryset = Banner.objects.filter(is_delete=False).order_by('order')[:3]
    serializer_class = BannerSerializer
    def list(self,request,*args,**kwargs):
        res =super().list(request,*args,**kwargs)

        notice =Notice.objects.all().order_by("create_time").first()
        serializer = NoticeSerializer(instance=notice)
        return Response({"code":100,"msg":"成功","banner":res.data,"notice":serializer.data})


from .models import Collection
from datetime import datetime
from rest_framework.mixins import ListModelMixin,DestroyModelMixin

class CollectionView(GenericViewSet, ListModelMixin,DestroyModelMixin):
    # 查出当天的--》没过滤当前用户
    queryset = Collection.objects.all().filter(create_time__gte=datetime.now().date())
    serializer_class = CollectionSerializer

    def list(self,request,*args,**kwargs):
        res = super().list(request,*args,**kwargs)
        today_count=len(self.get_queryset())
        return Response({"code":100,"msg":"成功","result":res.data,"today_count":{today_count}})
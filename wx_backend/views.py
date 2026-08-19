from django.shortcuts import render



from .models import Welcome
from django.http import JsonResponse
def welcome(request):
    # 1 查出order最大的一张图片，返回给前端
    res=Welcome.objects.all().order_by('-order').first()
    img='http://127.0.0.1:8000/media/'+str(res.img)
    return JsonResponse({'code':100,'msg':'成功','result':img})
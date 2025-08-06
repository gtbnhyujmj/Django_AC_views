from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'index/base.html')   # <=== 記得 [APP. Name 要打上去，不然會掛掉。]
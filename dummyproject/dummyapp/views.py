from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.
def home1(request):
    obj=Place.objects.all()
    t_obj=Team.objects.all()
    return render(request,'index.html',{'p_object':obj,'team_obj':t_obj})
# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res_sum=x+y
#     res_sub=x-y
#     res_mul=x*y
#     res_div=x/y
#     return render(request,'result.html',{'number1':x,'number2':y,'sum': res_sum,'difference':res_sub,
#                                          'product':res_mul,"quotient":res_div})

# def about(request):
#     name='Raseena'
#     return render(request,'about.html',{'obj':name})
# def contact(request):
#     return HttpResponse("You are in Contact Page")
# def detail(request):
#     return render(request,'detail.html')
# def thanks(request):
#     return HttpResponse("Thank you")



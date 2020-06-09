from django.http import HttpResponse
from django.shortcuts import render

'''-------- this is coding part of python--------- '''

def home(request):
    return render(request,"index.html")
def analyze(request):

    text1=request.POST.get('text','default')
    punch=request.POST.get("removepunch","off")
    upper=request.POST.get("upper","off")
    lower=request.POST.get("lower","off")
    digit=request.POST.get("digit","off")
    #remove_extra_space=request.POST.get("removespace","off")
    if punch=="on":
        s=""
        p='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in text1:
            if i not in p:
                s=s+i
        text1=s
        
    if(upper=="on"):
        text1=text1.upper()
    if(lower=="on"):
        text1=text1.lower()
    if(digit=="on"):
        dig="";
        diglist="1234567890"
        for i in text1:
            if i in diglist:
                continue
            else:
                dig=dig+i
        text1=dig
   
    return render(request,'response.html',{"data":text1})
# def lower(request):
#     return HttpResponse(''' lower case <br> <a href="/">back to homepage</a> ''')
# def charcount(request):
#     return HttpResponse(''' char count <br> <a href="/">back to homepage</a> ''')
# def textcount(request):
#     return HttpResponse(''' text count <br> <a href="/">back to homepage</a> ''')
from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    t=datetime.datetime.now()
    d={'filter':'hai FILTERS how are yoU','t':t,'c':5}
    return render(request,'filters.html',d)

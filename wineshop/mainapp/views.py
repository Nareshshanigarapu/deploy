from django.shortcuts import render
from mainapp.forms import mywine_form
# Create your views here.



def form_view(request):
    if request.method=='POST':
        form=mywine_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Data Inserted...')
        return index_view(request)
    form=mywine_form()
    return render(request,"form.html",{'form':form})

def index_view(request):
    return render(request,'index.html')

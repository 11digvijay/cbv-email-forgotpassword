from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class laptopview(LoginRequiredMixin,View):
    def get(self,request):
        form = LaptopForm()
        context = {'form':form}
        template_name = 'Accapp/laptop.html'
        return render(request,template_name,context)
    def post(self,request):
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_lap')
        context = {'form': form}
        template_name = 'Accapp/laptop.html'
        return render(request, template_name, context)


class showlaptopview(View):
    def get(self,request):
        lap_obj = Laptop.objects.all()
        context = {'lap_obj': lap_obj}
        template_name = 'Accapp/show.html'
        return render(request, template_name, context)


class deleteview(View):
    def get(self,request,i):
        lap_obj = Laptop.objects.get(id=i)
        template_name = 'Accapp/delete.html'
        context = {'lap_obj':lap_obj}
        return render(request, template_name, context)

    def post(self,request,i):
        lap_obj = Laptop.objects.get(id=i)
        lap_obj.delete()
        return redirect('show_lap')


class updateview(View):
    def get(self,request,i):
        lap_obj = Laptop.objects.get(id=i)
        form = LaptopForm(instance=lap_obj)
        template_name = 'Accapp/laptop.html'
        context = {'form':form}
        return render(request, template_name, context)

    def post(self,request,i):
        lap_obj = Laptop.objects.get(id=i)
        form = LaptopForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect('show_lap')



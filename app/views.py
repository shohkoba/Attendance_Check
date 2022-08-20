from django.shortcuts import render, get_object_or_404, redirect
#from django.utils import timezone
from datetime import date
from .models import Child, Attendance
from .forms import AttendanceForm, ResponForm
# Create your views here.

def home(request):
    return render(request, 'app/home.html', {})

def guardian(request):
    return render(request, 'app/guardian.html', {})

def resister(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save()
            attendance.save()
            return redirect('guardian')
    else:
        form = AttendanceForm()
    return render(request, 'app/resister.html', {'form': form})

def list(request):
    childs = Child.objects.all()
    attendances = []
    for c in childs:
        attendances.append(Attendance.objects.filter(child = c).latest('date'))
    
    #attendances = Attendance.objects.filter(date = timezone.now()).order_by('child')
    return render(request, 'app/list.html', {'attendances': attendances, 'today':date.today()})

def respon(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = ResponForm(request.POST, instance=attendance)
        if form.is_valid():
            attendance = form.save()
            attendance.save()
            return redirect('list')
    else:
        form = ResponForm(instance=attendance)
    return render(request, 'app/respon.html', {'form': form, 'name': attendance.child.name})

def cfm_hist(request):
    return render()
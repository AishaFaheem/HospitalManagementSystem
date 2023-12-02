# core/views.py
from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})

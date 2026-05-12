from django.shortcuts import render, redirect
from . import forms




def EventView(request):

    if request.method == 'POST':
        form = forms.EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_event')
    else:
        form = forms.EventRegistrationForm()



    return render(request, 'add_event.html', { 'forms': form})
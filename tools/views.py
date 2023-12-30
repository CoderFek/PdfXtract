from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadPdfForm
from django.contrib import messages
from .models import Category
# from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

# Create your views here.
def linkview(request):
    return render(request, 'Link.html')

def emailview(request):
    return render(request, 'Emails.html')

def textview(request):
    return render(request, 'Text.html')

def pdfUploadView(request):
    if request.method == 'POST':
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            catg = Category.objects.get(name = category)
            form.save()
            
            # return HttpResponse('The file is saved!')


            if catg.name == 'Link':
                messages.success(request, "Links extracted successfully!!")
                return redirect('link')
            elif catg.name == 'Emails':
                messages.success(request, "Emails extracted successfully!!")
                return redirect('emails')
            elif catg.name == 'Text':
                messages.success(request, "Text extracted successfully!!")
                return redirect('text')
    else:
        form = UploadPdfForm()
    
    return render(request, 'UploadPdf.html', {'form':form})
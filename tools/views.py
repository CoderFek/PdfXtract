from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadPdfForm

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
            form.save()
            # return HttpResponse('The file is saved!')

            # category = Category.objects.get(slug = category_slug)

            if category == 'Link':
                return redirect('linkview')
            elif category == 'Emails':
                return redirect('emailview')
            elif category == 'Text':
                return redirect('textview')
    else:
        form = UploadPdfForm()
    
    return render(request, 'UploadPdf.html', {'form':form})
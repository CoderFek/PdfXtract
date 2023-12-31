from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadPdfForm
from django.contrib import messages
from .models import Category


import PyPDF2
import re
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

# Create your views here.
def extract_links(text):
    link_pattern = r'https?://\S+'
    links = re.findall(link_pattern, text)
    return links

def linkview(request):
    extracted_links = request.session.get('extracted_links', None)

    if extracted_links:
        # Clear other session variables if exists
        request.session.pop('extracted_text', None)
        request.session.pop('extracted_emails', None)

        return render(request, 'Link.html', {'extracted_links': extracted_links})
    else:
        return HttpResponse("Extracted links not found")


def extract_emails(text):
    # expression to extract email addresses from text
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails

def emailview(request):
    extracted_emails = request.session.get('extracted_emails', None)

    if extracted_emails:
        # Extract emails from the extracted text
        request.session.pop('extracted_text', None)
        request.session.pop('extracted_links', None)


        # Pass the extracted emails to the 'text.html' template
        return render(request, 'Emails.html', {'extracted_emails': extracted_emails})
    else:
        return HttpResponse("Extracted email not found")



def extract_text_from_pdf(pdf_file):
    pdf = PyPDF2.PdfReader(pdf_file)
    extracted_text = ''
    for page_num in range(len(pdf.pages)):
        page = pdf.pages[page_num]
        extracted_text += page.extract_text()
    return extracted_text

def textview(request):
    extracted_text = request.session.get('extracted_text', None)

    if extracted_text:
        request.session.pop('extracted_emails', None)
        request.session.pop('extracted_links', None)


        return render(request, 'Text.html', {'extracted_text': extracted_text})
    else:
        return HttpResponse("Extracted text not found")


def pdfUploadView(request):
    if request.method == 'POST':
        form = UploadPdfForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            catg = Category.objects.get(name = category)
            pdf_file = request.FILES['pdf']
            form.save()
            

            extracted_text = extract_text_from_pdf(pdf_file)
            extracted_links = extract_links(extracted_text)
            extracted_emails = extract_emails(extracted_text)
            # return HttpResponse(len(pdf.pages))

            if catg.name == 'Link':
                messages.success(request, "Links extracted successfully!!")
                request.session['extracted_links'] = extracted_links
                return redirect('link')
            
            elif catg.name == 'Emails':
                messages.success(request, "Emails extracted successfully!!")
                request.session['extracted_emails'] = extracted_emails
                return redirect('emails')
            
            elif catg.name == 'Text':
                messages.success(request, "Text extracted successfully!!")
                request.session['extracted_text'] = extracted_text
                return redirect('text')
                
    else:
        form = UploadPdfForm()

    return render(request, 'UploadPdf.html', {'form':form})
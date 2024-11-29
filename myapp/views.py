import uuid
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.http import FileResponse, Http404
from django.conf import settings
from .forms import FileUploadForm
from django.shortcuts import render
import os

def landing_page(requests):
    return render(requests, 'index.html')

def send(request):
    if request.method == 'POST':
        form= FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file=form.save()
            unique_link =f"http://127.0.0:8000/receive/?id={upload_file.id}"
            return render(request, 'send.html',{
                'form':form,
                'unique_link':unique_link
            })
        else:
            return render(request, 'send.html',{'form':form})
    else:
        form=FileUploadForm()
        return render(request,'send.html',{'form':form})



            
        


# Receive view
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import File

from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import File
from urllib.parse import urlparse, parse_qs

def receive(request):
    error = None

    if request.method == 'POST':
        unique_link = request.POST.get('unique_link')

        if unique_link:
            try:
                # Extract the id parameter from the URL
                parsed_url = urlparse(unique_link)
                query_params = parse_qs(parsed_url.query)
                file_id = query_params.get('id', [None])[0]  # Get the 'id' parameter
                
                if not file_id:
                    raise ValueError("Invalid link format")

                # Fetch the file object using the id
                uploaded_file = get_object_or_404(File, id=file_id)
                file_to_download = uploaded_file.file

                # Return the file for download
                response = FileResponse(file_to_download, as_attachment=True)
                return response
            except (ValueError, Http404):
                error = "Invalid or expired link. Please check and try again."
        else:
            error = "Please provide a valid link."

    return render(request, 'receive.html', {'error': error})


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        #full_file_url=settings.MEDIA_URL+ filename
        # Display a success message with the file URL
        message = f"File uploaded successfully! You can download it from: <a href='{file_url}'>here</a>."
        return render(request, 'upload_result.html', {'message': message, 'file_url': file_url})
    
    return render(request, 'upload.html')


def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'  # Trigger download
            return response
    else:
        raise Http404("File does not exist")
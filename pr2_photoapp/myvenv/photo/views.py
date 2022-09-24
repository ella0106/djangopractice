import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})

def photo_post(request):
    if request.method == "POST": # 폼 버튼이 눌려서 요청이 온건지 확인
        form = PhotoForm(request.POST)
        if form.is_valid(): # 폼이 잘 작성됐는지 체크해주는 장고 함수
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk = photo.pk)
            # redirect는 다른 페이지로 이동시켜주는 함수
    else:
        form = PhotoForm() # 폼 버튼이 아니면 폼 입력을 할 수 있도록 해줌
    return render(request, 'photo/photo_post.html', {'form': form})

def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST": # 완료버튼
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save() # 정보 저장하고 세부내용으로 이동
            return redirect('photo_detail', pk=photo.pk)
    else: # 이부분이 edit photo를 눌렀을 때 페이지 이동
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})
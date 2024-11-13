
from django.shortcuts import render, redirect
from .forms import PersonForm

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()  # 保存数据到数据库
            return redirect('person_success')  # 重定向到成功页面
    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})

def person_success(request):
    return render(request, 'person_success.html')

# Create your views here.

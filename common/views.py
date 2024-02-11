from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.decorators import login_required

def logout_view(request):
    logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

@login_required
def mypage(request):
  user = request.user
  context = {"user": user}
  return render(request, "common/mypage.html", context)
  
from django.contrib.auth import logout as auth_logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(['POST'])
def remove_account(request):
  user_pk = request.user.pk
  auth_logout(request)
  User = get_user_model()
  User.objects.filter(pk=user_pk).delete()
  return redirect('index')
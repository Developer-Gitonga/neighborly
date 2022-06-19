from django.shortcuts import redirect, render
from .models import Business, Contact, Neighborhood, Profile
from .forms import RegisterForm, ProfileEdit, BusinessForm, SearchForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    form = BusinessForm()
    searchform = SearchForm()
    if request.method=='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            neighborhood = form.cleaned_data['neighborhood']
            created = Business(image=image, name=name,email=email,neighborhood=neighborhood,user=request.user)
            created.save()
            return redirect('business')

    if request.method == 'POST':
        searchform = SearchForm(request.POST)
        if searchform.is_valid():
            name = searchform.cleaned_data['search']
            try:
                business = Business.objects.get(name=name)
                return redirect('business')
            except Exception:
                return redirect('home')


    return render(request, 'ip4/index.html',{"title":'Home','form':form,'searchform':searchform})

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user=request.user.id)
    form = ProfileEdit(instance=request.user.profile)
    
    if request.method=='POST':
        form = ProfileEdit(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'ip4/profile.html',{"title":'Profile',"profile":profile,"form":form})

@login_required(login_url='login')
def business(request):
    user = request.user
    business = Business.objects.filter(neighborhood=user.profile.neighborhood).all()
    form = BusinessForm()
    if request.method=='POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            neighborhood = form.cleaned_data['neighborhood']
            created = Business(image=image, name=name,email=email,neighborhood=neighborhood,user=request.user)
            created.save()
            
    return render(request, 'ip4/business.html',{"title":'Business/Events','form':form,"business":business,'user':user})

@login_required(login_url='login')
def contact(request):
    user = request.user
    if not user.profile.neighborhood:
        return render(request, 'ip4/emergency.html',{"title":'Emergency Contact','user':user})
    police = Contact.objects.get(name='police',neighborhood=user.profile.neighborhood)
    medics = Contact.objects.get(name='medics',neighborhood=user.profile.neighborhood)
    return render(request, 'ip4/emergency.html',{"title":'Emergency Contact','user':user,"police":police,"medics":medics})



def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    return render(request, 'registration/register.html',{"title":'Register','form':form})
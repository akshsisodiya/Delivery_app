from django.shortcuts import render, HttpResponse, redirect, Http404, get_object_or_404
from django.http import JsonResponse
from .forms import CreateUserForm,UserDetailsForm, SendParcel
from django.contrib.auth.models import auth, User
from django.contrib.auth import login,logout
from .models import UserDetail, Friend, ParcelDelivery
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from . import get_data
from django.core.mail import send_mail

@login_required(login_url='/user/login')
def index(request):
    data = get_data.index_data()
    return render(request, 'user_index.html', {'data': data, 'active_class':'home'})

@login_required(login_url='/user/login')
def profile(request):
    details = UserDetail.objects.get(username = request.user)
    order_detail_obj = ParcelDelivery.Details(request.user)
    total_orders = order_detail_obj.all_orders_details(3)
    active_orders = order_detail_obj.active_orders_details(3)
    delivered_orders = order_detail_obj.delivered_orders_details(3)
    return render(request, 'user_profile.html', {'detail':details, 'total_orders':total_orders,
                                                 'active_orders':active_orders, 'previous_orders':delivered_orders})

@login_required(login_url='/user/login')
def edit_profile(request):
    user = User.objects.get_by_natural_key(request.user)
    details = UserDetail.objects.get(username=request.user)
    if request.method == 'POST':
        resp = request.POST

        if User.objects.filter(username=resp['username']).exists() and str(resp['username']) != str(request.user):
            messages.error(request,f'This username is already taken.')

        elif User.objects.filter(email=resp['email']).exists() and str(resp['email']) != str(user.email):
            messages.error(request,'This email is already registered.')

        elif UserDetail.objects.filter(number1 = resp['number1']).exists() and str(details.number1) != str(resp['number1']):
            messages.error(request, 'This Mobile number is already registered.')

        else:
            print('success')
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.email = request.POST['email']
            user.save()
            details.number1 = request.POST['number1']
            details.number2 = request.POST['number2']
            details.address1 = request.POST['address1']
            details.address2 = request.POST['address2']
            details.city = request.POST['city']
            details.state = request.POST['state']
            details.zip = request.POST['zip']
            details.country = request.POST['country']
            details.save()
            return redirect('profile')
    return render(request,'edit_profile.html', {'details' : details})

def track_delivery(request):
    orders = ParcelDelivery.Details(request.user)
    details = orders.search(request)
    return render(request, 'order_lists.html', {'details' : details})

@login_required(login_url='/user/login')
def send_parcel(request):
    form = SendParcel
    detail = UserDetail.objects.get(username=request.user)
    if request.POST:
        form = SendParcel(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = request.user
            obj.weight = request.POST['weight'] + request.POST['weight_unit']
            obj.height = request.POST['height'] + request.POST['height_unit']
            obj.width = request.POST['width'] + request.POST['size_unit']
            obj.description = request.POST['description'] + request.POST['description']
            obj.save()
            return HttpResponse('success')
    return render(request, 'send_parcel.html', {'form':form, 'detail':detail})

def check_user(request):
    try:
        User.objects.get_by_natural_key(username=request.GET['username'])
        return JsonResponse({'available':False})
    except:
        return JsonResponse({'available':True})

def get_user(request):
    search_query = request.GET['data']
    try:
        number = int(search_query)
        try:
            n1= UserDetail.objects.get(number1 = number)
            n1= True
        except:
            n1 =False
        try:
            n2= UserDetail.objects.get(number2 = number)
            n2= True
        except:
            n2 =False

        if n1:
            users = serializers.serialize('json', UserDetail.objects.filter(number1 = number))
            data = {'found' : True, 'data' : [users]}
        elif n2:
            users = serializers.serialize('json', UserDetail.objects.filter(number2 = number))
            data = {'found' : True, 'data' : [users]}
        else:
            data = {'found' : False}
    except:
        first_name = search_query.split()[0]
        try:
            last_name = search_query.split()[1]
        except:
            last_name = ''
        e1=True if User.objects.filter(first_name__iexact=first_name, last_name__iexact=last_name).exists else False
        e2=True if User.objects.filter(first_name__iexact=first_name).exists else False
        user_found=[]
        user_obj=[]
        if e1:
            best=User.objects.filter(first_name__iexact=first_name,last_name__iexact=last_name)
            for res in best:
                user_obj.append(res)
                user_found.append(serializers.serialize('json', UserDetail.objects.filter(username=res)))
        if e2:
            second=User.objects.filter(first_name__iexact=first_name)
            for res in second:
                if res not in user_obj:
                    user_obj.append(res)
                    user_found.append(serializers.serialize('json', UserDetail.objects.filter(username=res)))
            data = {'found':True,'data':user_found}
        else:
            data = {'found':False}
    print(data)
    return JsonResponse(data)

def user_profile_show(request, username):
    user = get_object_or_404(User, username=username)
    f = Friend.objects.get(person=request.user)
    if request.method == 'POST':
        if user in f.friends.all():
            f.friends.remove(user)
        else:
            f.friends.add(user)

    detail = UserDetail.objects.get(username = user)
    is_friend = True if user in f.friends.all() else False
    return render(request, 'user_profile.html', {'detail':detail, 'is_friend':is_friend})

def requset_parcel(request):
    msg = {
        'count': 100,
        'p1':{
            'msg':'Hemllo',
            'time':'200 BC',
        },
        'p2':{
            'msg':'Wahh bhaiya full message baazi',
            'time':'31 Fab, 2069',
        }
    }
    return render(request, 'chat.html', {'msg':msg})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        if '@' in user_id:
            try:
                username = User.objects.get(email=user_id).username
            except:
                pass
        else:
            try:
                user_id= int(user_id)
                username = UserDetail.objects.get(number1=user_id).username
            except:
                username = user_id

        check = auth.authenticate(request, username=username, password=password)
        if check is not None:
            login(request,check)
            return redirect('index')
        else:
            messages.error(request, 'Invaild Credentials.')
    return render(request, 'login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form2 = UserDetailsForm
        form = CreateUserForm
        print(1)
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            number1 = request.POST['number1']

            if UserDetail.objects.filter(number1=number1).exists():
                messages.error(request, 'This Mobile number is already registered.')

            elif User.objects.filter(email=request.POST['email']).exists():
                messages.error('This email is already registered.')

            elif form.is_valid():
                user = form.save()
                user = User.objects.get_by_natural_key(request.POST['username'])
                new_row = UserDetail()
                new_row.username = user
                new_row.number1 = number1
                new_row.number2 = request.POST['number2']
                new_row.save()
                return redirect('index')
        return render(request, 'registration_form.html', {'form':form, 'form2':form2})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        raise Http404("not exist")
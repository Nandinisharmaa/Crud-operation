from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Create_notes
from django.http import JsonResponse
# Create your views here.

#view home page
try:
    def home_view(request):
        return render(request,'home.html')
except:
    print('Error')


#user registration
try:
    def registerview(request):
        """A function that will take username,email,password from user and make registration if data is sufficient."""
        if request.method=='GET':
            return render(request,'register.html')
        elif request.method=='POST':
            username=request.POST.get('uname')
            email=request.POST.get('uemail')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            #check wheather User data is already exsiting or not
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect(registerview)
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists.')
                return redirect(registerview)
            #user_data=User(email=email,username=username)
            if password1!=password2:
                #messages.info(request,'Password Does not match')
                print('password not matched')
                return HttpResponse("<script>alert('Password did not matched');window.location.href='/register'</script>")                    
            else:
                # user.set_password(password1)
                # print('password matched')  
                user=User.objects.create_user(email=email,username=username,password=password1)#creates user
                user.save()
                login(request,user)
                messages.success(request,'User registered Successfully!!')
                return redirect(create_view)
            #print(username,email)
        return render(request,'register.html')
except:
    print("Invalid form")

#user login
def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password1')
        user=authenticate(username=username,password=password)
        # if not User.objects.filter(username=username).exists():
        #     messages.warning(request,'User does not exist.')       
        if user is not None:
            login(request,user)
            return redirect(create_view)
        else:
            return HttpResponse("<h1>Login failed</h1>")
            # messages.error(request,'Invalid Username or Password')
            # return redirect(login_view)
    return render(request,'login.html')
#user logout 
def logout_view(request):
    logout(request)
    return redirect(login_view)
# view for create notes
def create_view(request):
    if request.user.is_authenticated:
        notes=request.POST.get('note')
        if notes:#it prevent from resubmitting the null data on page refreshing
            create_data=Create_notes(note=notes,)
            create_data.save()
            # return HttpResponse("<script>alert('Created');window.location.href='/create'</script>")
        else:
            error_message="All filds are required"
            print(error_message)
        show_note=Create_notes.objects.all()
        d1={'show_note':show_note}
        return render(request,'create.html',context=d1)
    else:
        return HttpResponse("<script>alert('login');window.location.href='/login'</script>")

#user data delete view
def delete_data(request,id):
    dl_data=Create_notes.objects.filter(id=id)
    dl_data.delete()
    return HttpResponse("<script>alert('Deleted');window.location.href='/create'</script>")

#user data update  view It is not fully functional
def update_view(request,id):
    d1={'id':id}
    data=Create_notes.objects.get(id=id)
    d1={'data':data}
    print(data.note)
    # o_Ndata=request.POST.get('note')
    # udata=Create_notes(note=o_Ndata)
    # udata.save()
    # return HttpResponse("<script>alert('Created');window.location.href='/create'</script>")#it prevent from resubmitting the null data on page refreshing
    return render(request,'update.html',context=d1)


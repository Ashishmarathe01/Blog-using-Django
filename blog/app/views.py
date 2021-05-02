from django.shortcuts import render,HttpResponseRedirect,redirect
from  . forms import SingUpForm,LoginForm,PostForm
from django.contrib import messages # for messgaes
from django.contrib.auth import authenticate,login,logout
from . models import Post
from django.contrib.auth.models import Group # import group for permission

# Create your views here.

# HOME
def home(request):
    post=Post.objects.all()
    return render(request,'blog/home.html',{'post':post})


# ABOUT
def about(request):
    return render(request,'blog/about.html')    



# Contact
def contact(request):
    return render(request,'blog/contact.html')        


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        user=request.user
        full_name=user.get_full_name()# method which will give full name with space  
        gps=user.groups.all()

        return render(request,'blog/dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})           
    else:
        return HttpResponseRedirect('/userlogin/')


# Login
def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"welcome ")
                    return HttpResponseRedirect('/dashboard/')
              
          
                       
        else:
            form=LoginForm()
            return render(request,'blog/login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/dashboard/')



# singup
def singup(request):
    if request.method== "POST":
        form=SingUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Succesfully Register !')
            user=form.save() # aasingin into gropup
            group=Group.objects.get(name="Author")
            user.groups.add(group)
    else:
        form=SingUpForm()
    return render(request,'blog/singup.html',{'form':form})  


# logout
def userLogout(request):
    logout(request)
    return HttpResponseRedirect("/")



# add post 
def addPost(request):
     if request.user.is_authenticated:
        if request.method == 'POST':
            form=PostForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                Desc=form.cleaned_data['Desc']
                pst=Post(title=title,Desc=Desc)
                pst.save()
                form=PostForm()
        else:
            form=PostForm()        

        return render(request,'blog/addPost.html',{'form':form})
     else:
        return HttpResponseRedirect("/userlogin/")    
      

# update post 
def updatePost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)        
        return render(request,'blog/updatePost.html',{'form':form})
    else:
        return HttpResponseRedirect('/userlogin/')            

# delete  post 
def deletePost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect('/userlogin/')                    
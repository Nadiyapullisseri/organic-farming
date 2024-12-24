from audioop import reverse
from urllib import response
from . import forms,models
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import Customer
from .forms import CustomerUserForm
from .forms import CustomerForm
from .forms import Farmer
from .forms import FarmerUserForm
from .forms import FarmerForm
from .forms import ProductForm
from .forms import Product
from .forms import FeedbackForm
from .forms import QueryForm
from .forms import Query
from .forms import NoticeForm
from .forms import PaymentForm




from django.contrib.auth.models import User




from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydic={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group=Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'register.html',context=mydic)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid credentials.")
    return render(request,'login.html')

def dashboard_view(request):
    return render(request,'dashboard.html')


def farmer_register(request):
    userForm=forms.FarmerUserForm()
    farmerForm=forms.FarmerForm()
    mydic={'userForm':userForm,'farmerForm':farmerForm}
    if request.method=='POST':
        userForm=forms.FarmerUserForm(request.POST)
        farmerForm=forms.FarmerForm(request.POST,request.FILES)
        if userForm.is_valid() and farmerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            farmer=farmerForm.save(commit=False)
            farmer.user=user
            farmer.save()
            my_farmer_group=Group.objects.get_or_create(name='FARMER')
            my_farmer_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'farmer_register.html',context=mydic)


def farmer_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('farmer-dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid credentials.")
    return render(request,'farmer_login.html')

def farmer_dashboard_view(request):
    profile = get_object_or_404(Farmer,user=request.user)
    print(profile)
    return render(request,'farmer-dashboard.html',{'profile':profile})

def admin_login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin-dashboard')  # Redirect to dashboard
        else:
            messages.error(request, "Invalid credentials.")
    return render(request,'admin_login.html')

def admin_dashboard_view(request):
    return render(request,'admin_dashboard.html')

def admin_users_view(request):
    customers=models.Customer.objects.all()
    print(customers)
    return render(request,'admin-users.html',{'customers':customers})

def admin_farmers_view(request):
    farmers=models.Farmer.objects.all()
    return render(request,'admin-farmers.html',{'farmers':farmers})

def admin_feedback_view(request):
    feedbacks=models.Feedback.objects.all()
    return render(request,'admin-feedback.html',{'feedbacks':feedbacks})

def update_admin_users_view(request,pk):
    customeruser = Customer.objects.get(id=pk)
    user = User.objects.get(id=customeruser.user_id)
    userForm = CustomerUserForm(instance=user)
    customerForm = CustomerForm(instance=customeruser)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method == 'POST':
        userForm = CustomerUserForm(request.POST,request.FILES,instance=user)
        customerForm = CustomerForm(request.POST,request.FILES,instance=customeruser)
        if customerForm.is_valid() and userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('admin-users')
    return render(request,'update-admin-users.html',context=mydict)

def delete_admin_users_view(request,pk):
    customers = Customer.objects.get(id=pk)
    customers.delete()
    return redirect('admin-users')

def update_admin_farmers_view(request,pk):
    farmeruser = Farmer.objects.get(id=pk)
    user = User.objects.get(id=farmeruser.user_id)
    userForm = FarmerUserForm(instance=user)
    farmerForm = FarmerForm(instance=farmeruser)
    mydict={'userForm':userForm,'farmerForm':farmerForm}
    if request.method == 'POST':
        userForm = FarmerUserForm(request.POST,request.FILES,instance=user)
        farmerForm = FarmerForm(request.POST,request.FILES,instance=farmeruser)
        if farmerForm.is_valid() and userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            farmerForm.save()
            return redirect('admin-farmers')
    return render(request,'update-admin-farmers.html',context=mydict)

def delete_admin_farmers_view(request,pk):
    farmers = Farmer.objects.get(id=pk)
    farmers.delete()
    return redirect('admin-farmers')

def farmer_product_view(request):
    products=models.Product.objects.all()
    print(products)
    return render(request,'farmer-product.html',{'products':products})

def farmer_add_product_view(request):
    productForm=forms.ProductForm()
    if request.method == 'POST':
        productForm = ProductForm(request.POST,request.FILES)
        if productForm.is_valid():
            productForm.save()
            return HttpResponseRedirect('farmer-product')
    else:
        productForm = ProductForm()
    return render(request,'farmer-add-product.html',{'productForm':productForm})  

def edit_farmer_product_view(request,pk):
    products = Product.objects.get(id=pk)
    productForm = ProductForm(instance=products)
    if request.method == 'POST':
        productForm = ProductForm(request.POST,request.FILES,instance=products)
        if productForm.is_valid():
            productForm.save()
            return redirect('farmer-product')
    return render(request,'edit-farmer-product.html',{'productForm':productForm})

def delete_farmer_product_view(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('farmer-product')

def customer_product_view(request):
    products = Product.objects.all()
    return render(request,'customer-product.html',{'products':products})

def customer_feedback_view(request):
    feedbackForm=forms.FeedbackForm()
    if request.method == 'POST':
        feedbackForm = FeedbackForm(request.POST)
        if feedbackForm.is_valid():
            feedbackForm.save()
            return HttpResponseRedirect('dashboard')
    else:
        feedbackForm = FeedbackForm()
    return render(request,'customer-feedback.html',{'feedbackForm':feedbackForm})

def farmer_query_view(request):
    try:
        farmer=Farmer.objects.get(user=request.user)
        print(farmer)
    except:
        return redirect('error-page')
    if request.method == 'POST':
        queryForm = QueryForm(request.POST)
        if queryForm.is_valid():
            question=queryForm.save(commit=False)
            question.farmer=farmer
            question.save()
            return redirect('question-view')
    else:
        queryForm = QueryForm()
    return render(request,'farmer-query.html',{'queryForm':queryForm})

def error_page_view(request):
    return render(request,'error-page.html')

def question_view(request):
    farmer=models.Farmer.objects.get(user=request.user)
    questions=models.Query.objects.all().filter(farmer=farmer)
    return render(request,'questions-view.html',{'questions':questions,'farmer':farmer})

def admin_query_view(request):
    querys=models.Query.objects.all()
    return render(request,'admin-querys-view.html',{'querys':querys})

def update_admin_query_view(request,pk):
    queries = Query.objects.get(id=pk)
    queryForm = QueryForm(instance=queries)
    if request.method == 'POST':
        queryForm = QueryForm(request.POST,instance=queries)
        if queryForm.is_valid():
            replay=request.POST.get('replay')
            queries = queryForm.save(commit=False)
            queries.replay=replay
            queries.save()
            return redirect('admin-query')
    return render(request,'update-admin-query.html',{'queryForm':queryForm})

def admin_notices_view(request):
    noticeForm=forms.NoticeForm()
    if request.method == 'POST':
        noticeForm = NoticeForm(request.POST)
        if noticeForm.is_valid():
            noticeForm.save()
            return HttpResponseRedirect('admin-dashboard')
    else:
        noticeForm = NoticeForm()
    return render(request,'admin-notice.html',{'noticeForm':noticeForm})


def farmer_notice_view(request):
    notice=models.Notice.objects.all()
    return render(request,'farmer-notice-view.html',{'notice':notice})

def admin_notice_view(request):
    message=models.Notice.objects.all()
    return render(request,'admin-notice-view.html',{'message':message})



def add_to_cart_view(request,pk):
    products = models.Product.objects.all()
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter = product_ids.split('|')
        product_count_in_cart = len(set(counter))
    else:
        product_count_in_cart = 1
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    response = render(request,'customer-product.html',{'products':products,'product_count_in_cart':product_count_in_cart})
    if 'product_ids' in request.COOKIES:
        product_ids =request.COOKIES['product_ids']
        if product_ids == "":
            product_ids =str(pk)
        else:
            product_ids = product_ids + "|" + str(pk)
        response.set_cookie('product_ids',product_ids)
    else:
        response.set_cookie('product_ids',pk)
    
    product = models.Product.objects.get(id=pk)
    messages.info(request,product.product_name + 'added to cart successfully!')
    return response

def cart_page_view(request):
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    products=None
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids =request.COOKIES['product_ids']
        if product_ids != "":
            product_id_in_cart=product_ids.split('|')
            products=models.Product.objects.all().filter(id__in = product_id_in_cart)
            
            for p in products:
                total=total+p.product_price
    return render(request,'cart-page.html',{'products':products,'total':total,'product_count_in_cart':product_count_in_cart})



def remove_from_cart_view(request,pk):
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    
    total=0
    if 'product_ids' in request.COOKIES:
        product_ids =request.COOKIES['product_ids']
        product_id_in_cart=product_ids.split('|')
        product_id_in_cart=list(set(product_id_in_cart))
        product_id_in_cart.remove(str(pk))
        products=models.Product.objects.all().filter(id__in = product_id_in_cart)
        for p in products:
            total=total+p.product_price
            
        value=""
        for i in range(len(product_id_in_cart)):
            if i==0:
                value=value+product_id_in_cart[0]
            else:
                value=value+"|"+product_id_in_cart[i]
        response = render(request,'cart-page.html',{'products':products,'total':total,'product_id_in_cart':product_id_in_cart})
        if value=="":
            response.delete_cookie('product_ids')
        response.set_cookie(product_ids,value)
        return response
    
def cart_pay_view(request):
    paymentForm=forms.PaymentForm()
    if request.method == 'POST':
        paymentForm = PaymentForm(request.POST)
        if paymentForm.is_valid():
            paymentForm.save()
            return HttpResponseRedirect('payment-page')
    else:
        paymentForm = PaymentForm()
    return render(request,'cart-pay.html',{'paymentForm':paymentForm}) 

def payment_page_view(request):
    return render(request,'payment-page.html')

def admin_payment_view(request):
    payment=models.Payment.objects.all()
    return render(request,'admin-payment-view.html',{'payment':payment})

def cart_search_view(request):
    query = request.GET['query']
    products=models.Product.objects.all().filter(product_name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
    word="search Result :"
    
    if request.user.is_authenticated:
        return render(request,'customer-product.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})
    return render(request,'customer-product.html',{'products':products,'word':word,'product_count_in_cart':product_count_in_cart})

def contact_us_view(request):
    return render(request,'contact-us.html')

def customer_logout_view(request):
    return render(request,'index.html')

def farmer_logout_view(request):
    return render(request,'index.html')

def admin_logout_view(request):
    return render(request,'index.html')

def farmer_profile_view(request,id):
    profile=get_object_or_404(Farmer,id=id)
    return render(request,'farmer-profile.html',{'profile':profile})
    
    


            





    
    

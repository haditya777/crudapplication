from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime 
from ProjectApp.models import Register,Products,UserCart
from django.urls import path
from django.contrib import messages
from passlib.hash import pbkdf2_sha256

# Create your views here.
def index(request):
    print('index')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password=request.POST.get('password') 
        usertype=request.POST.get('usertype')
        encryptpass=pbkdf2_sha256.encrypt(password,rounds=12000,salt_size=32)       
        register = Register( name = name, email = email,password=encryptpass,usertype=usertype,date = datetime.today()) 
        register.save()
    return render(request,'index.html')

def redirectlogin(request):
    products = Products.objects.all()
    return render(request,'userproduct.html',{'productlist':products})

def login(request):
    if request.method == 'GET':
        print('user')
        email = request.GET.get('email1')
        password=request.GET.get('password1')
        userList = Register.objects.all()
        print(email)
        print(password)
        print(userList)
        for user in userList:
            print(user.email)
            print(user.usertype)
            if user.email==email:
                print(user.usertype)
                verify = pbkdf2_sha256.verify(password,user.password)
                #print(verify)
                if verify==True and user.usertype=='User':
                    print('userType-'+user.usertype)
                    productList = Products.objects.all()
                    print(productList)
                    return render(request,'userproduct.html', {'productlist':productList})
                elif verify==True and user.usertype=='Admin':
                    productList = Products.objects.all()
                    return render(request,'adminproduct.html', {'productlist':productList})
                else:
                    messages.error(request, 'password not correct')
                    return render(request,'index.html')            
            
        messages.error(request, 'Username not correct')  
        return render(request,'index.html')  
    return render(request,'index.html')



def adminproduct(request):
    return (request,'adminproduct.html')
#
#def userproduct(request):
#    return (request,'userproduct.html')    

def addproducts(request):
    if request.method == 'POST':
        srno= request.POST.get('srno')
        images = request.POST.get('images')
        productname=request.POST.get('productname') 
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        status=request.POST.get('status')
        print(srno)
        product = Products( srno = srno, images = images,productname=productname,price=price,totalquantity=quantity,status=status,remainingquantity=quantity,date = datetime.today()) 
        print(product)
        product.save()

    return render(request,'addproducts.html')

def selectproduct(request):
    Product1=Products.objects.all()
    return render(request,'selectproduct.html',{'product1':Product1})

def update(request):
    srno = request.POST.get('editButton')
    srno = int(srno)
    print('hola '+ str(srno))
    products = Products.objects.all()

    for product in products:
        print('yehi'+ str(product.srno))
        print(type(product.srno))
        if product.srno == srno:
            currProduct = product
            #print('curr'+currProduct)
            break

    return render(request,'editproduct.html', {'product':currProduct})

def update1(request):
    
    if request.method=='POST':
        
        srno = request.POST.get('srno')
        srno = int(srno)
        images = request.POST.get('images')
        productname=request.POST.get('productname') 
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        status=request.POST.get('status')    
        products = Products.objects.all()
        print('name is '+ productname)
        for product in products:  
            if product.srno == srno:
                #currProduct = product
                print('yahapr')
                product.images = images
                product.price = price
                product.totalquantity = quantity
                product.productname = productname
                product.status = status
                product.save()
                break
        messages.success(request,'Successfuly Updated')
        return render(request,'selectproduct.html', {'product1':products})

def delete(request):
    srno = request.POST.get('deleteButton')
    srno = int(srno)
    entry = Products.objects.all()
    for product in entry:
        if product.srno ==srno:
            product.delete()
            break
    entry = Products.objects.all()
    messages.success(request,'Successfuly deleted')
    return render(request,'selectproduct.html',{'product1':entry})    

def add_to_cart(request):
    print('add_to_cart')
    if request.method =='POST':
        userid = request.POST.get('userid')
        quantity = request.POST.get('quantity')
        #productid=UserCart()
        userCart = UserCart(UserId = userid, productid=0, quantity=quantity)
        userCart.save()
        messages.success(request,'successfully added')    
    return render(request,'userproduct.html')

def cart(request):
    return render(request,'cart.html' )

#        if request.user.is_authenticated():
#            try:
#                item = Products.objects.get(pk=products.srno)
#            except ObjectDoesNotExist:
#                pass
#            else :
#                try:
#                    cart = Cart.objects.get(user = request.user, active = True)
#                except ObjectDoesNotExist:
#                    cart = Cart.objects.create(user = request.user)
#                    cart.save()
#                    cart.add_to_cart(book_id)
#                    return redirect('cart')
#                else:
#                    return redirect('index')
#
#
#def remove_from_cart(request, book_id):
#    if request.user.is_authenticated():
#        try:
#            book = Book.objects.get(pk = book_id)
#        except ObjectDoesNotExist:
#            pass 
#        else:1
#    quantity=request.GET.get('quantity')
#    status=request.GET.get('status')
#    productlist=AddProducts.objects.all()

    #return render(request,'cart.html')



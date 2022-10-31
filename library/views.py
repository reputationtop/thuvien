from asyncio.windows_events import NULL
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import json
import os 
import collections
from collections import Counter
import datetime
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages #imports
from django.http import JsonResponse
from .models import User, Book, Category, Email,Listing ,active_all
import time
from .forms import CategoryForm, NewbookForm, NewemailForm , CommentsForm, CategoryForm
import array as arr 
from datetime import date
import datetime





def index(request):

    # print(Book.objects.all())
    if request.user.is_superuser:
        all_book = Book.objects.all().order_by("-timeb")

    else:
        # thisbook =Book.objects.exclude(numbe_book=0,dele_book = True).order_by("-timeb")
        all_book = Book.objects.exclude(numbe_book=0,dele_book = True).order_by("-timeb")
        # for lis_t in thisbook :
        #     all_book = all_book.update(lis_t)
        #     n += 1
        #     if sum > 5:
        #         break
        # all_book = arr.array(0, thisbook)

    if request.user.is_authenticated:
        user = request.user
        out_read = offer_book(user.id)
    else:
        out_read = offer_book( None)
    # print("is book")
    # print(out_read) 
    paginator = Paginator(all_book, 12)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, "library/index.html", {
        "books": books,
        "out_read":out_read
    })

def offer_book(user_id):
    b = []
    cz = []
    if user_id is not None:
        users = User.objects.get(pk=user_id)


        list_add = Listing.objects.filter(user=users).order_by("-timel")[:10]
        if list_add is not None:
            list_add = Listing.objects.all().order_by("-timel")
            for list in list_add :
                
                mylist = list.item.category.all()
                b += mylist
        else:
            for list in list_add :
                
                mylist = list.item.category.all()
                b += mylist
    else:
        list_add = Listing.objects.all().order_by("-timel")
        for list in list_add :
            
            mylist = list.item.category.all()
            b += mylist
    mystring_b =str( ",".join([str(char) for char in b]))
    print("test")
    len_xyz = len(Counter(mystring_b.split(",")))
    zyx =  Counter(mystring_b.split(","))
    print(zyx)
    if len_xyz <= 5 :
        for i in range(len_xyz):
            cz.append(zyx.most_common()[i][0])
    else: 
        for i in range(5):
            cz.append(zyx.most_common()[i][0])
    # print(c)

    x = []
    all_book = Book.objects.all()
    for i_a in cz:
        category_id = Category.objects.get(name = i_a)
        all_book = all_book.filter( category=category_id.id ).order_by("-timeb")

        for i in all_book:
            x.append(i)
    y = set(x[:10])
    # print(x)
    return y
    
        
csrf_exempt
def BookSearchView(request):
    search = request.GET.get('search')
    if request.user.is_superuser:
        all_book = Book.objects.filter(namebook__icontains=search).order_by("-timeb")

    else:
        all_book = Book.objects.filter(namebook__icontains=search).exclude(numbe_book=0,dele_book = True).order_by("-timeb")
    paginator = Paginator(all_book, 12)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, "library/index.html", {
        "books": books
    })
@csrf_exempt
@login_required(login_url='login')
def newcategory(request):
        if request.method == 'POST':
            name_category = request.POST["new_category"]
            new_category = Category.objects.create(name=name_category)
            new_category.save()
            reasons = "thêm thể loại mới"
            active_a = active_all.objects.create(performer=request.user,subject_active=request.user,category = new_category, reason = reasons)
            active_a.save()
            
            
            messages.success(request, 'Đã thêm thể loại thành công')
            return HttpResponseRedirect(reverse("categories"))
def categories(request):
    return render(request, "library/categories.html", {
        "Category_Form" :CategoryForm(),
        "categories": Category.objects.all().order_by('name'),
    })
def category(request, category_id):
    
    if request.user.is_superuser:
        all_book = Book.objects.filter(category=category_id).order_by("-timeb")

    else:
        all_book = Book.objects.filter(category=category_id).exclude(numbe_book=0,dele_book = True).order_by("-timeb")
    return render(request, "library/category.html", {
        "category": Category.objects.get(pk=category_id),
        "books": all_book
    })
    
    
    


@csrf_exempt
@login_required
def newbook(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = NewbookForm(request.POST ,request.FILES)
            form.save
            if form.is_valid():
                new_book = form
                reasons = "thêm sách mới vào kho"
                active_a = active_all.objects.create(performer=request.user,subject_active=request.user,item = new_book, reason = reasons)
                active_a.save()
                return HttpResponseRedirect(reverse("book", args=(new_book.pk,)))
            
        else:
            form = NewbookForm()
        return render(request, "library/newbook.html", {
            "form": form
        })
    else:
        messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
        return HttpResponseRedirect(reverse("index"))
@csrf_exempt
@login_required(login_url='login')
def del_book(request, book_id):
    book_del = Book.objects.filter(pk=book_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user.is_superuser:
                book_del.dele_book = True
                reasons = "xóa sách"
                active_a = active_all.objects.create(performer=request.user,subject_active=request.user,item = book_del,reason = reasons)
                active_a.save()
                book_del.save
                messages.success(request, 'Đã ẩn sách khoi thu vien')
                return HttpResponseRedirect(reverse("index"))  
        else:
            messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
            return HttpResponseRedirect(reverse("index"))
    messages.error(request, 'hãy thử lại')
    return HttpResponseRedirect(reverse("index"))





@login_required(login_url='login')
def Is_listing(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            list_add = Listing.objects.filter(active=False, dele_listing=False)
            list_in = Listing.objects.filter(active=True , dele_listing=False)
            return render(request, "library/list_add.html", {
                "list_add": list_add,
                "list_in": list_in,
            })
        else:
            list_add = Listing.objects.filter(user=request.user, active=False , dele_listing=False)
            list_in = Listing.objects.filter(user=request.user, active=True, dele_listing=False)
            return render(request, "library/list_add.html", {
                "list_add": list_add,
                "list_in": list_in,
            })
            
            
@login_required(login_url='login')    
def In_listing(request, listing_id):
    list = Listing.objects.get(pk=listing_id)
    if request.user.is_superuser:
        
        return render(request, "library/in_listing.html", {
            "list": list,
        })
    elif list.user == request.user:
        return render(request, "library/in_listing.html", {
            "list": list,
        })
    else:
        messages.error(request, 'Bạn chỉ có thể kiểm tra danh sách của bản thân')
        return Is_listing(request)
@login_required(login_url='login')
def NewListing(request, book_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.is_superuser:
                messages.error(request, 'bạn phải đăng nhập tài khoản hocj sinh để thực hiện thao tác này')
                return HttpResponseRedirect(reverse("book", args=(book_id,)))
            
            book = Book.objects.get(pk=book_id)
            
            try:
                listing = Listing.objects.get(item=book, user=request.user,dele_listing=False)
                messages.error(request, 'Hãy kiểm tra lại ')
                return HttpResponseRedirect(reverse("book", args=(book_id,)))
            except Listing.DoesNotExist:
                if book.numbe_book >= 1:
                    
                    User_acc =  request.user
                    if User_acc.money < book.bid :
                        messages.error(request, 'Bạn không đủ tiền hãy naph thêm ')
                        return HttpResponseRedirect(reverse("book", args=(book_id,)))
                    if User_acc.limit_book < 1:
                        messages.error(request, 'Bạn đã đạt giới hạn sách có thể mượn ')
                        return HttpResponseRedirect(reverse("book", args=(book_id,)))
                    User_acc.money = User_acc.money - book.bid
                    
                    listing = Listing.objects.create(item=book,user=request.user,active=False,)
                    User_acc.limit_book = User_acc.limit_book -1
                    book.numbe_book = book.numbe_book - 1
                    reasons = "Đã them sách vao danh sach muon"
                    
                    active_a = active_all.objects.create(performer=request.user, subject_active = request.user,item = book,money_flow = -book.bid,money_now=User_acc.money, classify_active = 2,reason = reasons)
                    active_a.save()
                    User_acc.save()
                    book.save()
                    listing.save()
                    messages.success(request, 'Đã them vao danh sach muon')
                    return HttpResponseRedirect(reverse("book", args=(book_id,)))
                else:
                    messages.error(request, 'sách này đã được đăng kí hết')
                    return HttpResponseRedirect(reverse("book", args=(book_id,)))
# active_all = active_all.objects.create(performer=book,subject =,item =,category =,money_flow =,reason =)
@csrf_exempt
@login_required(login_url='login')
def change_listing(request, listing_id):
    if request.method == "POST":
        if request.user.is_superuser:
            listing = Listing.objects.get(pk=listing_id)
            book = listing.item
            if"change" in request.POST:
                date = int(request.POST["num_date"])
                x = datetime.datetime.now()
                listing.convert_date = x + datetime.timedelta(days=date)

                if book.bid <= 30000: 
                    listing.bid_date = 300
                else:
                    
                    listing.bid_date = (listing.item.bid /100)
                if date >=7 and date <= 90:
                    listing.action_bid = round(((date//7)*4 + (date%7)/(2/3))*listing.bid_date, -2)
                elif date<7 and date :
                    listing.action_bid = round(((date//7)*4 + (date%7)/(2/3))*listing.bid_date, -2)
                else:
                    messages.error(request, 'Lỗi hãy thử lại')
                                           
                    return Is_listing(request)
                
                reasons = "Đã them sách vao danh sach muon"
                
                active_a = active_all.objects.create(performer=request.user, subject_active = request.user,item = book,money_flow = -book.bid,money_now=User_acc.money, classify_active = 2,reason = reasons)
                active_a.save()
            
                
                
                book.save()
                listing.active = True
                listing.save()
                messages.success(request, 'Đã  thành công')  
                return Is_listing(request)
            else:
                messages.error(request, 'Lỗi hãy thử lại')
                return Is_listing(request)
        else:
            messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
            return Is_listing(request)
                    # reasons = "Đã them sách vao danh sach muon"
                    # active_a = active_all.objects.create(performer=request.user,item = book,money_flow = -book.bid,reason = reasons)
                    # active_a.save()
@csrf_exempt
@login_required(login_url='login')
def close_listing(request):
    if request.method !="PUT":
        return JsonResponse({"error": " PUT request required"}, status=400)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.user.is_superuser:
        try:
            data = json.loads(request.body)
            listing_id = data.get("list_id","")
            listing = Listing.objects.get(pk=listing_id)
            user_listing = listing.user
            book_listing = listing.item
            book = Book.objects.get(id = book_listing.id)
            users = User.objects.get(username = user_listing.username)
            if Listing.objects.get(pk=listing_id) is None:
                messages.error(request, 'Không tìm thấy danh sách') 
                if"close_cation" in request.PUT:
                    return HttpResponseRedirect(reverse("views_active_book", args=(user_listing.id,)))
                elif"close_lis":
                    return Is_listing(request)
                else:
                    return HttpResponseRedirect(reverse("index"))
                # return JsonResponse({"error": "Không tìm thấy danh sách"})
                # return HttpResponseRedirect(reverse("index"))
            else:
                a = Listing.objects.get(pk=listing_id)
                if a.dele_listing == True:
                    messages.error(request, 'Danh sách này đã kết thúc chu trình cho mượn') 
                    if"close_cation" in request.PUT:
                        return HttpResponseRedirect(reverse("views_active_book", args=(user_listing.id,)))
                    elif"close_lis":
                        return Is_listing(request)
                    else:
                        return HttpResponseRedirect(reverse("index"))
                    
                    
            if listing.active == False:
                
                listing.return_date = datetime.datetime.now()
                book.numbe_book = book.numbe_book + 1
                users.money = users.money + book.bid
                users.limit_book = users.limit_book +1
                reasons = "Ket thuc hanh dong muon"
                active_a = active_all.objects.create(performer=request.user,subject_active =users,item =book,money_flow = book.bid,reason =reasons)

                listing.dele_listing = True
                # return Is_listing(request)
            else:
                listing.return_date = datetime.datetime.now()
                x = book.bid - listing.money_listing()
                if x>0:
                    users.money = users.money + x
                else:
                    users.money = users.money
                book.numbe_book = book.numbe_book + 1
                users.limit_book = users.limit_book +1
                reasons = "Ket thuc hanh dong muon"
                active_a = active_all.objects.create(performer=request.user,subject_active =users,item =book,money_flow = book.bid,money_now=users.money,reason =reasons)
                listing.dele_listing = True
            active_a.save()  
            users.save()
            book.save()
            listing.save()
            if"close_cation" in request.PUT:
                return HttpResponseRedirect(reverse("views_active_book", args=(user_listing.id,)))
            elif"close_lis":
                return Is_listing(request)
            else:
                return HttpResponseRedirect(reverse("index"))
        except Listing.DoesNotExist:
            # return JsonResponse({"error": "Hãy kiểm tra lại"})
            messages.error(request, 'Hãy kiểm tra lại ')
            if"close_cation" in request.PUT:
                return HttpResponseRedirect(reverse("views_active_book", args=(user_listing.id,)))
            elif"close_lis":
                return Is_listing(request)
            else:
                return HttpResponseRedirect(reverse("index"))

    else:
        if listing.active == False:
            book.numbe_book = book.numbe_book + 1
            users.limit_book = users.limit_book +1
            users.money = users.money + book.bid -1000
            listing.dele_listing = True
            reasons = "Ket thuc hanh dong muon"
            active_a = active_all.objects.create(performer=request.user,subject_active =users,item =book,money_flow = book.bid,money_now=users.money,reason =reasons)
            active_a.save()   
            users.save()
            book.save()
            listing.save()
            return JsonResponse({"message": "Đã xóa khỏi danh sách làm việc thành công"})
            # messages.success(request, 'Đã xóa khỏi anh sách thành công') 
            # return Is_listing(request)
        else:
            return JsonResponse({"error": "Bạn cần đến thư viện thì mới có thể trả sách"})
            # messages.error(request, 'Bạn cần đến thư viện thì mới có thể trả sách') 
            # return Is_listing(request)
                    

    

@login_required(login_url='login')
def changelike(request, book_id):
    if request.method == "POST":
        user = request.user
        book = Book.objects.get(pk=book_id)
        if book.is_in_listlike(user):
            book.likes.remove(user)
        else:
            book.likes.add(user)
        
        return HttpResponseRedirect(reverse("book", args=(book_id,)))

        #     book = Book.objects.get(pk=book_id)
        # if book.is_in_listlike(request.user):
        #     book.likes.remove(request.user)
        # else:
        #     book.likes.add(request.user)
        
        # return HttpResponseRedirect(reverse("book", args=(book_id,)))
        classify_active =1
def is_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    
    comments = book.active_comments.filter(classify_active =1).order_by("-time_2")
    total_coments = comments.count()
    if request.user.is_authenticated:
        is_in_listlike = book.is_in_listlike(request.user)
        try:
            listing = Listing.objects.get(item=book, user=request.user, dele_listing= False )
            is_in_list = True
        except Listing.DoesNotExist:
            listing = None
            is_in_list = False
        
        # listing = Listing.objects.get(item=book, user=request.user)
        # if not listing:
        #     is_in_list = False
        # else:
        #     is_in_list = True

            
    else:
        is_in_listlike = False
        listing = None
        is_in_list = None
        
    return render(request, "library/is_book.html", {
        "book": book,
        "comment_form" :CommentsForm(),
        "book_id": book_id,
        "comments": comments,
        "total_coments": total_coments,
        "is_in_listlike": is_in_listlike,
        "listing": listing,
        # "active_l": active_l,
        "is_in_list": is_in_list,
        "user": request.user,
    })
@login_required(login_url='login')
def all_user(request):
    
    
    if request.user.is_superuser:
        studen = User.objects.filter(is_superuser=False)
        teacher = User.objects.filter(is_superuser=True)
    else:
        messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
        return HttpResponseRedirect(reverse("index"))
    return render(request, "library/list_human.html", {
        "studen": studen,
        "teacher": teacher,
    })
csrf_exempt
@login_required(login_url='login')
def UserSearchView(request):
    search = request.GET.get('search_user')

    if request.user.is_superuser:
        teacher = User.objects.filter(username__icontains=search , is_superuser=True).order_by("-date_joined")
        studen = User.objects.filter(username__icontains=search ,is_superuser=False).order_by("-date_joined")

    else:
        messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
        return HttpResponseRedirect(reverse("index"))
    return render(request, "library/list_human.html", {
        "studen": studen,
        "teacher": teacher,
    })
# active_all = active_all.objects.create(performer=book,subject =,item =,category =,money_flow =,reason =)
@login_required(login_url='login')
def add_comment(request, book_id):
    
    if request.method == 'POST':
        book = Book.objects.get(pk=book_id)
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.instance.performer = request.user
            form.instance.subject_active =request.user
            form.instance.item = book
            form.instance.classify_active = 1

            form.save()
            messages.success(request, 'Đã thêm nhận xét thành công')
            return HttpResponseRedirect(reverse("book", args=(book_id,)))
csrf_exempt
@login_required(login_url='login')
def mailbook(request ):
    user_profile = request.user
    mysent_mail = Email.objects.filter( author=user_profile, archived=False)
    in_mail = Email.objects.filter(recipients=user_profile, archived=False)
    a_mysent_mail = Email.objects.filter( author=user_profile, archived=True)
    a_in_mail = Email.objects.filter(recipients=user_profile, archived=True)
    if request.method =="POST":
        maill = NewemailForm(request.POST)
        if maill.is_valid():
            maill.instance.author = request.user
            maill.save()
            maill = NewemailForm()
            return render(request, "library/mail.html", {
                "in_mail": in_mail,
                "mysent_mail": mysent_mail,
                "a_mysent_mail":a_mysent_mail,
                "a_in_mail": a_in_mail,
                "maill": maill,
            })
    else: 
        # If a GET (or any other method), we'll create a blank form
        maill = NewemailForm()
    return render(request, "library/mail.html", {
        "mysent_mail": mysent_mail,
        "in_mail": in_mail,
        "a_mysent_mail":a_mysent_mail,
        "a_in_mail": a_in_mail,
        "maill": maill
    })
    
    
@login_required(login_url='login')
def read_mail(request, email_id):
    user = request.user
    email =  Email.objects.get(pk=email_id)
    if user == email.recipients:
        if email.read == False:
            email.read = True
            email.save()
        return render(request, "library/is_read_mail.html", {
            "email": email,
        })
    
    elif user == email.author:
        return render(request, "library/is_read_mail.html", {
            "email": email,
        })
    else:
        messages.error(request, 'khong ìm thấy thư')
        return HttpResponseRedirect(reverse("mailbook"))
@login_required(login_url='login')
def archive_email(request,email_id):
    email =  Email.objects.get(pk=email_id)
    user = request.user
    if user == email.recipients:
        if email.archived == False:
            email.archived = True
            email.save()
        else:
            email.archived = False
            email.save()
        return HttpResponseRedirect(reverse("read_mail", args=(email_id,)))
    messages.error(request, 'chỉ tài khoản nhận tin mới đc lưu trữ')
    return HttpResponseRedirect(reverse("read_mail", args=(email_id,)))
    
    
@login_required(login_url='login')
def newemail(request):
    # if request.user.is_authenticated:
    #     if request.user.is_superuser:
    if request.method =="POST":
        user_profile = request.user
        mysent_mail = Email.objects.filter( author=user_profile, archived=False)
        in_mail = Email.objects.filter(recipients=user_profile, archived=False)
        a_mysent_mail = Email.objects.filter( author=user_profile, archived=True)
        a_in_mail = Email.objects.filter(recipients=user_profile, archived=True)
        # studen = User.objects.filter(is_superuser=False)
        # teacher = User.objects.filter(is_superuser=True)  
        
         
        maill = NewemailForm(request.POST)
        # Check if form data is valid (server-side)
        if maill.is_valid():
            
            # Sets author field in new listing
            # Đặt trường tác giả trong danh sách mới
            maill.instance.author = request.user
            # Saves new listing
            maill.save()
            # Redirect to listing page 
            maill = NewemailForm()
            return render(request, "library/mail.html", {
                "in_mail": in_mail,
                "mysent_mail": mysent_mail,
                "a_mysent_mail":a_mysent_mail,
                "a_in_mail": a_in_mail,
                "maill": maill,
            })
    else: 
        # If a GET (or any other method), we'll create a blank form
        maill = NewemailForm()

    return render(request, "library/newemail.html", {
        # "studen":studen,
        # "teacher":teacher,
        "maill": maill
    })


# @login_required
# def active_human(request):
#     if request.user.is_superuser:
#         all_active = active_all.objects.filter(performer=request.uers).order_by("-time_2")
#     else:
#         all_active = active_all.objects.filter(performer=request.uers).order_by("-time_2")
#     return render(request, "library/category.html", {
#         "all_active": all_active,
#     })





csrf_exempt
@login_required(login_url='login')
def views_active_all(request, user_id):
    x = []
    if request.user.is_superuser:
        users = User.objects.get(pk=user_id)
        # all_active = active_all.objects.filter(subject_active =users).order_by("-time_2")
    else:
        users = request.user
    active_book = Listing.objects.filter(user=users).order_by("-timel")[:5]
    active_mail = Email.objects.filter( recipients = users).order_by("-time")[:5]
    active_coment = active_all.objects.filter(subject_active =users, classify_active=1 ).order_by("-time_2")[:5]
    active_money = active_all.objects.filter(subject_active =users, classify_active=2 ).order_by("-time_2")[:5]
    active_over = active_all.objects.filter(subject_active =users, classify_active =0 ).order_by("-time_2")[:5]
    return render(request, "library/cation_all.html", {
        # "all_active": all_active,
        "users": users,
        "id_acc": user_id,
            
        "active_book": active_book,
        "active_mail": active_mail ,
        "active_coment": active_coment,
        "active_money": active_money,
        "active_over": active_over ,
        
        
        
    })

csrf_exempt
@login_required(login_url='login')
def views_active_human(request, user_id):
    users = User.objects.get(pk=user_id)
    return render(request, "library/cation_human.html", {
        "users": users,
        "id_acc": user_id,
    })
csrf_exempt
@login_required(login_url='login')
def views_active_book(request, user_id):
    if request.user.is_authenticated:
        users = User.objects.get(pk=user_id)
        acc_login = request.user
        if request.user.is_superuser:
            if acc_login.id == user_id:
                list_all = Listing.objects.all()
            else:
                list_all = Listing.objects.filter(user=users).order_by("-timel")
            return render(request, "library/cation_book.html", {
                "list_all":list_all,
                "users": users,
                "id_acc": user_id,
            })
        elif  acc_login.id == user_id:

            list_all = Listing.objects.filter(user=request.user).order_by("-timel")
            return render(request, "library/cation_book.html", {
                "list_all":list_all,
                "users": users,
                "id_acc": user_id,
            })
        else :
            messages.error(request, 'Kông đủ quyền hạn truy cập !')
            return HttpResponseRedirect(reverse("index"))
    
    
    
    
csrf_exempt
@login_required(login_url='login')
def views_active_mall(request, user_id):
    users = User.objects.get(pk=user_id)
    # user_profile = request.user
    user_profile = users
    mysent_mail = Email.objects.filter( author=user_profile, archived=False)
    in_mail = Email.objects.filter(recipients=user_profile, archived=False)
    a_mysent_mail = Email.objects.filter( author=user_profile, archived=True)
    a_in_mail = Email.objects.filter(recipients=user_profile, archived=True)
    
    if request.method =="POST":
        maill = NewemailForm(request.POST)
        if maill.is_valid():
            maill.instance.author = request.user
            maill.save()
            maill = NewemailForm()
            return render(request, "library/mail.html", {
                "in_mail": in_mail,
                "mysent_mail": mysent_mail,
                "a_mysent_mail":a_mysent_mail,
                "a_in_mail": a_in_mail,
                "id_acc": user_id,
                "maill": maill,
            })
    else: 
        # If a GET (or any other method), we'll create a blank form
        maill = NewemailForm()
    return render(request, "library/cation_mail.html", {
        "mysent_mail": mysent_mail,
        "in_mail": in_mail,
        "a_mysent_mail":a_mysent_mail,
        "a_in_mail": a_in_mail,
        "maill": maill,
        "users": users,
        "id_acc": user_id,
    })
    
    

    
csrf_exempt
@login_required(login_url='login')
def views_active_coment(request, user_id):
    users = User.objects.get(pk=user_id)
    comments = active_all.objects.filter(performer=users,classify_active = 1).order_by("-time_2")
    return render(request, "library/cation_coment.html", {
        "comments":comments,
        "users": users,
        "id_acc": user_id,
    })
     
csrf_exempt
@login_required(login_url='login')
def views_active_money(request, user_id):
    users = User.objects.get(pk=user_id)
    run_money = active_all.objects.filter(subject_active=users,classify_active = 2).order_by("-time_2")
    return render(request, "library/cation_money.html", {
        "run_money":run_money,
        "users": users,
        "id_acc": user_id,
    })
csrf_exempt
@login_required(login_url='login')
def views_active_over(request, user_id):
    users = User.objects.get(pk=user_id)
    if request.user.is_superuser:
        active_over = active_all.objects.filter(subject_active=users ).order_by("-time_2")
    else:
        active_over = active_all.objects.filter(subject_active=users,classify_active = 0).order_by("-time_2")
    return render(request, "library/cation_over.html", {
        "active_over":active_over,
        "users": users,
        "id_acc": user_id,
    })
    
    
    
    
    

@login_required(login_url='login')
def human(request, user_id):
    users = User.objects.get(pk=user_id)
    list_add = Listing.objects.filter(user=users, active=False)
    list_in = Listing.objects.filter(user=users, active=True)
    return render(request, "library/human.html", {
        "list_add": list_add,
        "list_in": list_in,
        "users": users
    })
@csrf_exempt
@login_required(login_url='login')
def add_bid(request, user_id):
    
        if request.user.is_superuser:
            if request.method == "POST":
        
                # Look up listing from request
                users = User.objects.get(pk=user_id)
                add_money = request.POST["add_money"]
                money_in = int(add_money) + users.money
                print(money_in)
                # user.money = money_in
                users.money=money_in
                users.save()
                messages.success(request, 'nap tien thanh cong')
                return HttpResponseRedirect(reverse("all_user"))

            else: 
                messages.error(request, 'phuong thuc phai la post.')
                return HttpResponseRedirect(reverse("all_user"))
        else: 
            messages.error(request, 'ban phai la giao vien moi co the nap tien.')
            return HttpResponseRedirect(reverse("index"))  
        


        
        
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, 'invalid username and password ')
            return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "library/login.html")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    
@login_required(login_url='login')
def register(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                avatar = request.FILES["avatar"]
                username = request.POST["username"]
                email = request.POST["email"]
                password = request.POST["password"]
                confirmation = request.POST["confirmation"]
                if avatar is None:
                    messages.error(request, 'thieu anh')
                    return HttpResponseRedirect(reverse("register"))
                if password != confirmation:
                    return render(request, "library/register.html", {
                        "mesage": "mật khẩu không đúng"
                    })
                try:
                    if"teacher" in request.POST:
                        user = User.objects.create_superuser( username, email, password, avatar=avatar)
                        user.save()
                        # user = User.objects.create_user(avatar=avatar, username=username, email=email, password=password)
                    elif "students" in request.POST:
                        user = User.objects.create_user( username, email, password, money = 30000,avatar=avatar)
                        user.save()
                        messages.success(request, 'bạn đã tạo thêm 1 tài khoản')
                        return render(request, "library/register.html")
                    else:
                        user = User.objects.create_user( username, email, password,money = 30000,avatar=avatar)
                        user.save()
                except IntegrityError:
                    """ return render(request, "library/register.html", {
                            "message":"tên người dùng đã được sử dụng"
                    })"""
                    messages.error(request, 'tên người dùng đã được sử dụng')
                    return HttpResponseRedirect(reverse("register"))
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "library/register.html")
        messages.error(request, 'bạn phải đăng nhập tài khoản giáo viên để thực hiện thao tác này')
        return HttpResponseRedirect(reverse("index"))
    else:
        return HttpResponseRedirect(reverse("index"))
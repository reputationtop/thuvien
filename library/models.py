
from pickle import TRUE
from unicodedata import category, name
from django.db import models
import datetime
# from datetime import datetime
# now = datetime.datetime.now()
# today = now.date()
# moment = now.time()

from datetime import timezone
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    money =models.IntegerField(default=0, blank=True)
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    limit_book = models.IntegerField(default=10,blank=True)
    # ratings = models.IntegerField(default=1,blank=True,null=True)
    # rating là trang thai tai khoan chua xac thuc 1 hoc sinh 2  giao vien  3    quan li giao vien( superuser)
    pass

    class Meta:
        ordering = ['-date_joined']
    def categorys(self):
        return str(self.category.all().count())
class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        ordering = ['name']
class Book(models.Model):
    namebook = models.CharField(max_length=100 ,)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    description = models.CharField(max_length=600)
    numbe_book = models.IntegerField()
    numbein_book = models.IntegerField()
    bid = models.IntegerField()
    numbe_views = models.IntegerField(default=0, blank=True)
    dele_book = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, blank=True, related_name="listcategory")
    # category = models.ManyToManyField(Category, on_delete=models.SET_DEFAULT, default='', blank=True, null=True)
    timeb = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name="listlike")
    def __str__(self):
        return f"{self.namebook}, {self.image}, {self.description}, {self.numbe_book}, {self.bid}, {self.category}, {self.dele_book}"
    def categorys(self):
        return str(self.category.all().count())
    def list_category(self):
        mylist = self.category.all()
        mystring = ",".join([str(char) for char in mylist])
        return str(mystring)
        # for y in self.category.all():
        #    x+=str(y)+""
        # print(x)   
        
    def listout_category(self):
        mylist = self.category.all()
        mystring = ",".join([str(char) for char in mylist])
        return str(mystring)
        # for y in self.category.all():
        #    x+=str(y)+""
        # print(x)   
    def is_in_listlike(self,user):
        """ kiem tra xem nguoi dung co like bai nay khong """
        return user.listlike.filter(pk=self.pk).exists()
    def num_like(self):
        return str(self.likes.count())
    def num_book_listing(self):
        # """ tra ve so luong sach da cho vao danh sach muon loai tru nhung danh sach đa ket thuc"""
        return self.listingbook.filter(dele_listing= False).count()
    
    def num_listing(self):
        # """ tra ve so luong sach da cho vao danh đang len danh sach muon"""
        return self.listingbook.filter(dele_listing= False).exclude(active=TRUE).count()
    
    # def id_human(self):
    #     """ tra ve so luong sach da cho vao danh sach muon"""
    #     return self.listing.all().count()
    def fix_active(self):
        """ kiem tra xeem trong kho con sach khong """
        if self.num_book_listing < self.numbe_book:
            return True
        else:
            return False
    # def is_in_listing(self,user):
    #     return user.listing.filter(pk=self.pk).exists()

    
    class Meta: 
        ordering = ['-timeb']

class Listing(models.Model):
    # Listing_action = models.ForeignKey(User, on_delete=models.PROTECT, related_name="Listing_action", blank=True, null=True)
    item = models.ForeignKey(Book,on_delete=models.PROTECT,related_name="listingbook")
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name="listinguser")
    active = models.BooleanField(default=False)
    dele_listing = models.BooleanField(default=False)
    convert_date =models.DateTimeField(null=True,blank=True,auto_now_add=False)
    return_date =models.DateTimeField(null=True,blank=True,auto_now_add=False)
    bid_date = models.IntegerField(null=True,blank=True)
    action_bid = models.IntegerField(null=True,blank=True)
    timel = models.DateTimeField(auto_now_add=True)
    def date_om(self):
        if self.active == False:
            return None
        elif self.convert_date is not None:
            x = datetime.datetime.now()
            t1 = self.convert_date
            t2 = datetime.date.today()
            x = t1.date() - t2
            tx = x.days
            if tx >= 0:
                return 0
            else:
                return tx
        else:
            return None
    def money_listing(self):
        a = self.date_om()
        b = self.action_bid
        c = self.bid_date
        if self.active == False:
            return None
        else:
            if self.date_om() < 0:
                money = b - a*c
                if money > self.item.bid:
                    return self.item.bid
                else:
                    return money
            else:
                return self.action_bid
   

                
    def __str__(self):
        return str(self.active)
    class Meta: 
        ordering = ['-timel']
# class Comment(models.Model):
#     item = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
#     user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="comments")
#     comment = models.CharField(max_length=1000)
#     timec = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return str(self.comment)
#     class Meta:
#         ordering =['-timec']
        
class Email(models.Model):
    author = models.ForeignKey(User, on_delete= models.PROTECT, related_name="emails_in")
    recipients = models.ForeignKey(User,on_delete= models.PROTECT, related_name="emails_received")
    subject = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    read = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    
    def is_in_archive_email(self,user):
        """ kiem tra xem nguoi dung co like bai nay khong """
        return user.archive_email.filter(pk=self.pk).exists()
    # "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
    def __str__(self):
        return f"Email sent by {self.author} with subject {self.subject}"
    class Meta: 
        ordering = ['-time']
class active_all(models.Model):
    performer = models.ForeignKey(User, on_delete=models.PROTECT, related_name="active_performer",null=False)
    subject_active = models.ForeignKey(User, on_delete=models.PROTECT, related_name="active_subject",default=None,  blank=True, null=True)
    item = models.ForeignKey(Book ,on_delete=models.PROTECT,related_name="active_comments", default=None,  blank=True, null=True)
    book_flow = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(Category,on_delete= models.PROTECT, default=None, blank=True, null=True)
    # coment_active= models.ForeignKey(Comment,on_delete= models.PROTECT, default=None, blank=True, null=True)
    classify_active = models.IntegerField(default=0, blank=True, null=False)
# 1= Comment
# 2= money
# 0 =over
    money_flow = models.IntegerField(default=0, blank=True)
    money_now = models.IntegerField(default=0, blank=True)
    reason = models.CharField(max_length=3000, default=None, null=True, blank=True)
    time_2 = models.DateTimeField(auto_now_add=True)
    class Meta: 
        ordering = ['-time_2']

000999
# 4

# Đây là của tôi views.py, để hiển thị các tài khoản người dùng hiện tại

# @login_required
# def account(request):
#     if request.user.is_superuser: # just using request.user attributes
#         accounts = get_user_model().objects.all()```
        
        
# from termios import VSTART


# views.py:

# def user_detail(request):
#    user_detail = CustomUser.objects.filter(id=id)
#    return(request,'user_datail.html',{'user_detail':user_detail})

# user_datail.html:

# {% for i in user_detail %}{% if i.is_superuser %}
# <td class="text-center"><span class="btn btn-success">You</span></td>
# {% else %}
# <td class="text-center"><span class="btn btn-info">Agent</span></td>
# {% endif %}{% endfor %}



# VS
# @login_required
# def account(request):
#     if request.user.is_superuser: # just using request.user attributes
#         accounts = get_user_model().objects.all()```
        
        
#         &#128150; html trai tom do
        
# 	& # 10084;  trai tim den
#     recipients = []
#     for email in emails:
#         try:
#             user = User.objects.get(email=email)
#             recipients.append(user)
#         except User.DoesNotExist:
            

POST /del_book/5 HTTP/1.1" 302 0
# from datetime import datetime, date

# import datetime
# str1= "21/02/13"
# d1 = datetime.datetime.strptime(str1, "%y/%m/%d")

# print(d1)
# #>> 2021-02-13 00:00:00
# print(d1 + datetime.timedelta(days=31))
# #>> 2021-03-16 00:00:00
# print(d1 + datetime.timedelta(days=-2))

# # khoảng thời gian chênh lệch giữa 2 ngày tháng
# t1 = date(year = 2018, month = 7, day = 12)
# t2 = date(year = 2017, month = 12, day = 23)
# t3 = t1 - t2
# print("t3 =", t3)

# t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
# t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
# t6 = t4 - t5
# print("t6 =", t6)


#     users = set()
#     users.add(request.user)
#     users.update(recipients)
Bạn có thể sử dụng đối tượng Q cho việc này. Chúng có thể được phủ định với ~toán tử và được kết hợp giống như các biểu thức Python bình thường:

from myapp.models import Entry
from django.db.models import Q

Entry.objects.filter(~Q(id=3))



Hãy thử django-cleanup , nó sẽ tự động gọi phương thức xóa trên FileField khi bạn loại bỏ mô hình.

pip install django-cleanup
INSTALLED_APPS = (
     ...
    'django_cleanup.apps.CleanupConfig',
)

string_1 = "Tên tôi là NIIT Hà Nội"
string_2 = "chuỗi 1/ chuỗi 2"

# Tách chuỗi mặc định sẽ tách từ khoảng trắng ' '
print(string_1.split())
# ['Tên', 'tôi', 'là', 'NIIT', 'Hà', 'Nội']

# Tách chuỗi từ ký tự '/'
print(string_2.split('/'))


list_of_strings = ['Tên', 'tôi', 'là', 'NIIT', 'Hà', 'Nội']

# Sử dụng join và phân tách bằng dấu phảy
print(','.join(list_of_strings))

# Output
# Tên,tôi,là,NIIT,Hà,Nội

# import Counter
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # Xác định đối tượng counter

print(count) # In thông tin tất cả
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b']) # Số lần xuất hiện của phần tử cụ thể
# 3

print(count.most_common(1)) # Phần tử xuất hiện nhiều nhất
# [('d', 5)]


Hợp nhất hai Dictionaries
sử dụng phương thức update() để hợp nhất hai Dictionaries.
dict_1 = {'apple': 9, 'banana': 6}
dict_2 = {'banana': 4, 'orange': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
# Kết quả
# {'apple': 9, 'banana': 4, 'orange': 8}
Nếu bạn muốn giữ các giá trị của chúng, bạn có thể làm như sau:



dict1 = {'apple': 9, 'banana': 6}
dict2 = {'banana': 4, 'orange': 8}

def mergeDict(dict1, dict2):
    """Hợp nhất dictionaries và giữ giá trị của key phổ biến trong list"""
    dict3 = {**dict1, **dict2}
    for key, value in dict3.items():
        if key in dict1 and key in dict2:
            dict3[key] = [value , dict1[key]]

    return dict3

# Hợp nhất dictionaries và thêm giá trị của key phổ biến trong list
dict3 = mergeDict(dict1, dict2)

print('Dictionary 3 :')
print(dict3)


#19. Chuyển đổi một số thành danh sách các chữ số trong Python
num = 123456

# Sử dụng map
list_of_digits = list(map(int, str(num)))

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]
# Sử dụng kỹ thuật list comprehension
list_of_digits = [int(x) for x in str(num)]

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]


def unique(l):
    if len(l) == len(set(l)):
        print("Tất cả phần tử là duy nhất")
    else:
        print("List có phần tử trùng lặp")

unique([1,2,3,4])
# Tất cả phần tử là duy nhất




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


chú ý
all_book = Book.objects.all().order_by("-timeb")[:10]  lay 10 phan tu cuoi
import collections

l = ['a', 'a', 'a', 'a', 'b', 'c', 'c']

c = collections.Counter(l)
print(c)
# Counter({'a': 4, 'c': 2, 'b': 1
print(c.keys())
# dict_keys(['a', 'b', 'c'])

print(c.values())
# dict_values([4, 1, 2])

print(c.items())
# dict_items([('a', 4), ('b', 1), ('c', 2)])
print(c.most_common())
# [('a', 4), ('c', 2), ('b', 1)]
print(c.most_common()[0])
# ('a', 4)

print(c.most_common()[-1])
# ('b', 1)

print(c.most_common()[0][0])
# a
print(c.most_common()[::-1])
# [('b', 1), ('c', 2), ('a', 4)]

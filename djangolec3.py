from lib2to3.pgen2 import driver
from lib2to3.pgen2.driver import Driver
from unittest import TestProgram

from lecture3.lecture3.settings import MIDDLEWARE
from lecture7.selenium.tests import file_uri


django-admin startproject lecture3 
tao file du an web lecture3
python manage.py startapp newyear

python manage.py runserver

vai tro cac tep:
    1 views.py :
        mo ta nhung gi ma nguoi truy cap thay
    2 setting.py:
        INSTALLED_APPS cac ung dung da cai dat
        trong tep hello tao urls.py
phai chu y cac duong dan nhuw setting.py. cac urls cua tep dau tien va cac urls cua cac tep con lai


MIDDLEWARE
csrf dien vao ma thong bao 
0   django-admin startproject airline
0.5  cd airline
0.6 mo setting.py va installed  ten app
 1  python  manage.py startapp flights
 2 python manage.py migrate 
  :cho phep tao tat ca cac bang mac dinh  ben trong csdl cua django
python manage.py makemigrations
 python manage.py runserver 8080   chuyen duong dan sang cong 8080



 tao tai khoanclass Name(models.Model):
     python manage.py createsuperuser
     1 tk  admin-admins  
     2 email admin@gmail.com
     1111
     3
 
     def __str__(self):
         return 
 
     def __unicode__(self):
         return 
 


 
python => from tests import * => uri = file_uri("xyz.html") => driver.get(uri) >>>
    driver.find_element_by_id ("ten phan tur")  tim 1 phan tu
    increase = driver.find_element_by_id ("ten phan tur")

cac mo hinh m-v-c vs m-t-v
     model-model:view-templates: controller-views
     model dung de tuong tac vs csdl(them sua xoa)
     template dao dien trang web site
     views dieu khien lozic cua chuong trinh la cau noi giua model va templates




 nguoi => hethong=>views=>model=>
    database=> tra ve=>model=>views=>tra lai =>nguoi


http://localhost/phpmyadmin/index.php kiem tra sql co chay binh thuong khong




    Using the quit() function.
Using the sys.exit() function.
Using the exit() function.
Using the KeyboardInterrupt command.
Using the raise SystemExit command.
Using the os._exit(0) function.

pip install djangorestframework
pip install django-filter
pip install markdow   
pip install django-heroku  
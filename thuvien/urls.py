"""thuvien URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    path("newbook", views.newbook, name="newbook"),
    path("book/<int:book_id>", views.is_book, name="book"),
    path("fixbook/<int:book_id>", views.fixbook, name="fixbook"),
    path("del_book/<int:book_id>", views.del_book, name="del_book"),
    
    path("mailbook", views.mailbook, name="mailbook"),
    path("newemail", views.newemail, name="newemail"),
    # path("read_mail/<int:email_id>", views.read_mail, name="read_mail"),
    path("read_mail/<int:email_id>", views.read_mail, name="read_mail"),
    path("archive_email/<int:email_id>", views.archive_email, name="archive_email"),
    
    path("newcategory", views.newcategory, name="newcategory"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    
    path("changebook", views.changebook, name="changebook"),#like/unlike
    
    
    
    path("human/<int:user_id>", views.human, name="human"),
    path("views_active_all/<int:user_id>", views.views_active_all, name="views_active_all"),
    path("views_active_human/<int:user_id>", views.views_active_human, name="views_active_human"),
    path("views_active_book/<int:user_id>", views.views_active_book, name="views_active_book"),
    path("views_active_mall/<int:user_id>", views.views_active_mall, name="views_active_mall"),
    path("views_active_coment/<int:user_id>", views.views_active_coment, name="views_active_coment"),
    path("views_active_money/<int:user_id>", views.views_active_money, name="views_active_money"),
    path("views_active_over/<int:user_id>", views.views_active_over, name="views_active_over"),
    
    
    path("add_bid", views.add_bid, name="add_bid"),
    
    path("NewListing/<int:book_id>", views.NewListing, name="NewListing"),
    path("change_listing",views.change_listing, name="change_listing"),
    # path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path("close_listing", views.close_listing, name="close_listing"),
    
    
    path("addcomment/<int:book_id>", views.add_comment, name="addcomment"),
    # path("add_borrow/<int:book_id>", views.add_borrow, name="add_borrow"),

    path("all_user", views.all_user, name="all_user"), 
    
    path("Is_listing", views.Is_listing, name="Is_listing"),
    path("In_listing/<int:listing_id>", views.In_listing, name="In_listing"),
    
    path("BookSearchView", views.BookSearchView, name="BookSearchView"),
    path("UserSearchView", views.UserSearchView, name="UserSearchView"),
    
    
    
    # path("bookcase", views.bookcase, name="bookcase"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

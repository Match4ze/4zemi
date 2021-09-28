from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path



urlpatterns = [
    path('', views.new_register, name='new_register'),
    path('topScreen', views.topScreen, name='topScreen'),
    path('details_screen', views.details_screen, name='details_screen'),
    path('personal', views.personal, name='personal'),
    path('select', views.select, name='select'),
    
    #ユーザの詳細情報を表示する処理を呼び出す
    path('<int:id>', views.showDetail, name='showDetail'),
    #ユーザの登録フォームを呼び出す
    path('create', views.showCreateUserForm, name='showCreateForm'),
    #ユーザ登録完了
    path('create_completion', views.create_completion, name='create_completion'),
    #ユーザ情報
    path('showUsers', views.showUsers, name='showUsers'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addUser, name='addUser'),
    #ログイン
    path('login_user', views.Login, name='login_user'),
    #ログアウト
    path("logout",views.Logout,name="Logout"),
    #ユーザ情報更新フォーム
    path("<int:id>/user_update",views.UserUpdate, name='user_update'),
    #ユーザ情報更新
    path('<int:id>/updateUser', views.updateUser, name='updateUser'),
    #マイページ登録画面を呼び出す
    path('<int:id>/user_adddetail', views.showUserDetail, name='user_adddetail'),
    #マイページ登録
    path('<int:id>/add_userdetail', views.addUserDetail, name='add_userdetail'),
    #マイページ更新画面を呼び出す
    path("<int:id>/mypage_update",views.MypageUpdate, name='Mypage_update'),
    #マイページ更新
    path('<int:id>/updateMypage', views.updateMypage, name='updateMypage'),
    #マイページ
    path('<int:id>/Mypage', views.showMypage, name='Mypage'),

    #趣味選択フォームを呼び出す
    path('<int:id>/show_selectHobby', views.showSelectHobby, name='show_selectHobby'),
    #趣味選択
    path('<int:id>/add_selectHobby', views.addSelectHobby, name='add_selectHobby'),
    #趣味選択を編集するフォームを呼び出す
    path('<int:id>/selectHobby_update', views.showUpdateSelectHobby, name='selectHobby_update'),
    #趣味選択の更新
    path('<int:id>/updateSelectHobby', views.updateSelectHobby, name='updateSelectHobby'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

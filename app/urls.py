from .import views
from django.urls import path


urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('home',views.home,name='home'),
    path('admin',views.adminhome,name='adminhome'),
    path('profile/<int:pk>',views.myprofile,name='myprofile'),
    path('leave/<int:pk>',views.leaveapply,name='leaveapply'),
    path('applyleave/<int:pk>',views.user_apply_leave,name='user_apply_leave'),
    path('viewleave/<int:pk>',views.viewleave,name='viewleave'),

    path('admin1',views.adminleave,name='adminleave'),
    path('aproove/<int:id>',views.Admin_approve,name='Admin_approve'),
    path('reject/<int:id>',views.Admin_reject,name='Admin_reject'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('add/<int:pk>',views.add,name='add'),
    path('add2/<int:pk>',views.add2,name='add2'),
    path('atten',views.atten,name='atten'),
    path('viewatten/<int:pk>',views.viewatten,name='viewatten'),
    path('addtask',views.addtask,name='addtask'),
    path('task',views.taskk,name='taskk'),
    path('viewtask/<int:pk>',views.viewtask,name='viewtask'),
    path('click_up/<int:pk>/<int:k>/',views.click_up,name='click_up'),
    path('uploadtask/<int:pk>/<int:k>/',views.uploadtask,name='uploadtask'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('addatten',views.addatten,name='addatten'),
    path('admin_viewtask',views.admin_viewtask,name='admin_viewtask'),
    #path('deletetask/<int:pk>',views.deletetask,name='deletetask'),
    path('update/<int:pk>',views.updateprofie,name='updateprofile'),
    path('upda/<int:pk>',views.upda,name='upda'),
    
]
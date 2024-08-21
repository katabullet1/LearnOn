from django.urls import path

from .views import home, signup_view, signin_view,room,signout_view, image_upload_view, view_name

app_name = 'chat'

urlpatterns = [
    path('', home, name='home'),
    path('room/<str:room_name>/', room, name='room'),
    #path('room2/<str:room_name>/', room2, name='room2'),
    path('signup/', signup_view, name='signup_namespace'),
    path('signin/', signin_view, name='signin_namespace'),
    path('signout/', signout_view, name='logout_namespace'),
    path('room/<str:room_name>/image_upload/', image_upload_view),

    path('room/<str:room_name>/', view_name, name='handle2'),
    path('room/<str:room_name>/',room, name='handle3'), 
    path('chatroom/', view_name, name='handle2'),
    #path('room/<str:room_name>/', start, name='handle3'),
    
]

# path('upload/', mongo_image_upload),
# path('<str:room_name>/upload/', mongo_image_upload),
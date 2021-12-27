from django.urls import path


from web.views import sad_msg ,happy_msg
urlpatterns = [
    path('sad/<str:name>/', sad_msg),
    path('happy/<str:name>/<int:times>/', happy_msg)
]

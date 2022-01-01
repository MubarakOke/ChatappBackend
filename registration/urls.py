from django.conf.urls import url
from registration.views import SignUp

app_name= "signup"
urlpatterns = [
    url('^$', SignUp.as_view(), name="register")
]

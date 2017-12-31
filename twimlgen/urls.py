from django.conf.urls import url
import views

urlpatterns = [
    url(r'^input/', views.UserInputView.as_view(), name = "input"),
    url(r'^enter_a_number/', views.TwimlGen.as_view(), name = "enter_number")
]
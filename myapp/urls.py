from django.urls import path
from .views import StudentListCreateAPIView

urlpatterns = [
    # .as_view() ব্যবহার করা হয় ক্লাস বেসড ভিউকে রাউট করার জন্য
    path('students/', StudentListCreateAPIView.as_view(), name='student-list'),
]
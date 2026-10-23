from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateAPIView(APIView):
    
    # GET মেথড: ডাটাবেস থেকে সব স্টুডেন্টের ডেটা এনে দেখাবে
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST মেথড: নতুন স্টুডেন্টের ডেটা ডাটাবেসে সেভ করবে
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(): # চেক করবে ডেটা ঠিক আছে কি না
            serializer.save() # ডাটাবেসে সেভ করবে
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from api.serializer.student_serializer import StudentSerializer
from student.models.student_model import StudentModel


def student_list(request):
    if request.method == 'GET':
        teacher = StudentModel.objects.all()
        serializer = StudentSerializer(teacher, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

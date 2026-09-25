from django.shortcuts import render
def student(request):
    return render(request,
        'student.html',
        {
            "name":"lalitha",
            "age":19,
            "course":"python fsd",
            "college":"ists",
        }
        )

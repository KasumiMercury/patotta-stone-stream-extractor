import functions_framework

@functions_framework.http
def function(request):
    return "Hello World!"

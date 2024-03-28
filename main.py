import functions_framework

@functions_framework.http
def function(request):
    vid = request.args.get('vid')
    if vid is not None:
        return f"Hello {vid}!"
    
    return "Hello World!"


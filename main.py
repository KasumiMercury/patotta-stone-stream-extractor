import functions_framework

@functions_framework.http
def function(request):
    vid = request.args.get('vid')
    # If vid is not provided, report an error
    if vid is None:
        raise RuntimeError("No vid provided")
    
    return "Hello World!"


from django.shortcuts import  render_to_response
# Create your views here.

def welcomepage(request):
    return render_to_response('common/welcome.html')

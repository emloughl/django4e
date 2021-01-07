from django.http import HttpResponse

# Create your views here.

def SessionCount(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits % 4

    response = """<html><body><p>Hello world! Visit Count = {}</p></body></html>""".format(num_visits)
    return HttpResponse(response)

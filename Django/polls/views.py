from django.http import HttpResponse

def index(request):
    napis1 = "Hello World"
    napis2 = "Jestem kacper"
    pelna_odpowiedz = napis1 + " <br> " + napis2
    return HttpResponse(pelna_odpowiedz) # Wysyłasz wszystko naraz

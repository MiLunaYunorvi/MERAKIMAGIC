from django.shortcuts import render

# Create your views here.

def initial(request):
    return render(request, "MERAKIMAGIC/index.html",{})
def formulario(request):
    return render(request, "MERAKIMAGIC/form.html")
def exploracion(request):
    return render(request, "MERAKIMAGIC/explora.html")
def juego(request):
    return render(request, "MERAKIMAGIC/juega.html")
def valida(request):
    if request.method == 'POST':
        nombres= request.POST["nombres"]
        apellidos = request.POST["apellido"]
        correo = request.POST["correo"]
        empresa = request.POST["empresa"]
        print(nombres,apellidos,correo,empresa)
    return render(request, "portal/portal.html")
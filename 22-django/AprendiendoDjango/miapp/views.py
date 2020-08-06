from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#MVC = Modelo Vista Controlador -> Acciones (metodos)
#MVT = Modelo Template Vista --> Acciones (metodos)

layout= """

    
    """

def index(request):

    html = """
        <h1>Inicio</h1>
        <p> Años hasta 2050: </p>
        <ul>
    """

    year=2021
    while year <= 2050:
        if year % 2 == 0:
            html +=f"<li> {str(year)} </li>" 
        
        year += 1   

    html += "</u>"

    return render(request,'index.html')
    #return HttpResponse(layout+html)

def hola_mundo(request):
    #return HttpResponse(layout+ """   """)
    return render(request,'hola_mundo.html')

def pagina(request, redirigir=0):

    if redirigir==1:
        #return redirect("/contacto/greivin/cruz")
        return redirect("contacto", nombre="greivin", apellidos="cruz")

    #return HttpResponse(layout+ "")
    return render(request,'pagina.html')

def contacto(request, nombre="",apellidos=""):
    
    html=""
    
    if nombre and apellidos:
        html +=f"<h3>{nombre} {apellidos}<h3>"
    
    return HttpResponse(layout+ f"<h1>Contacto </h1>" + html)
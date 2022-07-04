from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Universidad Nacional Tecnológica de Lima Sur</h1>"
                        "<h2>EP Ingeniería de Sistemas</h2>"
                        "<h3>Bienvenidos</h3>")
def uc3(request):
    return HttpResponse("<h1>Lenguaje de Programación III</h1>"
                        "<h2>Evaluación de la Unidad de Competencia 3</h2>"
                        "<h3>Docente: MG. FlorElizabeth Cerdán León</h3>"
                        "<h3>Integrante:</h3>"
                        "<h3>Quispe Cupe Jordy</h3>")
def noticia(request):
    return HttpResponse("<h1>Noticia de Hoy</h1>"
                        "<h2>Inició el paro indefinido de transporte multimodal a nivel nacional</h2>"
                        "<h3>Un 70 porciento de los gremios de transportistas urbanos que anunciaron acatar un paro hoy, firmaron un acuerdo para suspenderlo. Así lo informó el ministro de Transporte y Comunicaciones Juan Barrenzuela, durante una conferencia de prensa realizada ayer en la tarde. El 30% restante -señaló el funcionario- debatía los términos establecidos con sus bases. “Es altamente probable que se comuniquen y que también se unan a los acuerdos”, comentó.</h3>")
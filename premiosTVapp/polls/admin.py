from django.contrib import admin
from .models import Question, Choice

#stackedinline me crea la opcion de agregar respeustas en las preguntas
class ChoiceInLine(admin.StackedInline):
    #va a traer a Choice
    model = Choice
    #Se va a oider crear 3 respuesta
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    #Me permite elegir el orden
    fields = ["pub_date", "question_text"]
    #Coloco las clases que quiero se agregue
    inlines = [ChoiceInLine]
    #hace que aparezca todas estas opociones
    list_display = ("question_text", "pub_date", "was_published_recently")
    #crea un filtro
    list_filter = ["pub_date"]
    #crea un cuadro de busqueda
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

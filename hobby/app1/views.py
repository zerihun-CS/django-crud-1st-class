from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
# Create your views here.

   #  reading –I've always been a huge reader. It's a great hobby for relaxation and self-care, as well as a wonderful educational hobby to learn new skills or information.
   #  decorating a planner or Happy Planner.
   #  journaling.
   #  writing.
   #  crossword puzzles.
   #  sudoku.
   #  word scrambles.
   #  other word games.
   

list_of_hobbies = ['writing','sudoku',' word scrambles','journaling','decorating a planner']
def index(request):
   hobby_obj = Hobby.objects.all()
   


   data = {
      'hobby':hobby_obj
   }
   
   return render(request, 'index.html',data)


def add_hobby(request):
   if request.method == 'POST':
      hobby = request.POST.get('hobby')
      obj1 = Hobby()
      obj1.name = hobby
      obj1.save()
      print(hobby)
      list_of_hobbies.append(hobby)
      return render(request,'add_hobby.html' )
   else:
      pass
   
   return render(request,'add_hobby.html' )

def about(request):
   return HttpResponse("About Page ")
   
   
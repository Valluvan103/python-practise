from django.shortcuts import render
from myapp.forms import QuizForm

# Create your views here.
def index(request):
	con = QuizForm()
	return render(request,'index.html',{'form':con})
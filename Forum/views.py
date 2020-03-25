from django.shortcuts import render
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your answer has been posted')
            return redirect('detail', pk)
    else:
        form = AnswerForm()
    qns = Question.objects.all()
    context = {
        'questions':qns,
        'form':form
    }
    return render(request, 'Forum/home.html', context)

def detail(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your answer has been posted')
            return redirect('detail', pk)
    else:
        form = AnswerForm()

    qn = Question.objects.get(pk=pk)
    ans = Answer.objects.filter(question=qn)
    context ={
        'question': qn,
        'answers':ans,
        'form':form
    }
    return render(request, 'Forum/detail.html', context)

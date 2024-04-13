from django.shortcuts import render
from .models import Test, Queston, Scores
from .forms import TestForm, QuestionFormSet
from django.forms import formset_factory
from django.shortcuts import redirect

# Create your views here.
def index(request):
    tests = Test.objects.order_by('-release_date')
    scores = Scores.objects.filter(user=request.user)

    return render(request, 'nursultan/index.html', {'tests': tests, 'scores': scores})

def test(request, test_id):

    test = Test.objects.get(id=test_id)
    questions = Queston.objects.filter(test=test)

    if request.method == "GET":

        return render(request, 'nursultan/test.html', {'test': test, 'questions': questions})
    
    if request.method == "POST":
        right_answers = 0
        false_answers = 0


        for question in questions:


            answer = request.POST.get(question.title)
            print(answer, question.answer)

            if int(answer) == int(question.answer):
                right_answers += 1
                continue

            false_answers += 1

    result = round(right_answers * 100 / (right_answers + false_answers))

    if Scores.objects.filter(user=request.user, test=test).exists():
        if result > Scores.objects.get(user=request.user, test=test).score:
            Scores.objects.filter(user=request.user, test=test).update(score=result)
    else:
        Scores.objects.create(user=request.user, test=test, score=result)

    return render(request, 'nursultan/results.html', {'result': result})

def create_test(request):
    if request.method == "GET":
            
        question_formset = QuestionFormSet()
        test_form = TestForm()

        return render(request, 'nursultan/create_test.html', {'parent_form': test_form, 'formset': question_formset})
        

    print(request.POST)

    test_form = TestForm(request.POST)

    if not test_form.is_valid():
        return render(request, 'nursultan/index.html', {'error': 'Неправильно введены данные'})
    

    test = test_form.save()


    count = 0
    while True:


        title = request.POST[f'queston_set-{count}-title']
        option1 = request.POST[f'queston_set-{count}-option1']
        option2 = request.POST[f'queston_set-{count}-option2']
        option3 = request.POST[f'queston_set-{count}-option3']
        option4 = request.POST[f'queston_set-{count}-option4']
        answer = request.POST[f'queston_set-{count}-answer']

        question = Queston(test=test,
                            title=title,
                            option1=option1,
                            option2=option2,
                            option3=option3,
                            option4=option4,
                            answer=answer)
        
        print(question)
        question.save()

        try:
            title = request.POST[f'queston_set-{count+1}-title']
            count += 1
        except:
            break

    question_formset = Queston.objects.filter(test=test)
        

    return redirect('pass-test', test_id=test.id)
    
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,

    }

    return render(request, 'polls/index.html', context)

    """
    1.  context dict 객체를 생성
        'questions' 키에
        모든 Question 객체를 DB에서 가져온 QuerySet을 할당    
        render 함수를 사용해서 'polls/index.html'을 
        context로 rendering한 결과를 리턴

    2. 템플릿 파일들이 있는 디렉토리를 settings.py 에 설정
        settings.py에 TEMPLATE_DIR을 지정
        TEMPLATE = ...설정의 'DIRS'키를 갖는 리스트에 TEMPLATE_DIR추가

    3.  템플릿 파일 생성 Question들을 출력
        polls/index.html 파일을 생성
        해당 템플릿에 'questions'키로 전달된 QuerySet을 for loop하며
        가 loop에 해당하는 Question객체의 title을 출력


    :param request: 
    :return: 
    """


def question_detail(request, pk):
    """
    context에 pk에 해당하는 Question을 전달
    polls/question.html 에서 Question title을 표시

    url
        poll/<question_id>/$
    :param request:
    :param pk:
    :return:
    """

    question = Question.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'polls/question.html', context)


def vote(request, pk):
    if request.method == 'POST':

        question = Question.objects.get(pk=pk)

        #선택이 없을 경우 원래 페이지로 돌아가도록 처리
        try:
            choice_pk = request.POST['choice_pk']
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        except Question.DoesNotExist:
            return redirect('index')
        except MultiValueDictKeyError:
            pass
        except Choice.DoesNotExist:
            pass
        return redirect('question_detail', pk=question.pk)
    return HttpResponse('Permission denied', status=403)



"""
request.POST로 전달된 choice의 pk값을 이용
선택한 Choice를 choice변수에 할당
votes값을 1증가 후 DB에 저장
이후 투표한 Choice가 속한 question_detail로 이동

1. question변수에 pk가 question_pk인 Question객체를 DB에서 가져와 할당
2. choice 변수에 pk가 Choice객체를 DB에서 가져와 할당
3. choice의 votes 속성값을 1증가
4. choice의 변경사항을 DB에 저장
5. 
    
    :param request: 
    :param choice_pk: 
    :return: 
"""
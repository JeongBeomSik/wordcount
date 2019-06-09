from django.shortcuts import render

# Create your views here.
def home(request):
    text="워드카운트"
    fruit=['사과','배','감','귤']
    context={'text':text, 'fruit':fruit}
    return render(request, "helloworld/helloworld.html", context)

def result(request):
    text = request.GET.get('text')
    words = text.split(' ')
    wordcnt={}
    for i in words:
        if i in wordcnt:
            wordcnt[i]=wordcnt[i]+1
        else:
            wordcnt[i]=1    
    
    context = {'text': text, 'words':words, 'wordcnt_item':wordcnt.items()}
    return render(request,"helloworld/helloworld.html", context)

    
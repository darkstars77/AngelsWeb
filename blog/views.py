from django.shortcuts import render, render_to_response , HttpResponseRedirect
from .models import Post
from django.utils import timezone

# Create your views here.
def main_page(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'WebView/index.html', {})

def show_write_form(request):
    return render_to_response('WebView/writeBoard.html')

def DoWriteBoard(request):
    post = Post(title=request.POST['subject'],
              author=request.POST['name'],
              text=request.POST['memo'],
              created_date=timezone.now(),
              hits=0
              )
    post.save()

    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/listSpecificPageWork?current_page=1'
    return HttpResponseRedirect(url)

def listSpecificPageWork(request):
    return render_to_response('listSpecificPage.html')
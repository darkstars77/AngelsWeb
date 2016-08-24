from django.shortcuts import render, render_to_response , HttpResponseRedirect , HttpResponse , get_object_or_404
from .models import Post, Product
from django.utils import timezone

# Create your views here.
def main_page(request):
    return render(request, 'WebView/index.html', {})

def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    response_text = '<p>{product_id}번...{product_id}번 상품을 보여 드릴게요.</p>'
    response_text += '<p>{product_url}</p>'
    response_text += '<p><img src="{product_url}"/></p>'
    return HttpResponse(response_text.format(
        product_id=product_id,
        product_url=product.image_file.url
        )
    )



#기능 테스트용 함수들
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
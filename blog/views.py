from django.shortcuts import render, render_to_response , HttpResponseRedirect , HttpResponse , get_object_or_404
from .models import Product


# Create your views here.
def main_page(request):
    pants = Product.objects.filter(title="바지")
    skirts = Product.objects.filter(title="스커트")
    tshirts = Product.objects.filter(title="티셔츠")
    return render(request, 'WebView/index.html', {'pants': pants, 'tshirts': tshirts, 'skirts': skirts})

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
def search_product(request):
    if 'product_number' in request.GET:
        product_id = int(request.GET['product_number'])
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'WebView/search_result.html', {'product': product})
    else:
        return HttpResponse('검색어를 입력하지 않으셨습니다.')

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
def search_product(request):
    if 'product_number' in request.GET:
        product_id = int(request.GET['product_number'])
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'WebView/search_result.html', {'product': product})
    else:
        return HttpResponse('검색어를 입력하지 않으셨습니다.')
'''
    if 'product_number' in request.GET:
        product_id = int(request.GET['product_number'])
        product = get_object_or_404(Product, pk=product_id)
        response_text = '<p> 상품번호 : {product_id}번 상품이름 : {product_title}</p>'
        response_text += '<p><img src="{product_url}"/></p>'
        response_text += '<p>Price_Positive : {pricePos}</p>'
        response_text += '<p>Price_Negative : {priceNeg}</p>'
        response_text += '<p>Delivery_Positive : {deliveryPos}</p>'
        response_text += '<p>Delivery_Negative : {deliveryNeg}</p>'
        response_text += '<p>Size_Positive : {sizePos}</p>'
        response_text += '<p>Size_Negative : {sizeNeg}</p>'
        response_text += '<p>Extra_Positive : {extraPos}</p>'
        response_text += '<p>Extra_Negative : {extraNeg}</p>'
        return HttpResponse(response_text.format(
            product_id=product_id,
            product_url=product.image_file.url,
            product_title=product.title,
            pricePos=product.pricePos,
            priceNeg=product.priceNeg,
            deliveryPos=product.deliveryPos,
            deliveryNeg=product.deliveryNeg,
            sizePos=product.sizePos,
            sizeNeg=product.sizeNeg,
            extraPos=product.extraPos,
            extraNeg=product.extraNeg
            )
        )
'''



#기능 테스트용 함수들
def show_write_form(request):
    return render_to_response('WebView/writeBoard.html')

def search_result(request):
    return render(request, 'WebView/search_result.html', {})
from django.shortcuts import render, render_to_response , HttpResponseRedirect , HttpResponse , get_object_or_404
from .models import Product


# Create your views here.
def main_page(request):
    pants = Product.objects.filter(title="바지")
    skirts = Product.objects.filter(title="스커트")
    tshirts = Product.objects.filter(title="티셔츠")
    return render(request, 'WebView/index.html', {'pants': pants, 'tshirts': tshirts, 'skirts': skirts})
    #return render(request, 'WebView/product_list.html')


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
    if request.GET['product_number']:
        product_id = int(request.GET['product_number'])
        product = get_object_or_404(Product, pk=product_id)

        return render(request, 'WebView/search_result.html', {'product': product})
    else:
        return HttpResponse('검색어를 입력하지 않으셨습니다.')

def search_keyword_product(request):
    if request.GET['product_keyWord']:
        word = request.GET['product_keyWord']

        if word == "바지Size":
            products = Product.objects.filter(title="바지")
            ordered = products.order_by('-sizePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "바지Delivery":
            products = Product.objects.filter(title="바지")
            ordered = products.order_by('-deliveryPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "바지Price":
            products = Product.objects.filter(title="바지")
            ordered = products.order_by('-pricePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "바지Extra":
            products = Product.objects.filter(title="스커트")
            ordered = products.order_by('-extraPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "스커트Size":
            products = Product.objects.filter(title="스커트")
            ordered = products.order_by('-sizePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "스커트Delivery":
            products = Product.objects.filter(title="스커트")
            ordered = products.order_by('-deliveryPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "스커트Price":
            products = Product.objects.filter(title="스커트")
            ordered = products.order_by('-pricePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "스커트Extra":
            products = Product.objects.filter(title="바지")
            ordered = products.order_by('-extraPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "티셔츠Size":
            products = Product.objects.filter(title="티셔츠")
            ordered = products.order_by('-sizePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "티셔츠Delivery":
            products = Product.objects.filter(title="티셔츠")
            ordered = products.order_by('-deliveryPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "티셔츠Price":
            products = Product.objects.filter(title="티셔츠")
            ordered = products.order_by('-pricePos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "티셔츠Extra":
            products = Product.objects.filter(title="티셔츠")
            ordered = products.order_by('-extraPos')
            return render(request, 'WebView/product_list.html', {'products': ordered})

        if word == "바지" or word == "티셔츠" or word == "스커트":
            products = Product.objects.filter(title=request.GET['product_keyWord'])
            return render(request, 'WebView/product_list.html', {'products': products})
        else:
            return HttpResponse('해당 키워드의 검색 내용은 존재하지 않습니다')
    else:
        return HttpResponse('검색어를 입력하지 않으셨습니다.')

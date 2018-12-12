from django.shortcuts import render,render_to_response,get_list_or_404,redirect
from .models import Product_Details,Restaurant,User_Details,Cart
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

def resturent_data(request):
    data=Restaurant.objects.all()


    context={
        'data':data,




    }
    return render(request,'product/resturent.html',context)


def product_data(request,id):
    product_data = Product_Details.objects.all()
    data = Restaurant.objects.filter(id=id).values()

    context={
        'product_data':product_data,
        'data': data,




    }
    return render(request, 'product/product.html', context)

#
# def cart_data(request,product_id):
#     product=Product_Details.objects.get(id=product_id)
#     cart1=Cart.objects.create(user_id=request.user.id,quantity=1,total=product.product_price, products_id=product_id,unit_total=product.product_price)
#     # cart1.products.set(Product_Details.objects.filter(pk=product_id))
#     cart1.save()
#
#
#
#
#     # cart.products.add(product.product_name)
#     # cart.save()
#
#
#
#
#     # context={
#     #     'product_data':product,
#     #     'cart1':cart1
#     #
#     #
#     #
#     #
#     # }
#     # return render(request,'product/cart_add.html',context)
#
#     return redirect(cart_view)
#
#
#
#
#
#
# def cart_view(request):
#     cart_detail=Cart.objects.filter(user_id=request.user.id)
#     a=request.user
#     # product_data = Product_Details.objects.filter(id=product_id)
#     data = Restaurant.objects.all()
#     totals=0
#
#     for order in cart_detail:
#         totals += order.unit_total
#
#
#     context={
#         'cart_detail':cart_detail,
#         # 'product_data':product_data,
#         'data':data,
#         'a':a,
#         'totals':totals
#     }
#     return render(request,'product/cart_add.html',context)
#
# def update_quantity(request, n1, n2):
#     cart=Cart.objects.get(id=int(n1))
#
#     if int(n2) == 1:
#         cart.quantity +=1
#     if int(n2) == 0:
#         cart.quantity -= 1
#         if cart.quantity==0:
#             cart.delete()
#     cart.save()
#     return redirect(cart_view)
#
#
#








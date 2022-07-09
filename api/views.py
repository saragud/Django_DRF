# from django.shortcuts import render
# from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAdminUser
# from rest_framework.viewsets import ModelViewSet
# from eshop_products.models import Product
# from eshop_sliders.models import Slider
# from django.contrib.auth import get_user_model
# from .serializers import ProductSerializer, UserSerializer, SliderSerializer
# # Create your views here.
#
#
# # class ProductList(ListCreateAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
# #
# #
# # class ProductDetail(RetrieveUpdateDestroyAPIView):
# #     queryset = Product.objects.all()
# #     serializer_class = ProductSerializer
#
#
# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = (IsAdminUser,)
#     filterset_fields = ['active']
#     search_fields = ['title', 'description']
#     ordering_fields = ['price']
#     # def get_queryset(self):
#     #
#     #     active = self.request.query_params.get('active')
#     #     if active is not None:
#     #         queryset = queryset.filter(active=active)
#     #     return queryset
#
# def get_most_visit(self):
#         most_visit_product = Product.objects.order_by('-visit_count').all()[:8]
#         return most_visit_product
#
#
# def get_latest_product(self):
#         latest_products = Product.objects.order_by('-id').all()[:8]
#         return latest_products
#
#
# # class UserList(ListCreateAPIView):
# #     queryset = get_user_model().objects.all()
# #     serializer_class = UserSerializer
# #     permission_classes = (IsAdminUser,)
# #
# #
# # class UserDetail(RetrieveUpdateDestroyAPIView):
# #     queryset = get_user_model().objects.all()
# #     serializer_class = UserSerializer
# #     permission_classes = (IsAdminUser,)
#
#
# class UserViewSet(ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
#
#
# class SlidersList(ListAPIView):
#     queryset = Slider.objects.all()
#     serializer_class = SliderSerializer

# ************************************************************
import itertools

from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from eshop_products.models import Product
from eshop_products_category.models import ProductCategory
from eshop_sliders.models import Slider
from .serializers import ProductSerializer, SliderSerializer, CategorySerializer
from rest_framework import status
from django.http import Http404




# class GetActiveProducts(APIView):
#     def get_active(self, request):
#         query = Product.objects.filter(active=True)
#         serializer = ProductSerializer(query, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class GetProductDetail(APIView):
    # def product_detail(request, *args, **kwargs):
    #     selected_product_id = kwargs['productid']
    #     query = Product.objects.get(pk=selected_product_id)
    #     serializer = ProductSerializer(query)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def product_datail(request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ProductSerializer(product)
            if product is None or not product.active:
                raise Http404('محصول مورد نظر یافت نشد')
            product.visit_count += 1
            product.save()
            print('*****************************')
            print(product.visit_count)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_products(self):
     query = Product.objects.all()
     serializer = ProductSerializer(query, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST', 'GET'])
# def get_category(self, category):
#     print(category)
#     category_name = self.get('category_name')
#     category = ProductCategory.objects.filter(name__iexact=category_name).first()
#     if category is None:
#         raise Http404('صفحه مورد نظر یافت نشد')
#     query = Product.objects.get_products_by_category(category_name)
#     serializer = CategorySerializer(query, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# class SlidersList(ListAPIView):
#     queryset = Slider.objects.all()
#     serializer_class = SliderSerializer


@api_view(['GET'])
def get_sliders(self):
     query = Slider.objects.all()
     serializer = SliderSerializer(query, many=True)
     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def most_visited(self):
    most_visit_product = Product.objects.order_by('-visit_count').all()
    print(type(most_visit_product))
    for p in list(most_visit_product):
        p_id = Product.objects.get(id)
        print('**********************************************')
    query = Product.objects.filter(orderdetail__order_id=p_id)
    serializer = ProductSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def latest_product(self):
    latest_products = Product.objects.order_by('-id').all()
    print(latest_products)
    for l in list(latest_products):
        l_id = Product.objects.get(id)
    query = Product.objects.filter(orderdetail__order_id=l_id)
    serializer = ProductSerializer(query, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse
from django.shortcuts import render  # render 함수를 import

def main(request):
    # return HttpResponse("안녕하세요, pyburger입니다")
    return render(request, "main.html")  # HttpResponse 대신 render 함수 사용


def burger_list(request):
    # return HttpResponse("pyburger의 햄버거 목록입니다")
    return render(request, "burger_list.html")  # httpResponse 대신 render 함수 사용


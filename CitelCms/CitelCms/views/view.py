# -*- coding: utf-8 _*_

from django.shortcuts import render
from django.http import HttpResponse


def baseTemplate(request):
    return render(request,'base.html');
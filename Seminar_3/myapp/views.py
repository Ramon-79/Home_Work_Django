import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Висизэ а майн пайдж виз проджект")


def about(request):
    logger.info('Index page accessed')
    return HttpResponse("Хэлоу гайз! Майн найм из Саша. Ай эм фром раша.")


from django.shortcuts import render
from django.http import HttpResponse
import RPi.GPIO as GPIO
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

LED_PIN =12

def turnOn(request):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN,1)
    return HttpResponse("luz encendida")


def turnOff(request):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN,0)
    return HttpResponse("luz apagada")

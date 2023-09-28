import openai
import nltk
import cv2
import io
from PIL import Image, ImageTk
import tkinter as tk
import requests
import pytesseract

api_key = "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"

class Animator:
    def __init__(self, api_key):
        openai.api_key = api_key

        

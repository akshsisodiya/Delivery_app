from django.db import models

class CardView:
    def __init__(self,title,img,description):
        self.title=title
        self.img=img
        self.description=description
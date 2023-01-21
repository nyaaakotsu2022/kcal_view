from model.dezato.dezato import check_photo_dezato
from model.dezato.dezato2 import check_photo_dezato2

def dezato_judge(foodpicture, number): return sorted([check_photo_dezato(foodpicture, number), check_photo_dezato2(foodpicture, number)], reverse=True)[0]
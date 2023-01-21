from model.wasyoku.wasyoku import check_photo_wasyoku
from model.wasyoku.wasyoku2 import check_photo_wasyoku2
from model.wasyoku.wasyoku3 import check_photo_wasyoku3

def wasyoku_judge(foodpicture, number): return sorted([check_photo_wasyoku(foodpicture, number), check_photo_wasyoku2(foodpicture, number), check_photo_wasyoku3(foodpicture, number)], reverse=True)[0]

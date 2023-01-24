from model.tyuka.tyuka import check_photo_tyuka
from model.tyuka.tyuka2 import check_photo_tyuka2

def tyuka_judge(foodpicture, number): return sorted([check_photo_tyuka(foodpicture, number), check_photo_tyuka2(foodpicture, number)], reverse=True)[0]

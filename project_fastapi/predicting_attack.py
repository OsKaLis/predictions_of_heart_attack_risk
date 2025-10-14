"""
Обработка файла и дополнить его предсказанием по риску приступа
"""

import csv

def predict_the_risk(file_name: str, file: object):
    """Получаем фаил и делеем предсказание на данных и сохраняем фаил"""
    # обработка
    file.to_csv(file_name, index=False)
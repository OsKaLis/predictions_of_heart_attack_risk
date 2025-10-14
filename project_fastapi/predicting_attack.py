"""
Обработка файла и дополнить его предсказанием по риску приступа
"""

import csv
from joblib import load

def predict_the_risk(file_name: str, file: object):
    """Получаем фаил и делеем предсказание на данных и сохраняем фаил"""
    best_model = load('best_model.joblib')
    # Подготовка данных для предсказания
    file['y_pred'] = best_model.decision_function(file)
    file.to_csv(file_name, index=False)
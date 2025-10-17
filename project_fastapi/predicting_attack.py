"""
Обработка файла и дополнить его предсказанием по риску приступа
"""

import os
import csv
import logging
import datetime as dt
from joblib import load

class RiskPrediction:

    file_name: str = ''
    temp_file = 'temp_file'
    data: object = None
    model = 'best_model.joblib'

    def add(self, file_name: str, data: object):
        """Добавление название файла и сами данные"""
        self.file_name = file_name
        self.data = data

    def predict_the_risk(self):
        """Делаю предсказание"""
        if os.path.isfile(self.model):
            best_model = load('best_model.joblib')
            #self.data['y_pred'] = best_model.decision_function(self.data)
            self.data.to_csv(self.temp_file, index=False)
        else:
            logging.error(f'[{dt.datetime.now()}] Фаил обученой модели не найден.')

    def get_file(self):
        """Получить фаил"""
        if not os.path.isfile(self.temp_file):
            logging.error(f'[{dt.datetime.now()}] Фаил предсказание не найден.')
            return False
        return self.temp_file
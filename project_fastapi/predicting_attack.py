"""
Обработка файла и дополнить его предсказанием по риску приступа
"""

import os
import csv
import logging
import pandas as pd
import datetime as dt
from joblib import load

class RiskPrediction:

    # Основные показатели
    file_name: str = ''
    temp_file = 'temp_file'
    data: object = None
    model = 'best_model.joblib'
    target_probability_signs_of = 0.5
    target_attribute = 'heart_attack_risk'
    the_best_fields = [
        'gender',
        'diabetes',
        'age',
        'cholesterol',
        'heart_rate',
        'exercise_hours_per_week',
        'diet',
        'stress_level',
        'sedentary_hours_per_day',
        'income',
        'bmi',
        'triglycerides',
        'physical_activity_days_per_week',
        'sleep_hours_per_day',
        'blood_sugar',
        'ck-mb',
        'troponin',
        'systolic_blood_pressure',
        'diastolic_blood_pressure',
    ]
    full_fields = {
        'Age': 'age',
        'Cholesterol': 'cholesterol',
        'Heart rate': 'heart_rate',
        'Diabetes': 'diabetes',
        'Family History': 'family_history',
        'Smoking': 'smoking',
        'Obesity': 'obesity',
        'Alcohol Consumption': 'alcohol_consumption',
        'Exercise Hours Per Week': 'exercise_hours_per_week',
        'Diet': 'diet',
        'Previous Heart Problems': 'previous_heart_problems',
        'Medication Use': 'medication_use',
        'Stress Level': 'stress_level',
        'Sedentary Hours Per Day': 'sedentary_hours_per_day',
        'Income': 'income',
        'BMI': 'bmi',
        'Triglycerides': 'triglycerides',
        'Physical Activity Days Per Week': 'physical_activity_days_per_week',
        'Sleep Hours Per Day': 'sleep_hours_per_day',
        'Blood sugar': 'blood_sugar',
        'CK-MB': 'ck-mb',
        'Troponin': 'troponin',
        'Gender': 'gender',
        'Systolic blood pressure': 'systolic_blood_pressure',
        'Diastolic blood pressure': 'diastolic_blood_pressure',
    }

    def migration_by_gender(self, row):
        """Класифицируем признак конкретней на три значения"""
        if row == '1.0':
            return 'Male'
        elif row == '0.0':
            return 'Female'
        return row

    def сlassifying_the_feature_in_detail(self, row):
        """Подгатавливаем признак на три значения"""
        if row == 0:
            return 'нет'
        elif row == 1:
            return 'да'
        elif pd.isna(row):
            return 'неизвестно'

    def correction_of_signs(self):
        """Подготовка признаков для предсказаний"""
        temp_data = self.data.drop(['id', 'Unnamed: 0'], axis=1)
        list_columns = list()
        for x in temp_data.columns:
            list_columns.append(self.full_fields[x])
        temp_data.columns = list_columns
        list_signs = [
            'diabetes',
            'family_history',
            'smoking',
            'obesity',
            'alcohol_consumption',
            'previous_heart_problems',
            'medication_use'
        ]
        for x in list_signs:
            temp_data[x] = temp_data[x].apply(self.сlassifying_the_feature_in_detail)
        list_signs = [
            'stress_level',
            'physical_activity_days_per_week',
        ]
        for x in list_signs:
            temp_data[x] = temp_data[x].fillna(temp_data[x].median())
        temp_data['gender'] = temp_data['gender'].apply(self.migration_by_gender)
        return temp_data[self.the_best_fields]

    def matching_the_target_attribute(self):
        """Подготовка целевого признака к соответствию"""
        self.data['prediction'] = (
            self.data['prediction'].apply(lambda x: 1 if x > self.target_probability_signs_of else 0)
        )
    def add(self, file_name: str, data: object):
        """Добавление название файла и сами данные"""
        self.file_name = file_name
        self.data = data

    def predict_the_risk(self):
        """Делаю предсказание"""
        if os.path.isfile(self.model):
            best_model = load('best_model.joblib')
            self.data['prediction'] = best_model.decision_function(self.correction_of_signs())
            self.matching_the_target_attribute()
            self.data.to_csv(self.temp_file, index=False)
        else:
            logging.error(f'[{dt.datetime.now()}] Фаил обученой модели не найден.')

    def get_file(self):
        """Получить фаил"""
        if not os.path.isfile(self.temp_file):
            logging.error(f'[{dt.datetime.now()}] Фаил предсказание не найден.')
            return False
        return self.temp_file
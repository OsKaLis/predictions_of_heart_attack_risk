<div id="header" align="center">
  <h1>Predicting a heart attack</h1>
</div>

## Описание проекта:

> Представляем инновационное веб-приложение на базе современного фреймворка FastAPI, разработанное для автоматизации процесса анализа данных.
> Ключевая функциональность приложения заключается в обработке CSV-файлов тестовых выборок через интуитивно понятный веб-интерфейс. Система обеспечивает эффективное взаимодействие посредством POST-запросов к серверу для выполнения предсказаний, что гарантирует высокую производительность и надежность работы.
> Результаты анализа предоставляются в универсальном формате JSON, который экспортируется в виде готового файла. Такой подход обеспечивает:
+ Простоту использования для конечных пользователей;
+ Гибкость интеграции с другими системами;
+ Высокую скорость обработки данных;
+ Надёжность хранения и передачи информации.

## Cтек технологий:
<img src="https://img.shields.io/badge/Scikit--Learn:_-1.6.1-purple">
<img src="https://img.shields.io/badge/Pandas:_-2.2.3-slategrey">
<img src="https://img.shields.io/badge/Python:_-3.13.0-greem">
<img src="https://img.shields.io/badge/FastAPI:_-0.119.0-green">
<img src="https://img.shields.io/badge/Uvicorn:_-0.37.0-red">
<img src="https://img.shields.io/badge/Poetry:_-2.0.0-blue">

## Как развернуть проект на локальной машине:


### 1. Клонируем проект:
```
git clone git@github.com:OsKaLis/predictions_of_heart_attack_risk.git
```
### 2. Переходим в директорию проекта:
```
cd predictions_of_heart_attack_risk/
```
### 3. Необходимо проверить установленную версию Python:
```
python3 -V
```
- Если у вас версия 3.13.*, то можно переходить к шагу 4.
- Если версия не 3.13.*, то необходимо её установить.
### 4. Устанвка `poetry`:
```
pip install poetry
```
- [Не большое руководство по `poetry`](https://habr.com/ru/articles/740376/)
### 5. Проверка что `poetry` установлен:
```
poetry -V
```
### 6. Запускаем виртуальное окружение из папки "predictions_of_heart_attack_risk":
``` 
poetry shell
```
### 7. Устанавливаем установка зависимости для окружения:
```
poetry install
```
### 8. Переходим в директорию проекта:
```
cd project_fastapi/
```
### 9. Запускаем проекта локально: 
```
poetry run uvicorn main:app --reload
```

## Демонстрация работы:
### Стартовая страница
![Интерфейс программы GEryCH](https://github.com/OsKaLis/GEryCH/blob/8a9c36c2ccee63d744fd8acadb5bfd511656c791/images/GEryCH.png)
### Выбор файла
![Интерфейс программы GEryCH](https://github.com/OsKaLis/GEryCH/blob/8a9c36c2ccee63d744fd8acadb5bfd511656c791/images/GEryCH.png)
### После нажатия на кнопру [Загрузить]
![Интерфейс программы GEryCH](https://github.com/OsKaLis/GEryCH/blob/8a9c36c2ccee63d744fd8acadb5bfd511656c791/images/GEryCH.png)

## Сылка на документацию:
http://127.0.0.1:8000/docs

## Автор: Юшко Ю.Ю.

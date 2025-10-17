import logging
import datetime as dt
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.datastructures import UploadFile
from predicting_attack import RiskPrediction

logging.basicConfig(
    filename='main.log',
    level=logging.INFO
)
app = FastAPI()
templates = Jinja2Templates(directory='templates')
new_file = RiskPrediction()

logging.info(f'[{dt.datetime.now()}] Старт проекта !!!')

@app.get('/')
def main(request: Request):
    """Стартавая страница для загруски файла"""
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/result', response_class=HTMLResponse)
def main(request: Request):
    """Страница получения результата"""
    return templates.TemplateResponse('result.html', {'request': request, 'file_name': new_file.file_name})

@app.post('/submits')
def submits(file: UploadFile):
    """Загруска фаила с данными и обработка его к конечному результату"""
    new_file.add(file.filename, pd.read_csv(file.file))
    new_file.predict_the_risk()
    return {'url': '/result'}

@app.get("/download")
def download_file(request: Request):
    """Эндпоинт на скачивание готового файла"""
    if not new_file.get_file():
        text = 'Фаил не создан попробуйте ещё раз !!!'
        return templates.TemplateResponse('result.html', {'request': request, 'file_name': text})
    return FileResponse(
            path=new_file.get_file(),
            filename=new_file.file_name,
            media_type='multipart/form-data'
        )
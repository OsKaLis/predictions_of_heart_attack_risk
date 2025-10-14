import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.datastructures import UploadFile

from predicting_attack import predict_the_risk

app = FastAPI()
templates = Jinja2Templates(directory='templates')

FILE_TEMP: str = ''

@app.get('/')
def main(request: Request):
    """Стартавая страница для загруски файла"""
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/result', response_class=HTMLResponse)
def main(request: Request):
    """Страница получения результата"""
    return templates.TemplateResponse('result.html', {'request': request, 'file_name': FILE_TEMP})

@app.post('/submits')
def submits(file: UploadFile):
    """Загруска фаила с данными и обработка его к конечному результату"""
    global  FILE_TEMP
    FILE_TEMP = file.filename
    df = pd.read_csv(file.file)
    predict_the_risk(file.filename, df)
    return {'url': '/result'}

@app.get("/download")
def download_file():
    """Эндпоинт на скачивание готового файла"""
    return FileResponse(
        path=FILE_TEMP,
        filename='предсказание.csv',
        media_type='multipart/form-data'
    )
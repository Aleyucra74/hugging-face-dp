import fuzzywuzzy
import transformers
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from transformers import pipeline
import cv2
import pickle
import os, json
import pytesseract
from PIL import Image
from sklearn import preprocessing
from pdf2image import convert_from_path
from sklearn.feature_extraction.text import CountVectorizer
import config

model_name = 'pierreguillou/bert-large-cased-squad-v1.1-portuguese'
nlp = pipeline("question-answering", model=config.PATH_HUGGING_FACE)
answers={}

def answers_hugging_face(path, filename):
  tessdata_dir_config = '--tessdata-dir "C:\\Users\\rysilva\\AppData\\Local\\Programs\\Tesseract-OCR\\tessdata"'

  image_path = convert_from_path(path,500, output_folder=config.PATH_IMAGES,fmt='jpeg',output_file=filename,
                                 poppler_path=config.POPPLET_PATH)
  img = cv2.imread(config.PATH_IMAGES+f'/{filename}0001-1.jpg')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  pytesseract.pytesseract.tesseract_cmd = config.PATH_TESSERACT
  text = pytesseract.image_to_string(img, config=tessdata_dir_config)

  answers["texto"] = text

  for i in config.questions_nfse:
    result = nlp(question=i, context=text)
    answers[i] = {'resultado':result['answer'],'score':round(result['score'],4),'start':result['start'],'end':result['end']}

  return answers


def predict_template(text):

  with open('json_files_names_yml.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

  dataJson = json.loads(data)
  template={}

  for i in dataJson['file_names_yml']:
    result = fuzz.token_set_ratio(text,i)

    if result == 100:
      template['text']=text
      template['result']=result
      template['template']=i

  return template
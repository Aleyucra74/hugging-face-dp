from fuzzywuzzy import fuzz
from transformers import pipeline
import cv2
import pickle
import json
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from sklearn.feature_extraction.text import CountVectorizer
import config
from models.nfse_predict import NfsePredict

model_name = 'pierreguillou/bert-large-cased-squad-v1.1-portuguese'
nlp = pipeline("question-answering", model=config.PATH_HUGGING_FACE)
answers = []


def transform_nota_text(frompath,filename):
  convert_from_path(frompath, 500, output_folder=config.PATH_IMAGES, fmt='jpeg', output_file=filename,
                                 poppler_path=config.POPPLET_PATH)

  image_path = config.PATH_IMAGES + f'/{filename}0001-1.jpg'

  img = cv2.imread(image_path)
  height, width, channels = img.shape

  y1 = int(height * 0.13)
  x2 = int(width * 0.70)
  x1 = int(width * 0.20)

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  crop = gray[10:y1, x1:x2]

  cv2.imwrite(image_path, crop)
  pytesseract.pytesseract.tesseract_cmd = config.PATH_TESSERACT
  text = pytesseract.image_to_string(Image.open(image_path),config=config.tessdata_dir_config)
  main_text = text.replace('\n', ' ')

  return main_text


def return_predict_mun(text):

  vectorizer2 = CountVectorizer(vocabulary=config.GABARITO)
  dop1 = vectorizer2.transform([text]).toarray()

  with open(config.PATH_MODELPKL, 'rb') as training_model:
    model = pickle.load(training_model)
  output2 = model.predict(dop1)

  return convert_predict_to_municipio(int(output2))


def answers_hugging_face(path, filename):

  convert_from_path(path,500, output_folder=config.PATH_IMAGES,fmt='jpeg',output_file=filename,
                                 poppler_path=config.POPPLET_PATH)
  img = cv2.imread(config.PATH_IMAGES+f'/{filename}0001-1.jpg')
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  pytesseract.pytesseract.tesseract_cmd = config.PATH_TESSERACT
  text = pytesseract.image_to_string(img, config=config.tessdata_dir_config)

  # answers["texto"] = text

  for i in config.questions_nfse:
    result = nlp(question=i, context=text)
    answers.append(NfsePredict(i,result['answer'],round(result['score'],4)))

  return answers


def predict_template(text):

  with open('content\modelos\json_files_names_yml.json', encoding='utf-8') as json_file:
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

def convert_predict_to_municipio(nota):
    if nota == 1:
      return 'BARUERI'
    elif nota == 2:
      return 'CAMPINAS'
    elif nota == 3:
      return 'FORTALEZA'
    elif nota == 4:
      return 'HORTOLANDIA'
    elif nota == 5:
      return 'JUNDIAI'
    elif nota == 6:
      return 'MACAE'
    elif nota == 7:
      return 'POUSO ALEGRE'
    elif nota == 8:
      return 'SAO PAULO'
    elif nota == 9:
      return 'RIO DE JANEIRO'
    elif nota == 10:
      return 'SANTOS'
    elif nota == 12:
      return 'SAO CAETANO DO SUL'
    elif nota == 14:
      return 'SOROCABA'
    elif nota == 15:
      return 'VITORIA'
    else:
      return 'Nao existe no modelo'

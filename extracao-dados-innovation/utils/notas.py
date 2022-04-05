import os
import cv2
import pickle
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from sklearn.feature_extraction.text import CountVectorizer
import config
from config import UPLOAD_FOLDER

def transform_nota_text(filename):
    main_text = ''
    frompath = UPLOAD_FOLDER + 'a_notas_fiscais\\' + filename
    topath = UPLOAD_FOLDER + 'images'
    image_path = convert_from_path(frompath, 500, output_folder=topath, fmt='jpeg', output_file=filename,
                                   poppler_path=r"C:\Users\rysilva\Downloads\poppler-21.11.0\Library\bin")
    img = cv2.imread(UPLOAD_FOLDER + f'images/{filename}0001-1.jpg')
    height, width, channels = img.shape
    y1 = int(height * 0.13)
    x2 = int(width * 0.70)
    x1 = int(width * 0.20)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    crop = gray[10:y1, x1:x2]
    file = UPLOAD_FOLDER + f'images/{filename}0001-1.jpg'
    cv2.imwrite(file, crop)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rysilva\Documents\Tesseract\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(file))
    main_text = text.replace('\n', ' ')
    return main_text

def predict_nota(text):

  vectorizer2 = CountVectorizer(vocabulary=config.GABARITO)
  dop1 = vectorizer2.transform([text]).toarray()
  with open(config.PATH_MODELPKL, 'rb') as training_model:
    model = pickle.load(training_model)
  output2 = model.predict(dop1)
  return output2

def convert_predict_to_municipio(nota):
    if nota == 1:
        return 'BARUERI'
    elif nota == 2:
      return 'CAMPINAS'
    elif nota == 3 :
      return 'FORTALEZA'
    elif nota == 4 :
      return 'HORTOLANDIA'
    elif nota == 5 :
      return 'JUNDIAI'
    elif nota == 6 :
      return 'MACAE'
    elif nota == 7 :
      return 'POUSO ALEGRE'
    elif nota == 8 :
      return 'SAO PAULO'
    elif nota == 9 :
      return 'RIO DE JANEIRO'
    elif nota == 10 :
      return 'SANTOS'
    elif nota == 12 :
      return 'SAO CAETANO DO SUL'
    elif nota == 14:
      return 'SOROCABA'
    elif nota == 15:
      return 'VITORIA'
    else :
      return 'Nao existe no modelo'

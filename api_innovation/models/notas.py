import cv2
import pickle
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
from sklearn.feature_extraction.text import CountVectorizer
import config
from config import UPLOAD_FOLDER

def transform_nota_text(filename):
  frompath = UPLOAD_FOLDER+'a_notas_fiscais\\'+filename
  topath = UPLOAD_FOLDER+'images'
  image_path = convert_from_path(frompath, 500,output_folder=topath,fmt='jpeg',output_file=filename, poppler_path = config.POPPLET_PATH)
  img = cv2.imread(UPLOAD_FOLDER + f'images/{filename}0001-1.jpg')
  height, width, channels = img.shape
  y1=int(height*0.13)
  x2=int(width*0.70)
  x1=int(width*0.20)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  crop = gray[10:y1,x1:x2]
  file = UPLOAD_FOLDER + f'images/{filename}0001-1.jpg'
  cv2.imwrite(file,crop)
  pytesseract.pytesseract.tesseract_cmd = config.PATH_TESSERACT
  text = pytesseract.image_to_string(Image.open(file), lang="eng")
  #os.remove(path+'a_notas_fiscais\\'+filename)
  #os.remove(path+'images\\'+filename+'0001-1.jpg')
  #os.remove(path+'images_grays\\'+filename+'.png')
  return text.replace('\n', ' ')

def predict_nota(text):

  vectorizer2 = CountVectorizer(vocabulary=config.GABARITO)
  dop1 = vectorizer2.transform([text]).toarray()
  with open(config.PATH_MODELPKL, 'rb') as training_model:
    model = pickle.load(training_model)
  output2 = model.predict(dop1)
  return output2

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS
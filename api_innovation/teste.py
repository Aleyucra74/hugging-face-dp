from zipfile import ZipFile
import config

with ZipFile(r'C:\Users\rysilva\Documents\INNOVATION\hugging-face-dp\api_innovation\content\operacao\a_notas_fiscais\NFSe.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall(path = config.PATH_DESCOMPACTADOS)

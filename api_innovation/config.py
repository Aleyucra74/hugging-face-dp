import secrets
import urllib.parse

# UPLOAD_FOLDER = 'C:\\Users\\rysilva\\Desktop\\api_innovation\\content\\operacao\\'
UPLOAD_FOLDER = 'C:\\Users\\rysilva\\Documents\\INNOVATION\\hugging-face-dp\\api_innovation\\content\\operacao\\a_notas_fiscais\\'

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
ALLOWED_EXTENSIONS = {'pdf', 'zip'}

SECRET_KEY = secrets.token_hex(16)

GABARITO = ['0001', '0005', '004', '02', '06', '12', '13', '15', '17', '18',
       '19', 'alegre', 'aparecida', 'barueri', 'bernardo', 'caetano',
       'campinas', 'campo', 'carioca', 'cidade', 'dados', 'das', 'elo',
       'es', 'finangas', 'fortaleza', 'go', 'goiania', 'hortolandia',
       'imperial', 'iota', 'janeiro', 'jardim', 'jundiai', 'ltda',
       'macae', 'na', 'nfe', 'pagina', 'paulo', 'pouso', 'recife', 'rio',
       'rua', 'santos', 'servigos', 'sorocaba', 'sul', 'telecomunicagoes',
       'vitoria']

PATH_MODELPKL = 'C:\\Users\\rysilva\\Desktop\\api_innovation\\content\\operacao\\modelos\\model_pkl'

PATH_EXCEL = 'C:\\Users\\rysilva\\Documents\\INNOVATION\\hugging-face-dp\\api_innovation\\content\\operacao\\excel\\'

PATH_TESSERACT = r'C:\Users\rysilva\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

POPPLET_PATH = r"C:\Users\rysilva\Downloads\poppler-21.11.0\Library\bin"

PARAMS = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=BRDCVMTAXANDBD;DATABASE=INNOVATION;Trusted_Connection=yes")

PATH_DESCOMPACTADOS = r'C:\Users\rysilva\Documents\INNOVATION\hugging-face-dp\api_innovation\content\operacao\descompactados'

questions_nfse = [
  "Qual o CNPJ do Tomador de Serviço?",
  "Qual o CNPJ do Prestador de Serviço?",
  "Qual o Número da Nota/Nº ?",
  "Qual a Data de Emissão da Nota Fiscal?",
  "Qual a Hora de Emissão da Nota Fiscal?",
  "Qual o Código de Verificação?",
  "Qual o Código de Serviço?",
  "Qual o Valor dos serviços/Valor Total da Nota?",
]
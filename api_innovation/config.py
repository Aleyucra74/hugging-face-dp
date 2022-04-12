import secrets
import urllib.parse

UPLOAD_FOLDER = r'\\Brdcvmtaxanapd\innovation\operacao\a_notas_fiscais'

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

PATH_MODELPKL = r'\\Brdcvmtaxanapd\innovation\model\model_pkl'

PATH_IMAGES = r'\\Brdcvmtaxanapd\innovation\operacao\images'

PATH_EXCEL = r'\Brdcvmtaxanapd\innovation\operacao\excel'

PATH_TESSERACT = r'C:\Users\rysilva\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
PATH_TESSDATA = r'C:\Users\rysilva\AppData\Local\Programs\Tesseract-OCR\tessdata'

POPPLET_PATH = r"\\Brdcvmtaxanapd\innovation\poppler\Library\bin"

PARAMS = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=BRDCVMTAXANDBD\TAXDESENV;DATABASE=INNOVATION;Trusted_Connection=yes")

PATH_DESCOMPACTADOS = r'\\Brdcvmtaxanapd\innovation\operacao\descompactados'

import pytesseract
import cv2
import fitz

import os
def proc(imgn):
    img = cv2.imread(f'{imgn}')
    crop_img1 = img[25:73, 250:843].copy()
    crop_img2 = img[10:170,20:230].copy()
    text=pytesseract.image_to_string(crop_img1).replace('\n', '')
    return [text, crop_img2]


def convert_pdf2img(input_file: str, pages: tuple = None):
    if not os.path.isdir('pasta_pdf'): os.mkdir('pasta_pdf')
    """Converts pdf to image and generates a file by page"""
    pdfIn = fitz.open(input_file)
    output_files = []
    for pg in range(pdfIn.pageCount):
        if pages is not None:
            if str(pg) not in str(pages):
                continue
        page = pdfIn[pg]
        rotate = int(0)
        zoom_x = 2
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)
        output_file = f"pasta_pdf/{os.path.splitext(os.path.basename(input_file))[0]}_page{pg + 1}.png"

        pix.writePNG(output_file)

        output_files.append(output_file)
    pdfIn.close()
    summary = {
        "File": input_file, "Pages": str(pages), "Output File(s)": str(output_files)
    }
    return output_files

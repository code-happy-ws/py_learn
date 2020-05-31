import urllib
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams


class PDFUtils():

    def __init__(self):
        pass

    def pdf2txt(self, path):
        print('解析pdf中...')
        with open(path, 'rb') as f:
            praser = PDFParser(f)

            doc = PDFDocument(praser)

            # if not doc.is_extractable:
            #     raise PDFTextExtractionNotAllowed

            pdfrm = PDFResourceManager()

            laparams = LAParams()

            device = PDFPageAggregator(pdfrm, laparams=laparams)

            interpreter = PDFPageInterpreter(pdfrm, device)
            result=''
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    try:
                        if hasattr(x, "get_text"):
                            content = x.get_text()
                            with open(r'E:\pycharm_len\py_learn\learn\office\file\linux_pdf.txt', 'a') as f:
                                try:
                                    result+=content
                                    f.write(content)
                                except Exception as err:
                                    print('error_write', err)
                    except Exception as err:
                        print('error', err)
            print('__________'*10)
            print(result)


if __name__ == '__main__':
    path = r'E:\pycharm_len\py_learn\learn\office\file\鸟哥私房菜linux.pdf'
    pdf_utils = PDFUtils()
    pdf_utils.pdf2txt(path)
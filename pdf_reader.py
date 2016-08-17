

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def pdfparser(s):
    from StringIO import StringIO
    m_file=StringIO(s)

    parser=PDFParser(m_file)

    document=PDFDocument(parser)
    rsmgr=PDFResourceManager()
    rstr=StringIO()
    lpm=LAParams()
    cdc='utf-8'

    device=TextConverter(rsmgs,rstr,codec = cdc, laparams=lpm)

    interpreter= PDFInterpreter(rsmgr,device)

    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        data = rstr.getvalue()
        print data



def main():
    pdfparser("/home/mankul/text_reader/Karma-Yoga-by-Swami-Vivekananda.pdf")

if __name__ == "__main__" : main()

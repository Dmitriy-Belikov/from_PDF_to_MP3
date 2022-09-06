import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from gtts import gTTS

rm = PDFResourceManager()
f = io.StringIO()
con = TextConverter(rm, f)
pinter = PDFPageInterpreter(rm, con)

way = str(input(r'Укажите путь к файлу PDF и нажмите Enter '))
with open(way, 'rb') as pp:
    for page in PDFPage.get_pages(pp, caching=True, check_extractable=True):
        pinter.process_page(page)
    t = f.getvalue()
print(t)
s = gTTS(t, lang='en')
s.save("C:\\test.mp3")

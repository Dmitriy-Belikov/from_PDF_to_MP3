import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from gtts import gTTS
import easygui as g



def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text

fffop = ["*.pdf", "*.pdf"]
str1 = g.fileopenbox(msg=None, title=None, filetypes=["*.pdf"], default='*.pdf')
if str1 is None:
    print('Ошибка')
if __name__ == '__main__':
    t = extract_text_from_pdf(str1)
    print(t)


s = gTTS(t, lang='ru')
e = g.filesavebox(msg=None, title=None, filetypes=["*.mp3"], default='test.mp3')

if e is None:
    print('Ошибка')

else:
    s.save(e)

import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from gtts import gTTS
import easygui as g


# Преобразование PDF в Текст
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


# Диалог открытия файла
def open_file():
    str1 = g.fileopenbox(title='Открыть файл', filetypes=["*.pdf"], default='*.pdf')
    if str1 is None:
        print('Ошибка')
    else:
        return (str1)


# Преобразование текста в аудио и сохраненени
def save_mp3(text_pdf):
    s = gTTS(text_pdf, lang='ru')
    e = g.filesavebox(title='Сохранить в ', filetypes=["*.mp3"], default='test.mp3')
    if e is None:
        print('Ошибка')
    else:
        s.save(e)
    return e


# Сохранение текста
def save_txt(text_pdf):
    st = text_pdf
    e = g.filesavebox(title='Сохранить в ', filetypes=["*.txt"], default='test.txt')
    if e is None:
        print('Ошибка')
    else:
        f = open(e, 'w')
        f.write(st)
        f.close()
    return e

#Бесконечный цикл с выполнением программы
while True:
    openfile = open_file()
    pdf_text = extract_text_from_pdf(openfile)
    print(pdf_text)
    msg = "Как будем сохранять?"
    title = "Сохранение"
    choices = ("[<F1>]mp3", "[<F2>]Текст")
    s = g.ynbox(msg, title, choices, image=None, default_choice="[<F1>]MP3", cancel_choice="[<F2>]Текст")
    if s is True:
        save_mp = save_mp3(pdf_text)
        print('Файл сохранен в ' + save_mp)
    elif s is False:
        save_tx = save_txt(pdf_text)
        print('Файл сохранен в ' + save_tx)
    q = g.ynbox('Вы хотите продолжить?', 'Вы хотите продолжить?', image=None, default_choice="[<F1>]Да", cancel_choice="[<F2>]Нет")
    if q is False:
        break
    else:
        continue
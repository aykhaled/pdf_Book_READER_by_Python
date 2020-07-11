
# Python pdf book Reader
# !!!!!!!!!!!!!!

# import libraries

import pyttsx3
import PyPDF2

# 1.) Read a Sentence

sen = 'I am a Python Reader. Welcome ! How are you, my friend?'

pyReader = pyttsx3.init()
pyReader.say(sen)
pyReader.runAndWait()

# 2.) Read a page from a pdf book

book = open('2017_Book_IntroductionToDataScience.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page_num = 62

page = pdfReader.getPage(page_num - 1)
text = page.extractText()

pyReader = pyttsx3.init()
pyReader.say(text)
pyReader.runAndWait()


# 3.) Read multiple pages from a pdf book

book = open('2017_Book_IntroductionToDataScience.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page_num = pdfReader.numPages
print(page_num)

pyReader = pyttsx3.init()
for i in range(61, page_num):
    page = pdfReader.getPage(i)
    text = page.extractText()

    pyReader.say(text)
    pyReader.runAndWait()






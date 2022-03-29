import pyttsx3
import PyPDF2
book = open('reports.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

speaker = pyttsx3.init()
for num in range (4, pages):
    page = pdfreader.getPage(4)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

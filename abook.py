import pyttsx3
import PyPDF2
import pyaudio

book = open('E:\\Mini Project\\Pdf\\sample.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.pages
print(pages)

engine = pyttsx3.init('sapi5')
print("playing....")
page = pdfReader.getPage(0)
text = page.extractText()
engine.say(text)
engine.runAndWait()


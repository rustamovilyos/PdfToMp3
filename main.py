import gtts
from googletrans import Translator
from tika import parser


def readfile():
	pdf_file = parser.from_file('threeYears.pdf')
	return (pdf_file['content'])


def recorder():
	tts = gtts.gTTS(pdf_file['content'], lang='ru')
	tts.save('threeYears.mp3')
	return 'Successfully'

if __name__ = "__main__":
	print(readfile())
	print(recorder())

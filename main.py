import gtts
from googletrans import Translator
from tika import parser


pdf_file = parser.from_file('threeYears.pdf')
print(pdf_file['content'])

tts = gtts.gTTS(pdf_file['content'], lang='ru')
tts.save('threeYears.mp3')

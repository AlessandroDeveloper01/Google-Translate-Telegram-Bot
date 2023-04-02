from aiogram import executor
import config
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import logging

#funzioni di traduzione
from googletrans import Translator
import googletrans

translator=Translator()

def translate_func(string,lang):
    return translator.translate(string, dest=str(lang))

#Bot
logging.basicConfig(level=logging.INFO) #log

bot = Bot(token="TOKEN")
dp = Dispatcher(bot)

global lang #lang - dest language, src language define auto

#avvio e tastiera
@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Russo','Inglese','Francese','Tedesco','Spagnolo','Portoghese','Giapponese','Cinese','Persiano','Germania']
    keyboard.add(*buttons)
    await message.answer("""Sono un bot traduttore, tradurrò il tuo testo nella lingua dall'elenco""",reply_markup=keyboard)

#funzioni dei pulsanti
@dp.message_handler(lambda message: message.text=='Russo' or message.text=='Inglese' or
                    message.text=='Francese' or message.text=='Tedesco' or message.text=='Spagnolo' or 
                    message.text=='Portoghese' or message.text=='Giapponese' or message.text=='Cinese' or message.text=="Persiano" or
                    message.text=='Germania')
async def dest_lang(message: types.Message):
    global lang
    languages={'Russo':'ru','Inglese':'en','Francese':'fr',
                'Tedesco':'de','Spagnolo':'es','Portoghese':'pt',
                'Giapponese':'ja','Cinese':'zh-cn',
                'Persiano':'fa','Germania':'de'}
    lang=languages[message.text]
    await message.reply('Cosa tradurre?')

#traduzione
@dp.message_handler()
async def print_result(message:types.Message):
    global lang
    translated = translate_func (message.text,lang)
    await message.reply(translated.text)

#запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)
    

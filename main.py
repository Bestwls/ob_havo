from cgitb import text
from email import message
from lib2to3.pgen2 import token
import logging
from config import Token
from aiogram import Bot,executor,types,Dispatcher
from buttons import menu
import requests
from aiogram.types import ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)
bot=Bot(token=Token)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def do_start(message: types.Message):
  user=message.from_user.first_name
  await message.answer(f"Salom {user}", reply_markup=menu)
@dp.message_handler(text=["Ma'lumotnoma"])
async def do_help(message: types.Message):
  await message.answer(f"Menga shahar nomini kiritsangiz sizga ob-havo ma'lumotlarini ko'rsataman")
@dp.message_handler(text='Ob-havo')
async def answer(message: types.Message):
  await message.answer('Shahar nomini kiriting',reply_markup=ReplyKeyboardRemove())
@dp.message_handler()
async def obhavo(message: types.Message):
  shahar=message.text
  url=f'http://api.weatherapi.com/v1/current.json?key=91c4fb4f07eb40b5b3a125700220403&q={shahar}&aqi=yes'  
  obhavo=requests.get(url).json()
  try:
    a=obhavo['location']['country']
    b=obhavo['location']['region']
    c=obhavo['location']['name']
    d=obhavo['current']['last_updated']
    e=obhavo['current']['temp_c']
    f=obhavo['current']['condition']['text']
    g=obhavo['current']['wind_kph']
    i=obhavo['current']['pressure_mb']
    j=obhavo['current']['humidity']
    k=obhavo['current']['cloud']
    await message.answer (f'Davlat -{a} \nViloyat -{b}\nShahar -{c}\nOhirgi yangilanish -{d}\nTemperatura (C) -{e}\nHavo -{f}\nShamol tezligi(km/soat) -{g}\nBosim(mega pascal) -{i}\nNamlik -{j}\nBulut -{k} %')
  except:
    await message.answer("Shahar nomini to'g'ri kiriting \nMasalan(xiva=khiva,xonqa=khonqa)")










if __name__=='__main__':
  executor.start_polling(dp,skip_updates=True)
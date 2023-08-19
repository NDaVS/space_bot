import random
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from modules.API import load_nasa
from googletrans import Translator

translator: Translator = Translator()
router: Router = Router()


@router.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command('help'))
async def send_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command('apod'))
async def send_apod(message: Message):
    nasa = load_nasa()
    data = nasa.get_apod()
    main_text = translator.translate(data['title'] + '\n\n' + data['explanation'], src='en', dest='ru').text
    if len(main_text) < 1000:
        await message.answer_photo(photo=data['url'], caption=main_text + '\n' + 'by NASA')
    else:
        await message.answer_photo(photo=data['url'])
        await message.answer(main_text)
    try:
        await message.answer_document(data['hdurl'], caption='HD')
    finally:
        pass

@router.message(Command('rmars'))
async def send_rmars(message: Message):
    nasa = load_nasa()
    data = nasa.get_rmars()
    photo_id = random.randint(0, len(data['photos']))
    photo_url = data['photos'][photo_id]['img_src']
    photo_date = data['photos'][photo_id]['earth_date']
    camera_name = data['photos'][photo_id]['camera']['full_name']
    await message.answer_photo(photo_url, caption=camera_name + '\n\n' + photo_date)

@router.message(Command('astros'))
async def send_astros(message: Message):
    iss_data = load_nasa().get_iss_data()
    main_text = ''
    for person in iss_data['people']:
        main_text += f'{person["name"]} - {person["craft"]}\n'
    await message.answer(main_text)

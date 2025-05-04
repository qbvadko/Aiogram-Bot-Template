import asyncio

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer_sticker(
        sticker='CAACAgIAAxkBAAEOI8Bn339kfpTbEMRyVZcFbnpj6ham0gACeQEAAsMJ8AMtSyWjfRygRzYE', 
        message_effect_id='5046509860389126442'
    )
    await asyncio.sleep(0.4)
    await message.answer('Приветствую :)')

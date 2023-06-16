import logging
from aiogram import Router
from aiogram.types import Message

from keyboards.keyboard import start_kb
from lexicon.lexicon import LEXICON

router = Router()
logger = logging.getLogger(__name__)


@router.message()
async def other(message: Message):
    logger.info(f"{message.from_user.username}: {message.text}")
    await message.answer(LEXICON.handler.other, reply_markup=start_kb)


from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.keyboard import start_kb, game_kb
from lexicon.lexicon import LEXICON
from services.services import get_bot_choice, get_winner

command_router = Router()
router = Router()
game_router = Router()

game_router.message.filter(F.text.in_([LEXICON.button.rock, LEXICON.button.paper, LEXICON.button.scissors]))


@command_router.message(Command(commands="start"))
async def start_command(message: Message):
    await message.answer(LEXICON.handler.start, reply_markup=start_kb)


@command_router.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(LEXICON.handler.help, reply_markup=start_kb)


@router.message(F.text == LEXICON.button.yes)
async def yes_answer(message: Message):
    await message.answer(LEXICON.handler.yes_answer, reply_markup=game_kb)


@router.message(F.text == LEXICON.button.no)
async def no_answer(message: Message):
    await message.answer(LEXICON.handler.no_answer)


@game_router.message()
async def game(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(bot_choice)

    winner = get_winner(message.text, bot_choice)
    await message.answer(winner, reply_markup=start_kb)

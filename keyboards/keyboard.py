from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from lexicon.lexicon import LEXICON

start_kb_builder = ReplyKeyboardBuilder()
start_kb_builder.row(KeyboardButton(text=LEXICON.button.yes),
                     KeyboardButton(text=LEXICON.button.no),
                     width=1)
start_kb = start_kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

game_kb_builder = ReplyKeyboardBuilder()
game_kb_builder.row(KeyboardButton(text=LEXICON.button.rock),
                    KeyboardButton(text=LEXICON.button.scissors),
                    KeyboardButton(text=LEXICON.button.paper)
                    )

game_kb = game_kb_builder.as_markup(resize_keyboard=True)

from dataclasses import dataclass


@dataclass
class HandlerT:
    start: str
    help: str
    yes_answer: str
    no_answer: str
    draw: str
    user_won: str
    bot_won: str
    other: str


@dataclass()
class ButtonT:
    yes: str
    no: str
    rock: str
    scissors: str
    paper: str


@dataclass
class Lexicon:
    handler: HandlerT
    button: ButtonT


LEXICON = Lexicon(
    handler=HandlerT(
        start="Привет, я умею играть в камень, ножницы, бумага.\nПравила игры - /help\nСыграем?",
        help="Правила игры:\nКамень🔪Ножницы\nНожницы🔪Бумага\nБумага🔪Камень\nСыграем?",
        yes_answer="Отлично, выбирай!",
        no_answer="Жаль, если захочешь жми кнопку 'Давай'",
        draw="Ничья\nПродолжаем?",
        user_won="Ты выиграл, поздравляю!\nПродолжаем?",
        bot_won="Я победил!\nПродолжаем?",
        other="Не понимаю тебя :(\nМожет сыграем?"
    ),
    button=ButtonT(
        yes="Давай",
        no="Не хочу",
        rock="Камень 🗿",
        scissors="Ножницы ✂",
        paper="Бумага 📜"
    )
)

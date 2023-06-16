from random import choice

from lexicon.lexicon import LEXICON

rock = LEXICON.button.rock
paper = LEXICON.button.paper
scissors = LEXICON.button.scissors

rules = {
    rock: scissors,
    scissors: paper,
    paper: rock
}


def get_bot_choice():
    return choice([rock, paper, scissors])


def get_winner(user_choice: str, bot_choice: str):
    if user_choice == bot_choice:
        return LEXICON.handler.draw
    elif rules[user_choice] == bot_choice:
        return LEXICON.handler.user_won
    else:
        return LEXICON.handler.bot_won

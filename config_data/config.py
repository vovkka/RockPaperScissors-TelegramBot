from dataclasses import dataclass
from environs import Env


@dataclass
class TelegramBot:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBot


def load_config(path: str | None = None):
    env = Env()
    env.read_env(path=path)

    return Config(
        tg_bot=TelegramBot(
            token=env.str('TOKEN')
        )
    )

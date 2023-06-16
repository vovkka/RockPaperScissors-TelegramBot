import asyncio
import logging
from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info("Starting bot")

    config: Config = load_config()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    dp.include_routers(user_handlers.command_router,
                       user_handlers.router,
                       user_handlers.game_router,
                       other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

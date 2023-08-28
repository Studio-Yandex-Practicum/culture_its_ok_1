import asyncio

from aiogram import Bot, Dispatcher
from core.config import settings
from core.logger import log_dec, logger_factory
from core.middleware import SessionMiddleware
from handlers import admin_router, new_user_router, route_router, start_router
from aiogram.fsm.middleware import FSMContextMiddleware


@log_dec(logger=logger_factory(__name__))
async def main():
    bot = Bot(token=settings.bot.telegram_token, parse_mode='html')

    dispatcher = Dispatcher()
    dispatcher.message.middleware(SessionMiddleware())
    dispatcher.callback_query.middleware(SessionMiddleware())
    dispatcher.poll.middleware(SessionMiddleware())
    dispatcher.poll.middleware(dispatcher.fsm.storage)
    dispatcher.include_routers(
        start_router,
        new_user_router,
        route_router,
        admin_router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    settings.logging.init_global_logging_level()
    settings.sentry.init_sentry()

    asyncio.run(main())

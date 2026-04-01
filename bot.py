from aiogram import Bot,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from database.db import Database
import asyncio

from handlers.start import router as start_router
from test__aa.car import router as car_router
from test__aa.history import router as history_router
from test__aa.it import router as it_router
from handlers.register import router as register_router
from natija.natija import router as natija_router
from handlers.user.profile import router as profile_router
from handlers.admin.admin import router as admin_router


async def main():
    bot=Bot(token='8689455913:AAG4O0VhB4oEquSGoKAQeliQit2MeHYk38g')
    storage = MemoryStorage()
    dp=Dispatcher(storage=storage)
    
    db = Database()
    await db.connect()
    dp['db']=db

    
    dp.include_router(start_router)
    dp.include_router(car_router)
    dp.include_router(it_router)
    dp.include_router(history_router)
    dp.include_router(register_router)
    dp.include_router(natija_router)
    dp.include_router(profile_router)
    dp.include_router(admin_router)

    
    await dp.start_polling(bot)
if __name__=="__main__":
    print('Bot is started😎')
    asyncio.run(main())
from aiogram import Bot,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
import asyncio

from handlers.start import router as start_router
from test__aa.car import router as car_router
from test__aa.history import router as history_router
from test__aa.it import router as it_router


async def main():
    bot=Bot(token='8702350091:AAGTsYCRI8wR7pMzItfQ08M5EC6ACeiz7to')
    storage = MemoryStorage()
    dp=Dispatcher(storage=storage)
    
    dp.include_router(start_router)
    dp.include_router(car_router)
    dp.include_router(it_router)
    dp.include_router(history_router)

    
    await dp.start_polling(bot)
if __name__=="__main__":
    print('Bot is started😎')
    asyncio.run(main())
from aiohttp import web
import logging

from loader import bot, dp
from config import BOT_TOKEN, WEBHOOK_URL, PORT
from aiogram import types


app = web.Application()
logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    logging.warning("Starting up")
    await bot.set_webhook(url=WEBHOOK_URL)


async def on_shutdown(_):
    logging.warning('Shutting down..')
    await bot.delete_webhook()


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind("/")
    token = url[index+1:]
    logging.info("***REQUEST*** : "+str(request))

    if token == BOT_TOKEN:
        data = await request.json()
        update = types.Update(**data)
        await dp.process_update(update)

        return web.Response()
    return web.Response(status=404)


app.router.add_post(f"/{BOT_TOKEN}", handler=handle_webhook)


async def root(_):
    return web.Response(text="Welcome home!")

app.router.add_get("/", handler=root)


if __name__ == "__main__":
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(
        app,
        host="0.0.0.0",
        port=PORT
    )

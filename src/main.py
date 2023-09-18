import asyncio
import json
from datetime import datetime

import aio_pika
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from visitor_tracker.controllers import all_logs, new_log
from visitor_tracker.consumer import on_message
from visitor_tracker.middleware import Tracker
from visitor_tracker.sender import sender


app = FastAPI()

origins = ["*"]
methods = ["GET", "POST", "PUT", "DELETE"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_headers=headers,
)


@app.middleware("tracker")
async def tracker(request: Request, call_next):
    service_tracker = Tracker("service_one")
    tracker = str(service_tracker.visitor_tracker(request))
    sender(tracker)
    response = await call_next(request)
    return response


@app.on_event('startup')
async def startup():
    loop = asyncio.get_event_loop()
    connection = await aio_pika.connect("amqp://guest:guest@rabbitmq/", loop=loop)
    channel =  await connection.channel()
    queue = await channel.declare_queue("logs")
    await queue.consume(on_message)


@app.get("/logs")
async def receiver():
    logs = all_logs()
    return logs


@app.get("/json")
def some_func():
    return {
        "some_json": "Some Json"
    }

@app.get("/")
async def hello():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True)

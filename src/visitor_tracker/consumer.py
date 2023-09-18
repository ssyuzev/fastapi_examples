
import ast
import json

import aio_pika  

from visitor_tracker.controllers import new_log


async def on_message(message: aio_pika.IncomingMessage):
    tracker = ast.literal_eval(message.body.decode("utf-8"))
    new_log(
        tracker["ip_address"], tracker["request_url"], tracker["request_port"],
        tracker["request_path"], tracker["request_method"],
        tracker["browser_type"],tracker["request_time"], tracker["service_name"]
    )

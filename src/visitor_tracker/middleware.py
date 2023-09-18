
from datetime import datetime
from fastapi import Request


class Tracker:
    def __init__(self, service_name: str):
        self.service_name = service_name

    def visitor_tracker(self, request: Request):
        ip_address = request.client.host
        request_url = request.url._url
        request_port = request.url.port
        request_path = request.url.path
        request_method = request.method
        browser_type = request.headers["User-Agent"]
        request_time = str(datetime.now())
        service_name = self.service_name

        return {
            "ip_address": ip_address,
            "request_url": request_url,
            "request_port": request_port,
            "request_path": request_path,
            "request_method": request_method,
            "request_time": request_time,
            "browser_type": browser_type,
            "service_name": service_name,
        }
    
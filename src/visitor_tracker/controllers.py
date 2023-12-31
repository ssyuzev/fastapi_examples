
import json

from visitor_tracker.init_db import get_db_connection
from visitor_tracker.helpers import to_dict,list_dict


def all_logs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM logs;')
    logs = list_dict(cur.fetchall())
    cur.close()
    conn.close()
    return logs

def new_log(
        ip_address: str,
        request_url: str,
        request_port: int,
        request_path: str,
        request_method: str,
        browser_type: str,
        request_time: str,
        service_name:str, 
        **kwargs
    ):

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO logs (ip_address, request_url, request_port, request_path, request_method, browser_type, request_time, service_name)'
        'VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;',
        (
            ip_address,
            request_url,
            request_port,
            request_path,
            request_method,
            browser_type,
            request_time,
            service_name
        )
    )

    log = cur.fetchone()[:]
    log_dict = to_dict(log)
    conn.commit()
    cur.close()
    conn.close()

    return json.dumps(log_dict)
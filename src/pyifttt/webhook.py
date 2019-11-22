import os
import platform
import sys
from datetime import datetime

import __main__
import requests

EVENT_URL = "https://maker.ifttt.com/trigger/{event}/with/key/{key}"


class MissingKeyException(Exception):
    def __init__(self):
        default_message = "Key was not provided and neither ENV VAR (IFTTT_KEY) nor ~/.ifttt file are available."
        super().__init__(default_message)


def send_notification(event_name, data, key=None):
    """
    Send notification to your webhook. This will trigger
    a notification.
    """
    if key is None:
        key = os.getenv('IFTTT_KEY', None)
        if key is None:
            ifttt_path = os.path.join(
                os.path.expanduser("~"),
                ".ifttt",
            )
            if os.path.exists(ifttt_path):
                with open(ifttt_path) as fr:
                    key = fr.read()
            else:
                raise MissingKeyException()

    url = EVENT_URL.format(event=event_name, key=key)

    requests.post(
        url,
        json=data,
    )


def send_completion_notification(event_name, key=None, value3=''):
    """
    Sends a notification to a webhook when a program
    has stopped running.

    The message content has the following format:
    The program {{Value1}}, running on host machine {{Value2}} , finished at {{OccurredAt}}. {{Value3}}
    """
    try:
        value1 = os.path.basename(os.path.abspath(__main__.__file__))
    except AttributeError:
        value1 = 'Interactive Python'

    data = dict(
        value1=value1,
        value2=platform.uname().node,
        value3=value3,
    )

    send_notification(event_name, data, key)


class SendCompletionNotification():
    def __init__(self, event_name, key=None):
        self.event_name = event_name
        self.key = key

    def __enter__(self):
        pass

    def __exit__(self, _type, value, traceback):
        value3 = ''
        if traceback is not None:
            value3 = "Got exception {name}".format(name=_type.__name__)

        send_completion_notification(
            self.event_name,
            self.key,
            value3,
        )

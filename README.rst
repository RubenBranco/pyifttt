pyifttt: The Python IFTTT Webhook Interface
===========================================

This package provides a simple interface to interact with If This Then That (https://ifttt.com/) webhook events.

This project was born from the need to receive push notifications on a smartphone after long running jobs had finished running, particularly using a free service such as IFTTT.

Copyright ® 2019, Ruben Branco <ruben.branco@outlook.pt>. All rights reserved.

Links: https://github.com/RubenBranco/pyifttt | https://pypi.org/project/pyifttt/

Installation
------------

Install pyifttt using pip:

.. code:: bash

    pip3 install pyifttt

Usage
-----

There are three essential items to interact with a webhook:

1. Event Name: The event name for the webhook defined in the website.
2. Key: Your personal ifttt maker key.
3. Data: The values of each declared form variables.

General Usage
^^^^^^^^^^^^^

.. code:: python

    from pyifttt.webhook import send_notification

    data = dict(value1="Testing this event")
    key = "MySuperPrivateKey"

    send_notification("test_event", data, key)

This will send a notification to an webhook whose event is named **test_event** with value1 variable as "Testing this event" and with a **key**.

Since including a private key in script files can be bothersome and repetitive, ifttt has three ways of key input:

1. Through the function as a key kwarg.
2. As a system env variable named IFTTT_KEY (``export IFTTT_KEY="MySuperPrivateKey``).
3. As a home file (~/.ifttt). The only contents this file should have is the key.

Job Completion Notification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

pyifttt implements a general notification system for push notification of program exits.

In your IFTTT webhook you should include the following message:

::

    The program {{Value1}}, running on host machine {{Value2}} , finished at {{OccurredAt}}. {{Value3}}

Here's how you would use pyifttt to receive push notifications for when your long running program finishes using a context manager:

.. code:: python

    from pyifttt.webhook import SendCompletionNotification

    with SendCompletionNotification('test_event'):
        execute_long_job()

This will send a push notification to your smartphone or other device with the following structure:

::

    The program long_job.py, running on host machine Server1, finished at November 22, 2019 at 09:30PM.

If it had found an exception, it would show the following message:

::

    The program long_job.py, running on host machine Server1, finished at November 22, 2019 at 09:30PM. Got exception KeyboardInterrupt.

An optional argument to SendCompletionNotification is the IFTTT key, which as previously described, has several ways of input.

If you prefer to not use it as a context manager, you also use it in the following way:

.. code:: python

    from pyifttt.webhook import send_completion_notification

    execute_long_job()
    send_completion_notification('test_event')


License
-------

Distributed under GPL-3.0 License. See the `LICENSE`_ file for details.

.. _LICENSE: https://github.com/RubenBranco/pyifttt/blob/master/LICENSE


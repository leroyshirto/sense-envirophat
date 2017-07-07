#!/usr/bin/env python

import time
from datetime import datetime
import requests
import os
import json

from envirophat import light, weather


poll_frequency = float(os.environ.get('POLL_FREQUENCY', default=300))  # Sensor data reporting period (5 minutes)
location_name = os.environ.get('LOCATION_NAME', default='office')  # Sensor location
endpoint_url = os.environ.get('ENDPOINT_URL', default='http://127.0.0.1/')  # The Endpoint the data will be sent to


def run():
    while True:
        try:
            temperature = round(weather.temperature(),2)
            pressure = round(weather.pressure(),2)
            light = light.light()

            payload = {
                'location': location_name,
                'poll_frequency_in_seconds': poll_frequency,
                'temperature': temperature,
                'temperature_units': 'c',
                'pressure': pressure,
                'light': light,
                'date_polled': datetime.now()
            }

            print("Sense")
            output = """
            Location: {location}
            Temp: {temperature}c
            Pressure: {pressure}
            Light: {light}
            """.format(
                location=location_name,
                temperature=temperature,
                pressure=pressure,
                light=light
            )

            print(output)

            requests.post(endpoint_url, json=json.dumps(payload))
        except Exception as e:
            print("Error getting sense data: %s" % e)

        time.sleep(poll_frequency)

run()

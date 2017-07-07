#!/usr/bin/env python3

import time
from datetime import datetime
import requests
import json

from envirophat import light, weather
import config


def run():
    while True:
        try:
            temperature = round(weather.temperature() - config.TEMP_CALIBRATION, 2)
            pressure = round(weather.pressure() - config.PRESSURE_CALIBRATION, 2)
            light_intensity = light.light()
            r, g, b = light.rgb()

            payload = {
                'location': config.LOCATION_NAME,
                'poll_frequency_in_seconds': config.POLL_FREQUENCY,
                'temperature': temperature,
                'temperature_units': 'c',
                'pressure': pressure,
                'pressure_units': 'hPA',
                'light_intensity': light_intensity,
                'light_colour': '%s %s %s' % (r, g, b),
                'date_polled': datetime.now()
            }

            output = """
            Location: {location}
            Temperature: {temperature} c
            Pressure: {pressure} hPA
            Light Intensity: {light_intensity}
            Light RGB: r{r}, g{g}, b{b}
            """.format(
                location=config.LOCATION_NAME,
                temperature=temperature,
                pressure=pressure,
                light_intensity=light_intensity,
                r=r, g=g, b=b
            )

            print(output)

            if config.SUBMIT_TO_ENDPOINT:
                headers = {"Authorization": "Bearer %s" % config.WEATHER_ENDPOINT_AUTH_TOKEN}
                requests.post(config.WEATHER_ENDPOINT_URL, json=json.dumps(payload), headers=headers)
        except Exception as e:
            print("Error getting sense data: %s" % e)

        time.sleep(config.POLL_FREQUENCY)

run()

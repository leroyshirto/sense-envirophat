import os

# Sensor data reporting period (5 minutes)
POLL_FREQUENCY = float(os.environ.get('POLL_FREQUENCY', default=300))
# Sensor location
LOCATION_NAME = os.environ.get('LOCATION_NAME', default='office')
# The calibration value. i.e temperature - TEMP_CALIBRATION
TEMP_CALIBRATION = float(os.environ.get('TEMP_CALIBRATION', default=9))
# The calibration value. i.e pressure - PRESSURE_CALIBRATION
PRESSURE_CALIBRATION = float(os.environ.get('PRESSURE_CALIBRATION', default=0.0))
# The weather endpoint the json data will be sent to
WEATHER_ENDPOINT_URL = os.environ.get('WEATHER_ENDPOINT_URL', default='http://127.0.0.1/')
# Auth token for endpoint
WEATHER_ENDPOINT_AUTH_TOKEN = os.environ.get('WEATHER_ENDPOINT_AUTH_TOKEN', default='secret')
# Whether to submit the data to the endpoint
SUBMIT_TO_ENDPOINT = bool(os.environ.get('SUBMIT_TO_ENDPOINT', default=False))

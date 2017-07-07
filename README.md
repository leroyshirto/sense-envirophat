# sense-envirophat

Sends data gathered from an environment to a given endpoint.
Data is collected using an enviro-phat https://github.com/pimoroni/enviro-phat


## Running
Installing:
```
git clone git@github.com:leroyshirtoFH/sense-envirophat.git
cd sense-envirophat
pip3 install -r requirements.txt
```

Running:
```
./app.py
```

Configuration:
Configuration is available through environment variables.
```
POLL_FREQUENCY=300                      # Sensor data reporting period (5 minutes)
LOCATION_NAME=office                    # Sensor location
TEMP_CALIBRATION=-9                     # The calibration value. i.e temperature - TEMP_CALIBRATION
PRESSURE_CALIBRATION=0                  # The calibration value. i.e pressure - PRESSURE_CALIBRATION
WEATHER_ENDPOINT_URL=http://127.0.0.1/  # The weather endpoint the json data will be sent to
WEATHER_ENDPOINT_AUTH_TOKEN=secret      # Auth token for endpoint
SUBMIT_TO_ENDPOINT=False                # Whether to submit the data to the endpoint
```


## Example Payload
```
{
    'location': 'office',
    'poll_frequency_in_seconds': 300,
    'temperature': 25.00,
    'temperature_units': 'c',
    'pressure': 12.00,
    'light_intensity': 12456,
    'light_colour': '255 255 255'
    'date_polled': '2017-07-07 10:00:17.051275'
}
```

# sense-envirophat

Sends data gathered from an to a given endpoint

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
POLL_FREQUENCY=300              # Sensor data reporting period (5 minutes)
LOCATION_NAM=office             # Sensor location
ENDPOINT_URL=http://127.0.0.1/  # The Endpoint the data will be sent to
```


## Example Payload
```
{
    'location': 'office',
    'poll_frequency_in_seconds': 300,
    'temperature': 25.00,
    'temperature_units': 'c',
    'pressure': 12.00,
    'light': light,
    'date_polled': '2017-07-07 10:00:17.051275'
}
```

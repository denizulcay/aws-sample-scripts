import requests

def stream_data(api_endpoint, data_generator):
    """Streams data to an API endpoint using the requests library."""

    with requests.post(api_endpoint, stream=True) as r:
        for chunk in data_generator:
            r.send(chunk)

def data_generator():
    """Generates data to be streamed."""
    for i in range(10):
        yield f"Data chunk {i}\n"

api_endpoint = "https://your-api-endpoint"
stream_data(api_endpoint, data_generator())
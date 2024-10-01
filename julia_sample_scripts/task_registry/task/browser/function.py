from julia_sample_scripts.client.browser.client import BrowserClient


def launch_url(url: str):
    BrowserClient().launch_url(url=url)

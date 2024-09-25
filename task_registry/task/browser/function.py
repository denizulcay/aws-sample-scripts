from client.browser.client import BrowserClient


def launch_url(url: str):
    BrowserClient().launch_url(url=url)

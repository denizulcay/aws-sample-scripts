import webbrowser


class BrowserClient:
    def __init__(self, browser_path: str = "/Applications/Google\ Chrome.app"):
        self._browser = webbrowser.get(f"open -a {browser_path} %s")

    def launch_url(self, url: str):
        self._browser.open(url)

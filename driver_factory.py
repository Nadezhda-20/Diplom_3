from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def create_driver(browser: str):
    browser = (browser or "chrome").strip().lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--remote-allow-origins=*")
        return webdriver.Chrome(options=options)

    if browser == "firefox":
        options = FirefoxOptions()
        return webdriver.Firefox(options=options)

    raise ValueError(f"Unsupported browser: {browser}. Supported: chrome, firefox")

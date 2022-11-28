"""Controls a firefox or chromium browser instance to allow automation of
setting a GitHub SSH deploy key, GitHub personal access token, or getting a
GitLab runner token."""

from typing import Any

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_until_page_is_loaded(
    time_limit_sec: int, website_controller: Any
) -> None:
    """Waits until page is loaded for some time frame."""
    delay = time_limit_sec  # seconds
    try:
        _ = WebDriverWait(website_controller.driver, delay).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Header-link"))
        )
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

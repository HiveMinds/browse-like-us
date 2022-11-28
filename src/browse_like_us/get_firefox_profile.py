"""Gets and returns the firefox profile."""

import time
from typing import Any

from src.browse_like_us.helper import open_url


def get_firefox_profile(driver: Any) -> str:
    """Returns the extension id of Ublock Origin."""
    # Go to extension settings.
    driver = open_url(
        driver,
        "about:support",
    )
    time.sleep(1)

    # Get the extension id from the browser.
    firefox_profile = driver.find_element(
        "xpath",
        '//*[@id="profile-dir-box"]',
    )
    return firefox_profile.text

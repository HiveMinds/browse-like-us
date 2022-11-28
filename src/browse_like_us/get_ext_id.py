"""Gets and returns the id of the extension used to go to extension
settings."""

import time
from typing import Any

from src.browse_like_us.helper import open_url


def get_ext_id(driver: Any) -> str:
    """Returns the extension id of Ublock Origin."""
    # Go to extension settings.
    driver = open_url(
        driver,
        "about:debugging#/runtime/this-firefox",
    )
    time.sleep(1)

    # Get the extension id from the browser.
    dropdown_tab_index = 2
    cell_index = find_extension_id(driver, dropdown_tab_index, "uBlock Origin")

    ext_id_element = driver.find_element(
        "xpath",
        f"/html/body/div/div/main/article/section[{dropdown_tab_index}]/div/"
        + f"ul/li[{cell_index}]/section/dl/div[2]/dd",
    )

    return ext_id_element.text


def find_extension_id(
    driver: Any, dropdown_tab_index: int, ext_title: str
) -> int:
    """Finds the table id pertaining to the extension title."""

    cell_index = 1
    while True:
        some_elem = driver.find_element(
            "xpath",
            f"/html/body/div/div/main/article/section[{dropdown_tab_index}]/"
            + f"div/ul/li[{cell_index}]/span",
        )
        if some_elem.text == ext_title:
            return cell_index
        cell_index = cell_index + 1

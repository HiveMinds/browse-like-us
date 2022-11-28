"""Contains functions that are used to help other Python files."""
import os
from typing import Any

from selenium.webdriver.common.action_chains import ActionChains

from src.browse_like_us.Hardcoded import Hardcoded


def source_contains(website_controller: Any, string: str) -> bool:
    """USED Evaluates complete html source of the website that is being
    controlled, to determine if it contains the incoming string. Returns true
    if the string is found in the html source of the website, false if it is
    not found.

    :param website_controller: Object controlling the browser. Object
    that controls the browser.
    :param string: Set of characters that is searched for in the html code.
    """
    source = website_controller.driver.page_source
    source_contains_string = string in source
    return source_contains_string


def get_browser_drivers(hardcoded: Hardcoded) -> None:
    """USED Installs wget and then uses that to download the firefox and
    chromium browser controller drivers.

    :param hardcoded: An object containing all the hardcoded settings used
    in this program.
    """
    os.system("yes | sudo apt install wget")  # nosec

    if not file_is_found(
        f"{hardcoded.firefox_driver_folder}/"
        + f"{hardcoded.firefox_driver_filename}",
    ):
        get_firefox_browser_driver(hardcoded)
        install_firefox_browser()
    if not file_is_found(
        f"{hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_filename}",
    ):
        get_chromium_browser_driver(hardcoded)


def file_is_found(filepath: str) -> bool:
    """Checks if file is found or not.

    :param filepath: param hardcoded: An object containing all the hardcoded
    settings used in this program.
    :param hardcoded:
    """
    return os.path.isfile(filepath)


def get_firefox_browser_driver(hardcoded: Hardcoded) -> None:
    """USED Creates a folder to store the firefox browser controller downloader
    and then downloads it into that.

    :param hardcoded: An object containing all the hardcoded settings used in
    this program.
    """
    # TODO: include os identifier and select accompanying file
    os.system(f"mkdir {hardcoded.firefox_driver_folder}")  # nosec
    curl_firefox_drive = (
        f"wget -O {hardcoded.firefox_driver_folder}/"
        + f"{hardcoded.firefox_driver_tarname} {hardcoded.firefox_driver_link}"
    )
    os.system(curl_firefox_drive)  # nosec
    unpack_firefox_driver = (
        f"tar -xf {hardcoded.firefox_driver_folder}/"
        + f"{hardcoded.firefox_driver_tarname} -C "
        + f"{hardcoded.firefox_driver_folder}/"
    )
    print(f"unpacking with:{unpack_firefox_driver}")
    os.system(unpack_firefox_driver)  # nosec


def install_firefox_browser() -> None:
    """USED."""
    install_firefox_browser_command = "yes | sudo apt install firefox"
    print(f"install_firefox_browser:{install_firefox_browser_command}")
    os.system(install_firefox_browser_command)  # nosec


def get_chromium_browser_driver(hardcoded: Hardcoded) -> None:
    """Creates a folder to store the chromium browser controller downloader and
    then downloads it into that.
    TODO: include os identifier and select accompanying file

    :param hardcoded: An object containing all the hardcoded settings used in
    this program.

    """
    # mak dir
    os.system(f"mkdir {hardcoded.chromium_driver_folder}")  # nosec
    # get the zip
    curl_chromium_drive = (
        f"wget -O {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_tarname} "
        + f"{hardcoded.chromium_driver_link}"
    )
    os.system(curl_chromium_drive)  # nosec
    # unpak the zip
    unpack_chromium_driver = (
        f"unzip -d  {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_filename} "
        + f"{hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_tarname}"
    )
    os.system(unpack_chromium_driver)  # nosec

    # move file one dir up
    move_chromium_driver = (
        f"mv  {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_filename}/"
        + f"{hardcoded.chromium_driver_unmodified_filename} "
        + f"{hardcoded.chromium_driver_folder}"
    )
    print(move_chromium_driver)
    os.system(move_chromium_driver)  # nosec
    # remove unpacked dir
    cleanup = (
        f"rm -r {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_filename}"
    )
    print(cleanup)
    os.system(cleanup)  # nosec

    # remove zip file
    cleanup = (
        f"rm -r {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_tarname}"
    )
    print(cleanup)
    os.system(cleanup)  # nosec

    # rename driver file name to include hardcoded version name
    rename_chromium_driver = (
        f"mv  {hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_unmodified_filename} "
        + f"{hardcoded.chromium_driver_folder}/"
        + f"{hardcoded.chromium_driver_filename}"
    )
    print(rename_chromium_driver)
    os.system(rename_chromium_driver)  # nosec


def click_element_by_xpath(website_controller: Any, xpath: str) -> Any:
    """Clicks an html element based on its xpath.

    :param website_controller: Object controlling the browser. Object that
    controls the browser.
    :param xpath: A direct link to an object in an html page.
    """
    source_element = website_controller.driver.find_element("xpath", xpath)
    if "firefox" in website_controller.driver.capabilities["browserName"]:
        scroll_shim(website_controller.driver, source_element)

    # scroll_shim is just scrolling it into view, you still need to hover over
    # it to click using an action chain.
    actions = ActionChains(website_controller.driver)
    actions.move_to_element(source_element)
    actions.click()
    actions.perform()
    return website_controller


def scroll_shim(passed_in_driver: Any, browser_object: Any) -> None:
    """Scrolls down till object is found.

    :param passed_in_driver: An object within the object that controls an
      internet browser.
    :param object: Unknown, most likely an arbitrary html object..
    """
    x = browser_object.location["x"]
    y = browser_object.location["y"]
    scroll_by_coord = f"window.scrollTo({x},{y});"
    scroll_nav_out_of_way = "window.scrollBy(0, -120);"
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)


def open_url(driver: Any, url: str) -> Any:
    """USED # TODO: eliminate duplicate function. Makes the browser open an url
    through the driver object in the webcontroller.

    :param driver: object within website_controller that can control
    the driver.
    :param url: A link to a website.
    """
    try:
        driver.get(url)
    except TimeoutError:
        print("Retry")
        driver.refresh()
        print("Refreshed")
    except TypeError:
        print("Retry")
        driver.refresh()
        print("Refreshed")
    return driver


def get_value_from_html_source(
    source: str, substring: str, closing_substring: str
) -> str:
    """Returns value from html source code.

    :param source: Source code of website that is being controlled.
    :param substring::param substring: A substring that is sought.
    :param closing_substring: A substring that indicates the end of text that
     is searched.
    """
    nr_of_pages_index = source.find(substring) + len(substring)
    # print(f'nr_of_pages_index={nr_of_pages_index}')
    closing_quotation = source.find(closing_substring, nr_of_pages_index)
    # print(f'closing_quotation={closing_quotation}')
    # print(f'nr={source[nr_of_pages_index:closing_quotation]}')
    value = source[nr_of_pages_index:closing_quotation]
    return value

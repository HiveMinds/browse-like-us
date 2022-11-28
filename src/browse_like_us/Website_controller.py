"""Gets a website controller and opens it."""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from .Hardcoded import Hardcoded


# pylint: disable=R0903
class Website_controller:
    """Controls/commands website using selenium."""

    def __init__(self, default_profile: bool):
        """Constructs object that controls a firefox browser.

        TODO: Allow user to switch between running browser
        in background or foreground.
        """
        self.hardcoded = Hardcoded()
        # To run Firefox browser in foreground
        print("Loading geckodriver")
        try:
            options = Options()

            if default_profile:
                options.add_argument("-profile")
                options.add_argument(self.hardcoded.firefox_profile)
            else:
                options.add_argument("-private")

            # options.add_argument("window-size=400,600")
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference("useAutomationExtension", False)

            self.driver = webdriver.Firefox(
                options=options,
                executable_path=r"firefox_driver/geckodriver",
            )
        # pylint: disable=W0707
        except ValueError:
            # pylint: disable=W0707
            raise Exception(
                "Error, you have the snap Firefox browser installed. Please"
                " use the apt one instead. This switching is automated"
                + " in a bash script of the Self-host GitLab."
            )

        # To run Firefox browser in background
        # os.environ["MOZ_HEADLESS"] = "1"
        # self.driver = webdriver.Firefox(
        # executable_path=r"firefox_driver/geckodriver")

        # To run Chrome browser in background
        # options = webdriver.ChromeOptions();
        # options.add_argument('headless');
        # options.add_argument('window-size=1200x600'); // optional

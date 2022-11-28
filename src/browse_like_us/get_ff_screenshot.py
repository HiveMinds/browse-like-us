"""Object to run code based on incoming arguments."""
import time

from src.browse_like_us.Hardcoded import Hardcoded
from src.browse_like_us.helper import get_browser_drivers, open_url
from src.browse_like_us.Website_controller import Website_controller


# pylint: disable=R0903
# pylint: disable=R0913
class GetScreenshot:
    """Gets the GitLab runner from the GitLab server."""

    def __init__(
        self,
        url: str,
        width: int,
        height: int,
        output_path: str,
        default_profile: bool = True,
    ) -> None:
        """Initialises object that gets the browser controller, then it gets
        the issues from the source repo, and copies them to the target repo.

        :param login: [Boolean] True if the website_controller object should be
        created and should login to GitHub.
        """

        # Store the hardcoded values used within this project
        self.h_c = Hardcoded()

        # get browser drivers
        get_browser_drivers(self.h_c)
        website_controller = Website_controller(default_profile)
        time.sleep(1)

        # Go to extension settings.
        website_controller.driver = open_url(
            website_controller.driver,
            url,
        )
        time.sleep(5)

        website_controller.driver.set_window_size(width, height)
        time.sleep(3)
        website_controller.driver.save_screenshot(output_path)

        time.sleep(1)

        # Close website controller.
        website_controller.driver.close()
        print("Applied the backed-up settings to Ublock Origin.")

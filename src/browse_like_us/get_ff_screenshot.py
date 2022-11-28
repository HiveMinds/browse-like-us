"""Object to run code based on incoming arguments."""
import time

from browsercontroller.get_controller import get_ubuntu_apt_firefox_controller


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
        # Go to extension settings.
        driver = get_ubuntu_apt_firefox_controller(
            url=url, default_profile=default_profile
        )
        time.sleep(5)

        driver.set_window_size(width, height)
        time.sleep(3)
        driver.save_screenshot(output_path)

        time.sleep(1)

        # Close website controller.
        driver.close()
        print("Applied the backed-up settings to Ublock Origin.")

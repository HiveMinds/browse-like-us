"""Contains the hardcoded data for this project."""
import getpass
from glob import glob


# pylint: disable=C0301
# pylint: disable=R0902
# pylint: disable=R0903
class Hardcoded:
    """Runs jupyter notebooks, converts them to pdf, exports the notebook pdfs
    to latex and compiles the latex report of the incoming project nr."""

    # pylint: disable=R0915
    def __init__(self) -> None:
        """Constructs an object that contains all the hardcoded values that are
        used in this script.

        TODO: adjust browser drivers based on the detected device type.
        """

        self.firefox_driver_folder = "firefox_driver"
        self.firefox_driver_tarname = "firefox_driver.tar.gz"
        self.firefox_driver_filename = "geckodriver"
        self.firefox_driver_link = (
            "https://github.com/mozilla/geckodriver/"
            + "releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz"
        )

        self.chromium_driver_folder = "chrome_driver"
        self.chromium_driver_tarname = "chrome_driver.zip"
        self.chromium_driver_link = (
            "https://chromedriver.storage.googleapis."
            + "com/90.0.4430.24/chromedriver_linux64.zip"
        )
        self.chromium_driver_unmodified_filename = "chromedriver"
        self.chromium_driver_filename = "chromedriver90"

        self.firefox_profile = get_default_profile_dir()


def get_default_profile_dir() -> str:
    """Finds the default Firefox profile path and returns it."""

    ubuntu_username = getpass.getuser()
    some_dir = f"/home/{ubuntu_username}/.mozilla/firefox/"

    subdirs = glob(f"{some_dir}/*/", recursive=True)
    default_profile = list(
        filter(lambda x: x.endswith(".default-release/"), subdirs)
    )
    if not default_profile:
        for subdir in subdirs:
            if ".default-release" in subdir:
                default_profile.append(subdir)
        if len(default_profile) > 1 or len(default_profile) < 0:
            raise Exception(
                f"Error, default profile not found:{default_profile}"
            )
    return default_profile[0]

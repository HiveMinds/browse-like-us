"""Code to manage creating 2015 Drake meme."""
import time
from typing import List, Tuple

from browsercontroller.get_controller import get_ubuntu_apt_firefox_controller
from PIL import Image


# pylint: disable=R0903
# pylint: disable=R0913
class GetScreenshot:
    """Object to run code based on incoming arguments."""

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
        print("Applied the backed-up settings to UBlock Origin.")


def create_meme_content(output_dir: str) -> List[str]:
    """Ensures the Drake 2015 meme content is created.

    Does this by showing the difference between the websites with and
    without custom uBlock origin filters.
    """
    original_meme_name = "template0.jpeg"
    bottom_name = "bottom.png"
    top_name = "top.png"

    accepted_sites: dict = {
        "stack_no_login": (False, "https://stackoverflow.com/questions"),
        "startpagina": (False, "https://www.startpagina.nl"),
        # "stack_login":(True,"https://github.com/search?q=productivity"),
        "medium": (
            False,
            # pylint: disable=C0301
            (
                "https://jchyip.medium.com/what-improves-developer-"
                + "productivity-is-the-wrong-question-dcd2fc08531d"
            ),
        ),
    }

    # pylint: disable=W0612
    for name, (requires_login, url) in accepted_sites.items():
        # TODO: include option to login (manually) to show difference.
        # TODO: ask user to verify no private data is leaked.

        add_right_img(
            bottom_name,
            output_dir,
            original_meme_name,
            f"overlay_{name}.png",
            url,
            False,
        )
        add_right_img(
            top_name,
            output_dir,
            f"overlay_{name}.png",
            f"overlay_{name}.png",
            url,
            True,
        )
    meme_names = list(
        map(lambda x: f"{output_dir}overlay_{x}.png", accepted_sites.keys())
    )
    return meme_names


# pylint: disable=R0913
def add_right_img(
    bottom_name: str,
    output_dir: str,
    original_meme_name: str,
    overlay_name: str,
    url: str,
    is_top: bool,
) -> None:
    """Fills in the top- & bottom right images in 2015 Drake meme with the
    website as it is without UBlock origin filter, and with custom UBlock
    origin filter."""
    GetScreenshot(
        url,
        850,
        850 + 114,
        f"{output_dir}{bottom_name}",
        default_profile=not is_top,
    )
    upscale_image(f"{output_dir}{bottom_name}", 1000, 1000)

    if is_top:
        overlay_image(
            output_dir,
            original_meme_name,
            bottom_name,
            overlay_name,
            (1000, 0),
        )
    else:
        overlay_image(
            output_dir,
            original_meme_name,
            bottom_name,
            overlay_name,
            (1000, 1000),
        )


# Create gif file for frontpage meme.
def overlay_image(
    output_dir: str,
    original_name: str,
    cropped_name: str,
    overlayed_name: str,
    start_pos: Tuple[int, int],
) -> None:
    """Puts one image above another image and exports it."""

    # Opening the primary image (used in background)
    img1 = Image.open(f"{output_dir}{original_name}")

    # Opening the secondary image (overlay image)
    img2 = Image.open(f"{output_dir}{cropped_name}")

    # Pasting img2 image on top of img1
    # starting at coordinates (0, 0)
    # x_min: more is to right
    # y_max: more is more down
    img1.paste(img2, (start_pos[0], start_pos[1]), mask=img2)

    # Displaying the image
    img1.save(f"{output_dir}{overlayed_name}")


def upscale_image(filepath: str, width: int, height: int) -> None:
    """Reshapes an image at location filepath into the desired width and
    height, and overwrites it."""
    c = Image.open(filepath)
    d = c.resize((width, height), resample=Image.BOX)
    d.save(filepath)

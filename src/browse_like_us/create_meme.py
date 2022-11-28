"""Code to manage creating 2015 Drake meme."""
from src.browse_like_us.get_ff_screenshot import GetScreenshot
from src.browse_like_us.overlay_image import overlay_image
from src.browse_like_us.upscale_image import upscale_image


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
    website as it is without Ublock origin filter, and with custom Ublock
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

"""Puts one image over another."""
from typing import Tuple

from PIL import Image


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

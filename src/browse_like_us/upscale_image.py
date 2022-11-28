"""Reshapes an image at location filepath into the desired width and height,
and overwrites it."""
from PIL import Image


def upscale_image(filepath: str, width: int, height: int) -> None:
    """Reshapes an image at location filepath into the desired width and
    height, and overwrites it."""
    c = Image.open(filepath)
    d = c.resize((width, height), resample=Image.BOX)
    d.save(filepath)

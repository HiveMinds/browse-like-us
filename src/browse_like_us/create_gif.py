"""Merges a few images into a single gif."""

import imageio


# Create gif file for frontpage meme.
def create_gif(filenames: str, output_path: str, interval_sec: float) -> None:
    """Merges a few images into a single gif."""

    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(output_path, images, duration=interval_sec)

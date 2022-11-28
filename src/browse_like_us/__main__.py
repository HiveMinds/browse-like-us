"""Entry point for the project."""

from typing import List

from meme.create_gif import create_gif
from meme.create_meme_content import create_meme_content

# Create Drake 2015 meme to show the effect of UBlock Origin lists.
output_dir = "meme/"
output_gif_name = "output.gif"
meme_names: List[str] = create_meme_content(output_dir)
create_gif(meme_names, f"{output_dir}{output_gif_name}", interval_sec=2)

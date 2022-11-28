"""Entry point for the project."""

from src.browse_like_us.create_gif import create_gif
from src.browse_like_us.create_meme import add_right_img

x0 = 10
y0 = 200
width = 100
height = 200
output_dir = "meme/"
original_meme_name = "template0.jpeg"

# cropped_name = "cropped_1.png"
bottom_name = "bottom.png"
top_name = "top.png"
overlay_name = "overlay.png"
output_gif_name = "output.gif"
get_screenshots = False

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

for name, (requires_login, url) in accepted_sites.items():
    # TODO: include option to login (manually) to show difference.
    # TODO: ask user to verify no private data is leaked.
    if get_screenshots:
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
create_gif(meme_names, f"{output_dir}{output_gif_name}", interval_sec=2)

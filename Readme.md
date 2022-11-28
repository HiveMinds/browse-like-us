# Browse Like Us

[![Python 3.10][python_badge]](https://www.python.org/downloads/release/python-3106/)
[![License: AGPL v3][agpl3_badge]](https://www.gnu.org/licenses/agpl-3.0)
[![Code Style: Black][black_badge]](https://github.com/ambv/black)
[![Code Coverage][codecov_badge]](https://codecov.io/gh/a-t-0/snnalgos)

The Instagram of browsing experiences, except you get what you see.
This is a social network that allows you to share and adopt your browsing
experience based on how your peers experience the web.

<img src=https://github.com/HiveMinds/browse-like-us/blob/main/meme/output.gif
width="1000" height="1000" />

## Why

Raymond Hill made a wonderful application called [uBlock Origin](https://github.com/gorhill/uBlock). It allows you to
filter (web) content. There are hundreds if not thousands of lists that filter
web content to make sites look nice and simple. The creator of the
browser-extension even declines funding and suggest you donate to those who
maintain the lists. uBlock filter maintenance can be seen as an everlasting battle;

1. Content-providers want to push their adds/nonsense.
1. uBlock list maintainers block the adds/nonsense.
1. Content-providers catch up to this blocking, and try to
   circumvent it by updating their website.
1. Back to step 2.

I think there is a lot of value in a single person tediously cleaning up 1 tiny
corner of the internet really well, and in my experience it is not easy to find
these persons and integrate their work in your browsing experience. That is why
this repository exists.

## What Stage I

If you visit a site, you can quickly scroll through the list of Ublock Origin
filter lists created by the uBlock users. The one you like sticks, and you can
add your own mods on top of that. These mods then become available to others.

Some kind of rating/usage system should be used to filter the good mods from
the bad mods. A dial could be used to determine what you want to filter 
(content vs cosmetics), and how strict you want to minimalise your browsing 
experience.

## What Stage II

Large adoption creates a dataset with:

- pairs of: \[HTML source code, uBlock origin element filter list\] as input
- filter adoption/usage as labels/scores of the filter (list(s))

I think sufficient adoption (1M+ curated websites) may allow one to automate filtering the adds and
  nonsense using machine learning techniques.

## What Stage III

The network could be decentralised to automatically pay out the people cleaning
up websites, based on your usage. (Like spotify except without me/this as
middle-person.) (Like brave tokens without the 30% cut.)

## Contribute
1. Have a look at the [roadmap](https://github.com/HiveMinds/browse-like-us/milestones)
and [issues](https://github.com/HiveMinds/browse-like-us/issues)
1. Pick an issue you like
2. Build it :rocket:
3. Send me a pull request :)
 
Most issues can be solved in parallel. Currently I focus on graduating, and
I am not actively generating solutions/work on this, I am willing to perform 
maintenance, quality control and CI :)

<!-- Un-wrapped URL's (Badges and Hyperlinks) -->

[agpl3_badge]: https://img.shields.io/badge/License-AGPL_v3-blue.svg
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[codecov_badge]: https://codecov.io/gh/a-t-0/snn/branch/main/graph/badge.svg
[python_badge]: https://img.shields.io/badge/python-3.10-blue.svg

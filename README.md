# MGIV

![workflow](https://github.com/benarmstead/mgiv/actions/workflows/codeql-analysis.yml/badge.svg)

## Minimalist Gtk Image Viewer

MGIV is an image viewer written in python and GTK.

# Instalation

`git clone https://github.com/benarmstead/mgiv/`

`cd mgiv/src`

`python3 mgiv.py`

## Dependencies
- GTK

# Capabilities

- View other images in the same directory as the image you are viewing (Left and right arrow keys).
- If no image is passed as an argument, searches for images in current directory and displays if found.

# Usage

`python3 mgiv.py <image.extension>`

`python3 mgiv.py ~/<directory>/<image.extension>`

`python3 mgiv.py <directory>/<image.extension>`

## Examples

`python3 mgiv.py parabola.png`

`python3 mgiv.py ~/Pictures/parabola.png`

`python3 mgiv.py Photos/parabola.png`

# Screenshots

![demo1](https://user-images.githubusercontent.com/70973680/135155036-f26ae006-dbb3-4fb0-9260-c0ea737b6e57.png)

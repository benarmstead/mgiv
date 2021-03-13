# MGIV
## Minimalist Gtk Image Viewer

MGIV is an image viewer written in python and GTK

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
<img src="https://raw.githubusercontent.com/benarmstead/mgiv/main/README_images/demo1.png">

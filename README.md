# faces-in-randomness

Facial feature detection in random data (grayscale) using Python, OpenCV, and numpy.

This is just an experiment based on a random idea I had, it doesn't serve any purpose except for me researching Python.

## Installation

Run `pip install -r requirements.txt` to install the dependencies.

## Running

Run `python3 app.py` and wait until a window with an image shows.

> The code runs single threaded, don't expect great speeds. It took around 5 minutes to find the first face, although your mileage may vary.
>
> I'm getting speeds that hover around 60-70 images generated per second. Python-OpenCV runs on the CPU so the speeds will depend only on how powerful the CPU is.

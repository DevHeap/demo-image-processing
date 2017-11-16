# demo-image-processing


### image_split.py

A tool for splitting the image into channels.

Requirements:
* Python 3
* numpy & skimage packages

Usage:

```
	$ python3 filename1.jpg filename2.png
```

You can specify any number of images. Splitted images will be saved to the same directory as `r_filename1.jpg`, `g_filename1.jpg`, `b_filename1.jpg`.

If given nonexistent file, the tool will notify you and skip it.

It is assumed you do not try to give it non-image files.

No unit-tests attached, but manual testing has been performed.



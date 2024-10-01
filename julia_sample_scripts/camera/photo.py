import imageio as iio
import imageio.v3 as iio3


def take_picture():
    camera = iio.get_reader("<video0>")
    screenshot = camera.get_data(0)
    camera.close()
    jpg_encoded = iio3.imwrite("<bytes>", screenshot, extension=".jpeg")

    return jpg_encoded

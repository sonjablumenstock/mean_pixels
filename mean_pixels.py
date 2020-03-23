# This is my project

# Python knows how to du tuple unpacking for setting data
# e.g. x, y = 1, 2

import statistics


def calculate_pixel_brightness(x, y, z):
    return statistics.mean([x, y, z])


pixels = [
    {'red': 100, 'green': 0, 'blue': 0},
    {'red': 50, 'green': 100, 'blue': 0},
]

pixel_brightnesses = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]
mean_brightness = statistics.mean(pixel_brightnesses)
print(mean_brightness)
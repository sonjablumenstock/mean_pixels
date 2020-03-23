# This is my project

#Python knows how to du tuple unpacking for setting data
# e.g. x, y = 1, 2

import statistics

def calculate_pixel_brightness(x, y, z):
    brightness = statistics.mean([x, y, z])
    return brightness


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel2 = {'red': 50, 'green': 100, 'blue': 0}
pixels = [pixel, pixel2]

pixel_brightnesses = [calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue']) for pixel in pixels]

mean_brightness = statistics.mean(pixel_brightnesses)
print(mean_brightness)




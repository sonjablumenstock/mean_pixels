# This is my project

#Python knows how to du tuple unpacking for setting data
# e.g. x, y = 1, 2

import statistics

def calculate_pixel_brightness(x, y, z):
    brightness = statistics.mean([x, y, z])
    return brightness


pixel = {'red': 100, 'green': 0, 'blue': 0}
pixel_brightness = calculate_pixel_brightness(pixel['red'], pixel['green'], pixel['blue'])

pixel2 = {'red': 50, 'green': 100, 'blue': 0}
pixel_brightness2 = calculate_pixel_brightness(pixel2['red'], pixel2['green'], pixel2['blue'])



mean_brightness = statistics.mean([pixel_brightness, pixel_brightness2])
print(mean_brightness)




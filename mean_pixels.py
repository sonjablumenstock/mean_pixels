# This is my project

#Python knows how to du tuple unpacking for setting data
# e.g. x, y = 1, 2

red, green, blue = 100, 0, 0
pixel_brightness = (red + green + blue) / 3

red2, green2, blue2 = 50, 100, 0
pixel_brightness2 = (red2 + green2 + blue2) / 3

readiness = 0
readiness2 = 200

mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)




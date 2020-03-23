# This is my project

red_value = 100
red_value2 = 50
green_value = 0
green_value2 = 100
blue_value = 0
blue_value2 = 0
readiness_value = 0
readiness_value2 = 200


pixel_brightness = (red_value + green_value + blue_value) / 3
pixel_brightness2 = (red_value2 + green_value2 + blue_value2) / 3


mean_brightness = (pixel_brightness + pixel_brightness2) / 2
print(mean_brightness)

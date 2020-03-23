# This is my project

RedValue = 100
RedValue2 = 50
GreenValue = 0
GreenValue2 = 100
BlueValue = 0
BlueValue2 = 0
ReadinessValue = 0
ReadinessValue2 = 200

# Get pixel brightnesses
result = (RedValue + GreenValue + BlueValue) / 3
result2 = (RedValue2 + GreenValue2 + BlueValue2) / 3

# Get mean brightness
result3 = (result + result2) / 2
print(result3)

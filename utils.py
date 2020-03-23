import statistics



def calculate_pixel_brightness(red: int, green: int, blue: int) -> float:
    """Calculates the brightness of a pixel from its r, g, b values"""
    return statistics.mean([red, green, blue])
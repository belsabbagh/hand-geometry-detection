from src import BLACK, PEAK_INTENSITY


def quantize_intensity(r, min_level=BLACK, max_level=PEAK_INTENSITY):
    return min_level if r < min_level else (max_level if r > max_level else round(r))

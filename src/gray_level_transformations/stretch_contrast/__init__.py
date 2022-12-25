from src.gray_level_transformations.stretch_contrast.ignore_percentage import ignore_percentage


def contrast_stretch_function(r, r_min, r_max, s_min=0, s_max=255):
    slope = (s_max - s_min) / (r_max - r_min)
    return ((r-r_min) * slope) + s_min



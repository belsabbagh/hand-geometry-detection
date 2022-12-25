def gray_level_slice_function(r, min_thr, max_thr, keep_level):
    return (r if keep_level is True else 255) if min_thr < r < max_thr else 0



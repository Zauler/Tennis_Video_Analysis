
def convert_pixel_distance_to_meteres(pixel_distance, reference_height_in_meters, reference_height_in_pixels):
    return (pixel_distance * reference_height_in_meters) / reference_height_in_pixels


def conver_meters_to_pixel_distance(meters, reference_height_in_meters, reference_height_in_pixels):
    return (meters * reference_height_in_pixels) / reference_height_in_meters
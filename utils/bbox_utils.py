def get_center_of_bbox(bbox):
    x1, y1 ,x2 ,y2 = bbox
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
    return center_x, center_y

def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def get_foot_position(bbox):
    x1, y1, x2, y2 = bbox 
    return (int((x1+x2)/2), y2)

def get_clossest_keypoint_index(point, key_points, key_points_indices):
    closest_distance = float('inf')
    key_point_ind = key_points_indices[0]
    for keypont_indix in key_points_indices:
        keypoint = key_points[keypont_indix*2], key_points[keypont_indix*2+1]
        distance = abs(point[1]-keypoint[1])
        
        if distance < closest_distance:
            closest_distance = distance
            key_point_ind = keypont_indix
    
    return key_point_ind

def measure_xy_distance(p1,p2): #Antes int era abs
    return (p1[0] - p2[0]), (p1[1] - p2[1])

def get_center_of_bbox(bbox):
    return (int((bbox[0]+bbox[2])/2), int((bbox[1]+bbox[3])/2))


        
        
    
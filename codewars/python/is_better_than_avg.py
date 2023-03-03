def better_than_average(class_points, your_points):
    mean = sum(class_points) / len(class_points)
    return mean < your_points
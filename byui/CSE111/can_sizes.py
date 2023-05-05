import math

can_sizes = {
    "#1 Picnic": (6.83, 10.16, 0.28),
    "#1 Tall": (7.78, 11.91, 0.43),
    "#2": (8.73, 11.59, 0.45),
    "#2.5": (10.32, 11.91, 0.61),
    "#3 Cylinder": (10.79, 17.78, 0.86),
    "#5": (13.02, 14.29, 0.83),
    "#6Z": (5.40, 8.89, 0.22),
    "#8Z short": (6.83, 7.62, 0.26),
    "#10": (15.72, 17.78, 1.53),
    "#211": (6.83, 12.38, 0.34),
    "#300": (7.62, 11.27, 0.38),
    "#303": (8.10, 11.11, 0.42)
}

def main():
    print("Can Size\tStorage Efficiency")
    for can_name, can_dimensions in can_sizes.items():
        radius, height, cost = can_dimensions
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        efficiency = compute_efficiency(volume, surface_area)
        print(f"{can_name}\t{efficiency:.2f}")

    max_efficiency = max(can_sizes, key=lambda x: compute_efficiency(compute_volume(can_sizes[x][0], can_sizes[x][1]), compute_surface_area(can_sizes[x][0], can_sizes[x][1])))
    print(f"\nThe can size with the highest storage efficiency is {max_efficiency}.\n")

def compute_volume(radius, height):
    return math.pi * radius ** 2 * height

def compute_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

def compute_efficiency(volume, surface_area):
    return volume / surface_area

if __name__ == '__main__':
    main()
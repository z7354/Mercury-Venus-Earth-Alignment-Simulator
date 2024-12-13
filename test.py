def angular_difference(a, b):
    """
    Calculate the smallest difference between two angles (considering wrap-around).

    Parameters:
    a (float): First angle in degrees.
    b (float): Second angle in degrees.

    Returns:
    float: The smallest difference between the two angles in degrees.
    """
    diff = abs(a - b) % 360
    return min(diff, 360 - diff)

def are_aligned(angle1, angle2, angle3, tolerance=1.0):
    """
    Check if three angles are aligned within a specified tolerance, considering both same-side and opposite-side alignments.
    
    Parameters:
    angle1 (float): Angle of the first planet in degrees.
    angle2 (float): Angle of the second planet in degrees.
    angle3 (float): Angle of the third planet in degrees.
    tolerance (float): Allowed angular difference in degrees.
    
    Returns:
    tuple: (same_side, opposite_side)
           same_side: bool - True if all differences <= tolerance (same-side alignment)
           opposite_side: bool - True if one difference < 1 and the other two differences are ~180 degrees
    """
    diff12 = angular_difference(angle1, angle2)
    diff23 = angular_difference(angle2, angle3)
    diff31 = angular_difference(angle3, angle1)

    # Same-side alignment: all angle differences are within the tolerance
    same_side = (diff12 <= tolerance and diff23 <= tolerance and diff31 <= tolerance)

    # Opposite-side alignment logic:
    # There are three cases, each requires:
    # 1. One angle difference < 1 degree (meaning two planets are almost on the same side)
    # 2. The other two angle differences are close to 180 degrees (within tolerance)
    opposite_side = (
        (diff12 < 1 and abs(diff23 - 180) <= tolerance and abs(diff31 - 180) <= tolerance) or
        (diff23 < 1 and abs(diff12 - 180) <= tolerance and abs(diff31 - 180) <= tolerance) or
        (diff31 < 1 and abs(diff12 - 180) <= tolerance and abs(diff23 - 180) <= tolerance)
    )

    return same_side, opposite_side

def find_alignment_days(P_M, P_V, P_E, tolerance=1.0, max_days=10000000):
    """
    Simulate the orbits and find the first days when same-side and opposite-side alignments occur.

    Parameters:
    P_M, P_V, P_E (float): Orbital periods of Mercury, Venus, and Earth in days.
    tolerance (float): Allowed angular difference in degrees.
    max_days (int): Maximum number of days to simulate.

    Returns:
    tuple: (first_same_side_day, first_opposite_side_day)
    """
    omega_M, omega_V, omega_E = 360 / P_M, 360 / P_V, 360 / P_E
    first_same_side_day, first_opposite_side_day = None, None

    for day in range(1, max_days + 1):
        angle_M = (omega_M * day) % 360
        angle_V = (omega_V * day) % 360
        angle_E = (omega_E * day) % 360

        same_side, opposite_side = are_aligned(angle_M, angle_V, angle_E, tolerance)

        if same_side and first_same_side_day is None:
            first_same_side_day = day
        if opposite_side and first_opposite_side_day is None:
            first_opposite_side_day = day

        # Continue until both types of alignment are found or max_days is reached
        if first_same_side_day is not None and first_opposite_side_day is not None:
            break

    return first_same_side_day, first_opposite_side_day

# Example usage
P_M, P_V, P_E = 88, 225, 365.25  # Orbital periods of Mercury, Venus, and Earth in days
tolerance = 1.0  # Tolerance in degrees
first_same_side_day, first_opposite_side_day = find_alignment_days(P_M, P_V, P_E, tolerance)

print(f"First same-side alignment day: {first_same_side_day}")
print(f"First opposite-side alignment day: {first_opposite_side_day}")

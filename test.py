# Planet Alignment Simulation Program

def angular_difference(a, b):
    """
    Calculate the smallest difference between two angles (considering wrap-around).
    
    Parameters:
    a (float): First angle in degrees.
    b (float): Second angle in degrees.
    
    Returns:
    float: The smallest difference between the two angles in degrees.
    """
    diff = abs(a - b)
    return min(diff, 360 - diff)

def are_aligned(angle1, angle2, angle3, tolerance=1.0):
    """
    Check if three angles are aligned within a specified tolerance.
    
    Parameters:
    angle1 (float): Angle of the first planet in degrees.
    angle2 (float): Angle of the second planet in degrees.
    angle3 (float): Angle of the third planet in degrees.
    tolerance (float): Allowed angular difference in degrees.
    
    Returns:
    bool: True if all angles are within the tolerance, False otherwise.
    """
    diffs = [
        angular_difference(angle1, angle2),
        angular_difference(angle1, angle3),
        angular_difference(angle2, angle3)
    ]
    return all(diff <= tolerance for diff in diffs)

def find_alignment_day(P_M, P_V, P_E, tolerance=1.0, max_days=100000):
    """
    Find the minimum number of days until the planets realign within the specified tolerance.
    
    Parameters:
    P_M (float): Orbital period of Mercury in days.
    P_V (float): Orbital period of Venus in days.
    P_E (float): Orbital period of Earth in days.
    tolerance (float): Allowed angular difference in degrees.
    max_days (int): Maximum number of days to simulate.
    
    Returns:
    int or None: The day count when alignment occurs, or None if not found within max_days.
    """
    # Calculate angular velocities (degrees per day)
    omega_M = 360.0 / P_M
    omega_V = 360.0 / P_V
    omega_E = 360.0 / P_E

    for day in range(1, max_days + 1):
        # Calculate current angles
        angle_M = (omega_M * day) % 360
        angle_V = (omega_V * day) % 360
        angle_E = (omega_E * day) % 360

        # Check for alignment
        if are_aligned(angle_M, angle_V, angle_E, tolerance):
            return day  # Alignment found

    return None  # Alignment not found within max_days

# Define orbital periods
P_M = 88        # Mercury's orbital period (days)
P_V = 225       # Venus's orbital period (days)
P_E = 365.25    # Earth's orbital period (days)

# Allowed angular error
tolerance = 1.0  # degrees

# Maximum number of days to simulate
max_days = 100000  # Approximately 273.8 years

# Find alignment day
alignment_day = find_alignment_day(P_M, P_V, P_E, tolerance, max_days)

if alignment_day:
    print(f"Planets realign after: {alignment_day} days")
    years = alignment_day / 365.25
    print(f"Approximately {years:.2f} years")
else:
    print(f"No planetary alignment found within {max_days} days.")

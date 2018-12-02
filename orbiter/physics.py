def calc_eccentricity(dist_list):
    """Calculate and return eccentricity from list of radii."""
    apoapsis = max(dist_list)
    periapsis = min(dist_list)
    eccentricity = (apoapsis - periapsis) / (apoapsis + periapsis)
    return eccentricity

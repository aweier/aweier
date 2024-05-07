def calculate_water_column(well_depth, dtw_level):
    return well_depth - dtw_level

def get_positive_float_input(prompt):
    while True:
        try:
            value = round(float(input(prompt)), 2)
            if value <= 0:
                print("Value must be a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_casing_diameter():
    casing_diameter_factors = {
        2: 0.16,  # Conversion factor for 2-inch casing
        4: 0.65,  # Conversion factor for 4-inch casing
        6: 1.5    # Conversion factor for 6-inch casing
    }

    while True:
        try:
            casing_diameter = int(input("Enter the casing diameter in inches (2, 4, or 6): "))
            if casing_diameter not in casing_diameter_factors:
                print("Casing diameter must be 2, 4, or 6 inches.")
            else:
                return casing_diameter, casing_diameter_factors[casing_diameter]
        except ValueError:
            print("Invalid input. Please enter a valid integer for the casing diameter.")

def calculate_discharge_rate(fill_time_seconds):
    discharge_rate_lpm = 1000 / fill_time_seconds
    discharge_rate_gpm = discharge_rate_lpm / 3.8
    return discharge_rate_lpm, discharge_rate_gpm

# Example usage
casing_diameter, conversion_factor = get_casing_diameter()
print(f"Casing diameter entered: {casing_diameter} inches")
print(f"Conversion factor assigned: {conversion_factor} gallons per foot")

well_depth = get_positive_float_input("Enter the well depth in feet: ")
print(f"Well depth entered: {well_depth} feet")

dtw_level = get_positive_float_input("Enter the depth to water level (DTW) in feet: ")
print(f"Depth to water level entered: {dtw_level} feet")

# Calculate well parameters
wc_length = calculate_water_column(well_depth, dtw_level)
well_volume = wc_length * conversion_factor

# Output the results
print(f"Water column length: {wc_length:.2f} feet")
print(f"Well volume: {well_volume:.2f} gallons")

# Fill time testing
fill_time_seconds = get_positive_float_input("Enter the fill time in seconds for a 1000 mL graduated cylinder: ")
discharge_rate_lpm, discharge_rate_gpm = calculate_discharge_rate(fill_time_seconds)
print(f"Discharge rate: {discharge_rate_lpm:.2f} LPM, {discharge_rate_gpm:.2f} GPM")

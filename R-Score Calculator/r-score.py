def calculate_r_score(a, g, sigma=10, Z=5, C=50):
    """
    Calculate the R-Score based on class average (a), given grade (g), 
    standard deviation (sigma), constant Z, and constant C.
    
    Parameters:
    a (float): Class average
    g (float): Given grade
    sigma (float): Standard deviation (default is 10)
    Z (float): Constant Z (default is 5)
    C (float): Constant C (default is 50)
    
    Returns:
    str: R-Score calculation in the specified format
    """
    # Calculate the main component of the R-Score
    main_component = ((g - a) / sigma) * Z
    
    # Calculate R-Scores for different values of I
    r_score_minus_5 = main_component - 5 + C
    r_score_0 = main_component + C
    r_score_plus_5 = main_component + 5 + C
    
    # Format the output
    result = f"""
    R-Score Calculation:
    {r_score_minus_5:.2f} -- {r_score_0:.2f} -- {r_score_plus_5:.2f}
    """
    
    return result

# Example usage:
class_average = float(input("Enter Current Class Average: "))
given_grade = float(input("Enter Current Grade: "))
print(calculate_r_score(class_average, given_grade))
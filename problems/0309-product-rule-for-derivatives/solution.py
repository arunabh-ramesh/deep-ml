import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    f = np.poly1d(f_coeffs[::-1])
    g = np.poly1d(g_coeffs[::-1])
    fprime = f.deriv()
    gprime = g.deriv()
    product = f * gprime + g * fprime
    result = [float(round(x, 4)) for x in list(product)[::-1]]
    return result


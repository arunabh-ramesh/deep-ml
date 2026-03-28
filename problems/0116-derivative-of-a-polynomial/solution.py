def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    c = c * n
    n -= 1
    x = pow(x, n) * c
    return x
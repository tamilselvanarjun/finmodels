import numpy as np
import cvxpy as cp

def optimize_portfolio(expected_returns, covariance_matrix):
    """
    Optimize a portfolio using Mean-Variance Optimization.

    Parameters:
    - expected_returns: Expected returns for each asset
    - covariance_matrix: Covariance matrix of asset returns

    Returns:
    - Optimal portfolio weights if successful, None otherwise
    """
    num_assets = len(expected_returns)

    
    weights = cp.Variable(num_assets)
    expected_return = expected_returns @ weights
    risk = cp.quad_form(weights, covariance_matrix)

    
    objective = cp.Maximize(expected_return - 0.5 * risk)

    
    constraints = [cp.sum(weights) == 1, weights >= 0]

    
    problem = cp.Problem(objective, constraints)
    problem.solve()

    if problem.status == 'optimal':
        return weights.value
    else:
        print("Optimization problem could not be solved.")
        return None

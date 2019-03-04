import numpy as np


def cpk(measurements, lower_limit, upper_limit=None):
    """ Calculate Cpk statistics for a given set of measurements
        with one or two sided measurements. """

    result = {
        'mean': np.mean(measurements),
        'std' : np.std(measurements, ddof=1)
    }

    if upper_limit:
        result['lower_limit'] = lower_limit
        result['upper_limit'] = upper_limit
        result['cpl'] = (result['mean'] - result['lower_limit']) / (3 * result['std'])
        result['cpu'] = (result['upper_limit'] - result['mean']) / (3 * result['std'])
        result['cpk'] = min(result['cpl'], result['cpu'])
    else:
        result['limit'] = lower_limit
        result['cpk'] = abs((result['mean'] - result['limit']) / (3 * result['std']))
        result['comment'] = 'One sided limit.'
    
    return result
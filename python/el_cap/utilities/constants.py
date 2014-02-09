## @package constants
#
# A litany of germane physical constants.
#

## Radius of the Earth.
#  @param units Units to return the radius in (km or m).
#  @return Radius in specified units.
def RE(units='m'):
    if units.lower() == 'm':
        re = 6378137.0
    elif units.lower() == 'km':
        re = 6378.137
    return re 

## Mass of the Earth.
#  @param units Units to return the mass in (kg or lbm).
#  @return Mass in specified units.
def ME(units='kg'):
    if units.lower() == 'kg':
        mass = 5.97219E24
    elif units.lower() == 'lbm':
        mass = 1.31664252E25 
    return mass 

## Standard gravity of the Earth.
#  @return Standard gravity in m/s/s.
def g0():
    return 9.80665 

## Ideal gas constant.
#  @param units Units to return the constant in.
#  @return Radius in specified units.
def R_gas(units='J/Kmol'):
    if units.lower() == 'j/kmol':
        R = 8.3144621
    else:
        print "Units of " + repr(units) + " not yet implemented, returning J/Kmol"
        R = 8.3144621
    return R

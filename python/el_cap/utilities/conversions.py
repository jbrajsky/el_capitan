## @package conversions
#
# A litany of germane unit conversions.
#

## Feet to meters.
#  @param distance Distance in feet to convert to meters.
#  @return Distance in meters.
def ft2m(distance=1):
    return distance * 0.3048

## Meters to feet.
#  @param distance Distance in meters to convert to feet.
#  @return Distance in feet.
def m2ft(distance=1):
    return distance * 3.28084

## Kilometers to miles.
#  @param distance Distance in kilometers to convert to miles.
#  @return Distance in miles.
def km2miles(distance=1):
    return distance * 0.621371

## Miles to kilometers.
#  @param distance Distance in miles to convert to kilometers.
#  @return Distance in kilometers.
def miles2km(distance=1):
    return distance * 1.60934

## Knots to mph.
#  @param velocity Velocity in knots to convert to mph.
#  @return Velocity in mph.
def knots2mph(velocity=1):
    return velocity * 1.15078

## Mph to knots.
#  @param velocity Velocity in mph to convert to knots.
#  @return Velocity in knots.
def mph2knots(velocity=1):
    return velocity * 0.868976 

## m/s to mph.
#  @param velocity Velocity in m/s to convert to mph.
#  @return Velocity in mph.
def mps2mph(velocity=1):
    return velocity * 2.23694 

## Mph to m/s.
#  @param velocity Velocity in mph to convert to m/s.
#  @return Velocity in mps.
def mph2mps(velocity=1):
    return velocity * 0.44704 

## kg to lbm.
#  @param mass Mass in kg to convert to lbm.
#  @return Mass in lbm.
def kg2lbm(mass=1):
    return mass * 2.20462

## lbm to kg.
#  @param mass Mass in lbm to convert to kg.
#  @return Mass in kg. 
def lbm2kg(mass=1):
    return mass * 0.453592

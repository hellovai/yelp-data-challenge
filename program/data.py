import simplejson as json

bucket_size = 100 # number of days for a review bucket

import math

def distance(lat1, long1, lat2, long2):
  return distance_on_unit_sphere(lat1, long1, lat2, long2) * 3960

def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    return arc

class DataObject(object):
  """docstring for DataObject"""
  def __init__(self, arg):
    super(DataObject, self).__init__()
    self.__buisnessId = arg.id

class Data(object):
  """docstring for Data"""
  data_file_folder = 'dataset'
  data_file_starting = 'yelp_academic_dataset_'
  data_file_ext = '.json'

  def get_file_name(typeof):
    return data_file_folder + '/' + data_file_starting + typeof + data_file_ext

  def __init__(self, arg):
    super(Data, self).__init__()
    self.__lat = arg.lat
    self.__lng = arg.lng
    self.__distance = arg.distance
    self.__data = [] # array of DataObjects

  def fill(self):
    file_path = get_file_name('buisness')
    with open(file_path) as fin:
      for line in fin:
        b = json.loads(line)
        if (distance(self.__lat, self.__long, b['latitude'], b['longitude']) < self.__distance)
          add_to_data(b)

  def add_to_data(buisness):
    pass

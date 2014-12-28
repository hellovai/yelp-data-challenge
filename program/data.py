import simplejson as json
from datetime import datetime, date

bucket_size = 100 # number of days for a review bucket
num_buckets = 10  # total number of days to compare
date_format = "%Y-%m-%d"
d0 = datetime.combine(date.today(), datetime.min.time())

data_file_folder = '../dataset'
data_file_starting = 'yelp_academic_dataset_'
data_file_ext = '.json'

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

def get_file_name(typeof):
  return data_file_folder + '/' + data_file_starting + typeof + data_file_ext

class Structure(object):
  """docstring for Structure"""
  def __init__(self, arg):
    super(Structure, self).__init__()
    self.__name = arg
    self.content = {}

  def fetch(self, bid):
    if bid not in self.content:
      return []
    return self.content[bid]

  def fill(self):
    file_path = get_file_name(self.__name)
    with open(file_path) as fin:
      for line in fin:
        r = json.loads(line)
        bid = r['business_id']
        if bid not in self.content:
          self.content[bid] = []
        self.content[bid].append(r)

  def write(self, ending = '_data'):
    file_path = get_file_name(self.__name + ending)
    fout = open(file_path, 'w')
    data = json.dumps(self.content, separators=(',', ':'), sort_keys=False)
    fout.write(data)
    fout.close()

  def read(self, ending = '_data'):
    file_path = get_file_name(self.__name + ending)
    fin = open(file_path, 'r')
    data = fin.read()
    self.content = json.loads(data)
    fin.close()

  def add_content(self, key, value):
    self.content[key] = value

class Reviews(Structure):
  """docstring for Reviews"""
  def __init__(self):
    Structure.__init__(self, 'review')

  def bucket(self, bid):
    rs = self.fetch(bid)
    buckets = [0] * num_buckets
    for r in rs:
      index = self.map_bucket(r['date'])
      if index >= 0 and index < num_buckets:
        buckets[index]+=1
    return buckets

  def map_bucket(self, d):
    d1 = datetime.strptime(d, date_format)
    delta = d0 - d1
    return int(math.floor(delta.days / bucket_size))

class Checkins(Structure):
  """docstring for Checkins"""
  def __init__(self):
    Structure.__init__(self, 'checkin')

class Data(Structure):
  """docstring for Data"""

  def __init__(self, arg):
    Structure.__init__(self, 'business')
    self.__lat = arg['lat']
    self.__lng = arg['lng']
    self.__distance = arg['dist']

  def fill(self):
    file_path = get_file_name('business')
    with open(file_path) as fin:
      for line in fin:
        b = json.loads(line)
        if (distance(self.__lat, self.__lng, b['latitude'], b['longitude']) < self.__distance):
          self.add_to_data(b)

  def add_to_data(self, b):
    obj = {
      'lat' : b['latitude'],
      'lng' : b['longitude'],
      'stars': b['stars'],
      'categories': b['categories'],
      'attributes': b['attributes'],
      'reviews': False,
      'checkins': c.fetch(b['business_id']),
    }
    if b['review_count'] > 0:
      obj['reviews'] = r.bucket(b['business_id'])
    self.add_content(b['business_id'], obj)


r = Reviews()
c = Checkins()

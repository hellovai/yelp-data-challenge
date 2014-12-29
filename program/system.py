# -*- coding: utf-8 -*-
import argparse
from data import r, c, Data, get_file_name
import os.path
from sets import Set

# final program
# input: [lat, lng, category, distance]
# output:
# category - % related to success

# score
# determine success of a buisness
# our beleif, number of new reviews relates to success / growth
# a0 * (rating / 5.0) + a1 * (regression for growth in reviews) + a2 * (checkins / # of checkins for buisnesses in that category)
def score(buisness_id):
  pass

def train(buisnesses_list = []):
  pass

def init():
  f = get_file_name('review_data')
  if os.path.isfile(f):
    r.read()
  else:
    r.fill()
    r.write()

  f = get_file_name('checkin_data')
  if os.path.isfile(f):
    c.read()
  else:
    c.fill()
    c.write()

def main(lat, lng, dist, category, bad_category):
  d = Data({'lat': lat, 'lng': lng, 'dist': dist})
  ending = '-' + str(lat) + '-' + str(lng) + '-' + str(dist)
  f = get_file_name('business' + ending)
  if os.path.isfile(f):
    d.read(ending)
  else:
    print "Loading... this may take a while"
    init()
    d.fill()
    d.write(ending)

  content = d.content
  validid = []
  validid_val = []
  for ctid in content:
    ct = content[ctid]
    if len(ct['categories'].intersection(category)):
      validid.append(ctid)
      validid_val.append(10)
    elif len(ct['categories'].intersection(bad_category)):
      validid.append(ctid)
      validid_val.append(-10)

  print "x = [",
  for bid in validid:
    cd = content[bid]
    print cd['lat'],
  print "];"

  print "y = [",
  for bid in validid:
    cd = content[bid]
    print cd['lng'],
  print "];"

  print "v = [",
  for v in validid_val:
    print v,
  print "];"

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Determine relation between categories')

  parser.add_argument('latitude',type=float,help='',)

  parser.add_argument('longitude',type=float,help='',)

  parser.add_argument('distance',type=float,help='',)

  args = parser.parse_args()
  main(args.latitude, args.longitude, args.distance, Set(["Fast Food"]), Set(["Restaurants"]))

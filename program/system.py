# -*- coding: utf-8 -*-
import argparse

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

def main():
  pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Determine relation between categories',
            )

    parser.add_argument(
            'latitude',
            type=float,
            help='',
            )

    parser.add_argument(
            'longitude',
            type=float,
            help='',
            )

    parser.add_argument(
            'distance',
            type=float,
            help='',
            )

    args = parser.parse_args()
  main()

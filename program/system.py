# -*- coding: utf-8 -*-
import argparse

# features
# length of review, stars, setiment, date

# normalization
# user_id

# evaluation
# votes {funny, useful, cool}

# final program
# input: review_id
# output:
# Cool: %
# Funny: %
# Useful: %

def train(buisnesses_list = []):
  pass

def main():
  pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Determine optimal order for tips and reviews',
            )

    parser.add_argument(
            'buisness_id',
            type=str,
            help='This is the buisness you want to organize tips for',
            )

    args = parser.parse_args()
  main()

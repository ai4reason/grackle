#!/usr/bin/env python3

from grackle import jsondb

if __name__ == "__main__":
   import argparse
   
   parser = argparse.ArgumentParser(
      description='List performance of strategies in grackle db.')
   parser.add_argument('dbfile', nargs="?", default="db-trains-cache.json", 
      help="grackle db json filename (default: db-trains.cache.json)")
   parser.add_argument("-t", "--table", nargs="?", const="translate.txt", default=None,
      help="specify a translation table (default: translate.txt)")
   group = parser.add_mutually_exclusive_group()
   group.add_argument("--new", action="store_true", 
      help="consider only newly genereted strategies (requires translation table)")
   group.add_argument("--old", action="store_true", 
      help="consider only initial strategies (requires translation table)")
   args = parser.parse_args()
   
   fm = True if args.old else (False if args.new else None)
   results = jsondb.load(args.dbfile, args.table, filter_mode=fm)
   cnts = jsondb.counts(results)
   jsondb.perf(cnts)


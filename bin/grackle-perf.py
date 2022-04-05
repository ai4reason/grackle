#!/usr/bin/env python3

from grackle import jsondb

if __name__ == "__main__":
   import sys
   fin = sys.argv[1] if len(sys.argv) > 1 else "db-trains-cache.json" 
   results = jsondb.load(fin, "translate.txt")
   cnts = jsondb.counts(results)
   jsondb.perf(cnts)


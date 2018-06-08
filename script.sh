#!/bin/bash -
#===============================================================================
#
#          FILE: script.sh
#
#         USAGE: ./script.sh
#
#   DESCRIPTION:
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (),
#  ORGANIZATION:
#       CREATED: 06/07/2018 12:59
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

declare -a ITERS=(100 1000 10000 100000 1000000 10000000 100000000)

algos=4
runs=10 # How many run we want to do

for a in $(seq 1 $algos); do
  for i in "${ITERS[@]}"; do
    for run in $(seq 1 $runs); do
      node --max-old-space-size=4096 ./index.js "$i" "$a" >> case_"$a"_count_"$i"
    done
  done
done


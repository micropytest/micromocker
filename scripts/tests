#!/usr/bin/bash

shopt -s globstar; micropython -m unittest **/*_test.py

status=$?
if [ $status != 0 ]; then
  echo
  echo "Some test has failed."
  exit $status
fi
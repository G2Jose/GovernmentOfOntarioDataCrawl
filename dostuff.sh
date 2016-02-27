#!/bin/bash
pkill Excel
rm -rf test.csv
python3 parse.py

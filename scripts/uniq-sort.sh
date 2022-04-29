#!/bin/env bash

sort $1 > ${1}-sorted
uniq ${1}-sorted > $1
rm ${1}-sorted

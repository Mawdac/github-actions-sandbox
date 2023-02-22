#!/bin/bash
echo "$BRANCH"
TAGS=$(git tag -l "$BRANCH*")

for TAG in $TAGS
do
  echo "$TAG"
done

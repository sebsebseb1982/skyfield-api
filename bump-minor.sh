#!/bin/bash
set -e

VERSION=$(cat version.txt)
MAJOR=$(echo "$VERSION" | cut -d. -f1)
MINOR=$(echo "$VERSION" | cut -d. -f2)
PATCH=$(echo "$VERSION" | cut -d. -f3)

NEW_MINOR=$((MINOR + 1))
NEW_VERSION="${MAJOR}.${NEW_MINOR}.0"

echo "$NEW_VERSION" > version.txt
echo "Bumped version: $VERSION -> $NEW_VERSION"

git add version.txt
git commit -m "chore: bump version to $NEW_VERSION"
git tag "v$NEW_VERSION"
git push origin "v$NEW_VERSION"



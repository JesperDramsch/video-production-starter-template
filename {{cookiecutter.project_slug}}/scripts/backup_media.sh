#!/bin/bash

set -e

check_requirements() {
  if [[ -z "$(command -v exiftool)" ]]; then
    echo "Please install 'exiftool' on your machine."
    exit 1
  fi
}

main() {
  check_requirements
}

main

#!/bin/zsh
# Builds the engine with the test and runs it. Extra arguments go to the test (--update).
set -e
cd "$(dirname "$0")/.."
mkdir -p build
swiftc -O -swift-version 5 engine.swift tests/main.swift -o build/aura-test
build/aura-test "$PWD" "$@"

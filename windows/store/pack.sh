#!/bin/bash
# Builds the Microsoft Store package: dist/AURA-Switcher-<version>.msixbundle (x64 + ARM64), unsigned — the Store signs it.
# Needs Windows (makeappx from the Windows SDK) and Zig; runs in CI (.github/workflows/store.yml).
set -euo pipefail
cd "$(dirname "$0")"
VERSION=$(grep -m1 '^VERSION=' ../build.sh | cut -d= -f2)
source identity.env
MAKEAPPX=$(ls "/c/Program Files (x86)/Windows Kits/10/bin/"10.*/x64/makeappx.exe | sort -V | tail -1)
rm -rf build && mkdir -p build/bundle ../../dist
for T in x86_64:x64 aarch64:arm64; do
  A=${T##*:}; D=build/$A
  mkdir -p $D/Assets && cp Assets/*.png $D/Assets/
  (cd .. && zig c++ -target ${T%%:*}-windows-gnu -O2 -s -std=c++17 -municode -Wl,--subsystem,windows -DBUILD_TIME=$(date +%s) \
    aura.cpp aura.rc -o "store/$D/AURA Switcher.exe" -lole32 -lwinmm -luser32 -lshell32 -lgdi32 -ladvapi32 -static)
  rm -f $D/*.pdb
  sed -e "s|@NAME@|$NAME|" -e "s|@PUBLISHER@|$PUBLISHER|" -e "s|@PUBLISHER_NAME@|$PUBLISHER_NAME|" \
      -e "s|@VERSION@|$VERSION.0.0|" -e "s|@ARCH@|$A|" AppxManifest.xml > $D/AppxManifest.xml
  "$MAKEAPPX" pack /o /d "$(cygpath -w $D)" /p "$(cygpath -w build/bundle/AURA-Switcher-$A.msix)"
done
"$MAKEAPPX" bundle /o /bv $VERSION.0.0 /d "$(cygpath -w build/bundle)" /p "$(cygpath -w ../../dist/AURA-Switcher-$VERSION.msixbundle)"
rm -rf build
echo "dist/AURA-Switcher-$VERSION.msixbundle"

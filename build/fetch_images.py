#!/usr/bin/env python3
"""Download every photo, badge and the logo the concept uses into assets/img/,
so the site doesn't depend on Green Lawn's HubSpot file library at demo time.

Run once, then rebuild:
    python3 build/fetch_images.py
    python3 build/build.py

build.py uses a local copy whenever one exists and falls back to the HubSpot URL otherwise,
so a partial download still builds fine.
"""
import os, sys, urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # safe: build.py only builds when run as a script

# Widest size each image is shown at, so one file serves desktop and retina phones
WIDE = {"grill": 2000, "tech96": 2000, "team": 1800, "custtech": 2000, "custlawn": 1400,
        "fert": 1400, "lime": 1400, "pest": 1400, "natural": 1400, "comm": 1400}

def save(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "kept"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (concept image fetch)"})
    with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
        f.write(r.read())
    return "saved"

def main():
    os.makedirs(build.IMG_DIR, exist_ok=True)
    jobs = [(build.img(path, WIDE.get(key, 1400)), build.local_name(path)) for key, path in build.P.items()]
    jobs += [(build.img(f, 250), build.local_name(f)) for f, _ in build.BADGES]
    jobs.append((build.LOGO, "logo.svg"))
    failed = 0
    for url, name in jobs:
        try:
            print(f"{save(url, os.path.join(build.IMG_DIR, name)):5}  {name}")
        except Exception as ex:
            failed += 1
            print(f"FAIL   {name}  ({ex})")
    print(f"\n{len(jobs) - failed} of {len(jobs)} images in assets/img/. Now run: python3 build/build.py")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())

Portrait regeneration (local only; needs numpy, pillow, opencv-python-headless):

    python scripts/segment.py PHOTO MASK.png --preview check.png      # cut the person out (GrabCut)
    B="--cols 62 --rows 39 --aspect 2.05 --x 0.133 --y 0.26 --w 0.573 --mask MASK.png --ink 1"
    python scripts/ascii_art.py PHOTO scripts/ascii.txt $B --gamma 1.8 --edge 0.55 --hi 88
    python scripts/ascii_art.py PHOTO scripts/ascii_dark.txt $B --hi 97 --light --fx 0.49 --fy 0.50 --fw 0.31 --fh 0.40 --floor 0.1 --gamma 0.7 --cut 0.7 --edge 0.35
    python scripts/card.py --offline

ascii.txt is the light-theme portrait (dark ink), ascii_dark.txt the dark-theme one (bright face).
segment.py seeds are tuned for the current selfie; a new photo needs new seed fractions.

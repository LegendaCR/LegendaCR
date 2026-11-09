"""Cut the person out of a photo with OpenCV GrabCut -> grayscale mask PNG (255 = person).

Usage: python segment.py PHOTO OUT_MASK.png [--preview OUT.png]
Seeds are tuned for photo-street.jpg (selfie, head + shoulders, sky/buildings behind);
fractions are relative to the photo size.
"""
import sys
import cv2
import numpy as np

src, out = sys.argv[1], sys.argv[2]
img = cv2.imread(src)
H0, W0 = img.shape[:2]
scale = 640 / H0
im = cv2.resize(img, (int(W0 * scale), 640), interpolation=cv2.INTER_AREA)
h, w = im.shape[:2]
yy, xx = np.mgrid[0:h, 0:w] / np.array([h, w])[:, None, None]

m = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
ell = lambda cx, cy, rx, ry: ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1
# probable person: head with headphones, neck, shoulders
m[ell(0.42, 0.45, 0.26, 0.24)] = cv2.GC_PR_FGD
m[yy > 0.66 + 0.28 * np.abs(xx - 0.45)] = cv2.GC_PR_FGD   # shoulders slope down to the edges
# sure person: face, headphone cups, torso
m[ell(0.42, 0.48, 0.15, 0.17)] = cv2.GC_FGD
m[ell(0.20, 0.53, 0.035, 0.06)] = cv2.GC_FGD
m[ell(0.61, 0.54, 0.035, 0.06)] = cv2.GC_FGD
m[(yy > 0.80) & (xx > 0.15) & (xx < 0.85)] = cv2.GC_FGD
# sure background: sky, top band, sides above the shoulders
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
sky = (hsv[..., 0] > 95) & (hsv[..., 0] < 125) & (hsv[..., 1] > 60) & (hsv[..., 2] > 120)
m[sky] = cv2.GC_BGD
m[yy < 0.24] = cv2.GC_BGD
m[(yy < 0.62) & ((xx < 0.12) | (xx > 0.74))] = cv2.GC_BGD
m[(yy < 0.64 + 0.22 * np.abs(xx - 0.45)) & ((xx < 0.14) | (xx > 0.70))] = cv2.GC_BGD   # street beside the shoulders

bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(im, m, None, bgd, fgd, 8, cv2.GC_INIT_WITH_MASK)
mask = np.where((m == cv2.GC_FGD) | (m == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)

# keep the largest blob, fill holes, smooth the edge
n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
mask = np.where(lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]), 255, 0).astype(np.uint8)
inv = cv2.bitwise_not(mask)
n, lab, st, _ = cv2.connectedComponentsWithStats(inv)
for i in range(1, n):
    if st[i, cv2.CC_STAT_TOP] > 0 and st[i, cv2.CC_STAT_AREA] < 0.0008 * h * w:   # specks only, keep the gaps under the headband
        mask[lab == i] = 255
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
mask = cv2.resize(mask, (W0, H0), interpolation=cv2.INTER_LINEAR)
mask = cv2.GaussianBlur(mask, (0, 0), 3)
mask = np.where(mask > 127, 255, 0).astype(np.uint8)
cv2.imwrite(out, mask)

if "--preview" in sys.argv:
    pv = img.copy()
    pv[mask == 0] = (pv[mask == 0] * 0.15).astype(np.uint8)
    cv2.imwrite(sys.argv[sys.argv.index("--preview") + 1], cv2.resize(pv, (W0 // 4, H0 // 4)))

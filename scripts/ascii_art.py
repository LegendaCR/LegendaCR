"""Turn a portrait photo into ASCII art for the neofetch-style profile card.

Usage: python ascii_art.py PHOTO OUT.txt [--cols 40] [--rows 25] [--preview OUT.png]
"""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps

args = sys.argv[1:]
src, out = args[0], args[1]
opt = lambda k, d: type(d)(args[args.index(k) + 1]) if k in args else d
COLS, ROWS = opt("--cols", 40), opt("--rows", 25)
CELL_ASPECT = opt("--aspect", 2.27)  # glyph cell height / width (16px font, 20px lines = 2.27)

# Light -> heavy ramp; glyphs act as ink, so dark areas (hair, jacket) get dense glyphs
RAMP = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

img = Image.open(src).convert("RGB")
w, h = img.size
target = COLS / (ROWS * CELL_ASPECT)          # width / height of the crop
# Head-and-shoulders box (fractions of the photo), widened to the cell aspect
bx0, by0, bw = opt("--x", 0.12), opt("--y", 0.08), opt("--w", 0.76)
cw = int(w * bw); ch = int(cw / target)
x0, y0 = int(w * bx0), int(h * by0)
crop = img.crop((x0, y0, x0 + cw, min(h, y0 + ch)))

g = np.asarray(ImageOps.grayscale(crop).filter(ImageFilter.GaussianBlur(1.0)).filter(ImageFilter.UnsharpMask(6, 160, 2))).astype(float) / 255
# Isolate the subject: soft elliptical mask around head and shoulders kills the city lights
H, W = g.shape
yy, xx = np.mgrid[0:H, 0:W]
head = ((xx - W * opt("--hx", 0.50)) / (W * opt("--hw", 0.30))) ** 2 + ((yy - H * opt("--hy", 0.36)) / (H * opt("--hh", 0.30))) ** 2
body = ((xx - W * 0.50) / (W * 0.62)) ** 2 + ((yy - H * 0.98) / (H * 0.52)) ** 2
mask = np.clip(1.6 - np.minimum(head, body), 0, 1)
if "--mask" in args:   # precise person cut-out from segment.py: nothing outside it gets a glyph
    pm = Image.open(opt("--mask", "")).convert("L").crop((x0, y0, x0 + cw, min(h, y0 + ch)))
    mask = np.asarray(pm.filter(ImageFilter.GaussianBlur(1))).astype(float) / 255
# Equalize inside the subject so face, hair and jacket separate clearly
sel = mask > 0.5
vals = np.sort(g[sel])
lo, hi = np.percentile(vals, [3, opt("--hi", 92)])
tone = np.clip((g - lo) / (hi - lo), 0, 1)
if "--light" in args:   # dark theme: bright skin = dense glyphs, dark hair/clothes fade out
    rgb = np.asarray(crop.filter(ImageFilter.GaussianBlur(2))).astype(float)
    ycc = np.asarray(crop.filter(ImageFilter.GaussianBlur(3)).convert("YCbCr")).astype(float)
    cb, cr = ycc[..., 1], ycc[..., 2]
    sky = (rgb[..., 2] - rgb[..., 0] > 20) & (rgb[..., 2] > 110)
    skin = ((cr > 136) & (cr < 180) & (cb > 78) & (cb < 128)).astype(float)
    face = ((xx - W * opt("--fx", 0.5)) / (W * opt("--fw", 0.30))) ** 2 + ((yy - H * opt("--fy", 0.5)) / (H * opt("--fh", 0.36))) ** 2
    skin = np.asarray(Image.fromarray((skin * (face < 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))).astype(float) / 255
    lo2 = np.percentile(g[skin > 0.5], opt("--lo", 5))
    hi2 = np.percentile(g[skin > 0.5], 99)
    tone2 = np.clip((g - lo2) / (hi2 - lo2), 0, 1) ** opt("--gamma", 1.6)
    floor = opt("--floor", 0.0)   # hair / clothes keep a light texture so the silhouette reads
    ink = np.maximum(tone2 * skin, floor + 0.25 * tone2 * (1 - skin))
else:                   # light theme: glyphs as ink, dark = dense, skin stays light
    ink = (1 - tone) ** opt("--gamma", 1.6)
# Edges carry the facial features (brows, eyes, nose, lips) that flat shading loses
gy, gx = np.gradient(np.asarray(Image.fromarray((g * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(float) / 255)
edge = np.hypot(gx, gy)
edge = np.clip(edge / np.percentile(edge[sel], 97), 0, 1)
if "--light" in args:
    # Inside the face edges cut dark gaps (brows, eyes, nose, lips); outside they draw a faint outline
    g = np.clip(ink - opt("--cut", 0.8) * edge * skin + opt("--edge", 0.3) * edge * (1 - skin), 0, 1) * mask
else:
    g = np.clip(opt("--ink", 0.8) * ink + opt("--edge", 0.55) * edge, 0, 1) * mask

small = Image.fromarray((g * 255).astype(np.uint8)).resize((COLS, ROWS), Image.LANCZOS)
a = np.asarray(small).astype(float) / 255
a = np.clip((a - 0.06) / 0.90, 0, 1) ** 1.1   # levels + gamma
idx = np.where(np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).resize((COLS, ROWS), Image.BILINEAR)) < 110, 0,
               np.round(a * (len(RAMP) - 1))).astype(int)
lines = ["".join(RAMP[i] for i in row).rstrip() for row in idx]
open(out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines))

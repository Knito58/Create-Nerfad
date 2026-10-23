# Makes the ringed icons from new_nerfad_icon2.png: white ring, transparent outside.
# Run from the repo root: python3 art/add_ring.py   (needs Pillow and numpy)
from PIL import Image, ImageDraw
import numpy as np

N, S = 640, 4                     # output size, supersampling factor
RING = int(N * 0.035)             # white ring width

src = Image.open('art/new_nerfad_icon2.png').convert('RGBA')
a = np.array(src).astype(int)
ys, xs = np.nonzero(a[:, :, :3].sum(2) < 720)    # everything that is not pure white
cx, cy = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
r = ((xs.max() - xs.min()) + (ys.max() - ys.min())) / 4

r_out = N / 2 - 2
r_in = r_out - RING

def disc(rad):
    m = Image.new('L', (N * S, N * S), 0)
    c = N * S / 2
    ImageDraw.Draw(m).ellipse([c - rad * S, c - rad * S, c + rad * S, c + rad * S], fill=255)
    return m

side = N / ((r_in + 1) / r)       # crop so the blue circle just fills the inner disc
crop = src.crop((int(cx - side / 2), int(cy - side / 2), int(cx + side / 2), int(cy + side / 2)))
crop = crop.resize((N * S, N * S), Image.LANCZOS)

out = Image.new('RGBA', (N * S, N * S), (0, 0, 0, 0))
out.paste(Image.new('RGBA', out.size, (255, 255, 255, 255)), (0, 0), disc(r_out))
out.paste(crop, (0, 0), disc(r_in))
out = out.resize((N, N), Image.LANCZOS)

out.save('art/nerfad_icon_ring_640.png')
out.resize((400, 400), Image.LANCZOS).save('art/nerfad_icon_ring_400.png')   # CurseForge
out.resize((64, 64), Image.LANCZOS).save('create_nerfad/icon.png')           # in the jar

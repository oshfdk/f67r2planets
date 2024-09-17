# created by oshfdk
# a proof of obtaining a sigrature-like feature at the lower right corner of f116v
# by a linear combination of MSI TIFFs taken by Roger Easton
# for background information see 
# https://www.voynich.ninja/thread-4363.html (including my posts)
# and
# https://manuscriptroadtrip.wordpress.com/2024/09/08/multispectral-imaging-and-the-voynich-manuscript/
#

# you'll need Pillow and numpy libraries for this script to run,
# > pip install pillow
# > pip install numpy
from PIL import Image
import numpy as np

# you can change the path to TIFFs here
# include the slash at the end of the path
# note that if you saved the files using Google Drive and have "Copy of " prepended to each file,
# you can just add it here once, e.g., path_to_tiffs="./msi/Copy of " (don't forget the space after "of")

path_to_tiffs = "./"
#path_to_tiffs = "./Copy of "

result_filename = "oshfdk116v.png"

bias = 1.6710087437575252
weights = [ 2.86566222e-03, -7.31746714e-04, -7.91509891e-04,  6.26958368e-04,
  -5.44016711e-04,  2.13091826e-04,  6.41224414e-05, -1.15745158e-03,
      -1.19574426e-03, -1.41510511e-03, -1.77602363e-04, -1.28772144e-03,
      -2.78448038e-04, -2.21850204e-04, -5.14871113e-04,  1.41009356e-03,
        1.19763900e-03,  5.67961854e-04,  1.06700996e-03,  2.66545916e-04,
        1.35468789e-03, -5.18381671e-04,  1.60250474e-04, -6.39294269e-04,
      -6.06875071e-04, -5.26037804e-04, -8.50949681e-04, -1.46222198e-04,
        2.00271206e-04, -4.03289436e-03, -6.48766122e-04, -6.49732137e-05,
      -3.30974503e-03,  3.10579239e-03,  7.33322792e-03,  3.67331676e-03,
        3.36502464e-03,  1.67928168e-04]

files = [
"Voynich_116v+MB365UV_007_F.tif",
"Voynich_116v+MB365UV_029_F.tif",
"Voynich_116v+MB365UV_037_F.tif",
"Voynich_116v+MB450RB_001_F.tif",
"Voynich_116v+MB450RB_023_F.tif",
"Voynich_116v+MB450RB_031_F.tif",
"Voynich_116v+MB470LB_002_F.tif",
"Voynich_116v+MB470LB_024_F.tif",
"Voynich_116v+MB470LB_032_F.tif",
"Voynich_116v+MB505CN_003_F.tif",
"Voynich_116v+MB505CN_025_F.tif",
"Voynich_116v+MB505CN_033_F.tif",
"Voynich_116v+MB535GN_004_F.tif",
"Voynich_116v+MB535GN_026_F.tif",
"Voynich_116v+MB535GN_034_F.tif",
"Voynich_116v+MB570AM_005_F.tif",
"Voynich_116v+MB570AM_027_F.tif",
"Voynich_116v+MB570AM_035_F.tif",
"Voynich_116v+MB625RD_006_F.tif",
"Voynich_116v+MB625RD_028_F.tif",
"Voynich_116v+MB625RD_036_F.tif",
"Voynich_116v+MB700IR_008_F.tif",
"Voynich_116v+MB735IR_009_F.tif",
"Voynich_116v+MB780IR_010_F.tif",
"Voynich_116v+MB870IR_011_F.tif",
"Voynich_116v+MB870IR_030_F.tif",
"Voynich_116v+MB870IR_038_F.tif",
"Voynich_116v+MB940IR_012_F.tif",
"Voynich_116v+WBRBB47_018_F.tif",
"Voynich_116v+WBRBG58_016_F.tif",
"Voynich_116v+WBRBO22_021_F.tif",
"Voynich_116v+WBRBR25_014_F.tif",
"Voynich_116v+WBUVB47_017_F.tif",
"Voynich_116v+WBUVG58_015_F.tif",
"Voynich_116v+WBUVO22_020_F.tif",
"Voynich_116v+WBUVR25_013_F.tif",
"Voynich_116v+WBUVUVB_022_F.tif",
"Voynich_116v+WBUVUVP_019_F.tif"
]

weightedImage = None

for i, file in enumerate(files):

    print(f"Processing {file}")

    img = Image.open(path_to_tiffs + file)

    if weightedImage is None:
        weightedImage = np.array(img).astype(np.float32) * weights[i]
    else:
        weightedImage += np.array(img).astype(np.float32) * weights[i]

croppedImage = np.clip((weightedImage + bias) * 256, 0, 255).astype(np.uint8)

result = Image.fromarray(croppedImage)

print(f"Saving {result_filename}")
result.save(result_filename)


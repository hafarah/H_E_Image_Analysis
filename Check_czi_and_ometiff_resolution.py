### Checking resolution of CZI vs OME-TIFF export

from aicsimageio import AICSImage
from pathlib import Path

czi_path = Path(r"C:\Users\husse\VSCode_Projects\Image_Analysis\651CR_B.czi")
ome_path = Path(r"C:\Users\husse\VSCode_Projects\Image_Analysis\651CR_B-OME TIFF-Export-01.ome.tiff")

czi = AICSImage(czi_path)
ome = AICSImage(ome_path)

def summarize(img, name):
    print(f"\n{name}")
    print("  Shape (TZCYX):", img.shape)
    print("  Pixel size (µm):", img.physical_pixel_sizes)

summarize(czi, "CZI")
summarize(ome, "OME-TIFF")

# Hard checks
assert czi.shape[-3:] == ome.shape[-3:], "Pixel dimensions differ (Y, X, C)"
assert abs(czi.physical_pixel_sizes.X - ome.physical_pixel_sizes.X) < 1e-6, "❌ X pixel size mismatch"
assert abs(czi.physical_pixel_sizes.Y - ome.physical_pixel_sizes.Y) < 1e-6, "❌ Y pixel size mismatch"

print("\n CZI and OME-TIFF are pixel-aligned and annotation-compatible")

# Fluorescent Beads Subset of STEDSR Dataset

This subset contains paired confocal and STED images of 23 nm fluorescent
beads, acquired on the same custom-built STED microscope system. It is
intended for the cross-modal restoration task: reconstructing high-
resolution STED images from low-resolution confocal inputs.

## Folder Structure
beads/
├── confocal/         Low-resolution confocal images (depletion laser OFF)
├── STED/             High-resolution STED images
├── patch/            Pre-extracted paired image patches
│   ├── LR/             Patches cropped from confocal images
│   └── HR/             Patches cropped from STED images
└── beadspatch.py     Script used to extract patches from full FOVs

`confocal/` and `STED/` contain pixel-aligned full-FOV images of the same
fields of view. Each FOV is captured first in confocal mode, then in STED
mode, with no stage movement between acquisitions.

`patch/` contains pre-extracted paired patches that were used directly for
training and evaluation in the associated paper. Each LR patch in
`patch/LR/` corresponds to the HR patch with the same filename in
`patch/HR/`.

## File Specifications

- Format: 16-bit TIFF
- Patch size: 64 × 64 pixels
- Number of paired patches: 189

## How to Load (Python)

```python
import tifffile
from pathlib import Path

root = Path("beads/patch")
patch_id = "000017"

lr = tifffile.imread(root / "LR" / f"{patch_id}.tif")
hr = tifffile.imread(root / "HR" / f"{patch_id}.tif")
```

## Patch Extraction

Patches were extracted automatically from the full-FOV image pairs in
`confocal/` and `STED/` using `beadspatch.py`. The script can be re-run
to regenerate or customize the patch set (e.g. different patch size or
selection criteria) from the full-FOV images.

## License

CC BY 4.0. If you use this dataset, please cite the associated paper.
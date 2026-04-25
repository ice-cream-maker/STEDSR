# Microtubules Subset of STEDSR Dataset

This subset contains paired confocal and STED images of microtubules in fixed U2OS cells, acquired on the same custom-built STED microscope system. It is designed for training and benchmarking deep-learning models on the cross-modal restoration task: reconstructing high-resolution STED images from low-resolution confocal inputs.

## Folder Structure
microtubules/
├── confocal/         Low-resolution confocal images (depletion laser OFF)
├── STED_50mW_1/      STED images, depletion power = 50 mW (group 1)
├── STED_50mW_2/      STED images, depletion power = 50 mW (group 2)
└── STED_100mW/       STED images, depletion power = 100 mW

The four folders contain pixel-aligned images of the same fields of view
(FOVs). Each FOV is captured first in confocal mode, then in STED mode at
one or more depletion powers, with no stage movement between acquisitions.

## File Specifications

- Format: 16-bit TIFF
- Image size: 512 × 512 pixels
- Number of FOVs: 271 (each folder contains 271 images)

## File Naming

Files sharing the same index across folders correspond to the same field
of view. Example:
confocal/0017.tif      ←→  STED_50mW_1/0017.tif
←→  STED_50mW_2/0017.tif
←→  STED_100mW/0017.tif

## How to Load (Python)

```python
import tifffile
from pathlib import Path

root = Path("microtubules")
fov_id = "0017"

confocal = tifffile.imread(root / "confocal"    / f"{fov_id}.tif")
sted_50  = tifffile.imread(root / "STED_50mW_1" / f"{fov_id}.tif")
sted_100 = tifffile.imread(root / "STED_100mW"  / f"{fov_id}.tif")
```

## License

CC BY 4.0. If you use this dataset, please cite the associated paper.
# STEDSR: A Real-World Paired Dataset for Confocal-to-STED Cross-Modal Microscopy Image Restoration

STEDSR is a real-world paired microscopy image dataset designed for cross-
modal image restoration from confocal to stimulated emission depletion (STED)
microscopy. All images were acquired on the same custom-built STED microscope
system: confocal images were captured with the depletion laser turned off,
and STED images were captured with the depletion laser turned on, ensuring
pixel-level spatial correspondence between low-resolution and high-resolution
image pairs.

The dataset is intended for training and benchmarking deep-learning models
on the task of reconstructing high-resolution STED images from low-resolution
confocal inputs.

## Dataset Structure
STEDSR/
├── microtubules/         Microtubule images at multiple depletion powers
├── beads/                23 nm fluorescent bead images, with extracted patches
├── nuclear_pore/         Nuclear pore complex images (for generalization tests)
└── DataAugmentation.txt  Description of the patch extraction / data augmentation procedure

Each subset contains its own `README.md` with detailed information on its
folder structure, file naming, and loading examples. Please refer to those
files before using each subset.

## Subset Overview

| Subset         | Biological Structure       | Intended Use                              |
|----------------|----------------------------|-------------------------------------------|
| microtubules   | Microtubules               | Main training / evaluation set            |
| beads          | 23 nm fluorescent beads    | Small-sample benchmark                    |
| nuclear_pore   | Nuclear pore complexes     | Generalization test on unseen structures  |

## Patch Extraction and Data Augmentation

A unified MATLAB-based pipeline is provided for generating training and
validation patches from the full-FOV image pairs. The procedure includes
random cropping, random rotation, random flipping, and per-image
normalization. Details, parameters, and the script are described in
`DataAugmentation.txt`.

## Recommended Code

For training and inference, we recommend using the official open-source
implementations of the baseline models evaluated in the associated paper:

- CARE: https://github.com/CSBDeep/CSBDeep
- DFGAN: https://github.com/qc17-THU/DL-SR
- Restormer: https://github.com/swz30/Restormer

The hyperparameter settings used in the paper are reported in Section 3.2.

## License

This dataset is released under the Creative Commons Attribution 4.0
International License (CC BY 4.0). You are free to share and adapt the
material for any purpose, provided you give appropriate credit by citing
the associated publication.

## Citation

If you use this dataset, please cite:

>

## Contact

For questions about this dataset, please contact:

Jing Yan, Zhejiang University
Email: [yjwitch@zju.edu.cn]
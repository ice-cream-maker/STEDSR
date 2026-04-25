import os
import numpy as np
from tifffile import imread, imwrite
from scipy.ndimage import gaussian_filter
from skimage.feature import peak_local_max

# ======================
# 参数
# ======================

LR_DIR = r"D:\caredata\Beads\LR"
HR_DIR = r"D:\caredata\Beads\HR"

SAVE_LR = r"D:\caredata\Beads\LRpatch"
SAVE_HR = r"D:\caredata\Beads\HRpatch"

os.makedirs(SAVE_LR, exist_ok=True)
os.makedirs(SAVE_HR, exist_ok=True)

PATCH = 64
HALF = PATCH // 2

# 峰检测参数
MIN_DISTANCE = 6
THRESH_REL = 0.3

# 筛选参数
HR_SIGNAL_RATIO = 2.5
MAX_SHIFT = 3

patch_id = 0

# ======================
# 遍历图像
# ======================

for name in os.listdir(LR_DIR):

    if not name.endswith(".tif"):
        continue

    lr_path = os.path.join(LR_DIR, name)
    hr_path = os.path.join(HR_DIR, name)

    lr = imread(lr_path).astype(np.float32)
    hr = imread(hr_path).astype(np.float32)

    # 平滑防止假峰
    lr_s = gaussian_filter(lr, sigma=1)

    # 自动检测beads中心
    coords = peak_local_max(
        lr_s,
        min_distance=MIN_DISTANCE,
        threshold_rel=THRESH_REL
    )

    for y, x in coords:

        # 边缘检测
        if y-HALF < 0 or y+HALF >= lr.shape[0]:
            continue
        if x-HALF < 0 or x+HALF >= lr.shape[1]:
            continue

        lr_patch = lr[y-HALF:y+HALF, x-HALF:x+HALF]
        hr_patch = hr[y-HALF:y+HALF, x-HALF:x+HALF]

        # -------------------
        # HR 信号强度筛选
        # -------------------

        bg = np.mean(hr_patch)
        noise = np.std(hr_patch)

        if np.max(hr_patch) < bg + HR_SIGNAL_RATIO * noise:
            continue

        # -------------------
        # 峰位置对齐检测
        # -------------------

        lr_peak = np.unravel_index(np.argmax(lr_patch), lr_patch.shape)
        hr_peak = np.unravel_index(np.argmax(hr_patch), hr_patch.shape)

        shift = np.sqrt(
            (lr_peak[0] - hr_peak[0])**2 +
            (lr_peak[1] - hr_peak[1])**2
        )

        if shift > MAX_SHIFT:
            continue

        # -------------------
        # 保存patch
        # -------------------

        patch_name = f"{patch_id:06d}.tif"

        imwrite(os.path.join(SAVE_LR, patch_name), lr_patch.astype(np.uint16))
        imwrite(os.path.join(SAVE_HR, patch_name), hr_patch.astype(np.uint16))

        patch_id += 1

print("Finished.")
print("Total patches:", patch_id)

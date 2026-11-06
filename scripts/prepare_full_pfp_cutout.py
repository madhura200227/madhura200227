import numpy as np
from PIL import Image
from scipy import ndimage
import os
import shutil

def extract_full_pfp():
    src_path = r'C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/.user_uploaded/media_1793979237212_1db22f16.jpg'
    im = Image.open(src_path).convert('RGB')
    arr = np.array(im, dtype=np.float32)
    H, W, _ = arr.shape

    # 1. Detect checkerboard background
    # Checkerboard characteristics:
    # Highly desaturated (chroma < 14) AND high luminance (gray > 165)
    rg_diff = np.abs(arr[:, :, 0] - arr[:, :, 1])
    gb_diff = np.abs(arr[:, :, 1] - arr[:, :, 2])
    rb_diff = np.abs(arr[:, :, 0] - arr[:, :, 2])
    chroma = np.maximum(np.maximum(rg_diff, gb_diff), rb_diff)
    gray = np.mean(arr, axis=2)

    is_checker = (chroma < 14) & (gray > 165)

    # 2. Border connected component
    labeled, num_labels = ndimage.label(is_checker)
    # Check top, left, right borders (not bottom because subject goes to bottom)
    border_pixels = np.concatenate([
        labeled[0, :],      # top row
        labeled[:, 0],      # left col
        labeled[:, -1]      # right col
    ])
    border_labels = set(border_pixels) - {0} # 0 is foreground/unmatched

    # Mask of definite external background (covers both left and right sides)
    external_bg = np.isin(labeled, list(border_labels))

    # Also handle any tiny isolated checkerboard pockets near border
    for _ in range(3):
        dilated = ndimage.binary_dilation(external_bg)
        external_bg = dilated & is_checker

    # 3. Distance transform for smooth anti-aliased edge
    # Background is external_bg; subject is solid foreground ~external_bg
    fg_solid = ~external_bg

    dist_fg = ndimage.distance_transform_edt(fg_solid)
    dist_bg = ndimage.distance_transform_edt(external_bg)
    signed_dist = dist_fg - dist_bg

    # Smooth Hermite transition between -0.5px and +1.5px
    edge_min = -0.5
    edge_max = 1.5
    t = np.clip((signed_dist - edge_min) / (edge_max - edge_min), 0.0, 1.0)
    alpha = t * t * (3.0 - 2.0 * t)

    # De-fringe: edge pixels against light gray/white checkerboard
    rgb_clean = np.copy(arr)
    edge_band = (alpha > 0.02) & (alpha < 0.98)
    is_dark_fg = (gray < 140) & edge_band
    for c in range(3):
        c_val = rgb_clean[:, :, c]
        bg_est = 230.0
        recovered = (c_val[is_dark_fg] - (1.0 - alpha[is_dark_fg]) * bg_est) / np.maximum(alpha[is_dark_fg], 0.15)
        rgb_clean[:, :, c][is_dark_fg] = np.clip(recovered, 0.0, 255.0)

    # Combine into 32-bit RGBA
    rgba = np.dstack([
        rgb_clean.astype(np.uint8),
        (alpha * 255.0).astype(np.uint8)
    ])

    cutout_im = Image.fromarray(rgba, mode='RGBA')

    # Save to requested destination: assets/portrait/madhura-full-pfp-cutout.png
    os.makedirs('assets/portrait', exist_ok=True)
    
    p1 = 'assets/portrait/madhura-full-pfp-cutout.png'
    p2 = 'assets/portrait/madhura-pfp.png' # update default master
    p3 = 'assets/madhura-pfp.png'

    cutout_im.save(p1, format='PNG', optimize=True)
    cutout_im.save(p2, format='PNG', optimize=True)
    cutout_im.save(p3, format='PNG', optimize=True)
    print(f"Saved refined full portrait cutout to {p1} ({cutout_im.size})")

    # Delete misspelled folder if it exists
    if os.path.exists('assets/potrait'):
        shutil.rmtree('assets/potrait')
        print("Deleted misspelled directory 'assets/potrait'")

    # Composite preview against Espresso and Burgundy surfaces to verify
    for bg_name, hex_c in [('espresso', (33, 24, 23)), ('burgundy', (101, 13, 37))]:
        bg_im = Image.new('RGB', cutout_im.size, hex_c)
        bg_im.paste(cutout_im, (0, 0), cutout_im)
        bg_im.save(f'assets/portrait/preview-full-{bg_name}.png', format='PNG')
        print(f"Saved surface preview: assets/portrait/preview-full-{bg_name}.png")

if __name__ == "__main__":
    extract_full_pfp()

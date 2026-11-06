import numpy as np
from PIL import Image

def refine_cutout():
    src_path = 'assets/source/madhura-pfp-original.png'
    # Start fresh from the original source
    orig_im = Image.open(src_path).convert('RGB')
    orig_arr = np.array(orig_im, dtype=np.float32)
    H, W, _ = orig_arr.shape

    # 1. Definite external background: black void (<= 5)
    max_c = np.max(orig_arr, axis=2)
    from scipy import ndimage
    bg_seed = (max_c <= 5)
    labeled, _ = ndimage.label(bg_seed)
    
    # Border labels
    border_labels = set(labeled[0, :]).union(
        set(labeled[-1, :])
    ).union(
        set(labeled[:, 0])
    ).union(
        set(labeled[:, -1])
    )
    external_bg = np.isin(labeled, list(border_labels))
    fg_mask = ~external_bg

    # Distance transforms
    dist_fg = ndimage.distance_transform_edt(fg_mask)
    dist_bg = ndimage.distance_transform_edt(external_bg)
    signed_dist = dist_fg - dist_bg

    # Smoothstep interpolation
    edge_min = -0.6
    edge_max = 1.8
    t = np.clip((signed_dist - edge_min) / (edge_max - edge_min), 0.0, 1.0)
    alpha = t * t * (3.0 - 2.0 * t)

    # De-fringe
    rgb_clean = np.copy(orig_arr)
    fringe_mask = (alpha > 0.02) & (alpha < 0.98)
    scale = np.ones_like(alpha)
    scale[fringe_mask] = 1.0 / np.maximum(alpha[fringe_mask], 0.15)
    scale[fringe_mask] = np.clip(scale[fringe_mask], 1.0, 2.5)
    for c in range(3):
        rgb_clean[:, :, c] = np.clip(orig_arr[:, :, c] * scale, 0.0, 255.0)
    rgb_clean[alpha >= 0.98] = orig_arr[alpha >= 0.98]

    # 2. Feather the bottom and right circular cut
    # The original circle boundary is at dist_from_center ~ 502 from (512, 512)
    y_idx, x_idx = np.indices((H, W), dtype=np.float32)
    dist_center = np.sqrt((x_idx - 512.0)**2 + (y_idx - 512.0)**2)
    r_crop = 502.0

    # In the crop zone (lower half y > 400 or right side x > 650),
    # smoothly feather the boundary inwards by 42px
    feather_w = 42.0
    t_feather = np.clip((r_crop - dist_center) / feather_w, 0.0, 1.0)
    smooth_feather = t_feather * t_feather * (3.0 - 2.0 * t_feather)

    is_crop_zone = (y_idx > 380) | (x_idx > 600)
    edge_near_circle = is_crop_zone & (dist_center > (r_crop - feather_w))
    alpha[edge_near_circle] = alpha[edge_near_circle] * smooth_feather[edge_near_circle]

    # Bottom fade: y > 920
    bot_fade = np.clip((1024.0 - y_idx) / 100.0, 0.0, 1.0)
    bot_fade_smooth = bot_fade * bot_fade * (3.0 - 2.0 * bot_fade)
    alpha[y_idx > 920] = alpha[y_idx > 920] * bot_fade_smooth[y_idx > 920]

    # Combine RGBA
    rgba = np.dstack([
        rgb_clean.astype(np.uint8),
        (alpha * 255.0).astype(np.uint8)
    ])

    cutout_im = Image.fromarray(rgba, mode='RGBA')
    cutout_im.save('assets/portrait/madhura-pfp.png', format='PNG', optimize=True)
    cutout_im.save('assets/portrait/madhura-pfp-cutout.png', format='PNG', optimize=True)
    cutout_im.save('assets/madhura-pfp.png', format='PNG', optimize=True)
    print("Successfully built feathered, seamless portrait cutout!")

if __name__ == "__main__":
    refine_cutout()

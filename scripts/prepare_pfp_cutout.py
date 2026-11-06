import os
import numpy as np
from PIL import Image
from scipy import ndimage

def main():
    source_path = r'C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f/.user_uploaded/media_1793910496276_861d5dee.jpg'
    
    os.makedirs('assets/source', exist_ok=True)
    os.makedirs('assets/portrait', exist_ok=True)
    
    # 1. Save untouched original to assets/source/madhura-pfp-original.png
    orig_im = Image.open(source_path)
    orig_png_path = 'assets/source/madhura-pfp-original.png'
    orig_im.save(orig_png_path, format='PNG')
    # Backward compatibility copy
    orig_im.save('assets/source/new-pfp-original.png', format='PNG')
    print(f"Saved original image: {orig_png_path} ({orig_im.size})")

    # Convert to numpy array float32
    rgb = np.array(orig_im, dtype=np.float32)
    H, W, _ = rgb.shape
    max_c = np.max(rgb, axis=2)

    # 2. Definite external background extraction via border connectivity
    # Threshold 4 covers pure black and subtle JPEG compression noise in the void
    bg_seed = (max_c <= 4)
    labeled, num_features = ndimage.label(bg_seed)
    
    # Identify all labels touching the 1px outer frame
    border_labels = set(labeled[0, :]).union(
        set(labeled[-1, :])
    ).union(
        set(labeled[:, 0])
    ).union(
        set(labeled[:, -1])
    )
    external_bg = np.isin(labeled, list(border_labels))
    
    # Distance transforms from the border background and subject
    # dist_fg is distance inside foreground towards background
    fg_mask = ~external_bg
    dist_fg = ndimage.distance_transform_edt(fg_mask)
    # dist_bg is distance inside background towards foreground
    dist_bg = ndimage.distance_transform_edt(external_bg)

    # 3. Precision Sub-pixel Alpha Transition
    # Core subject (dist_fg >= 2.0px): alpha = 1.0
    # Outer void (dist_bg >= 1.0px): alpha = 0.0
    # Boundary zone (sub-pixel transition):
    # Normalized position: signed distance d = dist_fg if inside, -dist_bg if outside
    signed_dist = dist_fg - dist_bg
    
    # Smooth Hermite/Cubic smoothstep between -0.8px and +1.8px
    # This captures subpixel anti-aliasing without eroding hair strands or creating jagged edges
    edge_min = -0.6
    edge_max = 1.8
    t = np.clip((signed_dist - edge_min) / (edge_max - edge_min), 0.0, 1.0)
    # Smoothstep interpolation: 3t^2 - 2t^3
    alpha = t * t * (3.0 - 2.0 * t)

    # 4. Color De-fringing / Un-premultiplying
    # Since background was black, edge pixels were blended with black [0,0,0]
    # Un-premultiply edge pixels with alpha < 1.0 to restore true hair/clothing color
    # This prevents dark/black halos when placed over light surfaces like Ivory
    rgb_clean = np.copy(rgb)
    fringe_mask = (alpha > 0.02) & (alpha < 0.98)
    
    # Scale back color intensity based on alpha
    scale = np.ones_like(alpha)
    scale[fringe_mask] = 1.0 / np.maximum(alpha[fringe_mask], 0.15)
    # Limit max brightening to prevent noise amplification
    scale[fringe_mask] = np.clip(scale[fringe_mask], 1.0, 2.5)

    for c in range(3):
        rgb_clean[:, :, c] = np.clip(rgb[:, :, c] * scale, 0.0, 255.0)

    # Re-apply exact subject colors inside core
    rgb_clean[alpha >= 0.98] = rgb[alpha >= 0.98]

    # Assemble RGBA image
    rgba = np.dstack([
        rgb_clean.astype(np.uint8),
        (alpha * 255.0).astype(np.uint8)
    ])
    
    cutout_im = Image.fromarray(rgba, mode='RGBA')
    cutout_path = 'assets/portrait/madhura-pfp.png'
    cutout_im.save(cutout_path, format='PNG', optimize=True)
    # Also save aliases for backwards compatibility and exact matching
    cutout_im.save('assets/portrait/madhura-pfp-cutout.png', format='PNG', optimize=True)
    cutout_im.save('assets/portrait/new-pfp-cutout.png', format='PNG', optimize=True)
    cutout_im.save('assets/madhura-pfp.png', format='PNG', optimize=True)
    print(f"Saved transparent cutout: {cutout_path}")

    # 5. Composite onto the Three Strict Brand Backgrounds
    # Approved palette tokens:
    # Espresso: #211817 (33, 24, 23)
    # Burgundy: #650D25 (101, 13, 37)
    # Ivory:    #FFF5ED (255, 245, 237)
    bg_colors = {
        'espresso': (33, 24, 23),
        'burgundy': (101, 13, 37),
        'ivory':    (255, 245, 237)
    }

    a_norm = alpha[:, :, np.newaxis]
    previews = {}

    for name, (br, bg, bb) in bg_colors.items():
        bg_canvas = np.zeros_like(rgb)
        bg_canvas[:, :, 0] = br
        bg_canvas[:, :, 1] = bg
        bg_canvas[:, :, 2] = bb
        
        # Alpha compositing: result = alpha * fg + (1 - alpha) * bg
        comp = (a_norm * rgb_clean + (1.0 - a_norm) * bg_canvas)
        comp_im = Image.fromarray(np.clip(comp, 0, 255).astype(np.uint8), mode='RGB')
        
        p_path = f'assets/portrait/preview-{name}.png'
        comp_im.save(p_path, format='PNG', optimize=True)
        previews[name] = comp_im
        print(f"Saved preview against {name.capitalize()} background: {p_path}")

    # 6. Generate side-by-side composite comparison card for user inspection
    # 4 columns: Original, Cutout on Espresso, Cutout on Burgundy, Cutout on Ivory
    card_w = 4 * 512 + 5 * 24
    card_h = 512 + 120
    comp_sheet = Image.new('RGB', (card_w, card_h), (20, 14, 15))
    
    # Resize components to 512x512 for side-by-side viewing
    from PIL import ImageDraw, ImageFont
    draw = ImageDraw.Draw(comp_sheet)
    
    titles = [
        ("1. Original Source (Black Void)", orig_im.resize((512, 512), Image.Resampling.LANCZOS)),
        ("2. Cutout on Espresso (#211817)", previews['espresso'].resize((512, 512), Image.Resampling.LANCZOS)),
        ("3. Cutout on Burgundy (#650D25)", previews['burgundy'].resize((512, 512), Image.Resampling.LANCZOS)),
        ("4. Cutout on Ivory (#FFF5ED)", previews['ivory'].resize((512, 512), Image.Resampling.LANCZOS))
    ]

    for idx, (title, img_thumb) in enumerate(titles):
        pos_x = 24 + idx * (512 + 24)
        pos_y = 60
        comp_sheet.paste(img_thumb, (pos_x, pos_y))
        
        # Border around thumb
        draw.rectangle([pos_x - 1, pos_y - 1, pos_x + 512, pos_y + 512], outline=(135, 61, 80), width=2)
        # Title
        draw.text((pos_x + 10, 24), title, fill=(255, 245, 237))

    comparison_path = 'assets/portrait/preview-comparison.png'
    comp_sheet.save(comparison_path, format='PNG', optimize=True)
    print(f"Saved side-by-side comparison sheet: {comparison_path}")

if __name__ == "__main__":
    main()


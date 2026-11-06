import shutil, os
from PIL import Image

brain_dir = r'C:/Users/Admin/.gemini/antigravity/brain/9c315c8b-ce41-4231-97ec-457407fce54f'

files_to_copy = [
    ('assets/hero/hero-banner-preview.png', os.path.join(brain_dir, 'hero-espresso-preview.png')),
    ('assets/hero/hero-banner-cherry-preview.png', os.path.join(brain_dir, 'hero-cherry-preview.png')),
    ('assets/hero/hero-comparison.png', os.path.join(brain_dir, 'hero-theme-comparison.png')),
    ('assets/hero/hero-banner.gif', os.path.join(brain_dir, 'hero-animation-preview.gif'))
]

for src, dst in files_to_copy:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        size = os.path.getsize(dst)
        print(f"Copied {src} -> {dst} ({size} bytes)")
    else:
        print(f"Warning: {src} not found")


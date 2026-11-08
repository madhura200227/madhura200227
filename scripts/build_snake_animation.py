import os
import math
from PIL import Image, ImageDraw, ImageFont

def build_snake_gif(theme="cherry", output_path="assets/stats/snake-cherry.gif"):
    width, height = 840, 220
    
    if theme == "cherry":
        c_bg = (38, 5, 16)             # #260510
        c_border = (193, 18, 63)        # #C1123F
        c_accent = (255, 45, 96)        # #FF2D60
        c_empty = (42, 7, 18)           # #2a0712
        c_l1 = (84, 11, 32)             # #540b20
        c_l2 = (120, 14, 43)            # #780e2b
        c_l3 = (193, 18, 63)            # #C1123F
        c_l4 = (255, 45, 96)            # #FF2D60
        body_palette = [
            (255, 45, 96),
            (255, 74, 117),
            (193, 18, 63),
            (135, 61, 80),
            (101, 13, 37),
            (74, 16, 29)
        ]
    else: # espresso
        c_bg = (27, 18, 20)             # #1b1214
        c_border = (135, 61, 80)        # #873D50
        c_accent = (193, 18, 63)        # #C1123F
        c_empty = (33, 18, 23)          # #211217
        c_l1 = (61, 16, 30)             # #3d101e
        c_l2 = (101, 13, 37)            # #650D25
        c_l3 = (135, 61, 80)            # #873D50
        c_l4 = (193, 18, 63)            # #C1123F
        body_palette = [
            (193, 18, 63),
            (230, 28, 82),
            (135, 61, 80),
            (101, 13, 37),
            (74, 16, 29),
            (50, 12, 20)
        ]

    cols = 51
    rows = 7
    cell_sz = 11
    pitch = 15
    start_x = 38
    start_y = 80

    # Deterministic contribution grid
    base_grid = {}
    for c in range(cols):
        for r in range(rows):
            val = (c * 7 + r * 13 + (c * r) % 17) % 10
            if val < 4:
                col = c_empty
            elif val < 6:
                col = c_l1
            elif val < 8:
                col = c_l2
            elif val < 9:
                col = c_l3
            else:
                col = c_l4
            base_grid[(c, r)] = col

    # Generate a smooth continuous winding snake trajectory across the grid
    # A path of grid coordinates (col, row)
    path = []
    # Row 0 left-to-right
    for c in range(0, 16): path.append((c, 0))
    # Dip down into col 16
    for r in range(1, 4): path.append((16, r))
    # Sweep left
    for c in range(15, 6, -1): path.append((c, 3))
    # Dip down to row 6
    for r in range(4, 7): path.append((6, r))
    # Sweep right along bottom
    for c in range(7, 28): path.append((c, 6))
    # Wind up through col 28
    for r in range(5, 1, -1): path.append((28, r))
    # Sweep right
    for c in range(29, 42): path.append((c, 2))
    # Wind down through col 42
    for r in range(3, 7): path.append((42, r))
    # Sweep right to col 50
    for c in range(43, 51): path.append((c, 6))
    # Wind up col 50
    for r in range(5, -1, -1): path.append((50, r))
    # Sweep left along top
    for c in range(49, 32, -1): path.append((c, 0))
    # Dip through row 1-3
    for r in range(1, 4): path.append((32, r))
    # Sweep left through middle
    for c in range(31, 19, -1): path.append((c, 3))
    # Wind up to row 1
    for r in range(2, 0, -1): path.append((19, r))
    # Sweep left to col 0
    for c in range(18, -1, -1): path.append((c, 1))
    # Close loop back to (0, 0)
    path.append((0, 0))

    total_steps = len(path)
    body_len = 6

    # Load fonts
    try:
        f_meta = ImageFont.truetype('consolab.ttf', 12)
        f_title = ImageFont.truetype('georgiab.ttf', 20)
        f_status = ImageFont.truetype('consolab.ttf', 11)
    except Exception:
        f_meta = ImageFont.load_default()
        f_title = ImageFont.load_default()
        f_status = ImageFont.load_default()

    frames = []
    
    # We create 2 frames per step for smooth interpolation
    substeps = 2
    total_frames = total_steps * substeps

    # Keep track of eaten cells
    eaten_cells = set()

    for f_idx in range(total_frames):
        step = f_idx // substeps
        sub = f_idx % substeps
        t_frac = sub / float(substeps)

        im = Image.new('RGB', (width, height), c_bg)
        draw = ImageDraw.Draw(im)

        # 1. Architectural Card Frame
        draw.rounded_rectangle([10, 10, width - 10, height - 10], radius=12, fill=c_bg, outline=c_border, width=1)
        draw.line([(10, 10), (width - 10, 10)], fill=c_accent, width=3)

        # Corner Flourishes
        draw.line([(20, 32), (20, 20), (32, 20)], fill=c_accent, width=2)
        draw.line([(width - 20, 32), (width - 20, 20), (width - 32, 20)], fill=c_accent, width=2)
        draw.line([(20, height - 32), (20, height - 20), (32, height - 20)], fill=c_accent, width=2)
        draw.line([(width - 20, height - 32), (width - 20, height - 20), (width - 32, height - 20)], fill=c_accent, width=2)

        # 2. Header
        draw.rectangle([38, 28, 44, 34], fill=c_accent)
        draw.text((52, 24), "CONTRIBUTION TIMELINE // DAILY SNAKE STREAM", fill=(217, 154, 167), font=f_meta)
        draw.text((38, 44), "Contribution Activity", fill=(255, 255, 255), font=f_title)

        # Pulsing Live Indicator (NO GREEN DOT - THEME ACCENT)
        pulse_r = 4.0 + 1.2 * math.sin(f_idx * 0.2)
        draw.ellipse([690 - pulse_r, 52 - pulse_r, 690 + pulse_r, 52 + pulse_r], fill=c_accent)
        draw.text((702, 45), "LIVE STREAM", fill=(217, 154, 167), font=f_status)

        # Current head and body positions
        head_cell = path[step]
        next_head_cell = path[(step + 1) % total_steps]
        
        # Mark cell as eaten when head visits it
        eaten_cells.add(head_cell)
        if len(eaten_cells) > total_steps * 0.85:
            # Gradually regenerate earlier cells so the grid stays alive
            eaten_cells.clear()

        # Render Contribution Cells
        for c in range(cols):
            for r in range(rows):
                cx = start_x + c * pitch
                cy = start_y + r * pitch
                cell_col = base_grid[(c, r)]
                
                # If eaten by snake, render as empty or eaten glow
                if (c, r) in eaten_cells:
                    cell_col = c_empty

                draw.rounded_rectangle([cx, cy, cx + cell_sz, cy + cell_sz], radius=2.5, fill=cell_col)

        # Calculate interpolated positions for head and body
        curr_x = start_x + (head_cell[0] * (1.0 - t_frac) + next_head_cell[0] * t_frac) * pitch + cell_sz / 2
        curr_y = start_y + (head_cell[1] * (1.0 - t_frac) + next_head_cell[1] * t_frac) * pitch + cell_sz / 2

        # 3. Draw Body Segments (Connected Trail behind Head)
        for b_idx in range(body_len - 1, -1, -1):
            hist_step = (step - (b_idx + 1)) % total_steps
            hist_next = (step - b_idx) % total_steps
            b_cell = path[hist_step]
            b_next_cell = path[hist_next]

            bx = start_x + (b_cell[0] * (1.0 - t_frac) + b_next_cell[0] * t_frac) * pitch + cell_sz / 2
            by = start_y + (b_cell[1] * (1.0 - t_frac) + b_next_cell[1] * t_frac) * pitch + cell_sz / 2

            b_sz = max(7, 12 - b_idx)
            b_col = body_palette[min(b_idx, len(body_palette) - 1)]
            draw.rounded_rectangle([bx - b_sz/2, by - b_sz/2, bx + b_sz/2, by + b_sz/2], radius=3, fill=b_col)

        # 4. Draw Snake Head
        head_sz = 14
        draw.rounded_rectangle([curr_x - head_sz/2, curr_y - head_sz/2, curr_x + head_sz/2, curr_y + head_sz/2], radius=4, fill=(255, 255, 255), outline=c_accent, width=2)
        
        # Eyes pointing in movement direction
        dx = next_head_cell[0] - head_cell[0]
        dy = next_head_cell[1] - head_cell[1]
        if dx > 0: # moving right
            eye1 = (curr_x + 2, curr_y - 2.5)
            eye2 = (curr_x + 2, curr_y + 2.5)
        elif dx < 0: # moving left
            eye1 = (curr_x - 2, curr_y - 2.5)
            eye2 = (curr_x - 2, curr_y + 2.5)
        elif dy > 0: # moving down
            eye1 = (curr_x - 2.5, curr_y + 2)
            eye2 = (curr_x + 2.5, curr_y + 2)
        else: # moving up
            eye1 = (curr_x - 2.5, curr_y - 2)
            eye2 = (curr_x + 2.5, curr_y - 2)

        draw.ellipse([eye1[0]-1.5, eye1[1]-1.5, eye1[0]+1.5, eye1[1]+1.5], fill=c_accent)
        draw.ellipse([eye2[0]-1.5, eye2[1]-1.5, eye2[0]+1.5, eye2[1]+1.5], fill=c_accent)

        frames.append(im.quantize(colors=128, method=Image.Quantize.FASTOCTREE))

    # Save animated GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=65, # ~15 FPS smooth retro speed
        loop=0,
        optimize=True
    )
    print(f"Saved animated snake GIF: {output_path} ({len(frames)} frames)")

if __name__ == '__main__':
    print("Generating Cherry Snake GIF...")
    build_snake_gif("cherry", "assets/stats/snake-cherry.gif")
    print("Generating Espresso Snake GIF...")
    build_snake_gif("espresso", "assets/stats/snake.gif")


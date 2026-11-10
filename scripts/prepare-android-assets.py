import os
from PIL import Image, ImageDraw

def generate_android_icons():
    src_path = 'assets/icons/app-icon.jpg'
    if not os.path.exists(src_path):
        print(f"Error: {src_path} not found")
        return

    base_img = Image.open(src_path).convert('RGBA')

    # Densitites for legacy and adaptive
    densities = {
        'mdpi': {'legacy': 48, 'adaptive': 108},
        'hdpi': {'legacy': 72, 'adaptive': 162},
        'xhdpi': {'legacy': 96, 'adaptive': 216},
        'xxhdpi': {'legacy': 144, 'adaptive': 324},
        'xxxhdpi': {'legacy': 192, 'adaptive': 432},
    }

    res_dir = 'android/app/src/main/res'

    for density, sizes in densities.items():
        density_dir = os.path.join(res_dir, f'mipmap-{density}')
        os.makedirs(density_dir, exist_ok=True)

        leg_size = sizes['legacy']
        adap_size = sizes['adaptive']

        # 1. ic_launcher.png (legacy square)
        img_legacy = base_img.resize((leg_size, leg_size), Image.Resampling.LANCZOS)
        img_legacy.save(os.path.join(density_dir, 'ic_launcher.png'), 'PNG')

        # 2. ic_launcher_round.png (legacy round)
        mask = Image.new('L', (leg_size, leg_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, leg_size - 1, leg_size - 1), fill=255)
        round_img = img_legacy.copy()
        round_img.putalpha(mask)
        round_img.save(os.path.join(density_dir, 'ic_launcher_round.png'), 'PNG')

        # 3. ic_launcher_foreground.png (adaptive foreground)
        # Scaled to fit comfortably inside safe zone (~72% of adaptive canvas)
        content_size = int(adap_size * 0.76)
        scaled_content = base_img.resize((content_size, content_size), Image.Resampling.LANCZOS)
        
        # Round mask on the foreground so it looks neat if viewed standalone
        fg_img = Image.new('RGBA', (adap_size, adap_size), (0, 0, 0, 0))
        offset = (adap_size - content_size) // 2
        fg_img.paste(scaled_content, (offset, offset))
        fg_img.save(os.path.join(density_dir, 'ic_launcher_foreground.png'), 'PNG')

    # Update ic_launcher_background color
    bg_xml_path = os.path.join(res_dir, 'values', 'ic_launcher_background.xml')
    os.makedirs(os.path.dirname(bg_xml_path), exist_ok=True)
    with open(bg_xml_path, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n')
        f.write('<resources>\n')
        f.write('    <color name="ic_launcher_background">#17306D</color>\n')
        f.write('</resources>\n')

    print("✓ All Android mipmap icons and background color updated successfully.")

if __name__ == '__main__':
    generate_android_icons()

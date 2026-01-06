#!/usr/bin/env python3
"""
BlockRun.ai Brand Kit - PNG Export Script
Converts SVG logos to PNG at various sizes.

Usage:
    pip install cairosvg pillow
    python export-png.py
"""

import os
from pathlib import Path

try:
    import cairosvg
    from PIL import Image
except ImportError:
    print("Please install dependencies:")
    print("  pip install cairosvg pillow")
    exit(1)

# Paths
SCRIPT_DIR = Path(__file__).parent
SVG_DIR = SCRIPT_DIR / "svg"
PNG_DIR = SCRIPT_DIR / "png"
FAVICON_DIR = SCRIPT_DIR / "favicon"
SOCIAL_DIR = SCRIPT_DIR / "social"

# Ensure directories exist
PNG_DIR.mkdir(exist_ok=True)
FAVICON_DIR.mkdir(exist_ok=True)
SOCIAL_DIR.mkdir(exist_ok=True)

# Logo sizes to export
SIZES = [16, 32, 48, 64, 128, 256, 512, 1024]

# Favicon sizes
FAVICON_SIZES = [16, 32, 48, 180, 192, 512]

def export_svg_to_png(svg_path, output_path, size):
    """Convert SVG to PNG at specified size."""
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(output_path),
        output_width=size,
        output_height=size
    )
    print(f"  Created: {output_path.name}")

def export_all_sizes():
    """Export all logo variants at all sizes."""
    print("\n=== Exporting PNG files ===\n")

    variants = ["primary", "white", "black"]

    for variant in variants:
        svg_path = SVG_DIR / f"logo-{variant}.svg"
        if not svg_path.exists():
            print(f"Warning: {svg_path} not found")
            continue

        print(f"\n{variant.upper()} variant:")
        for size in SIZES:
            output_path = PNG_DIR / f"logo-{variant}-{size}.png"
            export_svg_to_png(svg_path, output_path, size)

def export_favicons():
    """Export favicon sizes."""
    print("\n=== Exporting Favicons ===\n")

    svg_path = SVG_DIR / "logo-primary.svg"
    if not svg_path.exists():
        print("Warning: logo-primary.svg not found")
        return

    for size in FAVICON_SIZES:
        output_path = FAVICON_DIR / f"favicon-{size}.png"
        export_svg_to_png(svg_path, output_path, size)

    # Create apple-touch-icon
    output_path = FAVICON_DIR / "apple-touch-icon.png"
    export_svg_to_png(svg_path, output_path, 180)

    print("\nFavicon files created. To create .ico file, use an online converter")
    print("or install imagemagick and run:")
    print("  convert favicon-16.png favicon-32.png favicon-48.png favicon.ico")

def export_social_media():
    """Export social media sizes."""
    print("\n=== Exporting Social Media Images ===\n")

    svg_path = SVG_DIR / "logo-white.svg"
    if not svg_path.exists():
        print("Warning: logo-white.svg not found")
        return

    # Profile image (square with blue background)
    profile_size = 400
    temp_path = SOCIAL_DIR / "temp-logo.png"
    export_svg_to_png(svg_path, temp_path, int(profile_size * 0.6))

    # Create profile with blue background
    img = Image.new('RGB', (profile_size, profile_size), '#2563EB')
    logo = Image.open(temp_path)

    # Center the logo
    offset = (profile_size - logo.width) // 2
    img.paste(logo, (offset, offset), logo if logo.mode == 'RGBA' else None)

    profile_path = SOCIAL_DIR / "profile-400.png"
    img.save(profile_path)
    print(f"  Created: {profile_path.name}")

    # Twitter/X profile
    twitter_path = SOCIAL_DIR / "twitter-profile-400.png"
    img.save(twitter_path)
    print(f"  Created: {twitter_path.name}")

    # OG Image (1200x630)
    og_width, og_height = 1200, 630
    og_img = Image.new('RGB', (og_width, og_height), '#2563EB')

    logo_og = Image.open(temp_path).resize((300, 300), Image.Resampling.LANCZOS)
    offset_x = (og_width - 300) // 2
    offset_y = (og_height - 300) // 2
    og_img.paste(logo_og, (offset_x, offset_y), logo_og if logo_og.mode == 'RGBA' else None)

    og_path = SOCIAL_DIR / "og-image-1200x630.png"
    og_img.save(og_path)
    print(f"  Created: {og_path.name}")

    # Clean up temp file
    temp_path.unlink()

def main():
    print("=" * 50)
    print("BlockRun.ai Brand Kit - PNG Export")
    print("=" * 50)

    export_all_sizes()
    export_favicons()
    export_social_media()

    print("\n" + "=" * 50)
    print("Export complete!")
    print("=" * 50)
    print(f"\nFiles saved to:")
    print(f"  PNG:      {PNG_DIR}")
    print(f"  Favicon:  {FAVICON_DIR}")
    print(f"  Social:   {SOCIAL_DIR}")

if __name__ == "__main__":
    main()

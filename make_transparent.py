from PIL import Image

def remove_white_bg(input_path, output_path, threshold=235):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if r >= threshold and g >= threshold and b >= threshold:
                pixels[x, y] = (r, g, b, 0)
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

remove_white_bg("logo_smbc_nikko.jpg", "logo_smbc_nikko.png")
remove_white_bg("logo_mufg_ms.webp", "logo_mufg_ms.png")

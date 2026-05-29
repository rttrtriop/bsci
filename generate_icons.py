from PIL import Image, ImageDraw
import os

os.makedirs('uiassets', exist_ok=True)

size = (64, 64)
# Dark purple background
bg_color = (60, 20, 100) # RGB for dark purple
# White foreground
fg_color = (255, 255, 255)

line_width = 2 # Thinner lines for minimalist look

def create_base_image():
    return Image.new('RGB', size, color=bg_color)

# 1. save.png (Floppy disk / Minimalist save icon)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.rectangle([16, 16, 48, 48], outline=fg_color, width=line_width)
draw.line([(16, 26), (48, 26)], fill=fg_color, width=line_width) # Header line
draw.rectangle([24, 16, 40, 22], outline=fg_color, width=line_width) # Top slider hole
draw.rectangle([22, 34, 42, 48], outline=fg_color, width=line_width) # Bottom label
img.save('uiassets/save.png')

# 2. set_nick.png (Minimalist Person icon)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.ellipse([24, 14, 40, 30], outline=fg_color, width=line_width) # head
draw.arc([14, 38, 50, 70], start=180, end=360, fill=fg_color, width=line_width) # shoulders
img.save('uiassets/set_nick.png')

# 3. reload.png (Minimalist Circular arrow)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.arc([16, 16, 48, 48], start=45, end=315, fill=fg_color, width=line_width) # partial circle
draw.line([(42, 10), (42, 22)], fill=fg_color, width=line_width) # Arrow lines
draw.line([(42, 22), (54, 22)], fill=fg_color, width=line_width)
img.save('uiassets/reload.png')

# 4. pause.png (Minimalist Two vertical bars)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.rectangle([22, 18, 26, 46], fill=fg_color)
draw.rectangle([38, 18, 42, 46], fill=fg_color)
img.save('uiassets/pause.png')

# 5. start.png (Minimalist Play triangle)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.polygon([(24, 16), (24, 48), (48, 32)], outline=fg_color, width=line_width)
img.save('uiassets/start.png')

# 6. info.png (Minimalist i symbol)
img = create_base_image()
draw = ImageDraw.Draw(img)
draw.ellipse([30, 14, 34, 18], fill=fg_color) # dot
draw.line([(32, 24), (32, 46)], fill=fg_color, width=line_width) # vertical line
draw.line([(28, 24), (32, 24)], fill=fg_color, width=line_width) # top hook
draw.line([(28, 46), (36, 46)], fill=fg_color, width=line_width) # bottom base
img.save('uiassets/info.png')

# 7. placeholder.png (Minimalist Dashed square / Plus sign)
img = create_base_image()
draw = ImageDraw.Draw(img)
# Draw dashed box manually
dash_len = 4
for i in range(12, 52, dash_len * 2):
    draw.line([(i, 12), (i + dash_len, 12)], fill=fg_color, width=line_width) # Top
    draw.line([(i, 52), (i + dash_len, 52)], fill=fg_color, width=line_width) # Bottom
    draw.line([(12, i), (12, i + dash_len)], fill=fg_color, width=line_width) # Left
    draw.line([(52, i), (52, i + dash_len)], fill=fg_color, width=line_width) # Right

draw.line([(32, 24), (32, 40)], fill=fg_color, width=line_width) # vertical plus
draw.line([(24, 32), (40, 32)], fill=fg_color, width=line_width) # horizontal plus
img.save('uiassets/placeholder.png')

print("Icons generated successfully with new requirements.")

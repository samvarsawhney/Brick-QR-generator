import qrcode

url = input("Enter URL: ")

# Smallest possible QR code with standard quiet zone (border=1)
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    border=1
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("1")
w, h = img.size
print(f"Original QR (with quiet zone): {w}x{h} modules")

# Scale down by factor 10
scale = 10
small_img = img.resize((w // scale, h // scale), resample=0)
sw, sh = small_img.size
print(f"Scaled mosaic: {sw}x{sh} studs")

# Build LDraw lines
lines = [
    "0 FILE main.ldr",
    "0 Name: QR Mosaic (10:1)",
    "0 Author: auto",
    "0 !LDRAW_ORG Unofficial_Model",
    ""
]

part = "3024.dat"   # 1x1 plate
stud = 20           # LDU per stud

for y in range(sh):
    for x in range(sw):
        colour = "0" if small_img.getpixel((x, y)) == 0 else "15"
        lx = x * stud
        lz = (sh - 1 - y) * stud
        line = f"1 {colour} {lx} 0 {lz} 1 0 0 0 1 0 0 0 1 {part}"
        lines.append(line)

lines.append("0 NOFILE")

# Ask for filename
filename = input("Enter output file name (no extension): ").strip()
if not filename:
    filename = "qr_mosaic"
filename = filename + ".ldr"

with open(filename, "w") as f:
    f.write("\n".join(lines))
print(f"Created {filename} – import into Studio")

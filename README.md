# Brick-QR-Generator

Generate an `.ldr` file containing a LEGO® brick QR code for any URL. The generated file can be opened and edited in BrickLink Studio.

## Installation

1. Download `QR.py` from this repository.

2. Install the required Python packages:

   ```bash
   pip install ldraw pillow
   ```

3. Download and install BrickLink Studio from:
   https://www.bricklink.com/v3/studio/download.page

## Usage

1. Run the generator:

   ```bash
   python3 QR.py
   ```

2. When prompted, enter the URL you want to encode as a QR code.

3. Enter an output filename (without the `.ldr` extension).

4. The script will generate an `.ldr` file containing the LEGO brick QR code.

5. Open the generated `.ldr` file in BrickLink Studio to view, edit, or export the model.

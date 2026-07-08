import shutil
import os

source_images = [
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\joinery_custom_closet_1783492674421.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\joinery_kitchen_cabinets_1783492701763.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\joinery_wood_paneling_1783492714157.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\joinery_custom_doors_1783492724435.png"
]

dest_dir = r"d:\MOSTECH\Wadi-Al-Manar-main\media"

dest_names = [
    "joinery_closet.png",
    "joinery_kitchen.png",
    "joinery_paneling.png",
    "joinery_doors.png"
]

for src, dest_name in zip(source_images, dest_names):
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(src, dest_path)
    print(f"Copied {src} to {dest_path}")

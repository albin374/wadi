import shutil
import os

source_images = [
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\civil_interior_concrete_1783493692686.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\civil_interior_structure_1783493721193.png"
]

dest_dir = r"d:\MOSTECH\Wadi-Al-Manar-main\media"

dest_names = [
    "civil_interior_1.png",
    "civil_interior_2.png"
]

for src, dest_name in zip(source_images, dest_names):
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(src, dest_path)
    print(f"Copied {src} to {dest_path}")

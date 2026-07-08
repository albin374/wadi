import shutil
import os

source_images = [
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\civil_commercial_construction_1783493493768.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\civil_structural_foundation_1783493505619.png"
]

dest_dir = r"d:\MOSTECH\Wadi-Al-Manar-main\media"

dest_names = [
    "civil_commercial.png",
    "civil_structural.png"
]

for src, dest_name in zip(source_images, dest_names):
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(src, dest_path)
    print(f"Copied {src} to {dest_path}")

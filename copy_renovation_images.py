import shutil
import os

source_images = [
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\renovation_villa_modern_1783492488004.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\renovation_bathroom_luxury_1783492500967.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\renovation_office_corporate_1783492522335.png"
]

dest_dir = r"d:\MOSTECH\Wadi-Al-Manar-main\media"

dest_names = [
    "renovation_villa.png",
    "renovation_bathroom.png",
    "renovation_office.png"
]

for src, dest_name in zip(source_images, dest_names):
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(src, dest_path)
    print(f"Copied {src} to {dest_path}")

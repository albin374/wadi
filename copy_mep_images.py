import shutil
import os

source_images = [
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\mep_mechanical_1783493898540.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\mep_electrical_1783493914103.png",
    r"C:\Users\albin\.gemini\antigravity\brain\74d49e6a-9db8-43d8-afb8-8efd6cc0dcab\mep_plumbing_1783493925401.png"
]

dest_dir = r"d:\MOSTECH\Wadi-Al-Manar-main\media"

dest_names = [
    "mep_performance.png",
    "mep_reliability.png",
    "mep_sustainability.png"
]

for src, dest_name in zip(source_images, dest_names):
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copy2(src, dest_path)
    print(f"Copied {src} to {dest_path}")

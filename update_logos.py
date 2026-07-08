import os
import glob

html_files = glob.glob('d:/MOSTECH/Wadi-Al-Manar-main/*.html')
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'media/WAM LOGO-02.png' in content:
        new_content = content.replace('media/WAM LOGO-02.png', 'media/WAM_LOGO_no_background.png')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

print("Done updating logos.")

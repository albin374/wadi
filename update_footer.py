import os
import glob
import re

html_files = glob.glob('d:/MOSTECH/Wadi-Al-Manar-main/*.html')

pattern = re.compile(r'(<div class="f-links">\s*<h4>Services</h4>\s*<ul>).*?(</ul>\s*</div>)', re.DOTALL)

new_list = """
                        <li><a href="design.html">Design</a></li>
                        <li><a href="renovations.html">Renovations</a></li>
                        <li><a href="joinery-works.html">Joinery Works</a></li>
                        <li><a href="services.html">MEP Services</a></li>
                        <li><a href="services.html" style="color: #F97316; font-weight: 600;">More Services &rarr;</a></li>
                    """

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = pattern.subn(r'\1' + new_list + r'\2', content)
    
    if count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path}")

print("Done updating footer services.")

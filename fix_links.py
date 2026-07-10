import glob
import os

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace social links
    content = content.replace('href="#" aria-label="Facebook"', 'href="https://facebook.com/wadialmanar" target="_blank" aria-label="Facebook"')
    content = content.replace('href="#" aria-label="Twitter"', 'href="https://twitter.com/wadialmanar" target="_blank" aria-label="Twitter"')
    content = content.replace('href="#" aria-label="Instagram"', 'href="https://instagram.com/wadialmanar" target="_blank" aria-label="Instagram"')
    content = content.replace('href="#" aria-label="LinkedIn"', 'href="https://linkedin.com/company/wadialmanar" target="_blank" aria-label="LinkedIn"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")

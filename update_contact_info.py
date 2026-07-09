import glob, sys, re

html_files = glob.glob('*.html')

new_contact = '''<div class="f-contact-info" style="color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                        <p style="margin-bottom: 0.5rem;">📍 Umm ramool, Building No 32, Warehouse No 9, Dubai UAE</p>
                        <p style="margin-bottom: 0.5rem;">📞 +971 56 424 4083</p>
                        <p style="margin-bottom: 0.5rem;">📞 +971 52 795 0408</p>
                        <p style="margin-bottom: 0.5rem;">📞 04 257 8976</p>
                        <p style="margin-bottom: 0.5rem;">✉️ info@wadialmanar.com</p>
                        <p>🌐 wadialmanar.com</p>
                    </div>'''

pattern = re.compile(r'<div class="f-contact-info".*?</div>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="f-contact-info"' in content:
        content, count = pattern.subn(new_contact, content)
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print('Updated ' + file)

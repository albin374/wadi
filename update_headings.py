import re
import os

pages = [
    'renovations.html',
    'fit-out-works.html',
    'ac-works.html',
    'painting-works.html',
    'gypsum-works.html',
    'flooring-works.html',
    'civil.html',
    'design.html'
]

for page in pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We look for the main h1. It usually looks like <h1 class="... text-[#111] ..."> or similar.
        # Since the classes can vary, let's use a more robust regex that finds the first h1 and changes its color class,
        # or adds text-[#F97316] if not present.
        
        def replace_h1(match):
            h1_tag = match.group(0)
            # Remove existing text color classes
            h1_tag = re.sub(r'text-\[#111\]', '', h1_tag)
            h1_tag = re.sub(r'text-brandDark', '', h1_tag)
            h1_tag = re.sub(r'text-gray-900', '', h1_tag)
            h1_tag = re.sub(r'text-brand-black', '', h1_tag)
            
            # Add text-[#F97316]
            h1_tag = h1_tag.replace('class="', 'class="text-[#F97316] ')
            # Clean up double spaces
            h1_tag = re.sub(r'\s+', ' ', h1_tag)
            return h1_tag

        # Find the first h1
        new_content = re.sub(r'<h1[^>]*>', replace_h1, content, count=1)
        
        if new_content != content:
            with open(page, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {page}")
        else:
            print(f"No changes made to {page}")
    else:
        print(f"{page} not found.")

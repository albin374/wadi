import os

css_addition = """
/* Specific override for pages that require dark text on the initial transparent navbar */
.premium-nav.nav-dark-text .nav-links a {
    color: #111111;
}
"""

# Append to style.css
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_addition)

service_pages = [
    'civil.html',
    'design.html',
    'fit-out-works.html',
    'renovations.html',
    'joinery-works.html',
    'painting-works.html',
    'electrical-works.html',
    'ac-works.html',
    'flooring-works.html',
    'gypsum-works.html'
]

for page in service_pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the header class
        if '<header class="navbar premium-nav">' in content:
            new_content = content.replace('<header class="navbar premium-nav">', '<header class="navbar premium-nav nav-dark-text">')
            with open(page, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {page}")
        else:
            print(f"Header class not found in exactly the expected format in {page}")
    else:
        print(f"File not found: {page}")

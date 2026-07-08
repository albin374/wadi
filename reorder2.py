import re

def reorder_html_blocks(file_path, wrapper_pattern, block_pattern, order):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    wrapper_match = re.search(wrapper_pattern, content, re.DOTALL)
    if not wrapper_match:
        print(f"Wrapper not found in {file_path}")
        return

    wrapper_content = wrapper_match.group(1)
    blocks = re.findall(block_pattern, wrapper_content, re.DOTALL)
    
    block_dict = {}
    for b in blocks:
        title_match = re.search(r'<h3>(.*?)</h3>', b)
        if title_match:
            normalized_title = title_match.group(1).lower().strip()
            block_dict[normalized_title] = b
            print(f"Found block: {normalized_title}")

    new_blocks = []
    for target in order:
        target_lower = target.lower()
        matched_key = None
        for key in list(block_dict.keys()):
            if target_lower in key or key in target_lower:
                matched_key = key
                break
        
        if matched_key:
            new_blocks.append(block_dict[matched_key])
            del block_dict[matched_key]
        else:
            print(f"Could not match target: {target}")

    new_blocks.extend(block_dict.values())
    new_wrapper_content = "\n\n            ".join(new_blocks)
    new_content = content.replace(wrapper_content, new_wrapper_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file_path}")

order = ['Joinery', 'MEP', 'Design', 'Civil', 'Renovations', 'IT', 'AC', 'Painting', 'Gypsum', 'Floor and wall']

reorder_html_blocks(
    'services.html',
    r'<div class="projects-grid">\s*(<!-- Card .*?-->.*?)\s*</div>\s*</section>',
    r'<!-- Card [^-]*?-->\s*<div class="project-card">.*?</div>\s*</div>',
    order
)

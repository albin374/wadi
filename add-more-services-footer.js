const fs = require('fs');
const path = require('path');

const directory = __dirname;
const htmlFiles = fs.readdirSync(directory).filter(file => file.endsWith('.html'));

const replacementHTML = `<ul>
                        <li><a href="painting-works.html">Painting Works</a></li>
                        <li><a href="electrical-works.html">Electrical Works</a></li>
                        <li><a href="fit-out-works.html">IT Solutions</a></li>
                        <li><a href="renovations.html">Renovations</a></li>
                        <li><a href="services.html" style="color: #F97316; font-weight: 600;">More Services &rarr;</a></li>
                    </ul>`;

htmlFiles.forEach(file => {
    const filePath = path.join(directory, file);
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Target the Services ul in the footer by matching <h4>Services</h4>
    const searchRegex = /(<h4>Services<\/h4>\s*)<ul[^>]*>[\s\S]*?(?:<\/ul>)/g;
    
    if (searchRegex.test(content)) {
        content = content.replace(searchRegex, `$1${replacementHTML}`);
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Added 'More Services' link to footer in ${file}`);
    }
});

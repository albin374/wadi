import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_str = '''                <p style="margin-bottom: 1rem; text-align: justify;">We Wadi AL Manar your one-stop partner for maintenance, construction, and interior fit-out solutions. We deliver reliable, high-quality services across residential, commercial, and industrial sectors. Our skilled team specializes in Joinery, MEP, IT infrastructure, AC works, Painting and General maintenance and more. Every project is crafted to enhance your property's functionality, safety, and appearance with excellence guaranteed.</p>
                <p style="margin-bottom: 1rem; text-align: justify;">We specialize in premium residential fit-out solutions that redefine modern living. We combine innovative design, superior craftsmanship, and meticulous attention to detail with seamless functionality.</p>
                <p style="margin-bottom: 1rem; text-align: justify;">Our team possesses a deep understanding of design, materials, and craftsmanship, guided by a holistic approach to interior fit-outs. From thoughtful space planning to custom finishes, every detail is carefully curated to reflect your unique lifestyle and personal taste.</p>
                <p style="margin-bottom: 2rem; text-align: justify;">At the heart of everything we do is a commitment to seamless functionality and bespoke elegance, because your home should be a true reflection of you.</p>'''

pattern = re.compile(r'                <h2>Your Trusted Partner.*?</div>', re.DOTALL)
text = pattern.sub(new_str, text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

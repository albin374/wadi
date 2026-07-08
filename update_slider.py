import sys

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace <head> to add swiper css
if 'swiper-bundle.min.css' not in content:
    content = content.replace("</head>", '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>')

# Wrap services in swiper
content = content.replace('<div class="services-grid-large">', '<div class="swiper services-swiper">\n                <div class="swiper-wrapper">')

# Add swiper-slide to service-card-luxury group
content = content.replace('<div class="service-card-luxury group">', '<div class="swiper-slide service-card-luxury group">')

old_end = """                </div>
            </div>
        </div>
    </section>"""

new_end = """                </div>
                </div>
                <!-- Add Pagination -->
                <div class="swiper-pagination"></div>
                <!-- Add Navigation -->
                <div class="swiper-button-next"></div>
                <div class="swiper-button-prev"></div>
            </div>
        </div>
    </section>"""

# Find the specific block for services closing
services_end_idx = content.find(old_end, content.find('id="services"'))
if services_end_idx != -1:
    content = content[:services_end_idx] + new_end + content[services_end_idx + len(old_end):]

# Add Swiper JS script at the end before </body>
if 'swiper-bundle.min.js' not in content:
    js_code = """
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            var swiper = new Swiper(".services-swiper", {
                slidesPerView: 1,
                spaceBetween: 30,
                loop: true,
                centeredSlides: true,
                autoplay: {
                    delay: 2500,
                    disableOnInteraction: false,
                },
                pagination: {
                    el: ".swiper-pagination",
                    clickable: true,
                },
                navigation: {
                    nextEl: ".swiper-button-next",
                    prevEl: ".swiper-button-prev",
                },
                breakpoints: {
                    768: { slidesPerView: 2 },
                    1024: { slidesPerView: 3 },
                }
            });
        });
    </script>
</body>"""
    content = content.replace("</body>", js_code)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

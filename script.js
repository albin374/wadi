document.addEventListener('DOMContentLoaded', () => {
    // Hero slideshow logic
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length > 0) {
        let currentSlide = 0;

        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 5000); // Change slide every 5 seconds
    }

    // Hamburger Menu
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }
    // Mobile Dropdown Toggle
    const dropdowns = document.querySelectorAll('.nav-dropdown');
    dropdowns.forEach(dropdown => {
        const toggleBtn = dropdown.querySelector('.mobile-toggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropdown.classList.toggle('open');
                if (dropdown.classList.contains('open')) {
                    toggleBtn.textContent = '▲';
                } else {
                    toggleBtn.textContent = '▼';
                }
            });
        }
    });

    // Sticky Navbar on Scroll
    const navbar = document.querySelector('.premium-nav');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                navbar.classList.add('nav-scrolled');
            } else {
                navbar.classList.remove('nav-scrolled');
            }
        });
    }
    // Project Filtering Logic
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    if (filterButtons.length > 0 && projectCards.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active button styling
                filterButtons.forEach(b => {
                    b.classList.remove('bg-primary', 'text-white');
                    b.classList.add('bg-white', 'text-secondary');
                });
                btn.classList.remove('bg-white', 'text-secondary');
                btn.classList.add('bg-primary', 'text-white');

                const filter = btn.getAttribute('data-filter');

                projectCards.forEach(card => {
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });

        // Trigger 'All Projects' filter on page load to ensure images render
        const allProjectsBtn = document.querySelector('.filter-btn[data-filter="all"]');
        if (allProjectsBtn) {
            allProjectsBtn.click();
        }
    }
});


// Brochure Modal Logic
function openBrochureModal(e) {
    if (e) e.preventDefault();
    const modal = document.getElementById('brochureModal');
    if (modal) {
        modal.classList.add('active');
        modal.style.opacity = '1';
        modal.style.visibility = 'visible';
        modal.style.zIndex = '999999';
    }
}

function closeBrochureModal() {
    const modal = document.getElementById('brochureModal');
    if (modal) {
        modal.classList.remove('active');
        modal.style.opacity = '0';
        modal.style.visibility = 'hidden';
    }
}

function handleBrochureDownload(e) {
    e.preventDefault();
    const name = document.getElementById('brochureName').value;
    const email = document.getElementById('brochureEmail').value;
    const btn = e.target.querySelector('button[type="submit"]');

    if (name && email) {
        const originalText = btn.innerText;
        btn.innerText = 'Sending...';
        btn.disabled = true;

        // Initialize EmailJS with your Public Key
        emailjs.init("18Zg9bhfs4wiSsBrP"); // Replace with your actual Public Key from EmailJS

        // Prepare template parameters
        const templateParams = {
            from_name: name,
            from_email: email,
            to_email: 'wadialmanarsales@gmail.com',
            message: 'Brochure Download Request'
        };

        // Send email using EmailJS
        emailjs.send(
            'service_dsoo5hj', // Replace with your EmailJS Service ID
            'template_gje4pga', // Replace with your EmailJS Template ID
            templateParams
        ).then(function (response) {
            console.log('SUCCESS!', response.status, response.text);

            // Trigger download
            const link = document.createElement('a');
            link.href = 'media/WADI AL MANAR - BROCHURE.pdf';
            link.download = 'WADI AL MANAR - BROCHURE.pdf';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

            // Close modal and reset form
            closeBrochureModal();
            e.target.reset();

            // Show success alert
            setTimeout(() => alert("Brochure download started and details sent successfully!"), 500);
        }, function (error) {
            console.log('FAILED...', error);
            alert("Failed to send details. However, your download will start now.");

            // Trigger download even if email fails
            const link = document.createElement('a');
            link.href = 'media/WADI AL MANAR - BROCHURE.pdf';
            link.download = 'WADI AL MANAR - BROCHURE.pdf';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

            closeBrochureModal();
            e.target.reset();
        }).finally(() => {
            btn.innerText = originalText;
            btn.disabled = false;
        });
    }
}

// Contact Form Submit Logic
function handleContactSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('contactName').value;
    const email = document.getElementById('contactEmail').value;
    const phone = document.getElementById('contactPhone').value;
    const service = document.getElementById('contactService').value;
    const brief = document.getElementById('contactBrief').value;

    const btn = document.getElementById('contactSubmitBtn');

    if (name && email && phone && service && brief) {
        const originalText = btn.innerHTML;
        btn.innerHTML = 'Sending...';
        btn.disabled = true;

        // Initialize EmailJS with your Public Key
        emailjs.init("18Zg9bhfs4wiSsBrP"); // Replace with your actual Public Key from EmailJS

        // Prepare detailed template parameters for the new Contact Template
        const templateParams = {
            from_name: name,
            from_email: email,
            phone_number: phone,
            service_category: service,
            project_brief: brief,
            to_email: 'wadialmanarsales@gmail.com'
        };

        // Send email using EmailJS
        emailjs.send(
            'service_dsoo5hj', // Your existing EmailJS Service ID
            'template_po9uvbi', // Replace with your NEW EmailJS Template ID for the contact form
            templateParams
        ).then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
            alert("Thank you! Your project inquiry has been sent successfully. Our team will reach out within 4 business hours.");
            e.target.reset();
        }, function (error) {
            console.log('FAILED...', error);
            alert("Failed to send your inquiry. Please try again or contact us directly at info@wadialmanar.com.");
        }).finally(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
        });
    }
}

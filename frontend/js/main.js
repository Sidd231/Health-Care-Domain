/**
 * ALIGN HEALTH & CLINICAL DIAGNOSTICS
 * Main Application Interactive Scripts
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollAnimations();
  initStickyNavbar();
  initMobileNav();
  initTestimonials();
});

/* -------------------------------------------------------------------------
   1. SCROLL-TRIGGERED FADE-IN ANIMATIONS
   ------------------------------------------------------------------------- */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.reveal-on-scroll');
  if (!elements.length) return;

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          obs.unobserve(entry.target);
        }
      });
    },
    {
      root: null,
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px',
    }
  );

  elements.forEach((el) => observer.observe(el));
}

/* -------------------------------------------------------------------------
   2. STICKY NAVBAR SHADOW & SCROLL EFFECT
   ------------------------------------------------------------------------- */
function initStickyNavbar() {
  const header = document.getElementById('siteHeader');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* -------------------------------------------------------------------------
   3. MOBILE MENU TOGGLE
   ------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobileNavToggle');
  const drawer = document.getElementById('mobileMenuDrawer');
  if (!toggleBtn || !drawer) return;

  toggleBtn.addEventListener('click', () => {
    drawer.classList.toggle('active');
  });

  // Close drawer on click of any link inside
  drawer.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      drawer.classList.remove('active');
    });
  });
}

/* -------------------------------------------------------------------------
   4. CARD DETAILS EXPANSION DRAWER
   ------------------------------------------------------------------------- */
function toggleCardDetails(btn) {
  const content = btn.parentElement.querySelector('.card-expanded-content');
  if (!content) return;

  const isExpanded = content.classList.contains('active');
  if (isExpanded) {
    content.classList.remove('active');
    btn.children[1].textContent = '+';
  } else {
    content.classList.add('active');
    btn.children[1].textContent = '−';
  }
}

/* -------------------------------------------------------------------------
   5. TESTIMONIALS SLIDER
   ------------------------------------------------------------------------- */
const testimonials = [
  {
    quote: "Align Health changed how I think about my cardiovascular health. Instead of generic advice, their risk evaluation pinpointed exactly what I needed to change in my daily routine.",
    author: "Michael R., 54 · Denver, CO · Preventative Cardiology Patient"
  },
  {
    quote: "The diabetic readmission prediction model allowed our care team to establish post-discharge home visits right on time. My recovery was smoother than ever.",
    author: "Eleanor T., 68 · Lakewood, CO · Endocrinology Patient"
  },
  {
    quote: "Having algorithms that explain the 'why' behind metabolic recommendations makes adherence so much more natural. Dr. Kim and her diagnostic suite are exceptional.",
    author: "David H., 46 · Boulder, CO · Executive Wellness Cohort"
  }
];

let activeTestimonialIndex = 0;
let testimonialInterval = null;

function initTestimonials() {
  const textEl = document.getElementById('testimonialText');
  if (!textEl) return;

  // Auto rotate every 7 seconds
  testimonialInterval = setInterval(() => {
    activeTestimonialIndex = (activeTestimonialIndex + 1) % testimonials.length;
    renderTestimonial();
  }, 7000);
}

function setTestimonial(index) {
  activeTestimonialIndex = index;
  renderTestimonial();
  // Reset auto-timer on manual interaction
  if (testimonialInterval) {
    clearInterval(testimonialInterval);
    testimonialInterval = setInterval(() => {
      activeTestimonialIndex = (activeTestimonialIndex + 1) % testimonials.length;
      renderTestimonial();
    }, 7000);
  }
}

function renderTestimonial() {
  const textEl = document.getElementById('testimonialText');
  const authorEl = document.getElementById('testimonialAuthor');
  const dots = document.querySelectorAll('.testimonial-dot');

  if (!textEl || !authorEl) return;

  textEl.style.opacity = '0';
  authorEl.style.opacity = '0';

  setTimeout(() => {
    textEl.textContent = testimonials[activeTestimonialIndex].quote;
    authorEl.textContent = testimonials[activeTestimonialIndex].author;
    textEl.style.opacity = '1';
    authorEl.style.opacity = '1';

    dots.forEach((dot, idx) => {
      dot.classList.toggle('active', idx === activeTestimonialIndex);
    });
  }, 200);
}

/* -------------------------------------------------------------------------
   6. SIMULATED PATIENT REGISTRY LOOKUP
   ------------------------------------------------------------------------- */
const demoPatients = [
  {
    id: "P-1042",
    name: "James Miller",
    age: 52,
    gender: "Male",
    lastVisit: "October 14, 2026",
    cardioRisk: "Moderate (24.8%)",
    status: "Active Monitoring",
    notes: "Elevated systolic BP (134 mmHg); compliant with low-sodium dietary plan."
  },
  {
    id: "P-2890",
    name: "Sarah Jenkins",
    age: 64,
    gender: "Female",
    lastVisit: "September 28, 2026",
    cardioRisk: "Elevated (68.4%)",
    status: "Care Coordination Enrolled",
    notes: "Diagnosed T2 Diabetes; Metformin titration steady. Lipid panel re-test ordered."
  },
  {
    id: "P-8831",
    name: "Robert Chen",
    age: 41,
    gender: "Male",
    lastVisit: "August 19, 2026",
    cardioRisk: "Optimal (8.2%)",
    status: "Annual Routine Screening",
    notes: "All vitals in prime athletic range; 180 min weekly aerobic conditioning."
  }
];

function searchPatientRegistry() {
  const query = (document.getElementById('registryInput')?.value || '').trim().toLowerCase();
  const resultCard = document.getElementById('registryResult');
  if (!resultCard) return;

  if (!query) {
    showToast("Please enter a patient ID or name to search.");
    return;
  }

  const match = demoPatients.find(p => 
    p.id.toLowerCase().includes(query) || 
    p.name.toLowerCase().includes(query)
  );

  if (match) {
    resultCard.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #DCE4E8; padding-bottom:0.75rem; margin-bottom:1rem;">
        <div>
          <h4 style="font-size:22px; font-family:'Cormorant Garamond', serif; margin:0; color:#1F3A4D;">${match.name}</h4>
          <span style="font-size:11px; color:#6C8291; text-transform:uppercase; letter-spacing:0.12em;">ID: ${match.id} &middot; ${match.age} yrs &middot; ${match.gender}</span>
        </div>
        <span class="badge-status" style="background-color:#EBF3F8; border-color:#7FB3D5;">${match.status}</span>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; font-size:13px; color:#334E61;">
        <div><strong>Last Clinical Visit:</strong> ${match.lastVisit}</div>
        <div><strong>Cardiovascular Stratification:</strong> ${match.cardioRisk}</div>
      </div>
      <div style="background-color:#F8F6F2; border:1px solid #DCE4E8; padding:0.85rem 1rem; margin-top:0.85rem; font-size:12.5px; color:#1F3A4D;">
        <strong>Clinical Chart Note:</strong> ${match.notes}
      </div>
      <div style="margin-top:1rem; display:flex; gap:10px;">
        <a href="heart.html" class="btn btn-primary" style="padding:8px 16px; font-size:10px;">Run Updated Heart Profiling</a>
        <a href="diabetes.html" class="btn btn-outline" style="padding:8px 16px; font-size:10px;">Run Readmission Model</a>
      </div>
    `;
    resultCard.classList.add('active');
    showToast(`Found registry chart for ${match.name}`);
  } else {
    resultCard.innerHTML = `
      <div style="padding:1rem; text-align:center; color:#6C8291;">
        <p style="font-size:14px; margin-bottom:6px;">No simulated patient found matching &ldquo;<strong>${query}</strong>&rdquo;.</p>
        <span style="font-size:12px;">Try searching <strong>P-1042</strong>, <strong>Sarah</strong>, or <strong>Robert</strong>.</span>
      </div>
    `;
    resultCard.classList.add('active');
  }
}

/* -------------------------------------------------------------------------
   7. FAQ TOGGLE
   ------------------------------------------------------------------------- */
function toggleFaq(item) {
  const detail = item.querySelector('.technique-detail');
  if (!detail) return;
  const isHidden = detail.style.display === 'none';
  detail.style.display = isHidden ? 'block' : 'none';
}

/* -------------------------------------------------------------------------
   8. TOAST NOTIFICATION UTILITY
   ------------------------------------------------------------------------- */
function showToast(message, duration = 3500) {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<span>ℹ️</span> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

// Global exposure for inline events
window.toggleCardDetails = toggleCardDetails;
window.setTestimonial = setTestimonial;
window.searchPatientRegistry = searchPatientRegistry;
window.toggleFaq = toggleFaq;
window.showToast = showToast;

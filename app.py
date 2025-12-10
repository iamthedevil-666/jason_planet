# app.py
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Jason's Planet — PC Workshop & Software Services",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------------
# CSS / Styling
# -------------------------
def local_css():
    st.markdown(
        """
        <style>
        /* Page background */
        .stApp {
            background: linear-gradient(180deg, #0f172a 0%, #071130 100%);
            color: #e6eef8;
        }
        /* Card style */
        .card {
            background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 4px 14px rgba(2,6,23,0.6);
        }
        .service-title {
            font-size: 18px;
            font-weight: 700;
            color: #fff;
        }
        .muted {
            color: #b8c6e5;
        }
        .big-cta {
            background: linear-gradient(90deg,#0ea5a6,#06b6d4);
            color: #021025;
            padding: 12px 20px;
            border-radius: 10px;
            font-weight: 700;
            text-decoration: none;
        }
        .feature-grid {
            display: flex;
            gap: 10px;
        }
        .footer {
            color: #9fb2d6;
            font-size: 14px;
            padding-top: 18px;
            padding-bottom: 18px;
        }
        /* Make header text nice on dark bg */
        .hero-title {
            font-size: 36px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 6px;
        }
        .hero-sub {
            color: #bcd6f5;
            font-size: 16px;
            margin-top: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

local_css()

# -------------------------
# Utility / Data
# -------------------------
COMPANY = {
    "name": "Jason's Planet",
    "tagline": " PC Workshop & Software Services",
    "phone": "+91 98765 43210",
    "email": "hello@jasonsplanet.tech",
    "address": "Unit 12, Techpark, Sector 42, Bengaluru, India",
    "hours": "Mon - Sat: 9:30 AM - 7:30 PM",
    "established": 2014,
}

# Simple image assets (Unsplash URLs) - safe public images for placeholder use
IMAGES = {
    "hero": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1600&q=80&auto=format&fit=crop",
    "repair": "https://images.unsplash.com/photo-1580894894517-9c4f4d4498d9?w=1200&q=80&auto=format&fit=crop",
    "service_software": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1200&q=80&auto=format&fit=crop",
    "team": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200&q=80&auto=format&fit=crop",
    "workbench": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?w=1200&q=80&auto=format&fit=crop",
    "customer": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1200&q=80&auto=format&fit=crop",
    "gallery_1": "https://images.unsplash.com/photo-1555617117-08a4d9b1f544?w=1200&q=80&auto=format&fit=crop",
    "gallery_2": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=1200&q=80&auto=format&fit=crop",
    "gallery_3": "https://images.unsplash.com/photo-1508057198894-247b23fe5ade?w=1200&q=80&auto=format&fit=crop",
}

SERVICES = [
    {
        "title": "Professional PC Repair",
        "desc": "Comprehensive diagnostics & hardware repair for desktops and laptops — motherboards, power supplies, cooling, and more.",
        "img": IMAGES["repair"],
        "price": "From ₹499",
    },
    {
        "title": "Custom PC Builds",
        "desc": "Performance-focused gaming rigs, content-creation workstations, and compact office PCs — custom picks, assembly & testing.",
        "img": IMAGES["workbench"],
        "price": "Quote-based",
    },
    {
        "title": "Software & OS Services",
        "desc": "OS installation, performance optimization, cleanup, driver updates, and reliable backup/restore solutions.",
        "img": IMAGES["service_software"],
        "price": "From ₹299",
    },
    {
        "title": "Data Recovery & Backup",
        "desc": "Secure data recovery from failing drives and guided backup strategies to prevent future data loss.",
        "img": IMAGES["gallery_1"],
        "price": "From ₹999",
    },
]

TEAM = [
    {"name": "Jason Verma", "role": "Founder & Lead Engineer", "bio": "20+ years in hardware repair and system architecture."},
    {"name": "Aisha Patel", "role": "Senior Software Engineer", "bio": "Specialist in system performance and software migrations."},
    {"name": "Rohan Gupta", "role": "Customer Success Lead", "bio": "Ensures fast, transparent service and warranty management."},
]

TESTIMONIALS = [
    {"name": "Suresh K.", "text": "My laptop recovered from a failing SSD — data intact. Superb service and clear explanation!"},
    {"name": "Priya R.", "text": "Custom gaming PC built and tuned perfectly. Runs cooler than expected."},
    {"name": "Kavita S.", "text": "Fast turnaround and honest pricing. Recommended for small businesses."}
]

FAQS = [
    {"q": "Do you offer on-site repairs?", "a": "Yes — we provide on-site diagnostics for businesses and premium customers. Charges may apply."},
    {"q": "How long does a typical repair take?", "a": "Minor fixes same-day; major repairs or parts replacement 1-5 business days."},
    {"q": "Do you offer warranty on repairs?", "a": "Yes. We provide a 30–180 day warranty depending on the service and component replaced."},
    {"q": "Can you build custom PCs for gaming?", "a": "Absolutely — we consult on parts, budget, and airflow, and perform full build/testing."}
]

# -------------------------
# Navigation
# -------------------------
def navigation():
    st.sidebar.image(IMAGES["hero"],  use_container_width=True)
    st.sidebar.markdown(f"## {COMPANY['name']}")
    st.sidebar.markdown(f"**{COMPANY['tagline']}**")
    page = st.sidebar.radio("Navigation", [
        "Home",
        "Services",
        
        "Team",
        "Pricing",
        "FAQ",
        "Testimonials",
        "Contact"
    ])
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"📞 {COMPANY['phone']}")
    st.sidebar.markdown(f"✉️ {COMPANY['email']}")
    st.sidebar.markdown(f"📍 {COMPANY['address']}")
    st.sidebar.markdown(f"⏰ {COMPANY['hours']}")
    st.sidebar.markdown("---")
    if st.sidebar.button("Request Call Back"):
        st.session_state.show_callback_modal = True
    return page

if "show_callback_modal" not in st.session_state:
    st.session_state.show_callback_modal = False

PAGE = navigation()

# -------------------------
# Hero / Home
# -------------------------
def show_hero():
    left, right = st.columns([2, 1])
    with left:
        st.markdown(
            f"""
            <div class="hero-title">{COMPANY['name']}</div>
            <div class="hero-sub">{COMPANY['tagline']} — Reliable repairs, brilliant software solutions.</div>
            <p class="muted">Established: {COMPANY['established']} • Trusted by thousands • Certified technicians</p>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.markdown(
            """
            <div class="card">
            <h4 style="margin:0px;">Why choose Jason's Planet?</h4>
            <ul class="muted" style="line-height:1.6;">
              <li>Fast turnaround & transparent pricing</li>
              <li>Genuine parts & skilled technicians</li>
              <li>On-site services for businesses</li>
              <li>Free diagnosis with repair</li>
            </ul>
            <div style="margin-top:10px;">
              
            </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.image(IMAGES["hero"], caption="Trusted workshop & experienced team",  use_container_width=True)

# -------------------------
# Services Page
# -------------------------
def show_services():
    st.markdown("## Our Services")
    st.markdown("We provide a full range of hardware and software services designed for home users, gamers, and businesses.")
    cols = st.columns(2)
    for i, svc in enumerate(SERVICES):
        col = cols[i % 2]
        with col:
            st.markdown(f"<div class='card'><img src='{svc['img']}' style='width:100%; border-radius:8px; margin-bottom:8px;'/>", unsafe_allow_html=True)
            st.markdown(f"<div class='service-title'>{svc['title']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='muted'>{svc['desc']}</div>", unsafe_allow_html=True)
            st.markdown(f"<b>{svc['price']}</b>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Popular Packages")
    st.info("Basic Tune-Up — Cleaning, software updates, malware scan — ₹799")
    st.info("Performance Boost — SSD upgrade suggestion and OS optimization — ₹1999")
    st.info("Business Care — On-site SLA & monthly maintenance plans — Contact us for pricing")

# -------------------------
# Gallery
# -------------------------
# -------------------------
# Team
# -------------------------
def show_team():
    st.markdown("## Meet the Team")
    st.markdown("Our team combines hardware expertise with software excellence.")
    cols = st.columns(len(TEAM))
    for i, member in enumerate(TEAM):
        with cols[i]:
            st.image(IMAGES["team"],  use_container_width=True)
            st.markdown(f"**{member['name']}**")
            st.markdown(f"*{member['role']}*")
            st.markdown(f"<div class='muted'>{member['bio']}</div>", unsafe_allow_html=True)

# -------------------------
# Pricing
# -------------------------
def show_pricing():
    st.markdown("## Pricing & Plans")
    st.markdown("Transparent pricing for common tasks. For full quotes, contact us or book a diagnostic.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h3>Basic</h3><p class='muted'>Cleaning & Tune-up</p><h2>₹799</h2><p>Ideal for home users</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>Pro</h3><p class='muted'>SSD upgrade & optimization</p><h2>₹1999</h2><p>Great for gamers & creators</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>Business</h3><p class='muted'>On-site SLA & monthly support</p><h2>Contact Us</h2><p>Custom pricing</p></div>", unsafe_allow_html=True)

# -------------------------
# FAQ
# -------------------------
def show_faq():
    st.markdown("## Frequently Asked Questions")
    for f in FAQS:
        with st.expander(f["q"]):
            st.write(f["a"])

# -------------------------
# Testimonials
# -------------------------
def show_testimonials():
    st.markdown("## What Our Customers Say")
    for t in TESTIMONIALS:
        st.markdown(f"> \"{t['text']}\"")
        st.markdown(f"**– {t['name']}**")
        st.markdown("---")

# -------------------------
# Contact Form
# -------------------------
def show_contact():
    st.markdown("## Contact & Bookings")
    st.markdown("Have a problem? Fill the form below and our support team will contact you within one business day.")
    with st.form("contact_form"):
        name = st.text_input("Full name", max_chars=100)
        email = st.text_input("Email address")
        phone = st.text_input("Phone number")
        service = st.selectbox("Service required", [s["title"] for s in SERVICES])
        message = st.text_area("Describe the issue or request", max_chars=1000)
        submitted = st.form_submit_button("Send Request")
        if submitted:
            # In a real site: integrate with an email service or CRM.
            # Here we record submission to session_state for demo & show success.
            if "submissions" not in st.session_state:
                st.session_state.submissions = []
            st.session_state.submissions.append({
                "time": datetime.now().isoformat(),
                "name": name,
                "email": email,
                "phone": phone,
                "service": service,
                "message": message
            })
            st.success("Thanks! Your request has been received. We will contact you shortly.")
    st.markdown("### Walk-in & Support")
    st.markdown(f"**Address:** {COMPANY['address']}")
    st.markdown(f"**Phone:** {COMPANY['phone']}  •  **Email:** {COMPANY['email']}")
    st.markdown("We also provide priority on-site service for businesses. Ask for Business Care plan.")

# -------------------------
# Footer
# -------------------------
def show_footer():
    st.markdown("---")
    st.markdown(
        f"""
        <div class="footer">
        © {datetime.now().year} {COMPANY['name']} — All rights reserved. &nbsp;&nbsp;|&nbsp;&nbsp;
        Designed for reliability • Made with care • <span class="muted">Privacy-focused</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------
# Page Router
# -------------------------
def run_app(page):
    if page == "Home":
        show_hero()
        st.markdown("---")
        #st.markdown("### Our Top Services")
        #st.write("Below are our main offerings:")
        #show_services()
    elif page == "Services":
        show_services()
    
    elif page == "Team":
        show_team()
    elif page == "Pricing":
        show_pricing()
    elif page == "FAQ":
        show_faq()
    elif page == "Testimonials":
        show_testimonials()
    elif page == "Contact":
        show_contact()
    else:
        st.write("Page not found")

    show_footer()

run_app(PAGE)

# -------------------------
# Callback modal (small simulation)
# -------------------------
if st.session_state.show_callback_modal:
    with st.modal("Request a Call Back"):
        st.write("Leave your number and we will call you within one business day.")
        cb_name = st.text_input("Name for callback")
        cb_phone = st.text_input("Phone Number")
        if st.button("Request Callback"):
            st.session_state.show_callback_modal = False
            st.success("Callback requested. We'll call you soon.")

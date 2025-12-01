import streamlit as st
import time
import base64
import pandas as pd
from datetime import datetime

# -----------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------
st.set_page_config(
    page_title="Jason's Planet",
    page_icon="🌍",
    layout="wide"
)

# -----------------------------------------------------------
# DARK THEME CUSTOM CSS
# -----------------------------------------------------------
def load_css():
    st.markdown("""
    <style>
        body, .stApp {
            background-color: #0f0f0f;
            color: #FFF;
            font-family: 'Segoe UI', sans-serif;
        }
        h1, h2, h3, h4 { color: #4db8ff; }
        
        .card {
            padding: 20px;
            border-radius: 15px;
            background: #1a1a1a;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4);
            margin-bottom: 20px;
        }

        .carousel-img {
            border-radius: 12px;
            width: 100%;
            height: 350px;
            object-fit: cover;
            box-shadow: 0 0 15px rgba(0,0,0,0.8);
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            color: #AAA;
            font-size: 14px;
        }
    </style>
    """, unsafe_allow_html=True)

load_css()

# -----------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "ℹ️ About Us", "🛠 Services", "🛒 Showroom", "📅 Appointments", "📞 Contact"]
)

# -----------------------------------------------------------
# IMAGE CAROUSEL FUNCTION
# -----------------------------------------------------------
# -----------------------------------------------------------
# IMAGE CAROUSEL (with embedded sample images)
# -----------------------------------------------------------
import base64

# 3 SAMPLE BASE64 IMAGES (royalty-free dark-tech images)
sample_img1 = "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80"
sample_img2 = "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80"
sample_img3 = "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80"

def img_to_base64_from_url(url):
    import requests
    from io import BytesIO
    response = requests.get(url)
    return base64.b64encode(response.content).decode()

carousel_base64_list = [
    img_to_base64_from_url(sample_img1),
    img_to_base64_from_url(sample_img2),
    img_to_base64_from_url(sample_img3)
]

def image_carousel():
    carousel_placeholder = st.empty()

    for img in carousel_base64_list:
        html = f"""
        <img src="data:image/jpeg;base64,{img}" class="carousel-img">
        """
        carousel_placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(2)


# -----------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------
if menu == "🏠 Home":
    st.title("🌍 Jason's Planet")
    st.subheader("The Ultimate Dark-Mode Hardware & Software Hub")

    st.write("### 🔥 Featured Highlights")
    image_carousel()

    st.write("")
    st.markdown("""
    <div class="card">
        <h3>Why Choose Jason's Planet?</h3>
        • Professional technicians  
        • Premium PC components  
        • Expert repairs  
        • Custom-built systems  
        • Genuine software solutions  
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------
# ABOUT US PAGE
# -----------------------------------------------------------
if menu == "ℹ️ About Us":
    st.title("ℹ️ About Jason’s Planet")
    
    st.markdown("""
    <div class="card">
        <h3>Who We Are</h3>
        Jason’s Planet is a premium PC hardware and software service centre with a showroom
        offering high-end products and expert technical solutions.
    </div>

    <div class="card">
        <h3>Our Mission</h3>
        To deliver world-class technology services to students, gamers, professionals,
        businesses and institutions.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------
# SERVICES PAGE
# -----------------------------------------------------------
if menu == "🛠 Services":
    st.title("🛠 Our Services")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>💻 Laptop Repair</h3>
            - Motherboard service  
            - Screen replacement  
            - Thermal cleaning  
            - Performance tuning  
        </div>

        <div class="card">
            <h3>🧰 Software Solutions</h3>
            - OS installation  
            - Antivirus & drivers  
            - Data recovery  
            - System optimization  
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🖥 Custom PC Builds</h3>
            - Gaming PCs  
            - Workstations  
            - Editing rigs  
            - RGB builds  
        </div>

        <div class="card">
            <h3>🏢 AMC & Corporate Services</h3>
            - Annual maintenance  
            - Full lab setup  
            - Institutional service  
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------
# SHOWROOM PAGE
# -----------------------------------------------------------
if menu == "🛒 Showroom":
    st.title("🛒 Showroom Products")

    st.markdown("""
    <div class="card">
        <h3>🔥 Components for Sale</h3>
        - GPUs (NVIDIA / AMD)  
        - CPUs (Intel / Ryzen)  
        - SSDs & HDDs  
        - RAM (DDR4/DDR5)  
        - Gaming Cabinets  
        - Power Supplies  
    </div>

    <div class="card">
        <h3>🎧 Accessories</h3>
        - Keyboards  
        - Headsets  
        - Webcams  
        - Mouse & Pads  
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------
# APPOINTMENTS PAGE
# -----------------------------------------------------------
if menu == "📅 Appointments":
    st.title("📅 Book an Appointment")

    st.write("Fill the form below to schedule your service visit:")

    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    email = st.text_input("Email Address")
    date = st.date_input("Preferred Date")
    time_slot = st.time_input("Preferred Time")
    service = st.selectbox("Service Needed", [
        "Laptop Repair",
        "PC Build Consultation",
        "Software Fix",
        "Showroom Visit",
        "Other"
    ])

    if st.button("Book Appointment"):
        if name and phone:
            df = pd.DataFrame([[name, phone, email, str(date), str(time_slot), service]],
                              columns=["Name", "Phone", "Email", "Date", "Time", "Service"])
            
            try:
                df_existing = pd.read_csv("appointments.csv")
                df_all = pd.concat([df_existing, df], ignore_index=True)
            except:
                df_all = df

            df_all.to_csv("appointments.csv", index=False)
            st.success("Your appointment has been booked successfully!")
        else:
            st.error("Name and phone number are required.")

# -----------------------------------------------------------
# CONTACT PAGE
# -----------------------------------------------------------
if menu == "📞 Contact":
    st.title("📞 Contact & Support")

    st.markdown("""
    <div class="card">
        <h3>📍 Address</h3>
        Jason’s Planet, Main Road, Tamil Nadu, India  
        
        <h3>📞 Phone</h3>
        +91 98765 43210  

        <h3>📧 Email</h3>
        support@jasonsplanet.com
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------
# FOOTER
# -----------------------------------------------------------
st.markdown("""
<div class="footer">
    © 2025 Jason's Planet — Premium Hardware & Software Solutions.
</div>
""", unsafe_allow_html=True)

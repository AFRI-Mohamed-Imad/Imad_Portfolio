import streamlit as st
import base64

def load_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def nav_bar():
    # List of pages
    pages = ["Home", "Experience", "Projects"]

    # Initialize session state for active page
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Home"

    # Load image
    image_data = load_image_as_base64("static/images/profile.jpg")

    # Create the navbar HTML
    st.markdown(
        f"""
        <style>
        .navbar {{
            background: linear-gradient(135deg, #49117C, #6A19B5);
            padding: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}
        .logo {{
            display: flex;
            align-items: center;
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
        }}
        .logo img {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            margin-right: 0.8rem;
        }}
        div[data-testid="stHorizontalBlock"] {{
            position: absolute;
            right: 1rem;
            top: 0.5rem;
            width: auto;
            background: transparent;
            display: flex;
            align-items: center;
            white-space: nowrap;
        }}
        div[data-testid="stHorizontalBlock"] > div {{
            min-width: auto !important;
            width: auto !important;
            margin-right: 0.5rem;
            flex: 0 0 auto;
        }}
        div[data-testid="stHorizontalBlock"] button {{
            background: transparent;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            margin: 0;
            border-radius: 5px;
            white-space: nowrap;
            min-width: fit-content;
            width: auto !important;
        }}
        div[data-testid="stHorizontalBlock"] button:hover {{
            background: #8A2BE2;
        }}
        button[kind="secondary"] {{
            background: {{'#A963EA' if st.session_state.active_page == page else 'transparent'}} !important;
        }}
        div[data-testid="column"] {{
            padding: 0 !important;
        }}
        </style>
        <div class="navbar">
            <div class="logo">
                <img src="data:image/jpg;base64,{image_data}" alt="Profile"/>
                Imad's Portfolio
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Create horizontal layout for buttons with auto-width columns
    cols = st.columns([0.1, 0.1, 0.1])
    
    with cols[0]:
        if st.button("Home", type="secondary"):
            st.session_state.active_page = "Home"
            st.rerun()
            
    with cols[1]:
        if st.button("Experience", type="secondary"):
            st.session_state.active_page = "Experience"
            st.rerun()
            
    with cols[2]:
        if st.button("Projects", type="secondary"):
            st.session_state.active_page = "Projects"
            st.rerun()
import streamlit as st
from controllers.navbar_controller import nav_bar
from controllers.profile_controller import get_profile
from controllers.skills_controller import get_skills
from controllers.experience_controller import get_experience
from controllers.projects_controller import get_projects
from views.about_me import about_me
from views.skills import skills
from views.contact import contact
from views.experience import experience
from views.projects import projects

st.set_page_config(layout="wide", page_title="Imad's Portfolio", page_icon="🧑‍💻")

# Initialize session state for the active page
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# Navigation logic
def render_page():
    if st.session_state.active_page == "Home":
        # Render Home: About Me, Skills, and Contact
        about_me(get_profile())
        st.markdown("---")
        skills(get_skills())
        st.markdown("---")
        contact()
    elif st.session_state.active_page == "Experience":
        # Render Experience page
        experience(get_experience())
    elif st.session_state.active_page == "Projects":
        # Render Projects page
        projects(get_projects())

# Render Navbar and active page
nav_bar()

render_page()

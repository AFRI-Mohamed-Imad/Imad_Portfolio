import streamlit as st

def contact():
    st.markdown(
        """
        <style>
        .contact-section {
            padding: 50px 20px;
            text-align: center;
            background: linear-gradient(135deg, #6A19B5, #C89BF1);
            color: white;
        }
        .contact-section h2 {
            margin-bottom: 20px;
        }
        .contact-section p {
            margin: 10px 0;
        }
        </style>
        <div class="contact-section" id="contact">
            <h2>Contact Me</h2>
            <p>Phone ✆: <a href="tel:+33781178404" style="color: #FFD700;">+33 7 81 17 84 04</a></p>
            <p>Email ✉: <a href="mailto:afriimad7551@gmail.com" style="color: #FFD700;">afriimad7551@gmail.com</a></p>
            <p>LinkedIn 🌐: <a href="https://www.linkedin.com/in/imad-afri-880262159/" style="color: #FFD700;">Imad Afri</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

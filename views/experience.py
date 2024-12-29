import streamlit as st

def experience(experience_data):
    st.markdown(
        """
        <style>
        .experience-section {
            padding: 50px 20px;
            text-align: center;
        }
        .experience-section h2 {
            color: #6A19B5;
            margin-bottom: 30px;
        }
        .experience-card {
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: left;
        }
        .experience-card h3 {
            margin: 0;
            font-size: 1.2rem;
            padding: 8px 0; /* Reduce padding */
            background-color: #6A19B5; /* Violet bar color */
            border-radius: 3px;
            margin-bottom: 10px;
            text-align: center;
            width: fit-content;
            margin-left: auto;
            margin-right: auto;
        }
        .experience-card ul {
            list-style-type: disc;
            padding-left: 20px;
            text-align: justify;
        }
        .experience-card ul li {
            margin-bottom: 8px;
        }
        </style>
        <div id="experience" class="experience-section">
            <h2>Professional Experience 💼</h2>
        """,
        unsafe_allow_html=True,
    )

    for exp in experience_data:
        st.markdown(
            f"""
            <div class="experience-card">
                <h3>{exp['title']}</h3>
                <ul>
            """,
            unsafe_allow_html=True,
        )
        for detail in exp["details"]:
            st.markdown(f"<li>{detail}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

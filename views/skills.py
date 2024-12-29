import streamlit as st

def skills(skill_list):
    # Create the skills section
    skill_cards = ''.join(
        [f'<div class="skill-card">{skill}</div>' for skill in skill_list]
    )
    
    st.markdown(
        f"""
        <style>
        .skills-section {{
            padding: 50px 20px;
            text-align: center;
        }}
        .skills-section h2 {{
            color: #6A19B5;
            margin-bottom: 30px;
            font-size: 2rem;
            font-weight: bold;
        }}
        .skills-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center; /* Center the cards */
            gap: 15px; /* Space between cards */
        }}
        .skill-card {{
            background: linear-gradient(135deg, #C89BF1, #A963EA);
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: inline-block;
        }}
        .skill-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }}
        </style>
        <div class="skills-section">
            <h2>Technical Skills 🚀</h2>
            <div class="skills-grid">
                {skill_cards}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

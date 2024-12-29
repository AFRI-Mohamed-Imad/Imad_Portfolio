import streamlit as st

def projects(project_data):
    # Generate the project cards dynamically
    project_cards = ''.join([
        f"""
        <div class="project-card">
            <h3>{project['name']}</h3>
            <p>{project['description']}</p>
        </div>
        """ for project in project_data
    ])

    # Single `st.markdown` for the entire section
    st.markdown(
        f"""
        <style>
        .projects-section {{
            padding: 50px 20px;
            text-align: center;
        }}
        .projects-section h2 {{
            color: #6A19B5;
            margin-bottom: 30px;
            font-size: 2rem;
            font-weight: bold;
        }}
        .projects-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center; /* Center the cards horizontally */
            gap: 20px; /* Space between cards */
        }}
        .project-card {{
            background: linear-gradient(135deg, #C89BF1, #A963EA);
            color: white;
            padding: 20px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            width: 250px; /* Fixed size for alignment */
            min-height: 150px; /* Ensure consistent card height */
        }}
        .project-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }}
        </style>
        <div class="projects-section">
            <h2>Projects 🗂️</h2>
            <div class="projects-grid">
                {project_cards}
        </div>
        """,
        unsafe_allow_html=True,
    )

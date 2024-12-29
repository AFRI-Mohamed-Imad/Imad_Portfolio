import streamlit as st

def about_me(profile_data):
    st.markdown(
        f"""
        <style>
        .about-section {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 50px 20px;
        }}
        .about-text {{
            max-width: 50%;
            text-align: left;
            color: white;
        }}
        .about-image img {{
            border-radius: 50%;
            width: 250px;
            height: 250px;
            border: 5px solid white;
        }}
        .about-section h2 {{
            color: #6A19B5;
            margin-bottom: 20px;
        }}
        .about-section p {{
            margin-bottom: 15px;
            font-size: 16px;
        }}
        .education-languages-section {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            padding: 50px 20px;
            color: white;
        }}
        .education {{
            flex: 2;
            margin-right: 20px;
        }}
        .languages-skills {{
            flex: 1;
        }}
        .education h2, .languages-skills h3 {{
            color: #6A19B5;
            margin-bottom: 20px;
        }}
        .languages-skills p {{
            margin-bottom: 10px;
            font-size: 16px;
        }}
        </style>
        <div class="about-section" id="about">
            <div class="about-text">
                <h2>About Me</h2>
                <p>Hi 😁, I am {profile_data['name']} - {profile_data['title']}.</p>
                <p>{profile_data['description']}</p>
            </div>
            <div class="about-image">
                <img src="data:image/jpg;base64,{profile_data['image']}" alt="Profile Picture">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Horizontal line
    st.markdown("---")

    # Education and Languages/Soft Skills Section
    st.markdown(
        """
        <style>
        .education h2 {
            font-size: 2rem;
            color: #6A19B5;
            margin-bottom: 20px;
        }
        .education p {
            margin-bottom: 15px;
            line-height: 1.5;
            color: white;
        }
        .education .school {
            font-size: 1.4rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .education .degree {
            font-size: 1.2rem;
            font-weight: normal;
            margin-bottom: 5px;
        }
        .education .year {
            font-size: 1rem;
            font-weight: lighter;
            color: #CCCCCC;
        }
        .languages-skills h3 {
            font-size: 1.5rem;
            color: #6A19B5;
            margin-bottom: 15px;
        }
        .languages-skills p {
            font-size: 1rem;
            color: white;
            margin-bottom: 10px;
        }
        </style>
        <div class="education-languages-section">
            <div class="education">
                <h2>Education 🎓</h2>
                <p>
                    <span class="school">Paris 1 Panthéon-Sorbonne</span><br>
                    <span class="degree">Master's Degree Innovation Management & Data Science</span><br>
                    <span class="year">2023 – 2024</span>
                </p>
                <p>
                    <span class="school">Télécom Paris</span><br>
                    <span class="degree">Data Science & AI Exchange Program</span><br>
                    <span class="year">2022 – 2023</span>
                </p>
                <p>
                    <span class="school">Mohammadia School Of Engineers</span><br>
                    <span class="degree">Computer Science Engineer</span><br>
                    <span class="year">2020 – 2023</span>
                </p>
            </div>
            <div class="languages-skills">
                <h3>Languages</h3>
                <p>French | Bilingual</p>
                <p>Anglais | professionnelle - C1 Cambridge</p>
                <p>Arabe | Native language</p>
                <h3>Soft Skills</h3>
                <p>Problem Solving</p>
                <p>Team Collaboration</p>
                <p>Adaptability</p>
                <p>Critical Thinking</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

import json
import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path
from PIL import Image
from styles import css_styles as css

st.set_page_config(
        page_title="Rodeo's Portfolio",
        page_icon=":smiley:",
        layout="wide",
        initial_sidebar_state="expanded",
        )

############################### PATH 
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "RestitutoPDF.pdf"
earthquake_data = current_dir / "images"/ "good_tableau_project.png"
covid_data = current_dir / "images"/ "covid_data.png"
profile = current_dir  / "images"/ "profile.jpg"
freecodecamp_cert = current_dir / "images" / "certificates" / "cert" / "data_analysis_certification_freecodecamp.png"
Coursera_cert_financial_analysis = current_dir / 'images' / 'certificates'/ 'other_cert' / "Coursera_PSFA.png"
banner = current_dir / "images" / "banner.png"

with open(css_file) as f:
    css_content = f.read()
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
image = Image.open(profile)
earthquake_image = Image.open(earthquake_data)
covid_image = Image.open(covid_data)
fcc = Image.open(freecodecamp_cert)
C_PSFAs = Image.open(Coursera_cert_financial_analysis)
ban = Image.open(banner)
################################ Banner



################################ Links
earthquake_link = "https://public.tableau.com/views/Philippine_Earthquake_Data2020-2024/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link"
covid_link = "https://public.tableau.com/views/CovidDashboard_17084094170250/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link"

################################ lottie function
def get(lottie:str):
    with open(lottie, "r") as p:
        return json.load(p)

lottie = get("./lottie_animation.json")
################################ Functions

def center_text(text):
    with open(css_file) as f:
        css_content = f.read()
    return f'<style>{css_content}</style><div class="centered-text">{text}</div>'

def txt(a,b,c,link):
    col1 , col2 = st.columns([1,1])
    with col1:
        st.write("#")
        st.image(a)
    with col2:
        st.header(b)
        st.write("###")
        st.write("#")
        st.write('\n')
        st.caption(c)
        st.markdown(f"[Go to Project...]({link})")

def txt1(a,b):
    txtcol1, txtcol2 = st.columns([1,1])
    with txtcol1:
        st.write("#")
        st.write(a)
    with txtcol2:
        st_lottie(b, height=400, key="user")

def textcolcon(title,details,link):
    with st.container():
        txtcol1 = st.columns(1)
        with txtcol1[0]:
            st.write("#")
            st.write(title)
            st.write('---')
            st.write(details)
            st.write(f'##### [Go to Certificate...]({link})')
################################ Assets

st.markdown(css.header, unsafe_allow_html=True)
st.write("###")
with st.container():
    # Layout
    st.markdown(css.new_banner_html, unsafe_allow_html=True)
    # CSS styling
    #st.markdown(css.new_banner_css, unsafe_allow_html=True)
st.write("###")


# About Me
st.markdown(css.about_me,unsafe_allow_html=True)
st.write("###")

with st.container():
    col1 , col2 = st.columns([1,2])
    with col1:
        st.image(image)
    with col2:
        st.markdown(css.Name,unsafe_allow_html=True)
        st.write("---")
        st.write("###")
        st.caption("As a budding data analyst, I prioritize trust and integrity, ensuring your data's confidentiality and security. Despite my introverted nature, I excel in visualization, transforming data into compelling insights with clarity and precision.")
        st.caption("With a commitment to continuous learning, I'm dedicated to delivering impactful results that drive informed decision-making.")
        st.markdown(css.details_aboutme,unsafe_allow_html=True)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream")

st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.projects,unsafe_allow_html=True)
st.write("###")
st.write("#")
st.write('\n')

##################### Projects

Tableau,PowerBi , Excel , Python ,SQL = st.tabs(["Tableau" , "Power Bi", "Excel" , "Python", "SQL"])
with st.container():
    with Tableau:
        txt(earthquake_image,
            " Analyzing Seismic Activity: \n A Study of Earthquakes in the Philippines (2020-2024)",
            """Exploring the Dynamics of Earthquake Occurrences and Patterns in the Philippines
            over a Five-Year Period, Unveiling Insights into Seismic Activity and Its Implications
                for Disaster Preparedness and Mitigation Efforts.""",earthquake_link)

        st.write("#")
        st.write("#")

        txt(covid_image,
            " Global COVID-19 Mortality Trends: \n Analysis of Deaths and Fatality Rates Across Continents",
            """Exploring the Dynamics of COVID-19 Mortality Patterns and Fatality Rates on a Global Scale, 
            Unveiling Insights into Regional Disparities and Implications for Public Health Strategies.""",covid_link)
            # Power bi
    with PowerBi:
        st.write("PowerBI")
    with Excel:
        st.write("Excel")
    with Python:
        st.write("Python")
    with SQL:
        st.write("SQL")

##################### Skills

st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.skills,unsafe_allow_html=True)
st.write("###")
st.write("#")
st.write('\n')


skills1= """
- ##### Programming: Python (basic), SQL (basic querying)
- ##### Data Manipulation:  Basic cleaning techniques, Pandas (Python)
- ##### Visualization:  Matplotlib, Tableau/Power BI, Streamlit (basic)
- ##### Statistical Analysis:  Basic concepts (mean, median, standard deviation), hypothesis testing
- ##### Database Management: SQL querying, data extraction/filtering
- ##### Data Analysis Tools: Jupyter Notebook
- ##### Soft Skills: Problem-solving, attention to detail, eagerness to learn
"""
st.markdown(css.hr, unsafe_allow_html=True)
txt1(skills1,lottie)

######################## Certificates
st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.certificates,unsafe_allow_html=True)
 # textcolcon(image,title,details,link)
textcolcon('- ## Data Analysis with Python', 
'##### Skill gain: Data Cleaning, Data Exploration, Visualizing Data, Python basics',
'https://www.freecodecamp.org/certification/Restituto_Rodeo_jr/data-analysis-with-python-v7')

st.write("###")
st.write("#")
st.write('\n')
######################## Other Certificates
st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.other_certificates,unsafe_allow_html=True)
# textcolcon(image,title,details,link)

textcolcon('- ## Python and Statistics for Financial Analysis',
            '##### Skills gain: Financial Data Analysis,Financial Analysis, Python Programming, Statistical Analysis, Data Visualization',
            'https://coursera.org/share/ad6dc78ca997f01f71365acbde55b814')

textcolcon('- ## Introduction to Statistics', 
           '##### Skills gain: Exploratory Data Analysis, Statistical Thinking Concepts, ',
           'https://coursera.org/share/69b40a6c47244c5c0e8187845b76d8b6')
st.write("###")
st.write("#")
st.write('\n')
######################## Education
st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.education,unsafe_allow_html=True)
with st.container():
    c = st.columns(1)
    with c[0]:
        st.markdown('## Bachelor of Science in Computer Engineering')
        st.markdown('##### (Undergraduate)')
        st.markdown('##### AMA University Caloocan Campus')
        st.markdown('##### MX5H+328, Caimito Road, Samson Rd, Caloocan, Metro Manila')


st.write("###")
st.write("#")
st.write('\n')
######################## Contact Information
st.write("###")
st.write("#")
st.write('\n')
st.markdown(css.contact,unsafe_allow_html=True)
st.write("###")
st.write("#")
st.write('\n')


with st.container():
    address, phone, email = st.columns(3)
    with address:
        st.write(" #### Address" )
        st.markdown(css.hr, unsafe_allow_html=True)
        st.caption(" #### Manila ,Philippines")
    with phone:
        st.write(" #### Phone")
        st.markdown(css.hr, unsafe_allow_html=True)
        st.caption(" #### +639602498779")
        
    with email:
        st.write(" #### Email")
        st.markdown(css.hr, unsafe_allow_html=True)
        st.caption(" #### restitutorodeo@gmail.com")

with st.container():
    st.subheader("Get in Touch With Me!")
    left_col1 , right_col2 = st.columns(2)
    with left_col1:
        st.markdown(css.contact_form, unsafe_allow_html=True)
    with right_col2:
        st.markdown(css.Nameko,unsafe_allow_html=True)
        st.write("---")
        st.write("###")
        st.markdown(css.bible_verse,unsafe_allow_html=True)


st.write("#")
st.write("#")
st.write('\n')
st.markdown(css.hr, unsafe_allow_html=True)

st.markdown(css.font_awesome_link,unsafe_allow_html=True)
st.markdown(css.social_links, unsafe_allow_html=True)


st.write("#")
st.write("#")
st.write('\n')








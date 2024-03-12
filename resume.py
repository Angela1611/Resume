import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Angela Escobar
##### *Resume* 
''')



image = Image.open('dp.png')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Committed entry-level data analyst proficient in Python, SQL, R, Excel, Tableau, & Power BI . Experienced in ETL and visualization through dashboards and tables.
- 3 years of experience as an Office Assistant with extensive file management skills, inventory, client, and supplier database management. Proficient in document and report generation, invoice processing, financial documentation and analysis, with a keen attention to detail, analytical skills, and customer service experience.
- Strong verbal and written communication skills and time management
- Strong proficiency in soft skills such as effective communication, collaboration, adaptability, professional ethics, intellectual curiosity, decision-making, and empathy.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="" target="_blank">Angela Escobar</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#portfolio">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Audio Engineer** (Bachelor Degree), *Universidad de los Andes, Bogotá, Colombia.*',
'(2015-2020)')
st.markdown('''
- GPA: `4.27`
- Designing speaker systems for large-scale spaces through electrical, mathematical and acoustic analysis..
- Management of sound design and acoustic software, such as SMART (System Measurement and Analysis for Real-Time), for live sound analysis.
- Understanding of electronic audio systems, problem-solving, and efficient signal flow management.
- Proficiency in multimedia editing software (Pro-Tools, Logic, Premiere, Sony Vegas, SMART).
''')

txt('**Data Analytics** (Professional Certificate), *Google Certificates* ',
'(2023-2024)')
st.markdown('''
- Competent with software like SQL, R, Tableau, and Excel.
- Skilled in using techniques for data cleaning and visualization.
- Competent with coding required for data analysis software.
- Development of effective ways to communicate data-driven findings to support decision-making processes
''')

txt('**Applied data science with Python** (Specialized Certificate), *University of Michigan* ',
'(In progress, 2024)')
st.markdown('''
- Currently enrolled in a specialized program focused on applied data science techniques using Python, emphasizing skills in data analysis, visualization, and machine learning. Actively engaged in expanding knowledge and exploring various aspects of data science to further develop skills in this field.
- Skilled in libraries such as NumPy, pandas, Matplotlib, Seaborn, Streamlit and scikit-learn.
- Development of skills in data visualization and communicating findings in Power BI.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Office Assistant**, Servicios Gráficos Impacop | Bogotá, Colombia',
'(2018-2021)')
st.markdown('''
- Organization and management of files, invoices, inventories, and databases using Excel and Microsoft Office.
- Production and presentation of reports on performance and other business-related analyses, as well as documents necessary for tax procedures, billing, and quotations.
- Customer service, communication with clients, and suppliers.
- Handling financial reports for the accounting and payroll departments.
- Scheduling coordination to align time management with deliveries, pending orders, and business events.
''')

txt('**Au Pair** Cultural Care | San Francisco, California',
'(2021-2022)')
st.markdown('''
- Childcare, Cultural Exchange
- Improved English proficiency through daily interactions with native speakers over the course of a whole year.

''')

txt('**Office Support Assistant**  Westcana Electric Inc | Calgary, Canadá',
'(2023)')
st.markdown('''
- Data entry into respective databases according to each sector of the company.
- Perform filing and record-keeping tasks.
- Assist in the preparation of reports and documents in Excel and Google Suites.
- Update and maintain contact, clients, and suppliers databases.
- Provide support to the project management department, including coordinating meetings and preparing documentation.
''')

txt('**Office Assistant**, Servicios Gráficos Impacop | Bogotá, Colombia',
'(2023-Present)')
st.markdown('''
- Communication with international clients
- File and database management to optimize inventory, sales, and company information processes using SQL and R
- Scheduling coordination to align time management with deliveries, pending orders, and business events.
- Implementation of data visualization tools for process optimization within the company using Power BI.
''')


#####################
st.markdown('''
## Portfolio
''')
txt4('SQL', 'Airbnb NYC Analysis', 'https://github.com/Angela1611/Airbnb_NYC_Analysis')
image = Image.open('01.png')
st.image(image, width=700)
txt4('SQL', 'Students mental health Analysis', 'https://github.com/Angela1611/Students_mental_health')
image = Image.open('02.png')
st.image(image, width=700)
txt4('R', 'Plane crashes through history Analysis','https://github.com/Angela1611/Plane_Crash_Analysis')
image = Image.open('03.png')
st.image(image, width=700)
txt4('R', 'Cyclistic company Analysis', 'https://github.com/Angela1611/Cyclistic_data_2019')
image = Image.open('04.png')
st.image(image, width=700)
txt4('R', 'Sales Analysis for Nike','https://github.com/Angela1611/Nike_analysis')
image = Image.open('05.png')
st.image(image, width=700)
txt4('Python', 'The Simpsons - Analysis', 'https://github.com/Angela1611/Simpsons-Analysis')
image = Image.open('06.png')
st.image(image, width=700)
txt4('Python', 'Distribution of billionaire people and industrys', 'https://github.com/Angela1611/Distribution_billionaire_industrys')
image = Image.open('07.png')
st.image(image, width=700)
txt4('Tableau', 'Airbnb NYC Analysis Dashboard', 'https://public.tableau.com/app/profile/angela161/viz/AirbnbNYCAnalysis_17093234133180/Dashboard3')
image = Image.open('08.png')
st.image(image, width=700)
txt4('Tableau', 'Students mental health Dashboard', 'https://public.tableau.com/app/profile/angela161/viz/Students_mental_health/Dashboard1')
image = Image.open('09.png')
st.image(image, width=700)
txt4('Power BI', 'Cyclistic company Analysis', 'https://app.powerbi.com/groups/me/reports/0015e8ad-7008-4f88-a7d4-e0c77efca611/ReportSection?experience=power-bi')
image = Image.open('10.jpg')
st.image(image, width=700)
txt4('Power BI', 'Plane crashes through history', 'https://app.powerbi.com/groups/me/reports/9f713b16-cf0c-4425-ad58-8f92fc086973?pbi_source=desktop')
image = Image.open('11.jpg')
st.image(image, width=700)


#####################
st.markdown('''
## Skills
''')
txt3('Data processing', ' `Excel`, `Google Sheets`, `SQL`, `R`, `Python`, `Git` ')
txt3('Data visualization', '`Tableau`, `Power BI`')
txt3('Python libraries', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`, `pandas`, `numpy`')


#####################
st.markdown('''
## Contact
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/angela-escobar161/')
txt2('GitHub', 'https://github.com/Angela1611')
txt2('Email', 'natescobar2@gmail.com')

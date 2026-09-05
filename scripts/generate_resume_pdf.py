from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, PageBreak, KeepTogether

OUT = Path('assets/resume/Gonzalo_Loayza_Resume.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)

BLACK = colors.HexColor('#111111')
MUTED = colors.HexColor('#444444')
RULE = colors.HexColor('#444444')

styles = getSampleStyleSheet()
name = ParagraphStyle(
    'Name', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=17.5,
    leading=19, textColor=BLACK, alignment=1, spaceAfter=2,
)
contact = ParagraphStyle(
    'Contact', parent=styles['Normal'], fontName='Helvetica', fontSize=8.6,
    leading=10.2, textColor=BLACK, alignment=1, spaceAfter=6,
)
section = ParagraphStyle(
    'Section', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10.2,
    leading=11.5, textColor=BLACK, spaceBefore=5, spaceAfter=1.5,
)
body = ParagraphStyle(
    'Body', parent=styles['Normal'], fontName='Helvetica', fontSize=8.6,
    leading=10.7, textColor=BLACK, spaceAfter=2.3,
)
role = ParagraphStyle(
    'Role', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.9,
    leading=10.5, textColor=BLACK, spaceAfter=0.5,
)
meta = ParagraphStyle(
    'Meta', parent=styles['Normal'], fontName='Helvetica', fontSize=8.35,
    leading=10, textColor=BLACK, spaceAfter=1.5,
)
bullet = ParagraphStyle(
    'Bullet', parent=body, leftIndent=11, firstLineIndent=-7, bulletIndent=0,
    fontSize=8.35, leading=10.15, spaceAfter=1.3,
)
label = ParagraphStyle(
    'Label', parent=body, fontSize=8.35, leading=10.3, spaceAfter=1.6,
)


def section_heading(title):
    return [
        Paragraph(title, section),
        HRFlowable(width='100%', thickness=0.65, color=RULE, spaceBefore=0, spaceAfter=3.0),
    ]


def bullets(items):
    return [Paragraph('• ' + item, bullet) for item in items]


def job(title, org, date, items):
    return KeepTogether([
        Paragraph(f'{title} | {org}', role),
        Paragraph(date, meta),
        *bullets(items),
        Spacer(1, 2.0),
    ])


def project(title, tech, items):
    return KeepTogether([
        Paragraph(title, role),
        Paragraph(tech, meta),
        *bullets(items),
        Spacer(1, 2.0),
    ])


story = [
    Paragraph('GONZALO LOAYZA', name),
    Paragraph('Provo, UT  •  +1 (801) 735-8034  •  gloayza5@byu.edu  •  LinkedIn  •  Portfolio', contact),
]

story += section_heading('SUMMARY')
story.append(Paragraph(
    'Senior Computer Science student at BYU with a Machine Learning emphasis and hands-on experience in data science, '
    'applied analytics, and ML workflows using real-world operational datasets. Skilled in Python, SQL, time-series analysis, '
    'feature engineering, model evaluation, and decision-support analytics. Strong ability to frame business and operational '
    'problems, identify value drivers, and apply machine learning to support practical decisions in industrial, infrastructure, '
    'and environmental contexts.', body))

story += section_heading('EDUCATION')
story.append(Paragraph('Brigham Young University (BYU), Provo, UT', role))
story.append(Paragraph('B.S. in Computer Science, Machine Learning Emphasis', meta))
story.append(Paragraph('<b>Expected Graduation:</b> December 2026', label))
story.append(Paragraph('<b>Relevant Coursework:</b> Deep Learning, Data Science Capstone, Machine Learning, Algorithms, Data Structures, Computer Systems, Probability & Statistics', label))
story.append(Paragraph('<b>Honors Thesis:</b> Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data', label))

story += section_heading('TECHNICAL SKILLS')
story.append(Paragraph('<b>Languages:</b> Python, SQL, C++, JavaScript', label))
story.append(Paragraph('<b>Data Science & ML:</b> time-series analysis, feature engineering, classification, unsupervised learning, model evaluation, exploratory data analysis, dimensionality reduction, predictive analytics', label))
story.append(Paragraph('<b>Libraries & Tools:</b> scikit-learn, Pandas, NumPy, Jupyter, Git, Linux, SHAP, Power BI', label))
story.append(Paragraph('<b>Business & Industrial Analytics:</b> problem framing, KPI analysis, bottleneck analysis, value-driver identification, operational mode discovery, dashboard-oriented thinking, decision-support analytics', label))

story += section_heading('EXPERIENCE')
story.append(job('Data Analytics Intern', 'Hatch Digital, Peru', 'June 2026 – August 2026', [
    'Supporting digital and analytics initiatives focused on mining and industrial operations, including data analysis, operational KPIs, and decision-support workflows.',
    'Contributing to early-stage problem framing, data preparation, dashboard-oriented analysis, and identification of opportunities for process improvement and operational value creation.',
]))
story.append(job('Maintenance Data Analyst Intern', 'Compañía de Minas Buenaventura, San Gabriel Unit, Peru', 'Jun 2025 – Aug 2025', [
    'Identified reliability and maintenance-analysis gaps in crushing and grinding equipment data, then processed and cleaned 50k+ noisy sensor time-series to support predictive-maintenance exploration.',
    'Analyzed operating signals linked to equipment wear, ore variability, and process behavior to support condition-monitoring and reliability-focused decision-making.',
    'Engineered 15+ features, including temperature deltas, load ratios, and transient-spike indicators, to improve the analytical basis for equipment monitoring workflows.',
    'Structured 100+ assets under ISO 14224/17359 standards, improving maintenance-data traceability, consistency, and analytical usability.',
]))
story.append(job('Data Analytics Intern', 'Hatch Ltd, Urban Solutions Sector, Vermont, USA', 'May 2024 – Aug 2024', [
    'Evaluated operational delay and network-performance challenges across simulation scenarios, then analyzed 200k+ records to identify bottlenecks and support planning decisions.',
    'Built Python and C++ automation workflows that reduced processing time by about 70%, improving analysis speed, repeatability, and scenario-evaluation capacity.',
    'Integrated rider-survey information with onboard sensor data to strengthen scenario interpretation and validate service-level assumptions.',
    'Supported planning teams through statistical and optimization-based analysis, translating simulation outputs into practical insights for operational decision-making.',
]))

story.append(PageBreak())
story += section_heading('PROJECTS')
story.append(project(
    'Honors Thesis – Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data',
    'Python | Time-Series Analytics | PCA | Clustering | Business Value Analysis — BYU Honors Program, 2025 - 2026', [
        'Framed an industrial analytics problem around operating variability, recovery losses, throughput pressure, and equipment bottlenecks in a real concentrator environment.',
        'Integrated minute-level process data with daily KPI context to evaluate how different operating patterns affect recovery, losses, and production stability.',
        'Applied preprocessing, feature scaling, PCA, and clustering techniques to identify recurrent operational modes and support interpretable performance profiling.',
        'Connected data infrastructure, control-loop performance, instrumentation gaps, and ML opportunities to a staged roadmap focused on throughput, recovery stability, energy optimization, and business value.',
    ]))
story.append(project(
    'Wildfire Prediction System',
    'Python | XGBoost | Time-Series | API Integration — BYU, 2026', [
        'Built a wildfire-risk prediction prototype using 7-day weather time-series and reported fire data from Utah to prioritize high-risk locations.',
        'Trained and compared XGBoost, Random Forest, and Naive Bayes models on imbalanced wildfire-event data.',
        'Applied SHAP interpretability and designed a workflow combining weather APIs, satellite imagery retrieval, and dashboard-style risk visualization.',
    ]))

story += section_heading('CERTIFICATIONS')
story.append(Paragraph('<b>AWS Certification in Progress</b>', role))
story.append(Paragraph('Expected completion: August 2026', meta))

story += section_heading('AWARDS')
story.append(Paragraph('Donald Goodyear Doll Sr. Scholarship | Dr. Gerald Hatch Scholarship | BYU Honors Program', body))

story += section_heading('LEADERSHIP')
story.append(Paragraph('<b>Emergency Response & Rescue Program, Peruvian Army</b>', role))
story.append(Paragraph('Leadership training focused on coordination, rapid decision-making, and execution in high-pressure environments.', body))

story += section_heading('LANGUAGES')
story.append(Paragraph('English (Fluent) | Spanish (Native) | French (Intermediate)', body))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 6.6)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.28 * inch, 'Gonzalo Loayza')
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.28 * inch, f'Page {doc.page}')
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    leftMargin=0.55 * inch,
    rightMargin=0.55 * inch,
    topMargin=0.42 * inch,
    bottomMargin=0.45 * inch,
    title='Gonzalo Loayza Resume',
    author='Gonzalo Loayza',
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f'Generated {OUT}')

from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

OUT = Path('assets/resume/Gonzalo_Loayza_Resume.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('ResumeSans', REG))
pdfmetrics.registerFont(TTFont('ResumeSans-Bold', BOLD))

INK = colors.HexColor('#111111')
TEXT = colors.HexColor('#202020')

styles = getSampleStyleSheet()
name = ParagraphStyle('Name', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=17.0, leading=19.0, textColor=INK, spaceAfter=4)
contact = ParagraphStyle('Contact', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.6, leading=10.0, textColor=TEXT, spaceAfter=9)
section = ParagraphStyle('Section', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=10.1, leading=11.5, textColor=INK, spaceBefore=7.0, spaceAfter=3.0)
body = ParagraphStyle('Body', parent=styles['Normal'], fontName='ResumeSans', fontSize=9.0, leading=10.9, textColor=TEXT, spaceAfter=2.4)
role = ParagraphStyle('Role', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=9.25, leading=10.6, textColor=INK, spaceAfter=0.7)
meta = ParagraphStyle('Meta', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.55, leading=9.7, textColor=TEXT, spaceAfter=2.0)
bullet = ParagraphStyle('Bullet', parent=body, leftIndent=14, firstLineIndent=-7, bulletIndent=2, spaceAfter=1.4)
small = ParagraphStyle('Small', parent=body, fontSize=8.8, leading=10.4, spaceAfter=1.7)


def p(text, style=body):
    return Paragraph(text, style)


def sec(title):
    return [Paragraph(title.upper(), section)]


def bullets(items):
    return [Paragraph('• ' + item, bullet) for item in items]


def job(title, org, date, items):
    return KeepTogether([
        Paragraph(f'{title} | {org}', role),
        Paragraph(date, meta),
        *bullets(items),
        Spacer(1, 2.8),
    ])


def project(title, tech, items):
    return KeepTogether([
        Paragraph(title, role),
        Paragraph(tech, meta),
        *bullets(items),
        Spacer(1, 3),
    ])


story = [
    Paragraph('GONZALO LOAYZA', name),
    Paragraph(
        'Provo, UT  •  +1 (801) 735-8034  •  '
        '<link href="mailto:gloayza5@byu.edu" color="#1a0dab"><u>gloayza5@byu.edu</u></link>  •  '
        '<link href="https://www.linkedin.com/in/gonzaloayza" color="#1a0dab"><u>LinkedIn</u></link>  •  '
        '<link href="https://gonza055.github.io/" color="#1a0dab"><u>Portfolio</u></link>',
        contact,
    ),
]

story += sec('Summary')
story.append(p(
    'Senior Computer Science student at BYU with a Machine Learning emphasis and hands-on experience in data science, '
    'applied analytics, and ML workflows using real-world operational datasets. Skilled in Python, SQL, time-series analysis, '
    'feature engineering, model evaluation, and decision-support analytics. Strong ability to frame business and operational '
    'problems, identify value drivers, and apply machine learning to support practical decisions in industrial, infrastructure, '
    'and environmental contexts.'
))

story += sec('Education')
story.append(Paragraph('Brigham Young University (BYU), Provo, UT', role))
story.append(Paragraph('B.S. in Computer Science, Machine Learning Emphasis', body))
story.append(Paragraph('Expected Graduation: December 2026', body))
story.append(Paragraph('<b>Relevant Coursework:</b> Deep Learning, Data Science Capstone, Machine Learning, Algorithms, Data Structures, Computer Systems, Probability & Statistics', small))
story.append(Paragraph('<b>Honors Thesis:</b> Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data', small))

story += sec('Experience')
story.append(job('Data Analytics Intern', 'Hatch Digital, Peru', 'June 2026 - August 2026', [
    'Contributed across three applied digital workstreams: tailings-data validation and automation, drone-enabled measurement concepts, and shift-level decision-support workflows for mining and engineering applications.',
    'Supported problem framing, data preparation, operational KPI logic, and multidisciplinary validation so analytical outputs remained connected to real engineering decisions.',
    'Presented the internship work and lessons learned to the Hatch Young Professionals community through a technical retrospective focused on measurement, data reliability, and operational decision support.',
]))
story.append(job('Maintenance Data Analyst Intern', 'Compañía de Minas Buenaventura, San Gabriel Unit, Peru', 'Jun 2025 - Aug 2025', [
    'Identified reliability and maintenance-analysis gaps in crushing and grinding equipment data, then processed and cleaned 50k+ noisy sensor time-series to support predictive-maintenance exploration.',
    'Analyzed operating signals linked to equipment wear, ore variability, and process behavior to support condition-monitoring and reliability-focused decision-making.',
    'Engineered 15+ features, including temperature deltas, load ratios, and transient-spike indicators, to improve the analytical basis for equipment monitoring workflows.',
    'Structured 100+ assets under ISO 14224/17359 standards, improving maintenance-data traceability, consistency, and analytical usability.',
]))
story.append(job('Data Analytics Intern', 'Hatch Ltd, Urban Solutions Sector, Vermont, USA', 'May 2024 - Aug 2024', [
    'Evaluated operational delay and network-performance challenges across simulation scenarios, then analyzed 200k+ records to identify bottlenecks and support planning decisions.',
    'Built Python and C++ automation workflows that reduced processing time by about 70%, improving analysis speed, repeatability, and scenario-evaluation capacity.',
    'Integrated rider-survey information with onboard sensor data to strengthen scenario interpretation and validate service-level assumptions.',
    'Supported planning teams through statistical and optimization-based analysis, translating simulation outputs into practical insights for operational decision-making.',
]))

story.append(PageBreak())

story += sec('Technical Skills')
story.append(p('<b>Languages:</b> Python, SQL, C++, JavaScript', small))
story.append(p('<b>Data Science & ML:</b> time-series analysis, feature engineering, classification, unsupervised learning, model evaluation, exploratory data analysis, dimensionality reduction, predictive analytics', small))
story.append(p('<b>Libraries & Tools:</b> scikit-learn, Pandas, NumPy, Jupyter, Git, Linux, SHAP, Power BI', small))
story.append(p('<b>Business & Industrial Analytics:</b> problem framing, KPI analysis, bottleneck analysis, value-driver identification, operational mode discovery, dashboard-oriented thinking, decision-support analytics', small))

story += sec('Projects')
story.append(project(
    'Honors Thesis - Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data',
    'Python | Time-Series Analytics | PCA | DBSCAN | Business Value Analysis - BYU Honors Program, 2025 - 2026',
    [
        'Framed an industrial analytics problem around operating variability, recovery losses, throughput pressure, and equipment bottlenecks in a real processing environment.',
        'Integrated minute-level process data with daily KPI context, standardized process features, and reduced dimensionality with PCA using a 95% explained-variance target.',
        'Applied DBSCAN and identified three recurrent operating regimes, then profiled them against recovery, production, variability, and equipment-configuration signatures.',
        'Connected data infrastructure, control-loop performance, instrumentation gaps, and ML opportunities to a staged roadmap focused on throughput, recovery stability, energy optimization, and business value.',
    ],
))
story.append(project(
    'Wildfire Prediction System',
    'Python | XGBoost | Time-Series | API Integration | Docker - BYU, 2026',
    [
        'Built a wildfire-risk prioritization prototype using 7-day weather histories and reported Utah fire data to narrow where satellite-image follow-up should occur first.',
        'Trained and compared XGBoost, Random Forest, and Naive Bayes models on balanced and imbalanced wildfire-event datasets.',
        'Selected the unbalanced XGBoost workflow, which achieved 23% precision, 9.7% recall, and PR AUC 0.110 versus a 0.006 random baseline on the evaluated rare-event task.',
        'Connected model scoring to a browser-based risk map and satellite-image retrieval workflow using a Python backend and containerized services.',
    ],
))

story += sec('Certifications')
story.append(p('<b>AWS Certification in Progress</b>'))

story += sec('Awards')
story.append(p('Donald Goodyear Doll Sr. Scholarship | Dr. Gerald Hatch Scholarship | BYU Honors Program'))

story += sec('Leadership')
story.append(p('<b>Emergency Response & Rescue Program, Peruvian Army</b><br/>Leadership training focused on coordination, rapid decision-making, and execution in high-pressure environments.'))

story += sec('Languages')
story.append(p('English (Fluent) | Spanish (Native) | French (Intermediate)'))


doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    rightMargin=0.46 * inch,
    leftMargin=0.46 * inch,
    topMargin=0.38 * inch,
    bottomMargin=0.38 * inch,
    title='Gonzalo Loayza Resume',
    author='Gonzalo Loayza',
)
doc.build(story)
print(f'Generated {OUT}')

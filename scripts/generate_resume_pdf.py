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
LINK = colors.HexColor('#1a0dab')

styles = getSampleStyleSheet()
name = ParagraphStyle('Name', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=16.2, leading=18.2, textColor=INK, spaceAfter=3)
contact = ParagraphStyle('Contact', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.25, leading=9.4, textColor=TEXT, spaceAfter=7)
section = ParagraphStyle('Section', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=9.4, leading=10.5, textColor=INK, spaceBefore=5.2, spaceAfter=2.0)
body = ParagraphStyle('Body', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.55, leading=10.25, textColor=TEXT, spaceAfter=2.0)
role = ParagraphStyle('Role', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=8.8, leading=10.0, textColor=INK, spaceAfter=0.4)
meta = ParagraphStyle('Meta', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.15, leading=9.2, textColor=TEXT, spaceAfter=1.5)
bullet = ParagraphStyle('Bullet', parent=body, leftIndent=13, firstLineIndent=-7, bulletIndent=2, spaceAfter=0.9)
small = ParagraphStyle('Small', parent=body, fontSize=8.35, leading=9.8, spaceAfter=1.2)


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
        Spacer(1, 1.5),
    ])


def project(title, tech, items):
    return KeepTogether([
        Paragraph(title, role),
        Paragraph(tech, meta),
        *bullets(items),
        Spacer(1, 2),
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

story += sec('Technical Skills')
story.append(p('<b>Languages:</b> Python, SQL, C++, JavaScript', small))
story.append(p('<b>Data Science & ML:</b> time-series analysis, feature engineering, classification, unsupervised learning, model evaluation, exploratory data analysis, dimensionality reduction, predictive analytics', small))
story.append(p('<b>Libraries & Tools:</b> scikit-learn, Pandas, NumPy, Jupyter, Git, Linux, SHAP, Power BI', small))
story.append(p('<b>Business & Industrial Analytics:</b> problem framing, KPI analysis, bottleneck analysis, value-driver identification, operational mode discovery, dashboard-oriented thinking, decision-support analytics', small))

story += sec('Experience')
story.append(job('Data Analytics Intern', 'Hatch Digital, Peru', 'June 2026 - August 2026', [
    'Supported digital and analytics initiatives focused on mining and industrial operations, including data analysis, operational KPIs, and decision-support workflows.',
    'Contributed to early-stage problem framing, data preparation, dashboard-oriented analysis, and identification of opportunities for process improvement and operational value creation.',
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

# Keep the same two-page rhythm as the established CV: page 1 ends with Experience.
story.append(PageBreak())

story += sec('Projects')
story.append(project(
    'Honors Thesis - Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data',
    'Python | Time-Series Analytics | PCA | Clustering | Business Value Analysis — BYU Honors Program, 2025 - 2026',
    [
        'Framed an industrial analytics problem around operating variability, recovery losses, throughput pressure, and equipment bottlenecks in a real concentrator environment.',
        'Integrated minute-level process data with daily KPI context to evaluate how different operating patterns affect recovery, losses, and production stability.',
        'Applied preprocessing, feature scaling, PCA, and clustering techniques to identify recurrent operational modes and support interpretable performance profiling.',
        'Connected data infrastructure, control-loop performance, instrumentation gaps, and ML opportunities to a staged roadmap focused on throughput, recovery stability, energy optimization, and business value.',
    ],
))
story.append(project(
    'Wildfire Prediction System',
    'Python | XGBoost | Time-Series | API Integration — BYU, 2026',
    [
        'Built a wildfire-risk prediction prototype using 7-day weather time-series and reported fire data from Utah to prioritize high-risk locations.',
        'Trained and compared XGBoost, Random Forest, and Naive Bayes models on imbalanced wildfire-event data.',
        'Applied SHAP interpretability and designed a workflow combining weather APIs, satellite imagery retrieval, and dashboard-style risk visualization.',
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
    rightMargin=0.38 * inch,
    leftMargin=0.38 * inch,
    topMargin=0.30 * inch,
    bottomMargin=0.30 * inch,
    title='Gonzalo Loayza Resume',
    author='Gonzalo Loayza',
)
doc.build(story)
print(f'Generated {OUT}')

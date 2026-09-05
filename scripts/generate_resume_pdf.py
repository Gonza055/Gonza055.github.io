from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether, PageBreak
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

OUT = Path('assets/resume/Gonzalo_Loayza_Resume.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('ResumeSans', REG))
pdfmetrics.registerFont(TTFont('ResumeSans-Bold', BOLD))

INK = colors.HexColor('#111827')
TEXT = colors.HexColor('#1f2937')
MUTED = colors.HexColor('#4b5563')
RULE = colors.HexColor('#cbd5e1')

styles = getSampleStyleSheet()
name = ParagraphStyle('Name', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=18.5, leading=20.5, textColor=INK, spaceAfter=2)
contact = ParagraphStyle('Contact', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.4, leading=10, textColor=TEXT, spaceAfter=7)
section = ParagraphStyle('Section', parent=styles['Heading2'], fontName='ResumeSans-Bold', fontSize=10.2, leading=11.5, textColor=INK, spaceBefore=7, spaceAfter=2.5)
body = ParagraphStyle('Body', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.8, leading=11.1, textColor=TEXT, spaceAfter=3)
role = ParagraphStyle('Role', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=9.2, leading=10.8, textColor=INK, spaceAfter=0.5)
meta = ParagraphStyle('Meta', parent=styles['Normal'], fontName='ResumeSans', fontSize=8.2, leading=9.8, textColor=MUTED, spaceAfter=2)
bullet = ParagraphStyle('Bullet', parent=body, leftIndent=11, firstLineIndent=-6, bulletIndent=0, spaceAfter=1.6)
small = ParagraphStyle('Small', parent=body, fontSize=8.5, leading=10.7, spaceAfter=2.2)


def p(text, style=body):
    return Paragraph(text, style)


def sec(title):
    return [
        Paragraph(title.upper(), section),
        HRFlowable(width='100%', thickness=0.65, color=RULE, spaceBefore=0, spaceAfter=3.5),
    ]


def bullets(items):
    return [Paragraph('• ' + item, bullet) for item in items]


def job(title, org, date, items):
    return KeepTogether([
        Paragraph(f'{title} | {org}', role),
        Paragraph(date, meta),
        *bullets(items),
        Spacer(1, 2.5),
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
    Paragraph('Provo, UT  •  +1 (801) 735-8034  •  gloayza5@byu.edu  •  LinkedIn  •  Portfolio', contact),
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

# Preserve the original two-page CV rhythm: experience closes page 1, projects lead page 2.
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
story.append(p('<b>AWS Certification in Progress</b><br/>Expected completion: August 2026'))

story += sec('Awards')
story.append(p('Donald Goodyear Doll Sr. Scholarship | Dr. Gerald Hatch Scholarship | BYU Honors Program'))

story += sec('Leadership')
story.append(p('<b>Emergency Response & Rescue Program, Peruvian Army</b><br/>Leadership training focused on coordination, rapid decision-making, and execution in high-pressure environments.'))

story += sec('Languages')
story.append(p('English (Fluent) | Spanish (Native) | French (Intermediate)'))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 0.39 * inch, letter[0] - doc.rightMargin, 0.39 * inch)
    canvas.setFont('ResumeSans', 6.7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.24 * inch, 'Gonzalo Loayza')
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.24 * inch, f'Page {doc.page}')
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    rightMargin=0.58 * inch,
    leftMargin=0.58 * inch,
    topMargin=0.46 * inch,
    bottomMargin=0.52 * inch,
    title='Gonzalo Loayza Resume',
    author='Gonzalo Loayza',
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f'Generated {OUT}')

from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

OUT = Path('assets/resume/Gonzalo_Loayza_Resume.pdf')
OUT.parent.mkdir(parents=True, exist_ok=True)
REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('ResumeSans', REG))
pdfmetrics.registerFont(TTFont('ResumeSans-Bold', BOLD))
NAVY = colors.HexColor('#0f172a')
BLUE = colors.HexColor('#2563eb')
TEXT = colors.HexColor('#334155')
MUTED = colors.HexColor('#64748b')
RULE = colors.HexColor('#dbe4ee')

styles = getSampleStyleSheet()
name = ParagraphStyle('Name', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=17.5, leading=19, textColor=NAVY, spaceAfter=1)
contact = ParagraphStyle('Contact', parent=styles['Normal'], fontName='ResumeSans', fontSize=7.35, leading=8.5, textColor=TEXT, spaceAfter=3)
section = ParagraphStyle('Section', parent=styles['Heading2'], fontName='ResumeSans-Bold', fontSize=8.7, leading=9.6, textColor=BLUE, spaceBefore=3.1, spaceAfter=1.2)
body = ParagraphStyle('Body', parent=styles['Normal'], fontName='ResumeSans', fontSize=7.45, leading=8.95, textColor=TEXT, spaceAfter=1.3)
role = ParagraphStyle('Role', parent=styles['Normal'], fontName='ResumeSans-Bold', fontSize=8.0, leading=9.0, textColor=NAVY, spaceAfter=0)
meta = ParagraphStyle('Meta', parent=styles['Normal'], fontName='ResumeSans', fontSize=7.1, leading=8.1, textColor=MUTED, spaceAfter=0.8)
bullet = ParagraphStyle('Bullet', parent=body, leftIndent=8, firstLineIndent=-5, bulletIndent=0, spaceAfter=0.45)
small = ParagraphStyle('Small', parent=body, fontSize=7.15, leading=8.45, spaceAfter=0.8)


def p(text, style=body):
    return Paragraph(text, style)


def sec(title):
    return [Paragraph(title.upper(), section), HRFlowable(width='100%', thickness=0.45, color=RULE, spaceBefore=0, spaceAfter=1.6)]


def bullets(items):
    return [Paragraph('• ' + item, bullet) for item in items]


def job(title, org, date, items):
    return KeepTogether([Paragraph(title, role), Paragraph(f'{org}  |  {date}', meta), *bullets(items), Spacer(1, 0.8)])


def project(title, tech, items):
    return KeepTogether([Paragraph(title, role), Paragraph(tech, meta), *bullets(items), Spacer(1, 0.8)])


story = [
    Paragraph('GONZALO LOAYZA', name),
    Paragraph('Provo, UT  •  +1 (801) 735-8034  •  gloayza5@byu.edu  •  linkedin.com/in/gonzaloayza  •  gonza055.github.io', contact),
]

story += sec('Summary')
story.append(p('Senior Computer Science student at BYU with a Machine Learning emphasis and applied experience in data engineering, industrial analytics, time-series, simulation, and decision-support workflows. Skilled in Python, SQL, feature engineering, model evaluation, and translating real-world operational data into practical technical insights.'))

story += sec('Education')
story.append(Paragraph('Brigham Young University (BYU), Provo, UT', role))
story.append(Paragraph('B.S. Computer Science, Machine Learning Emphasis  |  Expected Dec 2026  |  BYU Honors Program', meta))
story.append(p('<b>Coursework:</b> Deep Learning, Data Science Capstone, Machine Learning, Algorithms, Data Structures, Computer Systems, Probability & Statistics  |  <b>Honors Thesis:</b> Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data', small))

story += sec('Technical Skills')
story.append(p('<b>Languages:</b> Python, SQL, C++, JavaScript  |  <b>ML & Data:</b> time-series analysis, feature engineering, classification, unsupervised learning, PCA, model evaluation, EDA, predictive analytics  |  <b>Tools:</b> scikit-learn, Pandas, NumPy, Jupyter, Git, Linux, SHAP, Power BI  |  <b>Applied Analytics:</b> KPI analysis, bottleneck analysis, operational mode discovery, value-driver identification, decision support', small))

story += sec('Experience')
story.append(job('Data Analytics Intern', 'Hatch Digital, Peru', 'Jun 2026 - Aug 2026', [
    'Supported digital and analytics initiatives for mining and industrial operations, including tailings-data automation, operational KPIs, measurement concepts, and decision-support workflows.',
    'Contributed to problem framing, data preparation, dashboard-oriented analysis, and identification of opportunities for process improvement and operational value creation.',
]))
story.append(job('Maintenance Data Analyst Intern', 'Compañía de Minas Buenaventura, Peru', 'Jun 2025 - Aug 2025', [
    'Processed and cleaned 50k+ noisy sensor time-series from crushing and grinding equipment; engineered 15+ reliability features including temperature deltas, load ratios, and transient-spike indicators.',
    'Analyzed equipment wear, ore variability, and process signals for condition-monitoring workflows; structured 100+ assets under ISO 14224/17359 to improve traceability and analytical usability.',
]))
story.append(job('Data Analytics Intern', 'Hatch Ltd, Urban Solutions Sector, Vermont, USA', 'May 2024 - Aug 2024', [
    'Analyzed 200k+ rail-simulation records to evaluate delays, network performance, and operational bottlenecks; built Python and C++ automation that reduced output-processing time by about 70%.',
    'Integrated rider-survey information with onboard sensor data and supported scenario planning through statistical and optimization-based analysis.',
]))

story += sec('Selected Projects')
story.append(project('Honors Thesis - Operational Mode Discovery & Business Value Analysis', 'Python  |  Industrial Time-Series  |  PCA  |  Clustering  |  BYU Honors, 2025-2026', [
    'Integrated minute-level process data with daily KPI context, then applied preprocessing, scaling, PCA, and clustering to identify recurrent operating modes in a real industrial processing environment.',
    'Connected operating modes, control performance, instrumentation gaps, and ML opportunities to performance stability and business-value drivers.',
]))
story.append(project('Wildfire Prediction System', 'Python  |  XGBoost  |  SHAP  |  APIs  |  BYU, 2026', [
    'Built a wildfire-risk prototype using seven-day weather time-series and reported fire data; compared XGBoost, Random Forest, and Naive Bayes on imbalanced event data.',
    'Applied SHAP interpretability and designed a workflow combining weather APIs, satellite-imagery retrieval, and dashboard-style risk visualization.',
]))

story += sec('Awards, Leadership & Languages')
story.append(p('<b>Awards:</b> Donald Goodyear Doll Sr. Scholarship; Dr. Gerald Hatch Scholarship; BYU Honors Program  |  <b>Leadership:</b> Emergency Response & Rescue Program, Peruvian Army  |  <b>Languages:</b> English (Fluent), Spanish (Native), French (Intermediate)', small))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('ResumeSans', 6.4)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 0.27 * inch, 'Gonzalo Loayza | Resume')
    canvas.drawRightString(letter[0] - doc.rightMargin, 0.27 * inch, 'gonza055.github.io')
    canvas.restoreState()


doc = SimpleDocTemplate(
    str(OUT),
    pagesize=letter,
    rightMargin=0.43 * inch,
    leftMargin=0.43 * inch,
    topMargin=0.35 * inch,
    bottomMargin=0.40 * inch,
    title='Gonzalo Loayza Resume',
    author='Gonzalo Loayza',
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f'Generated {OUT}')

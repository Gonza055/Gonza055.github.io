from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630
BG = '#f8fafc'
WHITE = '#ffffff'
INK = '#0f172a'
TEXT = '#334155'
MUTED = '#64748b'
BORDER = '#dbe4ee'
BLUE = '#2563eb'
BLUE_MID = '#60a5fa'
BLUE_DARK = '#1e3a8a'
BLUE_SOFT = '#eff6ff'

OUT = Path('assets/images/social')
OUT.mkdir(parents=True, exist_ok=True)

FONT_REG = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size=size)


def rr(draw, box, radius=24, fill=WHITE, outline=BORDER, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_multiline(draw, xy, lines, fnt, fill, spacing=8):
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((x, y), line, font=fnt)
        y = bbox[3] + spacing
    return y


def base_card(eyebrow, title_lines, subtitle_lines, footer='GONZALO LOAYZA  ·  PORTFOLIO'):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    rr(d, (70, 58, 1130, 572), radius=28)
    d.text((110, 100), eyebrow, font=font(24, True), fill=BLUE)
    y = draw_multiline(d, (110, 165), title_lines, font(54, True), INK, spacing=8)
    y += 18
    draw_multiline(d, (110, y), subtitle_lines, font(25), TEXT, spacing=4)
    d.text((110, 520), footer, font=font(18, True), fill=MUTED)
    rr(d, (815, 88, 1095, 542), radius=24, fill=BLUE_SOFT, outline='#bfd7f0', width=2)
    return img, d


def save(img, name):
    img.save(OUT / name, quality=88, optimize=True, progressive=True)


def portfolio():
    img, d = base_card(
        'COMPUTER SCIENCE @ BYU',
        ['Data, ML, and software', 'for real-world systems'],
        ['Machine Learning · Data Engineering · Industrial', 'Analytics · Decision Support']
    )
    pts = [(865, 180), (940, 240), (1025, 170), (1050, 330), (990, 420), (880, 365)]
    for a, b in zip(pts, pts[1:] + pts[:1]):
        d.line((a, b), fill='#8fc4ee', width=3)
    for i, (x, y) in enumerate(pts):
        c = BLUE_DARK if i in (4,) else BLUE if i in (0, 2) else BLUE_MID
        d.ellipse((x-12, y-12, x+12, y+12), fill=c)
    save(img, 'portfolio-social.jpg')


def hatch():
    img, d = base_card(
        'HATCH DIGITAL · 2026',
        ['Data Engineering &', 'Decision Support'],
        ['Operational data, automation, and decision-oriented', 'analytics for mining and industrial systems.']
    )
    boxes = [(855, 135, 1055, 218, 'DATA'), (855, 274, 1055, 357, 'CONTEXT'), (855, 413, 1055, 496, 'DECISION')]
    for x1, y1, x2, y2, label in boxes:
        rr(d, (x1, y1, x2, y2), radius=18, fill=WHITE, outline='#9fc7e5', width=2)
        tb = d.textbbox((0,0), label, font=font(23, True))
        d.text(((x1+x2-(tb[2]-tb[0]))/2, (y1+y2-(tb[3]-tb[1]))/2-3), label, font=font(23, True), fill=BLUE_DARK)
    for y in (220, 359):
        d.line((955, y, 955, y+42), fill='#94bff0', width=5)
        d.polygon([(946, y+33), (964, y+33), (955, y+47)], fill='#94bff0')
    save(img, 'hatch-digital-social.jpg')


def predictive():
    img, d = base_card(
        'BUENAVENTURA · 2025',
        ['Predictive Maintenance', '& Reliability Analytics'],
        ['50k+ industrial time-series, feature engineering, and', 'condition-monitoring workflows.']
    )
    for x in range(840, 1080, 50): d.line((x, 130, x, 500), fill='#d9e6f2', width=1)
    for y in range(160, 500, 50): d.line((840, y, 1070, y), fill='#d9e6f2', width=1)
    pts=[]
    for i in range(115):
        x = 840 + i*2
        y = 310 + 25*math.sin(i/9.0) + 18*math.sin(i/4.7)
        if i in (22, 56, 88): y -= 55
        pts.append((x,y))
    d.line(pts, fill=BLUE, width=4)
    d.text((845, 503), 'SENSOR SIGNAL', font=font(18, True), fill=MUTED)
    save(img, 'predictive-maintenance-social.jpg')


def operational():
    img, d = base_card(
        'BYU HONORS · 2025–2026',
        ['Operational Mode', 'Discovery & Business', 'Value Analysis'],
        ['PCA, clustering, and time-series analysis for', 'interpretable operating-state discovery.']
    )
    d.line((845, 500, 1065, 500), fill='#8da0b3', width=2)
    d.line((845, 500, 845, 150), fill='#8da0b3', width=2)
    clusters = [
        ([(875,255),(900,235),(920,268),(940,220),(965,245),(900,290),(950,275)], BLUE),
        ([(965,185),(995,220),(1015,245),(1030,210),(1000,265),(970,240),(1020,235)], BLUE_MID),
        ([(960,365),(985,390),(1015,420),(1040,380),(995,445),(1030,430),(975,410)], BLUE_DARK),
    ]
    for pts, c in clusters:
        for x,y in pts: d.ellipse((x-7,y-7,x+7,y+7), fill=c)
    d.text((890, 510), 'reduced dimension 1', font=font(15), fill=MUTED)
    save(img, 'operational-mode-social.jpg')


def trainops():
    img, d = base_card(
        'HATCH URBAN SOLUTIONS · 2024',
        ['TrainOps Simulation', 'Data Engineering'],
        ['Python and C++ automation for 200k+ simulation', 'records, reducing processing time by ~70%.']
    )
    for y in range(140, 500, 70): d.line((840, y, 1070, y), fill='#d9e6f2', width=1)
    p1=[]; p2=[]
    for i in range(115):
        x=842+i*2
        p1.append((x, 315 + 45*math.sin(i/16.0) + 25*math.sin(i/7.0)))
        p2.append((x, 420 + 28*math.sin(i/18.0+1.2)))
    d.line(p1, fill=BLUE, width=4); d.line(p2, fill=BLUE_MID, width=4)
    d.text((845, 503), 'SIMULATION PROFILE', font=font(18, True), fill=MUTED)
    save(img, 'trainops-social.jpg')


def wildfire():
    img, d = base_card(
        'BYU · 2026',
        ['Wildfire Prediction', 'System'],
        ['Weather time-series, XGBoost, SHAP interpretability,', 'and API-driven risk scoring.']
    )
    vals=[0.20,0.45,0.28,0.52,0.55,0.17,0.10,0.33,0.62,0.38,0.07,0.12,0.48,0.57,0.18,0.08,0.22,0.31,0.06,0.04,0.16,0.13,0.03,0.02]
    x0,y0=845,135; s=47; gap=12
    for idx,v in enumerate(vals):
        r=idx//4; c=idx%4
        x=x0+c*(s+gap); y=y0+r*(s+gap)
        # blue risk scale consistent with the portfolio palette
        base=(235,241,255); target=(37,99,235)
        rgb=tuple(int(base[j]+(target[j]-base[j])*v) for j in range(3))
        d.rounded_rectangle((x,y,x+s,y+s), radius=9, fill=rgb, outline='#c8d8ea', width=1)
    d.text((845, 503), 'RISK GRID', font=font(18, True), fill=MUTED)
    save(img, 'wildfire-social.jpg')


if __name__ == '__main__':
    portfolio(); hatch(); predictive(); operational(); trainops(); wildfire()
    print(f'Generated social previews in {OUT}')

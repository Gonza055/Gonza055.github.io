from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 1200, 630
BG = '#f8fafc'
WHITE = '#ffffff'
INK = '#0f172a'
TEXT = '#334155'
MUTED = '#64748b'
BORDER = '#dbe4ee'
BLUE = '#2563eb'
BLUE_SOFT = '#eff6ff'

OUT = Path('assets/images/social')
REAL = Path('assets/images/real')
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


def paste_cover(canvas, path, box, position=(0.5, 0.5)):
    x1, y1, x2, y2 = box
    im = Image.open(path).convert('RGB')
    fitted = ImageOps.fit(im, (x2-x1, y2-y1), method=Image.Resampling.LANCZOS, centering=position)
    canvas.paste(fitted, (x1, y1))


def base_card(eyebrow, title_lines, subtitle_lines, image_path=None, footer='GONZALO LOAYZA  ·  PORTFOLIO'):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    rr(d, (70, 58, 1130, 572), radius=28)

    # Text area
    d.text((110, 100), eyebrow, font=font(23, True), fill=BLUE)
    y = draw_multiline(d, (110, 160), title_lines, font(49, True), INK, spacing=6)
    y += 18
    draw_multiline(d, (110, y), subtitle_lines, font(22), TEXT, spacing=4)
    d.text((110, 520), footer, font=font(17, True), fill=MUTED)

    # Real-evidence image panel
    panel = (765, 88, 1095, 542)
    rr(d, panel, radius=22, fill=BLUE_SOFT, outline='#bfd7f0', width=2)
    if image_path and Path(image_path).exists():
        paste_cover(img, image_path, panel)
        # Redraw border over the image
        d.rounded_rectangle(panel, radius=22, outline='#bfd7f0', width=2)
    return img, d


def save(img, name):
    img.save(OUT / name, quality=88, optimize=True, progressive=True)


def portfolio():
    img, d = base_card(
        'COMPUTER SCIENCE @ BYU',
        ['Data, ML, and software', 'for real-world systems'],
        ['Machine Learning · Data Engineering · Industrial', 'Analytics · Decision Support'],
        REAL / 'hatch-control-room.webp'
    )
    save(img, 'portfolio-social.jpg')


def hatch():
    img, d = base_card(
        'HATCH DIGITAL · 2026',
        ['Data Engineering &', 'Decision Support'],
        ['Drones · HITM · SIC', 'From reliable information to operational action.'],
        REAL / 'hatch-presentation-hitm.webp'
    )
    save(img, 'hatch-digital-social.jpg')


def predictive():
    img, d = base_card(
        'BUENAVENTURA · 2025',
        ['Predictive Maintenance &', 'Reliability Analytics'],
        ['50k+ industrial time-series · 15+ engineered features', '100+ assets structured for reliability analysis'],
        REAL / 'buenaventura-site.webp'
    )
    save(img, 'predictive-maintenance-social.jpg')


def operational():
    img, d = base_card(
        'BYU HONORS · 2025–2026',
        ['Operational Mode', 'Discovery'],
        ['Industrial time-series · PCA · DBSCAN', 'Three recurrent operating regimes'],
        REAL / 'thesis-regimes.webp'
    )
    save(img, 'operational-mode-social.jpg')


def trainops():
    img, d = base_card(
        'HATCH URBAN SOLUTIONS · 2024',
        ['TrainOps Simulation', 'Data Engineering'],
        ['Python + C++ · 200k+ simulation records', '~70% reduction in output-processing time'],
        'assets/images/projects/trainops-caps-009-2.webp'
    )
    save(img, 'trainops-social.jpg')


def wildfire():
    img, d = base_card(
        'BYU · 2026',
        ['Wildfire Prediction', 'System'],
        ['7-day weather histories · XGBoost · Utah risk maps', 'Satellite-image retrieval for prioritized locations'],
        REAL / 'wildfire-team.webp'
    )
    save(img, 'wildfire-social.jpg')


if __name__ == '__main__':
    portfolio(); hatch(); predictive(); operational(); trainops(); wildfire()
    print(f'Generated social previews in {OUT}')

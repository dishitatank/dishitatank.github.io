import platform
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    KeepTogether, Table, TableStyle
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# --- DYNAMIC FONT CONFIGURATION ---
if platform.system() == "Linux":
    # Paths for GitHub Actions (Ubuntu)
    font_dir = "/usr/share/fonts/truetype/msttcorefonts/"
    v_reg = os.path.join(font_dir, "Verdana.ttf")
    v_bold = os.path.join(font_dir, "Verdana_Bold.ttf")
    v_ital = os.path.join(font_dir, "Verdana_Italic.ttf")
else:
    # Paths for your Local Mac
    font_dir = "/System/Library/Fonts/Supplemental/"
    v_reg = os.path.join(font_dir, "Verdana.ttf")
    v_bold = os.path.join(font_dir, "Verdana Bold.ttf")
    v_ital = os.path.join(font_dir, "Verdana Italic.ttf")

pdfmetrics.registerFont(TTFont("Verdana",        v_reg))
pdfmetrics.registerFont(TTFont("Verdana-Bold",   v_bold))
pdfmetrics.registerFont(TTFont("Verdana-Italic", v_ital))
# -----------------------------------------------

OUTPUT = "DishitaTank_Resume.pdf"
W, H = A4

BLACK = colors.HexColor("#0A0A0A")
DGRAY = colors.HexColor("#2C2C2C")
MGRAY = colors.HexColor("#5A5A5A")
LGRAY = colors.HexColor("#A0A0A0")
RULE  = colors.HexColor("#BBBBBB")
LINK  = colors.HexColor("#1a0dab")

def PS(n, **k): return ParagraphStyle(n, **k)

s_name  = PS("nm",  fontName="Verdana-Bold",   fontSize=20, textColor=BLACK, leading=26, spaceAfter=3,  alignment=TA_CENTER)
s_ct    = PS("ct",  fontName="Verdana",         fontSize=7.5,textColor=MGRAY, leading=12, spaceAfter=1,  alignment=TA_CENTER)
s_sec   = PS("sc",  fontName="Verdana-Bold",    fontSize=8,  textColor=BLACK, leading=11, spaceBefore=8, spaceAfter=2, alignment=TA_LEFT)
s_jobt  = PS("jt",  fontName="Verdana-Bold",    fontSize=8.5,textColor=BLACK, leading=13, spaceAfter=0)
s_date  = PS("dt",  fontName="Verdana-Italic",  fontSize=7.5,textColor=MGRAY, leading=13, alignment=TA_RIGHT)
s_co    = PS("co",  fontName="Verdana-Italic",  fontSize=7.5,textColor=MGRAY, leading=12, spaceAfter=3)
s_bul   = PS("bl",  fontName="Verdana",         fontSize=7.5,textColor=DGRAY, leading=13, leftIndent=12, firstLineIndent=-6, spaceAfter=2)
s_body  = PS("bd",  fontName="Verdana",         fontSize=7.5,textColor=DGRAY, leading=13, spaceAfter=4)
s_skk   = PS("skk", fontName="Verdana-Bold",    fontSize=7.5,textColor=BLACK, leading=12)
s_skv   = PS("skv", fontName="Verdana",         fontSize=7.5,textColor=DGRAY, leading=12)
s_cert  = PS("cr",  fontName="Verdana-Bold",    fontSize=7.5,textColor=BLACK, leading=12, spaceAfter=0)
s_cerd  = PS("cd",  fontName="Verdana",         fontSize=7.5,textColor=DGRAY, leading=12, spaceAfter=4)
s_link  = PS("lk",  fontName="Verdana",         fontSize=7,  textColor=LINK,  leading=11, spaceAfter=3)

def thick_rule():
    return HRFlowable(width="100%", thickness=1.2, color=BLACK, spaceAfter=5, spaceBefore=1)

def thin_rule():
    return HRFlowable(width="100%", thickness=0.4, color=RULE, spaceAfter=4, spaceBefore=2)

def sec_header(title):
    return [Spacer(1, 4), Paragraph(title, s_sec), thick_rule()]

def bul(text):
    return Paragraph(f"\u2022  {text}", s_bul)

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    title="DishitaTank_Resume", # Add this line
    leftMargin=20*mm,
    rightMargin=20*mm,
    topMargin=16*mm,
    bottomMargin=16*mm
)
PW = W - 40*mm
story = []

# ── HEADER ─────────────────────────────────────────────────────────────────────
story.append(Paragraph("DISHITA RUPESH TANK", s_name))
story.append(Paragraph(
    "Ahmedabad, Gujarat  |  7096919019  |  tank.dishita@gmail.com  |  "
    "linkedin.com/in/dishitatank  |  github.com/dishitatank",
    s_ct))
story.append(HRFlowable(width="100%", thickness=2,   color=BLACK, spaceAfter=2, spaceBefore=6))
story.append(HRFlowable(width="100%", thickness=0.5, color=BLACK, spaceAfter=6, spaceBefore=1))

# ── PROFILE ────────────────────────────────────────────────────────────────────
story += sec_header("PROFESSIONAL PROFILE")
story.append(Paragraph(
    "Computer Engineering graduate from Marwadi University with a dual track in backend development "
    "and technical project coordination. Experienced in building scalable RESTful APIs using Python, "
    "Django, and FastAPI, and in managing cross-functional delivery using Agile methodologies. "
    "Currently driving project coordination at AddWeb Solutions, Ahmedabad, with a focus on aligning "
    "engineering teams with stakeholder goals. Seeking to grow in a role that bridges technology and "
    "project delivery within a fast-paced product or tech services environment.",
    s_body))

# ── SKILLS ─────────────────────────────────────────────────────────────────────
story += sec_header("TECHNICAL SKILLS")
skills = [
    ("Languages",    "Python, Java, C, C++, C#, SQL"),
    ("Frameworks",   "Django, Django REST Framework (DRF), FastAPI"),
    ("Databases",    "MySQL, PostgreSQL, MongoDB"),
    ("Tools & IDEs", "Git, Tableau, Streamlit, Celery, Redis, VS Code, Jupyter Notebook"),
    ("Concepts",     "Data Structures, OOP, DBMS, SDLC, Agile Methodologies, REST APIs"),
    ("PM Skills",    "Stakeholder Communication, Workflow Optimisation, Team Leadership"),
]
for k, v in skills:
    row = Table([[Paragraph(k, s_skk), Paragraph(v, s_skv)]], colWidths=[40*mm, PW - 40*mm])
    row.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2),
        ("LINEBELOW",(0,0),(-1,0),0.3,RULE),
    ]))
    story.append(row)

# ── EXPERIENCE ─────────────────────────────────────────────────────────────────
story += sec_header("PROFESSIONAL EXPERIENCE")

def job(title, co, period, loc, bullets):
    def hdr_row():
        t = Table([[Paragraph(title, s_jobt), Paragraph(period, s_date)]], colWidths=[PW-42*mm, 42*mm])
        t.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"BOTTOM"),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
        ]))
        return t
    blk = [hdr_row(), Paragraph(co + ("  —  " + loc if loc else ""), s_co)]
    for b in bullets: blk.append(bul(b))
    blk += [Spacer(1,3), thin_rule()]
    story.append(KeepTogether(blk))

job("Technical Project Coordinator", "AddWeb Solutions", "Feb 2026 – Present", "Ahmedabad", [
    "Coordinate cross-functional communication between development teams and stakeholders, ensuring technical requirements are accurately translated into project deliverables.",
    "Drive SDLC management and apply Agile methodologies to streamline sprint planning and enable on-time delivery of web and mobile solutions.",
    "Lead project documentation, monitor KPIs, and proactively surface blockers to keep delivery on schedule.",
])
job("Python Developer Intern", "Simform", "Jan 2025 – Jul 2025", "Ahmedabad", [
    "Designed and implemented scalable RESTful APIs using Python, Django, and FastAPI, improving endpoint response efficiency by over 20%.",
    "Collaborated with senior engineers on full-stack development tasks; applied Git version control and DBMS best practices throughout.",
])
job("Student Research Intern", "Marwadi University", "May 2024 – Jun 2024", "Rajkot", [
    "Developed a Kidney Tumor, Cyst and Stone Detector and Classifier using SMOTE and machine learning algorithms, achieving over 90% classification accuracy.",
    "Designed end-to-end data preprocessing and model training pipelines; presented findings to the faculty review panel.",
])
job("Java Developer Intern", "Sampaarsh Technology", "Jun 2023", "Rajkot", [
    "Built a comprehensive Billing System using Java Swing, JDBC, and MySQL for efficient real-time customer and invoice management.",
    "Designed both the user interface and backend logic to handle data storage and retrieval with minimal latency.",
])

# ── PROJECTS — header locked inside first KeepTogether ────────────────────────
def proj(name, stack, bullets, github=None, include_section_header=False):
    blk = []
    if include_section_header:
        blk += sec_header("PROJECTS")
    blk += [Paragraph(name, s_jobt), Paragraph(stack, s_co)]
    if github:
        blk.append(Paragraph(f'<link href="{github}" color="#1a0dab">{github}</link>', s_link))
    for b in bullets: blk.append(bul(b))
    blk += [Spacer(1,3), thin_rule()]
    story.append(KeepTogether(blk))

proj("Expense Tracker",
     "Django · Django REST Framework · PostgreSQL · Celery · Redis · Bootstrap 5 · JWT",
     [
        "Developed a full-stack responsive expense tracking application with secure JWT authentication and real-time notifications via Celery and Redis.",
        "Designed a dynamic Bootstrap 5 dashboard for financial data visualisation and user account management.",
     ],
     github="https://github.com/dishitatank/ExpenseTracker",
     include_section_header=True)

proj("Jute Pest Image Classifier",
     "MobileNet · TensorFlow · Streamlit",
     [
        "Achieved 96% accuracy in pest detection and classification using the MobileNet architecture on a custom jute pest image dataset.",
        "Deployed the trained model as a Streamlit web application for practical use by agricultural field workers.",
     ],
     github="https://github.com/dishitatank/Jute-Pest-Detection-Classification-Model")

proj("Attendance Tracker", "JSP · MySQL", [
    "Engineered a web-based attendance management system to track and query student and employee records with high efficiency.",
])

# ── EDUCATION ──────────────────────────────────────────────────────────────────
story += sec_header("EDUCATION")
edu = Table([
    [Paragraph("<b>Bachelor of Technology — Computer Engineering</b>", s_skv), Paragraph("Sep 2021 – May 2025", s_date)],
    [Paragraph("Marwadi University, Rajkot", s_co), Paragraph("", s_co)],
    [Paragraph('CPI: <b>8.03 / 10.0</b>', s_skv), Paragraph("", s_co)],
    [Spacer(1, 4), Paragraph("", s_co)],
    [Paragraph("<b>ISC Class 12 (Science Stream)</b>", s_skv), Paragraph("2009 – 2021", s_date)],
    [Paragraph("SNK School, Rajkot", s_co), Paragraph("", s_co)],
    [Paragraph('ISC Score: <b>85%</b>  ·  ICSE Score: <b>83%</b>', s_skv), Paragraph("", s_co)],
], colWidths=[PW-40*mm, 40*mm])
edu.setStyle(TableStyle([
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),1),
]))
story.append(edu)
story.append(thin_rule())

# ── CERTIFICATIONS ─────────────────────────────────────────────────────────────
story += sec_header("CERTIFICATIONS & PROFESSIONAL DEVELOPMENT")
certs = [
    ("Infosys SpringBoard", "Real-World Projects with Flutter  ·  Tableau BootCamp  ·  Machine Learning with SciKit-Learn"),
    ("University of Michigan (Coursera)", "Programming for Everybody (Getting Started with Python)  ·  Python Data Structures"),
    ("Oracle Academy",              "Database Programming with SQL"),
    ("NISM / SEBI",                 "National Financial Literacy Quiz 2024 — Gold Medalist"),
    ("HP Life / LinkedIn Learning", "AI For Beginners  ·  How to Speak with Effortless Confidence"),
]
for t, d in certs:
    story.append(Paragraph(t, s_cert))
    story.append(Paragraph(d, s_cerd))

story.append(Paragraph(
    'Full Certificates: <link href="https://drive.google.com/drive/u/0/folders/1W4fSAVo6wOVSNYDPSJFN7Uqo5an5z9ky" color="#1a0dab">Google Drive</link>',
    s_link))
story.append(thin_rule())

# ── ACHIEVEMENTS ───────────────────────────────────────────────────────────────
story += sec_header("ACHIEVEMENTS & LEADERSHIP")
for a in [
    "<b>MU Fest 2024 — Core Team Member:</b> Managed a team of 600+ members and coordinated registrations for over 8,000 participants.",
    "<b>Class Representative — All Semesters:</b> Elected as the student-faculty liaison for every semester of the undergraduate programme.",
    "<b>Interdepartmental Cricket League:</b> Awarded Most Valuable Player (MVP) and Player of the Match.",
    "<b>State Football Championship:</b> Represented the institution as a participant in the state-level tournament.",
]:
    story.append(Paragraph(f"\u2022  {a}", s_bul))

doc.build(story)
print("Done! Saved as:", OUTPUT)
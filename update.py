from bs4 import BeautifulSoup
from pathlib import Path

root=Path('/mnt/data/sitework')

common_benefits='''<section class="benefits"><div class="container benefit-grid"><div class="benefit"><div class="benefit-icon">♢</div><div><strong>Quality Glass</strong><p>Quality auto glass that meets safety standards.</p></div></div><div class="benefit"><div class="benefit-icon">♙</div><div><strong>Expert Technicians</strong><p>Experienced technicians and proper installation.</p></div></div><div class="benefit"><div class="benefit-icon">▣</div><div><strong>Mobile Service</strong><p>We come to you at home, work or another location.</p></div></div><div class="benefit"><div class="benefit-icon">◇</div><div><strong>Safe & Reliable</strong><p>Professional replacement focused on road safety.</p></div></div><div class="benefit"><div class="benefit-icon">♧</div><div><strong>Satisfaction</strong><p>We stand behind our replacement workmanship.</p></div></div></div></section>'''

def replace_benefits(soup, html):
    old=soup.select_one('section.benefits')
    if old: old.replace(BeautifulSoup(html,'html.parser').section)

def add_photo_grid(soup, heading, eyebrow, cards):
    sec=BeautifulSoup(f'''<section class="section photo-section"><div class="container"><div class="section-head"><div class="eyebrow">{eyebrow}</div><h2>{heading}</h2></div><div class="service-photo-grid">{''.join(f'''<article class="service-photo"><img src="assets/{img}" alt="{alt}" loading="lazy"><div><h3>{title}</h3><p>{text}</p></div></article>''' for img,alt,title,text in cards)}</div></div></section>''','html.parser').section
    # insert before benefits
    b=soup.select_one('section.benefits')
    b.insert_before(sec)

# About
p=root/'about-us.html'; soup=BeautifulSoup(p.read_text(),'html.parser')
hero=soup.select_one('section.hero'); hero['class'] += ['page-about']
add_photo_grid(soup,'More Than a Trip to the Glass Shop','Why Mobile Service',[
 ('mobile-van.jpg','Santa Monica Car Glass Repair mobile service van','Mobile Service','We bring replacement service to a convenient location whenever possible.'),
 ('windshield.jpg','Technician installing a replacement windshield','Windshield Replacement','Professional windshield replacement for many makes and models.'),
 ('auto-glass.jpg','Technician replacing a vehicle side window','Vehicle Glass','Side, rear and quarter glass replacement for your vehicle.')])
replace_benefits(soup,common_benefits); p.write_text(str(soup),encoding='utf-8')

# Services
p=root/'services.html'; soup=BeautifulSoup(p.read_text(),'html.parser')
hero=soup.select_one('section.hero'); hero['class'] += ['page-services']
# add visual grid before benefits
add_photo_grid(soup,'Our Replacement Services','Auto Glass Options',[
 ('windshield.jpg','Windshield replacement technician at work','Windshield Replacement','A complete replacement service focused on fit, seal and road-ready installation.'),
 ('auto-glass.jpg','Technician replacing a side window','Side Window Replacement','Replacement service for damaged door and side glass.'),
 ('mobile-van.jpg','Mobile auto glass service vehicle','Mobile Auto Glass','Convenient service at home, work or another suitable location.')])
replace_benefits(soup,common_benefits); p.write_text(str(soup),encoding='utf-8')

# Locations
locations={
 'windshield-repair-in-westwood.html':('page-westwood','Westwood Auto Glass Service','westwood','windshield.jpg','Westwood','Windshield Replacement in Westwood','Convenient mobile windshield and auto glass replacement for drivers around Westwood.','Windshield Replacement','Professional windshield replacement service for Westwood drivers.','auto-glass.jpg','Side & Rear Glass','Replacement for side windows, rear windows and other vehicle glass.','mobile-van.jpg','Mobile Service','We come to a convenient location instead of requiring a shop visit.'),
 'windshield-repair-in-beverly-hills.html':('page-beverly','Beverly Hills Auto Glass Service','beverly','auto-glass.jpg','Beverly Hills','Auto Glass Replacement in Beverly Hills','Mobile auto glass replacement for drivers in Beverly Hills, with convenient scheduling and professional installation.','Auto Glass Replacement','Side window, rear window and quarter glass replacement in Beverly Hills.','windshield.jpg','Windshield Replacement','Replacement windshield service for many makes and models.','mobile-van.jpg','Mobile Service','We bring the service to your home, office or another convenient location.'),
 'windsheild-repair-in-hollywood.html':('page-hollywood','Hollywood Auto Glass Service','hollywood','mobile-van.jpg','Hollywood','Mobile Auto Glass Replacement in Hollywood','Convenient mobile windshield and vehicle glass replacement serving Hollywood and nearby communities.','Mobile Replacement','Mobile windshield and auto glass replacement at a convenient location.','windshield.jpg','Windshield Service','Professional windshield replacement for many vehicle makes and models.','auto-glass.jpg','Vehicle Glass','Replacement options for side, rear and quarter glass.')
}
for fn,(cls,eyebrow,slug,img,city,h1,desc,t1,t1d,img2,t2,t2d,img3,t3,t3d) in locations.items():
    p=root/fn; soup=BeautifulSoup(p.read_text(),'html.parser')
    hero=soup.select_one('section.hero'); hero['class'] += [cls]
    # Replace generic first content section with unique location layout while keeping existing location SEO content concise.
    first=soup.select_one('main > section.section')
    new=BeautifulSoup(f'''<section class="section location-intro"><div class="container location-layout"><div class="location-copy"><div class="eyebrow">{eyebrow}</div><h2>{h1}</h2><p>{desc}</p><p>Our mobile service is designed to make replacement easier by coming to a convenient location in or around {city}. Call us with your vehicle information to discuss your replacement needs.</p><div class="actions"><a class="btn call" href="tel:3109060066">Call (310) 906-0066</a><a class="btn alt dark-alt" href="contact-us.html">Request an Estimate</a></div></div><div class="location-photo"><img src="assets/{img}" alt="{city} auto glass replacement service" loading="lazy"></div></div></section>''','html.parser').section
    first.replace_with(new)
    # Remove old duplicate about-band section, if present, then add unique gallery before benefits.
    for s in list(soup.select('main > section.about-band')): s.decompose()
    add_photo_grid(soup,f'Auto Glass Services in {city}','Services Available',[
        (img,'Auto glass technician serving '+city,t1,t1d),
        (img2,'Auto glass replacement service in '+city,t2,t2d),
        (img3,'Mobile auto glass service near '+city,t3,t3d)])
    replace_benefits(soup,common_benefits)
    p.write_text(str(soup),encoding='utf-8')

# Contact
p=root/'contact-us.html'; soup=BeautifulSoup(p.read_text(),'html.parser')
hero=soup.select_one('section.hero'); hero['class'] += ['page-contact']
# Add photos below form section and replace map section with visual contact panel.
for s in list(soup.select('main > section.about-band')): s.decompose()
add_photo_grid(soup,'Mobile Service Makes It Easier','Before You Call',[
 ('mobile-van.jpg','Santa Monica Car Glass Repair mobile service van','We Come to You','Tell us where you need service and we can discuss scheduling.'),
 ('windshield.jpg','Windshield replacement technician','Windshield Replacement','Have a damaged windshield? Call for an estimate and appointment.'),
 ('auto-glass.jpg','Technician replacing a vehicle window','Auto Glass Replacement','We also replace side, rear and quarter glass.')])
# Benefits add to contact page too, after photos
replace_benefits(soup,common_benefits)
p.write_text(str(soup),encoding='utf-8')

# CSS additions
css=root/'assets/site.css'
with css.open('a',encoding='utf-8') as f:
    f.write('''\n/* Page-specific imagery and layouts */\n.hero.page-about{background-image:url("mobile-van.jpg");background-position:center 55%}\n.hero.page-services{background-image:url("windshield.jpg");background-position:center 45%}\n.hero.page-westwood{background-image:url("windshield.jpg");background-position:center 50%}\n.hero.page-beverly{background-image:url("auto-glass.jpg");background-position:center 48%}\n.hero.page-hollywood{background-image:url("mobile-van.jpg");background-position:center 45%}\n.hero.page-contact{background-image:url("auto-glass.jpg");background-position:center 45%}\n.location-layout{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:stretch}\n.location-copy{padding:16px 0}\n.location-copy h2{font-size:clamp(2rem,4vw,3rem);margin:0 0 14px;line-height:1.08}\n.location-photo{min-height:360px;border-radius:9px;overflow:hidden;box-shadow:var(--shadow);border:1px solid var(--line);background:#e9eef3}\n.location-photo img{width:100%;height:100%;min-height:360px;display:block;object-fit:cover}\n.dark-alt{background:#fff!important;color:var(--blue)!important}\n.photo-section{background:#fff}\n.photo-section:nth-of-type(even){background:var(--soft)}\n.service-photo{transition:transform .2s ease,box-shadow .2s ease}\n.service-photo:hover{transform:translateY(-3px);box-shadow:0 14px 30px rgba(15,44,78,.12)}\n@media(max-width:780px){.location-layout{grid-template-columns:1fr;gap:25px}.location-photo,.location-photo img{min-height:260px;height:260px}.hero.page-about,.hero.page-services,.hero.page-westwood,.hero.page-beverly,.hero.page-hollywood,.hero.page-contact{background-position:center}}\n''')

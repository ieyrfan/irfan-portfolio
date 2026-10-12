from pathlib import Path
import re

p = Path(__file__).parent / 'index.html'
s = p.read_text(encoding='utf-8')
s = s.replace('family=Space+Grotesk:wght@400;500;600;700', 'family=Manrope:wght@400;500;600;700;800')
s = s.replace('style.css?v=2', 'style.css?v=3')
s = s.replace('<body>', '<body>\n  <a class="skip-link" href="#projects">Skip to projects</a>')
nav = '''<nav class="navbar" id="navbar" aria-label="Main navigation">
    <div class="container nav-inner">
      <a href="#top" class="brand" aria-label="Irfan Rizal home"><span class="brand-logo">ir<span>↗</span></span><span class="brand-name">irfan rizal<span class="brand-period">.</span></span></a>
      <div class="nav-links" id="navLinks">
        <a href="#projects" class="is-current">Work <span>01</span></a><a href="#about">About <span>02</span></a><a href="#skills">Expertise <span>03</span></a><a href="#services">Services <span>04</span></a><a href="#contact" class="nav-cta">Let’s talk <span>↗</span></a>
      </div>
      <div class="nav-actions">
        <button id="commandToggle" class="icon-btn command-trigger" aria-label="Open quick navigation" title="Quick navigation (Ctrl+K)"><i class="fa-solid fa-command" aria-hidden="true"></i><span>⌘ K</span></button>
        <button id="themeToggle" class="icon-btn" aria-label="Switch to light theme" title="Switch theme"><i class="fa-solid fa-sun" aria-hidden="true"></i></button>
        <button id="menuToggle" class="icon-btn menu-btn" aria-label="Open navigation menu" aria-controls="navLinks" aria-expanded="false"><i class="fa-solid fa-bars" aria-hidden="true"></i></button>
      </div>
    </div>
  </nav>'''
s = re.sub(r'<nav class="navbar".*?</nav>', lambda _: nav, s, count=1, flags=re.S)
hero = '''<section class="hero" aria-labelledby="heroTitle">
      <div class="container">
        <div class="hero-topline"><span class="mono-label">PORTFOLIO / 2026</span><span class="location-label"><span class="small-cross">+</span> MELAKA, MY <span id="localTime">UTC+08</span></span></div>
        <div class="hero-grid">
          <div class="hero-content">
            <div class="status-badge"><span class="pulse-dot"></span> Available for internships &amp; opportunities</div>
            <h1 id="heroTitle" class="hero-title"><span class="title-line">Building cloud.</span><span class="title-line">Thinking <em>secure.</em></span></h1>
            <p class="hero-lead">I’m Irfan. A cloud computing student turning complex infrastructure into thoughtful, secure digital experiences.</p>
            <div class="hero-actions"><a class="btn btn-primary" href="#projects">Explore my work <span class="button-arrow">↗</span></a><a class="btn btn-text" href="./asset/Muhammad_Irfan_Resume.pdf" download>Download CV <i class="fa-solid fa-arrow-down" aria-hidden="true"></i></a></div>
            <div class="hero-person"><span class="person-avatar" aria-hidden="true">MI</span><div><strong>Muhammad Irfan Bin Rizal</strong><span>B.Tech Cloud Computing · UTeM</span></div><span class="person-mark" aria-hidden="true">↗</span></div>
          </div>
          <div class="hero-side">
            <div class="orbital-stage">
              <div class="scene-header"><span><span class="tiny-dot"></span> THE CONNECTED WORLD</span><span>FIG. 001</span></div>
              <div class="scene-grid" aria-hidden="true"></div>
              <canvas id="orbitalCanvas" aria-hidden="true"></canvas>
              <span class="scene-coordinate coord-top" aria-hidden="true">03° N / 102° E</span><span class="scene-coordinate coord-side" aria-hidden="true">IDEAS WITHOUT BORDERS</span>
              <div class="orbit-label orbit-label-cloud" aria-hidden="true"><i class="fa-solid fa-cloud"></i><span>CLOUD<br><small>ARCHITECTURE</small></span></div>
              <div class="orbit-label orbit-label-secure" aria-hidden="true"><i class="fa-solid fa-shield-halved"></i><span>SECURITY<br><small>BY DESIGN</small></span></div>
              <div class="scene-caption"><span class="scene-cross" aria-hidden="true">✳</span><div><strong id="sceneTitle">Cloud architecture</strong><span id="sceneDescription">Connected by design.</span></div><span class="scene-caption-index">01 / 03</span></div>
            </div>
            <div class="scene-controls" role="group" aria-label="Explore the orbital visual"><button class="scene-mode" data-scene="cloud" aria-pressed="true">01 Cloud</button><button class="scene-mode" data-scene="security" aria-pressed="false">02 Security</button><button class="scene-mode" data-scene="systems" aria-pressed="false">03 Systems</button><button id="motionToggle" class="motion-toggle" aria-label="Pause animations" aria-pressed="false" title="Pause animations"><i class="fa-solid fa-pause" aria-hidden="true"></i></button></div>
          </div>
        </div>
        <div class="hero-bottom"><a href="#projects" class="scroll-cue"><span>↓</span> SCROLL TO EXPLORE</a><p>Cloud architecture <span>·</span> Cyber defense <span>·</span> Creative development</p><span class="hero-edition">DESIGNED TO GO FURTHER ↗</span></div>
      </div>
    </section>
    <div class="stack-ribbon" aria-label="Technology toolkit"><div class="container stack-ribbon-inner"><span class="mono-label">THE TOOLKIT</span><span><i class="fa-brands fa-aws" aria-hidden="true"></i> AWS</span><span><i class="fa-brands fa-microsoft" aria-hidden="true"></i> Azure</span><span><i class="fa-solid fa-layer-group" aria-hidden="true"></i> OpenStack</span><span><i class="fa-brands fa-python" aria-hidden="true"></i> Python</span><span><i class="fa-brands fa-docker" aria-hidden="true"></i> Docker</span><span><i class="fa-brands fa-linux" aria-hidden="true"></i> Linux</span></div></div>'''
s = re.sub(r'<section class="hero">.*?</section>', lambda _: hero, s, count=1, flags=re.S)

sections = {m.group(1):m.group(0) for m in re.finditer(r'<section id="([^"]+)".*?</section>', s, flags=re.S)}
projects = sections['projects']
articles = re.findall(r'<article\b.*?</article>', projects, re.S)
def title(a): return re.search(r'<h3[^>]*>(.*?)</h3>', a, re.S).group(1)
by_title = {title(a):a for a in articles}
def preview(kind):
    if kind == 'aegis':
        return '''<div class="project-visual visual-aegis" aria-hidden="true"><div class="visual-topline"><span>AEGIS / CYBER DEFENSE</span><span>INTERFACE STUDY ↗</span></div><div class="mini-dashboard"><div class="mini-sidebar"><b>Æ</b><span>◈</span><span>▤</span><span>◎</span><span>⌘</span></div><div class="mini-content"><div class="mini-nav">Security overview <span>● WORKSPACE</span></div><div class="mini-panels"><div class="radar-display"><span></span><i></i><b></b></div><div class="mini-events"><span>THREAT LIFECYCLE</span><p><i></i> Identify signals</p><p><i></i> Investigate events</p><p><i></i> Orchestrate response</p><div class="mini-bars"><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b><b></b></div></div></div></div></div><span class="visual-bottomline">VISIBILITY. CONTEXT. CONTROL.</span></div>'''
    return '''<div class="project-visual visual-niyyah" aria-hidden="true"><div class="visual-topline"><span>NIYYAH / EVERYDAY FAITH</span><span>INTERFACE STUDY ↗</span></div><div class="niyyah-art"><div class="niyyah-copy"><span>A LITTLE INTENTION.</span><strong>A deeper<br>connection.</strong><span>YOUR FAITH. YOUR EVERYDAY.</span></div><div class="niyyah-phone"><div class="phone-notch"></div><div class="phone-nav">niyyah<span>☾</span></div><div class="phone-greeting">Assalamualaikum.</div><div class="phone-arch"><span>بِسْمِ اللَّهِ</span><small>Begin with intention.</small></div><div class="phone-tiles"><span>☷<small>Al-Quran</small></span><span>◷<small>Prayer</small></span><span>♡<small>Community</small></span></div><div class="phone-bottom">A meaningful moment, every day.</div></div></div></div>'''
featured=[]
for number,(name,kind) in enumerate([('AEGIS Cyber Dashboard','aegis'),('NIYYAH','niyyah')],1):
    a=by_title[name]
    body=re.sub(r'^<article[^>]*>|</article>$','',a).strip()
    body=re.sub(r'<div class="card-icon".*?</div>', '', body, count=1, flags=re.S)
    featured.append(f'<article class="project-card featured-project reveal" data-category="{"security" if kind=="aegis" else "apps"}">{preview(kind)}<div class="project-body"><div class="project-number">SELECTED PROJECT / 0{number}</div>{body}</div></article>')
archive=[]; lab=[]
for a in articles:
    name=title(a)
    if name in ('AEGIS Cyber Dashboard','NIYYAH'): continue
    if 'tool-card' in a: lab.append(a); continue
    category='security' if any(x in name for x in ['Threat','Governance','Security']) else 'cloud' if any(x in name for x in ['Omniverse','AMERTA','SmartChef']) else 'apps'
    a=re.sub(r'class="project-card[^"]*"',f'class="project-card archive-project reveal" data-category="{category}"',a,count=1)
    archive.append(a)
project_head='''<section id="projects" class="section"><div class="container"><div class="section-head section-head-row reveal"><div><p class="section-eyebrow">01 / SELECTED WORK</p><h2 class="section-title">From ideas.<br>To <em>real things.</em></h2></div><div class="section-aside"><p>Experiments, platforms, and systems.<br>A look at what I’ve been building.</p><a class="text-link" href="https://github.com/ieyrfan" target="_blank" rel="noopener noreferrer">Explore GitHub <span>↗</span></a></div></div><div class="project-filters" role="group" aria-label="Filter projects"><button class="filter-btn" data-filter="all" aria-pressed="true">All work <span>14</span></button><button class="filter-btn" data-filter="cloud" aria-pressed="false">Cloud &amp; infrastructure</button><button class="filter-btn" data-filter="security" aria-pressed="false">Cybersecurity</button><button class="filter-btn" data-filter="apps" aria-pressed="false">Applications</button></div><p id="projectFilterStatus" class="sr-only" role="status"></p>'''
sections['projects']=project_head+'<div class="featured-grid">'+''.join(featured)+'</div><div class="archive-heading"><span class="mono-label">MORE THINGS I’VE BUILT</span><span class="mono-label">THE PROJECT INDEX ↙</span></div><div class="projects-grid">'+''.join(archive)+'</div></div></section>'
sections['lab']='''<section id="lab" class="section section-alt"><div class="container"><div class="section-head section-head-row reveal"><div><p class="section-eyebrow">THE PLAYGROUND</p><h2 class="section-title">Less scrolling.<br><em>More trying.</em></h2></div><p class="section-aside">Small tools, right here in your browser.<br>Go on, give them a spin.</p></div><div class="lab-grid">'''+''.join(lab)+'</div></div></section>'
sections['about']='''<section id="about" class="section"><div class="container about-layout"><div class="about-portrait reveal"><div class="about-monogram" aria-hidden="true">IRFAN.</div><div class="portrait-caption"><span>A BUILDER AT HEART.</span><span>MY ↗</span></div><span class="portrait-stamp" aria-hidden="true">CURIOUS BY NATURE<br>PRECISE BY PRACTICE</span></div><div class="about-copy reveal"><p class="section-eyebrow">02 / THE PERSON BEHIND THE PROJECTS</p><h2 class="section-title">Curiosity is<br>my <em>default setting.</em></h2><p class="about-intro">I like understanding how things work.<br>Then figuring out how to make them better.</p><p>I’m Muhammad Irfan, a B.Tech Cloud Computing student at Universiti Teknikal Malaysia Melaka. My journey started with IT system support at KV Besut and grew into cloud architecture, cybersecurity, and building applications.</p><p>From private clouds on OpenStack to serverless systems on AWS, I connect the infrastructure underneath with the experience people actually use.</p><div class="about-links"><a class="text-link" href="#programs">Follow my journey <span>↗</span></a><button class="text-link" onclick="downloadVCard()">Save my contact <span>↓</span></button></div><div class="hero-stats"><div class="stat-box"><strong data-count="12" data-suffix="+">12+</strong><span>Repositories</span></div><div class="stat-box"><strong data-count="4">4</strong><span>Skill domains</span></div><div class="stat-box"><strong data-count="21">21</strong><span>Certifications</span></div></div></div></div></section>'''
sections['skills']=sections['skills'].replace('Capabilities','03 / CAPABILITIES').replace('Technical Skill Domains','Different layers.<br>One <em>connected mindset.</em>').replace('Specializing across four technology domains.','From the network to the application. The tools and thinking behind my work.')
sections['services']=sections['services'].replace('>Freelance<','>04 / FUNTECHZ DIGITAL SERVICES<').replace('FunTechz Digital Services</h2>','Your next idea.<br><em>Let’s make it happen.</em></h2>')
sections['programs']=sections['programs'].replace('>Experience<','>THE JOURNEY<').replace('Programs & Activities','Always learning.<br><em>Always building.</em>')
sections['certs']=sections['certs'].replace('Technical Skills & Certifications','Learning with <em>intention.</em>')
sections['insights']=sections['insights'].replace('System Design & Insights','Under the <em>surface.</em>')
# Keep every credential while making the long list easier to browse.
cert=sections['certs']; certitems=list(re.finditer(r'<div class="cert-item">.*?</h4><p>.*?</p></div></div>',cert,re.S))
if len(certitems)>5:
    begin=certitems[5].start(); end=certitems[-1].end()
    cert=cert[:begin]+'<details class="credential-details"><summary>Explore all 21 certifications <span>+</span></summary>'+cert[begin:end]+'</details>'+cert[end:]
sections['certs']=cert
# Contact retains the original form and integration fields.
c=sections['contact'].replace("Let's Work Together",'Have something<br>in <em>mind?</em>').replace('>Get In Touch<','>05 / LET’S CONNECT<')
c=c.replace('<div class="container">','<div class="container contact-layout">',1)
c=c.replace('Have a project in mind or just want to say hi? Drop me a message.','A project, an opportunity, or a good conversation.<br>I’d love to hear from you.')
c=c.replace('<div class="contact-wrap reveal">','<div class="contact-wrap reveal">',1)
c=c.replace('''        </div>

        <div class="contact-wrap''','''          <a class="contact-email" href="mailto:Irfanizzani46@gmail.com">Irfanizzani46@gmail.com <span>↗</span></a><div class="contact-socials"><a href="https://github.com/ieyrfan" target="_blank">GitHub ↗</a><a href="https://www.linkedin.com/in/irfanrizal2004" target="_blank">LinkedIn ↗</a><a href="https://wa.me/60103796742" target="_blank">WhatsApp ↗</a></div><span class="status-badge"><span class="pulse-dot"></span> Let’s build something meaningful.</span>
        </div>

        <div class="contact-wrap''',1)
c=c.replace('<div class="spinner"></div>','<div id="contactStatusIcon" class="spinner" aria-hidden="true"></div>').replace('id="encryptionStatus" class="form-status hidden"','id="encryptionStatus" class="form-status hidden" role="status" tabindex="-1"')
c=c.replace('id="senderName"','autocomplete="name" id="senderName"').replace('id="senderEmail"','autocomplete="email" id="senderEmail"')
sections['contact']=c
start=re.search(r'    <!-- ABOUT -->',s).start(); end=s.index('  </main>',start)
s=s[:start]+ '\n\n'.join(sections[k] for k in ['projects','about','skills','lab','services','certs','programs','insights','contact'])+'\n'+s[end:]
s=s.replace('URL Phishing Scanner','URL Pattern Check').replace('Analyze URLs for suspicious patterns, fake TLDs, and missing security protocols.','A local heuristic demo that flags suspicious URL patterns. It does not verify whether a website is safe.').replace('Analyzing threat intelligence...','Checking URL patterns...').replace('id="urlInput"','id="urlInput" aria-label="URL to check" inputmode="url"').replace('>SAFE</h4>','>NO OBVIOUS PATTERNS</h4>').replace('id="phishingResultBox"','id="phishingResultBox" role="status"').replace('id="gpaResultBox"','id="gpaResultBox" role="status"')
s=re.sub(r'<div id="imageLightbox".*?</div>', '',s,flags=re.S)
s=s.replace('  <script src="https://cdnjs.cloudflare.com/ajax/libs/vanilla-tilt/1.8.1/vanilla-tilt.min.js"></script>','''  <dialog id="commandPalette" class="command-palette" aria-labelledby="commandTitle"><div class="command-head"><span id="commandTitle">Where would you like to go?</span><button id="commandClose" class="icon-btn" aria-label="Close quick navigation">×</button></div><label class="sr-only" for="commandSearch">Search sections</label><input id="commandSearch" placeholder="Search work, tools, certifications…" autocomplete="off" /><div id="commandResults"><a href="#projects">Selected work <span>01 ↗</span></a><a href="#about">About Irfan <span>02 ↗</span></a><a href="#skills">Expertise <span>03 ↗</span></a><a href="#lab">Interactive playground <span>↗</span></a><a href="#services">FunTechz services <span>04 ↗</span></a><a href="#certs">Certifications <span>↗</span></a><a href="#programs">Programs &amp; experience <span>↗</span></a><a href="#insights">Architecture &amp; insights <span>↗</span></a><a href="#contact">Get in touch <span>05 ↗</span></a></div><p id="commandEmpty" class="hidden">No matches. Try “work”, “tools”, or “contact”.</p><div class="command-foot">TAB to navigate <span>ESC to close</span></div></dialog>
  <script src="experience.js?v=3" defer></script>
  <script src="navigation.js?v=3" defer></script>''')
s=s.replace('script.js?v=2','script.js?v=3')
s=re.sub(r'target="_blank"(?! rel=)', 'target="_blank" rel="noopener noreferrer"',s)
# Hide decorative glyphs from assistive technology.
s=re.sub(r'<i class="([^"]+)"(?! aria-hidden)',r'<i class="\1" aria-hidden="true"',s)
# Prevent font/style flash when a visitor has already picked a theme.
s=s.replace('  <title>', '''  <script>try { const t = localStorage.getItem('irfanPortfolioTheme'); if(t === 'light' || t === 'dark') document.documentElement.dataset.theme = t; } catch {}</script>
  <title>''',1)
p.write_text(s,encoding='utf-8')
print('Updated portfolio structure. Preserved form and tracker integration attributes without logging them.')

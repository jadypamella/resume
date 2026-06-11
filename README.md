# Jady Pamella - Professional Portfolio

Professional portfolio website at [jadypamella.com](https://jadypamella.com). Source of truth for CV variants (industry + academic, 2-page + 1-page), portfolio content, Lattes and ORCID update checklists, and the SEO/AEO/GEO discoverability configuration.

## Overview

This portfolio presents Jady Pamella's work as an AI engineer and founder: SoiQet (LLM-powered SaaS), Tree++ (climate-tech), MSc thesis at Deep Forestry (LiDAR perception on Jetson Orin NX), Bank of Brasília (10+ years), LabRisk / UnB cybersecurity research, and volunteer engineering at Drivhuset, DevOpsDays Brasília, Alla Ska Få Mat, and Stiftelsen Effekt / Ge Effektivt. Used as the canonical link in job and PhD applications.

## Features

- Responsive design optimized for all devices (desktop, tablet, mobile)
- SEO-optimized with complete meta tags and structured data
- Accessibility compliant (WCAG 2.1 AA)
- Progressive Web App (PWA) support
- Security headers and best practices implemented
- Fast loading with performance optimizations
- Professional sections: About, Projects, Publications, Experience, Education, Skills, Certifications

## Technical Stack

- HTML5 with semantic markup
- CSS3 with modern features (CSS Grid, Flexbox, Custom Properties)
- Vanilla JavaScript (no frameworks)
- Google Fonts (Plus Jakarta Sans)
- SVG icons for scalability
- JSON-LD structured data for search engines

## Project Structure

```
resume/
├── index.html                          # Main portfolio page
├── Jady_Pamella_CV.html                # Industry CV (2-page, HTML)
├── Jady_Pamella_CV.pdf                 # Industry CV (2-page, PDF)
├── Jady_Pamella_CV_1page.html          # Industry CV (1-page, HTML, recruiter screens)
├── Jady_Pamella_CV_1page.pdf           # Industry CV (1-page, PDF, recruiter screens)
├── Jady_Pamella_CV_Academic.html       # Academic CV (PhD / postdoc, HTML)
├── Jady_Pamella_CV_Academic.pdf        # Academic CV (PhD / postdoc, PDF)
├── Jady_Pamella_CV_Academic_1page.html # Academic CV (1-page)
├── Jady_Pamella_CV_Academic_1page.pdf  # Academic CV (1-page, PDF)
├── lattes_update_checklist.md          # CNPq Lattes update checklist
├── orcid_update_checklist.md           # ORCID update checklist
├── llms.txt                            # LLM crawler policy / citable summary
├── site.webmanifest                    # PWA configuration
├── sitemap.xml                         # Search engine sitemap
├── robots.txt                          # Search engine directives
└── images/
    ├── profile.png                     # Profile photo
    ├── favicon.png                     # Site favicon
    └── logos/                          # Company and institution logos
```

### CV variants

Four CV variants are kept in sync from a single source of truth (`Jady_Pamella_CV.html`):

| File | Audience | Length | When to use |
|---|---|---|---|
| `Jady_Pamella_CV.html` / `.pdf` | Industry, direct application | 2 pages | Default for senior engineering, EM, founder roles |
| `Jady_Pamella_CV_1page.html` / `.pdf` | Recruiter screens, consultancies | 1 page | Default attached to every cover letter |
| `Jady_Pamella_CV_Academic.html` / `.pdf` | PhD, postdoc, MSCA, WASP, ERC | Multi-page | Academic applications with publications, conferences, teaching |
| `Jady_Pamella_CV_Academic_1page.html` / `.pdf` | Academic intros, recruiter screens | 1 page | Short academic networking pings |

## SEO & Performance

The website implements comprehensive SEO best practices:

- Complete Open Graph tags for social media sharing
- Twitter Card optimization
- Schema.org structured data (JSON-LD)
- Semantic HTML5 elements
- Optimized meta descriptions and keywords
- XML sitemap for search engines
- Canonical URLs to prevent duplicate content
- Mobile-first responsive design

Performance optimizations include:
- Font preloading and display swap
- Resource hints (preconnect, dns-prefetch)
- Efficient CSS with minimal specificity
- Optimized images
- Clean, minified code structure

## Accessibility

The website meets WCAG 2.1 AA standards:
- Skip to main content link
- Proper heading hierarchy
- ARIA labels and landmarks
- Keyboard navigation support
- Screen reader friendly
- High contrast support
- Reduced motion preferences respected
- Minimum 44px touch targets for mobile

## Security

Security headers and best practices:
- X-Content-Type-Options: nosniff
- X-Frame-Options: SAMEORIGIN
- X-XSS-Protection enabled
- Strict referrer policy
- HTTPS enforcement ready
- Content Security Policy ready

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment

The website is designed to be deployed on any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3 + CloudFront
- Any web server (Apache, Nginx)

### Pre-deployment Checklist

1. Update all absolute URLs to production domain
2. Configure server security headers
3. Enable HTTPS with SSL certificate
4. Submit sitemap to Google Search Console
5. Test on multiple devices and browsers
6. Validate HTML and CSS
7. Run performance audits (Lighthouse, PageSpeed Insights)
8. Test accessibility with WAVE or axe DevTools

## Local Development

To run locally, simply open `index.html` in a web browser. For a better development experience with live reload:

```bash
# Using Python
python -m http.server 8000

# Using Node.js (npx http-server)
npx http-server -p 8000

# Then open http://localhost:8000
```

## Content Updates

### Updating Sections

All content is contained within `index.html`. Search by `id="<section>"` rather than line numbers since the file evolves:

- `#hero`
- `#about` (career highlights and core expertise tags)
- `#projects` (Featured Projects)
- `#publications`
- `#experience` (includes paid roles and volunteer entries: Drivhuset, DevOpsDays Brasília, Alla Ska Få Mat, Ge Effektivt / Stiftelsen Effekt)
- `#education`
- `#certifications` (includes EA Sweden Fellowship 2026)

### Adding New Projects

Add a new project item within the `#projects` section:

```html
<div class="project-item">
    <div class="project-logo">
        <img src="images/logos/project-logo.png" alt="Project Name">
    </div>
    <div class="project-content">
        <h3>Project Name</h3>
        <p class="project-type">Project Category</p>
        <p class="project-description">Description of the project...</p>
        <div class="project-tech">
            <span>Tech1</span>
            <span>Tech2</span>
        </div>
        <a href="https://project-url.com" target="_blank">View Project →</a>
    </div>
</div>
```

### Adding Publications

Add new publications within the `#publications` section:

```html
<div class="publication-item">
    <div class="pub-logo">
        <img src="images/logos/journal-logo.png" alt="Journal Name">
    </div>
    <div class="pub-content">
        <h3>Publication Title</h3>
        <p class="pub-venue">Journal Name, Year</p>
        <p class="pub-description">Abstract or description...</p>
        <div class="pub-meta">
            <a href="https://doi.org/..." target="_blank">DOI Link</a>
        </div>
    </div>
</div>
```

## Maintenance

Regular maintenance tasks:
- Update `sitemap.xml` lastmod dates when content changes
- Keep contact information current
- Add new projects and publications
- Update certifications and skills
- Monitor analytics and search console
- Run periodic security and performance audits

## License

This portfolio is the personal website of Jady Pamella. Content is proprietary. Code structure may be used as reference with attribution.

## Contact

- Email: hello@jadypamella.com
- LinkedIn: https://linkedin.com/in/jadypamella
- GitHub: https://github.com/jadypamella
- Location: Stockholm, Sweden
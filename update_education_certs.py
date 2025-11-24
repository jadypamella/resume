#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update Education and Certifications sections in index.html to match Jady_Pamella_CV.html
"""

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New Education section content from CV (adapted to index.html structure)
new_education = '''        <!-- Education -->
        <section id="education">
            <h2 class="section-title">Education</h2>
            
            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/stockholm-university-logo.png" alt="Stockholm University logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Stockholm University – SU</h3>
                            <p class="role">Master of Science in Computer and Systems Sciences (AI and IoT)</p>
                        </div>
                    </div>
                    <ul>
                        <li>Specialization: Machine Learning, Deep Learning, Computer Vision, Natural Language Processing, IoT Systems, Autonomous Systems.</li>
                        <li>Research collaboration with Deep Forestry on autonomous drones and computer vision for environmental monitoring.</li>
                        <li>Student Ambassador at Drivhuset Stockholm, Teaching Assistant in Internet of Things (IoT).</li>
                        <li>Member of the Network for Global Professionals (NFGP) by the Swedish Institute.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 0 1 3 3h-15a3 3 0 0 1 3-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 0 1-.982-3.172M9.497 14.25a7.454 7.454 0 0 0 .981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 0 0 7.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 0 0 2.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 0 1 2.916.52 6.003 6.003 0 0 1-5.395 4.972m0 0a6.726 6.726 0 0 1-2.749 1.35m0 0a6.772 6.772 0 0 1-3.044 0" />
                        </svg>
                        Award: Swedish Institute Scholarship for Global Professionals (SISGP)
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/unb-logo.png" alt="UnB logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>University of Brasília – UnB</h3>
                            <p class="role">Master of Engineering in Cybersecurity</p>
                        </div>
                    </div>
                    <ul>
                        <li>Specialization: Risk management, AI for cybersecurity, critical infrastructure protection, and security governance frameworks.</li>
                        <li>Published research in top-tier journal (Impact Factor: 5.6) on cybersecurity frameworks for judicial systems.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
                        </svg>
                        Publication: <a href="https://www.sciencedirect.com/science/article/pii/S0167404825002731" target="_blank">Elsevier's Computers & Security Journal (2025) | DOI: 10.1016/j.cose.2025.104584</a>
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/mit-logo.png" alt="MIT logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Massachusetts Institute of Technology – MIT</h3>
                            <p class="role">Designing and Building AI Products</p>
                        </div>
                    </div>
                    <ul>
                        <li>Specialization: 40-hour executive program on AI product development, deployment strategies, and scaling ML systems in production environments.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/descomplica-logo.png" alt="Descomplica logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Descomplica</h3>
                            <p class="role">MBA in Innovation, Technology & Entrepreneurship</p>
                        </div>
                    </div>
                    <ul>
                        <li>Focus: Business model innovation, technology strategy, startup development, and lean startup methodology.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/descomplica-logo.png" alt="Descomplica logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Descomplica</h3>
                            <p class="role">Postgraduate in Data Analysis</p>
                        </div>
                    </div>
                    <ul>
                        <li>Focus: Statistical modeling, machine learning algorithms, predictive analytics, data visualization, and business intelligence.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/fgv-logo.png" alt="FGV logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Fundação Getulio Vargas – FGV</h3>
                            <p class="role">MBA in Project Management</p>
                        </div>
                    </div>
                    <ul>
                        <li>Specialization: Agile methodologies, Scrum, PMBOK, risk management, stakeholder management, and change management for IT project delivery.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="institution-logo">
                    <img src="images/logos/upis-logo.png" alt="UPIS logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Faculdades Integradas – UPIS</h3>
                            <p class="role">BSc in Information Systems</p>
                        </div>
                    </div>
                    <ul>
                        <li>Focus: Algorithms, data structures, software engineering, database systems, and technology entrepreneurship fundamentals.</li>
                    </ul>
                </div>
            </div>
        </section>'''

# New Certifications section content from CV (adapted to index.html structure)
new_certifications = '''        <!-- Certifications -->
        <section id="certifications">
            <h2 class="section-title">Certifications</h2>
            <div class="certifications-list">
                <div class="cert-section">
                    <h4>Leadership</h4>
                    <ul>
                        <li>Women's Leadership Program (SOUL, 2024)</li>
                        <li>Self-Leadership Program (Hyper Island & Swedish Institute, 2024)</li>
                        <li>Collaborative Approaches to Societal Issues (Stockholm School of Entrepreneurship, 2024)</li>
                    </ul>
                </div>

                <div class="cert-section">
                    <h4>AI & Data</h4>
                    <ul>
                        <li>Designing & Building AI Products (MIT, 2022)</li>
                        <li>Data Analysis (ENAP, 2023)</li>
                        <li>Business Intelligence Foundation (Certiprof, 2024)</li>
                    </ul>
                </div>

                <div class="cert-section">
                    <h4>IT Governance</h4>
                    <ul>
                        <li>DevOps Master (EXIN, 2020)</li>
                        <li>Lean IT Foundation (EXIN, 2019)</li>
                        <li>COBIT 5 Foundation (ISACA, 2015)</li>
                        <li>ITIL V3 Foundation (EXIN, 2015)</li>
                    </ul>
                </div>

                <div class="cert-section">
                    <h4>Agile & Process</h4>
                    <ul>
                        <li>Scrum Foundation (Certiprof, 2019)</li>
                        <li>Lean Six Sigma White Belt (Certiprof, 2024)</li>
                    </ul>
                </div>

                <div class="cert-section">
                    <h4>Language</h4>
                    <ul>
                        <li>TOEFL iBT (ETS, 2024)</li>
                    </ul>
                </div>
            </div>
        </section>'''

# Update Education section
edu_start = content.find('        <!-- Education -->')
edu_end = content.find('        </section>', edu_start)
if edu_start != -1 and edu_end != -1:
    content = content[:edu_start] + new_education + content[edu_end + len('        </section>'):]
    print("✓ Education section updated")
else:
    print("✗ Could not find Education section markers")

# Update Certifications section
cert_start = content.find('        <!-- Certifications -->')
cert_end = content.find('        </section>', cert_start)
if cert_start != -1 and cert_end != -1:
    content = content[:cert_start] + new_certifications + content[cert_end + len('        </section>'):]
    print("✓ Certifications section updated")
else:
    print("✗ Could not find Certifications section markers")

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ All sections synchronized with CV successfully!")
print("\nKey changes made:")
print("  • Education: Added UnB entry with publication award, updated SU description")
print("  • Education: Changed SU degree from 'MSc in Data Science' to 'Master of Science in Computer and Systems Sciences (AI and IoT)'")
print("  • Education: Added research collaboration details, student ambassador role, and NFGP membership")
print("  • Certifications: Added missing 'Lean IT Foundation (EXIN, 2019)' certification")

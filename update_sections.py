"""
Script to update index.html Experience, Education, and Certifications sections
to match the content from Jady_Pamella_CV.html
"""

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Experience section start and end
exp_start = content.find('<!-- Experience -->')
exp_end = content.find('</section>', exp_start)

# Find the Education section start and end  
edu_start = content.find('<!-- Education -->')
edu_end = content.find('</section>', edu_start)

# Find the Certifications section start and end
cert_start = content.find('<!-- Certifications -->')
cert_end = content.find('</section>', cert_start)

# New Experience section content matching CV
new_experience = '''        <!-- Experience -->
        <section id="experience">
            <h2 class="section-title">Experience</h2>
            
            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/treepp-logo.png" alt="Tree++ logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Tree++ (Climate Tech Startup)</h3>
                            <p class="role">Co-founder and Chief Innovation Officer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Lead technical strategy, engineering roadmap, and sustainability-aligned vision for AI-powered autonomous drones for reforestation, managing fundraising, investor relations, and strategic partnerships.</li>
                        <li>Architect end-to-end AI/IoT platform: computer vision for terrain analysis, autonomous flight control, real-time telemetry processing (1M+ events/day) using Python, TensorFlow, Kubernetes, and AWS.</li>
                        <li>Build and mentor engineering team, overseeing hiring, performance management, delivery standards, and technical excellence.</li>
                        <li>Manage budget allocation, burn rate optimization, and financial planning for business scalability and growth.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 0 1 3 3h-15a3 3 0 0 1 3-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 0 1-.982-3.172M9.497 14.25a7.454 7.454 0 0 0 .981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 0 0 7.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 0 0 2.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 0 1 2.916.52 6.003 6.003 0 0 1-5.395 4.972m0 0a6.726 6.726 0 0 1-2.749 1.35m0 0a6.772 6.772 0 0 1-3.044 0" />
                        </svg>
                        Award: Impact Cup – Drivhuset (2025)
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/brb-logo.png" alt="Bank of Brasília logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Bank of Brasília – BRB</h3>
                            <p class="role">IT Analyst and DevOps Engineer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Delivered value through AI and automation initiatives: built production AI chatbot (Python, TensorFlow, NLP) in Silicon Valley reducing customer response time by 40% for 100K+ users.</li>
                        <li>Architected DevSecOps CI/CD pipelines (Jenkins, GitLab, Docker, OpenShift, Kubernetes) reducing deployment time by 60%.</li>
                        <li>Developed Power BI executive dashboards enabling data-driven decisions for C-suite stakeholders and ensuring regulatory compliance (BACEN, LGPD).</li>
                        <li>Collaborated directly with CIO, CFO, and COO to align IT initiatives with business strategy and objectives.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/brb-logo.png" alt="Bank of Brasília logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Bank of Brasília – BRB</h3>
                            <p class="role">IT Manager</p>
                        </div>
                    </div>
                    <ul>
                        <li>Managed $1M+ IT budget with full P&L accountability, reducing operational costs by 15% ($150K+ savings) through strategic vendor optimization and contract restructuring.</li>
                        <li>Led team of 10+ IT professionals with full responsibility for hiring, performance management, career development, implementing COBIT, ITIL, Agile, and Lean IT frameworks.</li>
                        <li>Improved compliance and audit accuracy by 40% redesigning Change and Configuration Management processes, reducing regulatory risk and ensuring business continuity.</li>
                        <li>Led organizational transformation initiatives including Lean IT practices (20% waste reduction) and DevSecOps adoption across IT department.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 0 1 3 3h-15a3 3 0 0 1 3-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 0 1-.982-3.172M9.497 14.25a7.454 7.454 0 0 0 .981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 0 0 7.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 0 0 2.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 0 1 2.916.52 6.003 6.003 0 0 1-5.395 4.972m0 0a6.726 6.726 0 0 1-2.749 1.35m0 0a6.772 6.772 0 0 1-3.044 0" />
                        </svg>
                        Award: Strategic Configuration Management – Efinance (2019)
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/ibict-logo.png" alt="IBICT logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Brazilian Institute of Information in Science and Technology - IBICT</h3>
                            <p class="role">Research Engineer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Customized Archivematica for Kubernetes and OpenShift deployment, enabling scalable digital preservation infrastructure for government agencies managing millions of digital assets.</li>
                        <li>Supported national initiatives in knowledge management, data governance, and digital transformation for public sector with improved automation workflows.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/mcid-logo.png" alt="MCID logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Ministry of Integration and Regional Development – MCID</h3>
                            <p class="role">Software Engineer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Modernized legacy PHP and MySQL systems improving scalability, maintainability, and performance for national integration services.</li>
                        <li>Developed responsive web and mobile applications increasing citizen access to government digital services and platforms.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/senai-logo.png" alt="SENAI logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>SENAI – National Industrial Training Service</h3>
                            <p class="role">Web Developer and Designer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Developed e-learning platforms supporting 2,000+ students with interactive learning modules, progress tracking, and assessment tools.</li>
                        <li>Built PHP and MySQL systems for statewide education programs, optimized UX for digital curriculum delivery and multi-device access.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 0 1 3 3h-15a3 3 0 0 1 3-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 0 1-.982-3.172M9.497 14.25a7.454 7.454 0 0 0 .981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 0 0 7.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 0 0 2.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 0 1 2.916.52 6.003 6.003 0 0 1-5.395 4.972m0 0a6.726 6.726 0 0 1-2.749 1.35m0 0a6.772 6.772 0 0 1-3.044 0" />
                        </svg>
                        Award: WorldSkills National Phase – Web Design (2012)
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/su-heroes-logo.png" alt="SU Heroes logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>SU Heroes - Hackathon Team</h3>
                            <p class="role">Team Leader</p>
                        </div>
                    </div>
                    <ul>
                        <li>Lead multidisciplinary teams building applied AI automation and agentic AI systems, mentor students and engineers in AI/ML, cloud architecture, and rapid prototyping.</li>
                    </ul>
                    <div class="item-award">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" style="width: 16px; height: 16px; display: inline-block; vertical-align: middle; margin-right: 4px;">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 18.75h-9m9 0a3 3 0 0 1 3 3h-15a3 3 0 0 1 3-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 0 1-.982-3.172M9.497 14.25a7.454 7.454 0 0 0 .981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 0 0 7.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 0 0 2.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 0 1 2.916.52 6.003 6.003 0 0 1-5.395 4.972m0 0a6.726 6.726 0 0 1-2.749 1.35m0 0a6.772 6.772 0 0 1-3.044 0" />
                        </svg>
                        Awards: Kong AI Assisted-Coding Hackathon (2025), Kolomolo AI-Assisted Coding Hackathon (2025) & Nordcloud Agentic AI Software Modernization Hackathon (2025)
                    </div>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/stockholm-university-logo.png" alt="Stockholm University logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Stockholm University – SU</h3>
                            <p class="role">Teaching Assistant - Internet of Things</p>
                        </div>
                    </div>
                    <ul>
                        <li>Support 200+ students in IoT coursework: Python programming, sensor integration (MQTT), edge computing, and data processing pipelines.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/drivhuset-logo.png" alt="Drivhuset logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Drivhuset Stockholm – SU</h3>
                            <p class="role">Student Ambassador</p>
                        </div>
                    </div>
                    <ul>
                        <li>Support founders and students in entrepreneurship programs, mentor on technology strategy and product development, promote innovation activities across Stockholm University.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/devopsdays-logo.png" alt="DevOpsDays logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>DevOpsDays Brasília</h3>
                            <p class="role">Volunteer Organizer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Coordinate technical conferences with 250+ participants, develop partnerships with industry and academia, curate DevSecOps and AI/ML content.</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="company-logo">
                    <img src="images/logos/allaskafamat-logo.png" alt="Alla Ska Få Mat logo" onerror="this.parentElement.style.display='none'">
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <div>
                            <h3>Alla Ska Få Mat</h3>
                            <p class="role">Volunteer Organizer</p>
                        </div>
                    </div>
                    <ul>
                        <li>Help volunteer teams supporting vulnerable families and people experiencing homelessness, optimize marketing and digital presence for community impact.</li>
                    </ul>
                </div>
            </div>
        </section>'''

# Replace Experience section
content = content[:exp_start] + new_experience + content[exp_end + len('</section>'):]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Experience section updated successfully!")
print("Note: Education and Certifications need manual review as they may have different structures")

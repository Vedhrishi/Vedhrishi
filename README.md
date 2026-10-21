<p align="center">
  <img src="assets/banner.svg" alt="Pasupuleti Vedh Rishi - Computer Vision, Security, Automation, Full-stack" width="100%">
</p>

<p align="center">
  <a href="https://github.com/Vedhrishi/Vedhrishi">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3200&pause=900&color=7EE7FF&center=true&vCenter=true&width=760&lines=Software+developer+from+Hyderabad;I+build+computer+vision+that+runs+in+the+browser;Security+tools%3A+face+auth+%2B+AES-256-GCM+vaults;Automation+pipelines+that+publish+across+3+platforms;Open+to+software+engineering+roles" alt="Typing animation: software developer, computer vision, security, automation, open to roles">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Open%20to-Software%20Engineering%20Roles-2ea44f?style=for-the-badge" alt="Open to software engineering roles">
  <a href="https://www.linkedin.com/in/vedhrishi-pasupuleti-6b6856408/"><img src="https://img.shields.io/badge/LinkedIn-Vedhrishi%20Pasupuleti-0a66c2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn profile"></a>
  <img src="https://img.shields.io/badge/Based%20in-Hyderabad%2C%20India-0a66c2?style=for-the-badge" alt="Hyderabad, India">
  <img src="https://komarev.com/ghpvc/?username=Vedhrishi&label=Profile%20views&color=7c3aed&style=for-the-badge" alt="Profile views">
</p>

---

**Software engineer | Computer vision, security and automation**

I design, build and ship complete systems: the model or pipeline, the application around it, the deployment, and the tests and documentation that keep it maintainable. I care about the parts that make software trustworthy in production: privacy by default, secure data handling, measured performance and automated checks.

> Every project below is live, open source and licensed. Where a number appears, I measured it.

## Core strengths

- **Applied machine learning, shipped:** I take models out of notebooks and into real products, including running vision models on-device in the browser so user data never leaves the phone.
- **Security-minded engineering:** authenticated encryption, row-level security, threat classification and deception techniques, and a habit of auditing dependencies and keeping secrets out of source control.
- **Full-stack delivery:** React and TypeScript front ends, Supabase and Postgres back ends, Vercel deployments and CI pipelines, handled end to end.
- **Automation at scale:** media-rendering and multi-platform publishing pipelines that run on a schedule with little manual work.

## What I work with

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,ts,js,react,vite,tailwind,nodejs,supabase,vercel,opencv,tensorflow,sklearn,github,githubactions,git&perline=8" alt="Skills: Python, TypeScript, JavaScript, React, Vite, Tailwind, Node.js, Supabase, Vercel, OpenCV, TensorFlow, scikit-learn, GitHub, GitHub Actions, Git">
</p>

| Area | Tools |
|---|---|
| Languages | Python, TypeScript, JavaScript |
| Web | React, Vite, Tailwind CSS, Vercel, Supabase (Postgres, Auth, row-level security) |
| ML and vision | YOLOv8, ResNet-18, COCO-SSD, OpenCV, TensorFlow.js, scikit-learn (RandomForest) |
| Security | AES-256-GCM, face-based authentication with liveness checks, honeypots, MFA and OTP flows |
| Automation | FFmpeg render pipelines, YouTube / Facebook / Instagram publishing workflows, GitHub Actions |
| Quality | Unit and end-to-end tests, CI, `npm audit` gates, documented security policies |

## Selected projects

### [Plastic Decoder](https://github.com/Vedhrishi/AI-PLASTIC-SORTING-WEBSITE) ([live](https://plastic-decoder-project.vercel.app))
**Problem:** people can't tell plastic resin types apart, so recyclable material gets contaminated.
**Solution:** a camera app that identifies the resin (PET, HDPE, PP, PS) in real time and gives disposal guidance for India's plastic-waste rules.
**Engineering:** YOLOv8 and ResNet-18 run on-device over WebGL, so photos never leave the browser. A person/hand veto step reduces false positives. It ships with end-to-end tests, CI and a published security policy. Measured on mobile with Lighthouse: 100 SEO, 96 best practices.

### [INTELLITRAP](https://github.com/Vedhrishi/INTELLITRAP) ([live](https://intellitrap-batch-3.vercel.app))
**Problem:** stolen credentials let attackers browse a user's files unnoticed.
**Solution:** secure cloud storage with an AI deception layer. Behavioural risk scoring (RandomForest) flags suspicious sessions and diverts them to honeypot data while an admin console shows the threat.
**Engineering:** full-stack TypeScript with Supabase: role-based access, row-level security, OTP-protected sharing, a threat classifier and a tested risk engine.

### [BioLock SSD](https://github.com/Vedhrishi/BIO-LOCK)
**Problem:** a lost USB drive means lost data.
**Solution:** a face-authenticated lock for external drives with multi-step liveness detection and an AES-256-GCM encrypted vault.
**Engineering:** deep face recognition (YuNet detection, SFace recognition), two-factor cryptography, a Windows desktop app in Python, and automated tests in CI.

### [RISHI | Indian Stocks Explained](https://github.com/Vedhrishi/RISHI-INDIAN-STOCKS-EXPLAINED) ([live](https://rishi-indian-stocks-explained.vercel.app))
**Problem:** stock-market education for first-time Indian investors is jargon-heavy and mostly English-only.
**Solution:** an animated short-video series, with 100 episodes (200 parts) rendered in English, Hindi and Telugu and published on Instagram, YouTube and Facebook.
**Engineering:** I built the video pipeline, the website and the publishing tools. On the site I profiled before optimizing: phones skip the 3D intro libraries entirely and get a purpose-built stacked layout instead.

### [RISHI Automation](https://github.com/Vedhrishi/RISHI-AUTOMATION)
The publishing engine behind the series: scheduling, captions, uploads and status tracking across three platforms with minimal manual work, plus project documentation and retrospectives.

### [SIH Code Mavericks](https://github.com/Vedhrishi/SIH-CODE_MAVERICKS)
A multilingual admission assistant built for the Smart India Hackathon with React, TypeScript and Tailwind.

## Certifications and learning

| Credential | Issuer | Completed | Verify |
|---|---|---|---|
| **Google AI Professional Certificate** (7 courses) | Google via Coursera | Jun 2026 | [Verify](https://coursera.org/verify/professional-cert/KE2UAD30CICU) |
| Financial Markets | Yale University via Coursera | May 2026 | [Verify](https://coursera.org/verify/BKT2CQFSGG1D) |
| Foundations of Project Management | Google via Coursera | Jul 2026 | [Verify](https://coursera.org/verify/FU65M9YKDMUZ) |
| Generative AI: Prompt Engineering Basics | Coursera | | [Course](https://www.coursera.org/learn/generative-ai-prompt-engineering-for-everyone) |
| Drupal Training | EduPyramids, SINE, IIT Bombay (via CMR Technical Campus) | Mar 2026 | Certificate ID 3920325YWC |

<details>
<summary>Courses in the Google AI Professional Certificate</summary>

- [AI Fundamentals](https://coursera.org/verify/0L3ILS7HMF10)
- [AI for Brainstorming and Planning](https://coursera.org/verify/XZY4AFK2JZ0M)
- [AI for Research and Insights](https://coursera.org/verify/WV3D6WJKOWUB)
- [AI for Writing and Communicating](https://coursera.org/verify/9XF2KCFA7K6F)
- [AI for Content Creation](https://coursera.org/verify/DQN3C5ZNED4N)
- [AI for Data Analysis](https://coursera.org/verify/SOTYUUR9ZNGX)
- [AI for App Building](https://coursera.org/verify/HJYCFFY5SWDO)

</details>

**Also:** completed the NISM Series-VIII (Equity Derivatives) study program in 2023, and took part in Technovanza 4.0 and 5.0, a national-level tech event run alongside the Smart India Hackathon. Outside code: Model United Nations (High Commendation and Special Mention awards). The finance coursework underpins the content in the RISHI series.

## Engineering principles

1. **Measure first.** I profile with Lighthouse and tests before changing code, then re-measure.
2. **Secure by default.** No committed secrets, audited dependencies, least-privilege data access, privacy-first design.
3. **Ship, then document.** Live demo, clear README, license and tests for every project.
4. **Automate the boring parts.** CI, dependency checks and publishing pipelines run without me.

## Get in touch

Open to software engineering roles and collaborations.

- **LinkedIn:** [linkedin.com/in/vedhrishi-pasupuleti-6b6856408](https://www.linkedin.com/in/vedhrishi-pasupuleti-6b6856408/)
- **Email:** [vedhrishi54@gmail.com](mailto:vedhrishi54@gmail.com)
- **GitHub:** you are here; the pinned repositories are my best work
- **Projects:** [RISHI website](https://rishi-indian-stocks-explained.vercel.app)

## GitHub at a glance

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=Vedhrishi&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&rank_icon=github" alt="GitHub stats">
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Vedhrishi&layout=compact&theme=tokyonight&hide_border=true&langs_count=6" alt="Top languages">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=Vedhrishi&theme=tokyonight&hide_border=true" alt="Contribution streak">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vedhrishi/Vedhrishi/output/github-snake-dark.svg">
    <img alt="Contribution graph snake animation" src="https://raw.githubusercontent.com/Vedhrishi/Vedhrishi/output/github-snake.svg">
  </picture>
</p>

<p align="center">
  <img src="assets/banner.svg" width="100%" height="90" style="object-fit:cover" alt="">
</p>

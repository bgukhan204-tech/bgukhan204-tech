export const generateMarkdown = (profile) => {
  const {
    name = "GUKHAN B",
    githubUsername = "bgukhan204-tech",
    title = "B.Tech Student in Artificial Intelligence & Data Science",
    location = "Coimbatore, India",
    email = "bgukhan204@gmail.com",
    phone = "+91 8838844579",
    linkedin = "https://www.linkedin.com/in/gukhan-b-97674a381",
    objective = "Motivated AI & Data Science engineering student passionate about software development, intelligent systems, and scalable web solutions.",
    education = "B.Tech in AI & Data Science (2022-2026) | V.S.B College of Engineering Technical Campus | CGPA: 8.2",
    skills = [],
    projects = [],
    certifications = [],
    statsTheme = "tokyonight"
  } = profile;

  // Build typing header
  const typingLines = [
    `Hi 👋 I'm ${name.toUpperCase()}`,
    `AI %26 Data Science Engineer`,
    `Full-Stack Java %26 Python Developer`,
    `Building Scalable Web %26 AI Solutions`
  ].join(";");

  const typingSvgUrl = `https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines=${typingLines}`;

  // Categorize selected skill badges
  const badgeMap = {
    Python: "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white",
    TensorFlow: "https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white",
    Streamlit: "https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white",
    Java: "https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white",
    "Spring Boot": "https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=spring-boot&logoColor=white",
    "Spring Security": "https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=spring&logoColor=white",
    JWT: "https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white",
    MySQL: "https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white",
    React: "https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB",
    JavaScript: "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black",
    HTML5: "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
    CSS3: "https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white",
    Git: "https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white",
    GitHub: "https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white",
    Render: "https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white"
  };

  const selectedBadges = skills
    .map(skill => badgeMap[skill] ? `![${skill}](${badgeMap[skill]})` : '')
    .filter(Boolean)
    .join("\n");

  const projectCards = projects.map(proj => `
    <td width="50%" valign="top">
      <h3 align="center">${proj.icon || '🚀'} ${proj.title}</h3>
      <p align="center">
        ${(proj.tags || []).map(t => `<img src="https://img.shields.io/badge/${t}-38BDF8?style=flat-square"/>`).join(" ")}
      </p>
      <ul>
        ${(proj.description || []).map(desc => `<li>${desc}</li>`).join("\n        ")}
      </ul>
    </td>`).join("");

  return `<div align="center">

<!-- Typing SVG Header -->
<a href="https://git.io/typing-svg">
  <img src="${typingSvgUrl}" alt="Typing SVG" />
</a>

<p align="center">
  <b>${title}</b> • <i>${location}</i>
</p>

<!-- Social & Contact Badges -->
<p align="center">
  ${linkedin ? `<a href="${linkedin}">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>` : ''}
  ${email ? `<a href="mailto:${email}">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>` : ''}
  ${githubUsername ? `<a href="https://github.com/${githubUsername}">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>` : ''}
</p>

---

</div>

### 💫 About Me

${objective}

- 🎓 **Education**: ${education}
- 🚀 **Currently Building**: Intelligent multimedia AI systems & microservices architectures
- 💡 **Core Expertise**: Full-Stack Development, Machine Learning, Deep Learning, Secure API Design
- 💬 **Ask Me About**: Java Spring Security, JWT, TensorFlow, React, and Database Optimization
- 📫 **Contact Me**: [${email}](mailto:${email}) | [${phone}](tel:${phone.replace(/\s+/g, '')})

---

### 🛠️ Tech Stack & Skills

<div align="left">

${selectedBadges}

</div>

---

### 📌 Featured Projects

<table>
  <tr>${projectCards}
  </tr>
</table>

---

### 🎓 Education & Certifications

- **${education}**
${certifications.map(c => `- **📜 ${c.name}** — *${c.issuer}*`).join("\n")}

---

### 📊 GitHub Analytics

<div align="center">

<p align="center">
  <img width="48%" src="https://github-readme-stats.vercel.app/api?username=${githubUsername}&show_icons=true&theme=${statsTheme}&hide_border=true&count_private=true&title_color=38BDF8&text_color=94A3B8&icon_color=38BDF8&bg_color=0F172A" alt="GitHub Stats" />
  <img width="48%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=${githubUsername}&layout=compact&theme=${statsTheme}&hide_border=true&title_color=38BDF8&text_color=94A3B8&bg_color=0F172A" alt="Top Languages" />
</p>

<p align="center">
  <img width="98%" src="https://github-readme-streak-stats.herokuapp.com/?user=${githubUsername}&theme=${statsTheme}&hide_border=true&background=0F172A&ring=38BDF8&fire=38BDF8&currStreakLabel=38BDF8" alt="GitHub Streak" />
</p>

</div>

---

<div align="center">

⭐ **Thank you for visiting my GitHub Profile!** Feel free to reach out for collaborations or networking.

</div>`;
};

import React, { useState } from 'react';
import { FormEditor } from './components/FormEditor';
import { MarkdownPreview } from './components/MarkdownPreview';
import { generateMarkdown } from './utils/markdownGenerator';
import { Sparkles, Github, BookOpen, ExternalLink } from 'lucide-react';

const INITIAL_PROFILE = {
  name: "GUKHAN B",
  githubUsername: "bgukhan204-tech",
  title: "B.Tech Student in Artificial Intelligence & Data Science",
  location: "Coimbatore, India",
  email: "bgukhan204@gmail.com",
  phone: "+91 8838844579",
  linkedin: "https://www.linkedin.com/in/gukhan-b-97674a381",
  objective: "Motivated Artificial Intelligence and Data Science engineering student passionate about software development and AI-driven solutions. Experienced in developing scalable web applications and intelligent systems through academic and personal projects.",
  education: "B.Tech in Artificial Intelligence & Data Science (2022-2026) | V.S.B College of Engineering Technical Campus | CGPA: 8.2",
  skills: [
    'Python', 'TensorFlow', 'Streamlit', 'Java', 'Spring Boot', 
    'Spring Security', 'JWT', 'MySQL', 'React', 'JavaScript', 
    'HTML5', 'CSS3', 'Git', 'GitHub', 'Render'
  ],
  projects: [
    {
      title: "Deepfake Detection Engine",
      icon: "🕵️",
      tags: ["Python", "TensorFlow", "Streamlit"],
      description: [
        "Engineered an AI-powered web application utilizing Python, TensorFlow, and Streamlit with an efficient multimedia video processing pipeline.",
        "Designed a dual-engine detection system with advanced scoring & reasoning algorithms to evaluate authenticity & deliver precise prediction metrics."
      ]
    },
    {
      title: "Full-Stack B2C E-Commerce Marketplace",
      icon: "🛒",
      tags: ["Spring_Boot", "React", "MySQL"],
      description: [
        "Architected a full-stack B2C e-commerce marketplace using Spring Security & JWTs to implement robust role-based access control (RBAC).",
        "Integrated Razorpay API for secure payment processing alongside an interactive frontend with real-time map-based delivery tracking."
      ]
    }
  ],
  certifications: [
    { name: "Introduction to Data Science and Artificial Intelligence", issuer: "Infosys Springboard" },
    { name: "Cloud Computing", issuer: "NPTEL" }
  ],
  statsTheme: "tokyonight"
};

export default function App() {
  const [profile, setProfile] = useState(INITIAL_PROFILE);
  const markdown = generateMarkdown(profile);

  return (
    <div className="app-root">
      {/* Navbar */}
      <header className="app-header">
        <div className="brand-title">
          <Github size={24} style={{ color: '#38bdf8' }} />
          <span>GitHub Profile README Builder</span>
        </div>
        <div className="header-actions">
          <a 
            href="https://github.com/bgukhan204-tech" 
            target="_blank" 
            rel="noreferrer"
            className="btn btn-secondary"
            style={{ textDecoration: 'none' }}
          >
            <ExternalLink size={16} /> My GitHub Profile
          </a>
        </div>
      </header>

      {/* Main App Grid */}
      <main className="main-container">
        {/* Left Column: Form Editor */}
        <section className="panel">
          <div className="panel-header">
            <div className="panel-title">
              <Sparkles size={18} /> Profile Details & Customizer
            </div>
            <span style={{ fontSize: '0.8rem', color: '#94a3b8' }}>Live Syncing</span>
          </div>
          <div className="panel-body">
            <FormEditor profile={profile} setProfile={setProfile} />
          </div>
        </section>

        {/* Right Column: Previewer */}
        <section className="panel">
          <div className="panel-header">
            <div className="panel-title">
              <BookOpen size={18} /> Live Profile Preview
            </div>
          </div>
          <div className="panel-body">
            <MarkdownPreview markdown={markdown} />
          </div>
        </section>
      </main>
    </div>
  );
}

import React from 'react';
import { User, Code, FolderGit2, Award, Palette, Phone, Mail, Link as LinkIcon } from 'lucide-react';

const ALL_SKILLS = [
  'Python', 'TensorFlow', 'Streamlit', 'Java', 'Spring Boot', 
  'Spring Security', 'JWT', 'MySQL', 'React', 'JavaScript', 
  'HTML5', 'CSS3', 'Git', 'GitHub', 'Render'
];

const THEMES = [
  { id: 'tokyonight', name: 'Tokyo Night (Default)' },
  { id: 'dracula', name: 'Dracula' },
  { id: 'catppuccin', name: 'Catppuccin' },
  { id: 'radical', name: 'Radical' },
  { id: 'onedark', name: 'One Dark' },
  { id: 'nord', name: 'Nord' }
];

export function FormEditor({ profile, setProfile }) {
  const handleChange = (e) => {
    const { name, value } = e.target;
    setProfile(prev => ({ ...prev, [name]: value }));
  };

  const toggleSkill = (skill) => {
    setProfile(prev => {
      const skills = prev.skills.includes(skill)
        ? prev.skills.filter(s => s !== skill)
        : [...prev.skills, skill];
      return { ...prev, skills };
    });
  };

  return (
    <div className="form-editor">
      {/* Personal Information */}
      <div className="form-section">
        <div className="section-title">
          <User size={18} /> Personal Info & Contact
        </div>

        <div className="form-group">
          <label>Full Name</label>
          <input
            type="text"
            name="name"
            className="form-input"
            value={profile.name}
            onChange={handleChange}
            placeholder="e.g. GUKHAN B"
          />
        </div>

        <div className="form-group">
          <label>GitHub Username</label>
          <input
            type="text"
            name="githubUsername"
            className="form-input"
            value={profile.githubUsername}
            onChange={handleChange}
            placeholder="e.g. bgukhan204-tech"
          />
        </div>

        <div className="form-group">
          <label>Headline Title</label>
          <input
            type="text"
            name="title"
            className="form-input"
            value={profile.title}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Email</label>
          <input
            type="email"
            name="email"
            className="form-input"
            value={profile.email}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>LinkedIn Profile URL</label>
          <input
            type="text"
            name="linkedin"
            className="form-input"
            value={profile.linkedin}
            onChange={handleChange}
          />
        </div>
      </div>

      {/* Tech Stack Picker */}
      <div className="form-section">
        <div className="section-title">
          <Code size={18} /> Select Skills & Technologies
        </div>
        <div className="skills-grid">
          {ALL_SKILLS.map(skill => {
            const isSelected = profile.skills.includes(skill);
            return (
              <div
                key={skill}
                className={`skill-checkbox ${isSelected ? 'selected' : ''}`}
                onClick={() => toggleSkill(skill)}
              >
                <input
                  type="checkbox"
                  checked={isSelected}
                  readOnly
                  style={{ pointerEvents: 'none' }}
                />
                <span>{skill}</span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Stats Theme Selector */}
      <div className="form-section">
        <div className="section-title">
          <Palette size={18} /> GitHub Stats Card Theme
        </div>
        <select
          name="statsTheme"
          className="form-select"
          value={profile.statsTheme}
          onChange={handleChange}
        >
          {THEMES.map(theme => (
            <option key={theme.id} value={theme.id}>
              {theme.name}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}

import React, { useState } from 'react';
import { marked } from 'marked';
import confetti from 'canvas-confetti';
import { Copy, Check, Download, Eye, Code2 } from 'lucide-react';

export function MarkdownPreview({ markdown }) {
  const [activeTab, setActiveTab] = useState('preview');
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(markdown);
      setCopied(true);
      confetti({ particleCount: 50, spread: 60, origin: { y: 0.8 } });
      setTimeout(() => setCopied(false), 2500);
    } catch (err) {
      console.error('Failed to copy markdown:', err);
    }
  };

  const handleDownload = () => {
    const blob = new Blob([markdown], { type: 'text/markdown;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'README.md';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    confetti({ particleCount: 80, spread: 70, origin: { y: 0.8 } });
  };

  const htmlContent = marked.parse(markdown || '');

  return (
    <div className="preview-container" style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
        <div className="tabs">
          <button
            className={`tab-btn ${activeTab === 'preview' ? 'active' : ''}`}
            onClick={() => setActiveTab('preview')}
          >
            <Eye size={14} style={{ display: 'inline', marginRight: 4 }} /> Rendered Preview
          </button>
          <button
            className={`tab-btn ${activeTab === 'code' ? 'active' : ''}`}
            onClick={() => setActiveTab('code')}
          >
            <Code2 size={14} style={{ display: 'inline', marginRight: 4 }} /> Raw Markdown
          </button>
        </div>

        <div style={{ display: 'flex', gap: '0.5rem' }}>
          <button className="btn btn-secondary" onClick={handleCopy}>
            {copied ? <Check size={16} className="text-emerald-400" /> : <Copy size={16} />}
            {copied ? 'Copied!' : 'Copy Code'}
          </button>
          <button className="btn btn-primary" onClick={handleDownload}>
            <Download size={16} /> Download README.md
          </button>
        </div>
      </div>

      <div style={{ flex: 1, overflowY: 'auto' }}>
        {activeTab === 'preview' ? (
          <div
            className="rendered-markdown"
            dangerouslySetInnerHTML={{ __html: htmlContent }}
          />
        ) : (
          <pre className="code-preview">
            <code>{markdown}</code>
          </pre>
        )}
      </div>
    </div>
  );
}

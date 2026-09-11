"""
Snake SVG Vector Paths & Frames Module
Contains SVG path definitions for a smooth animated snake traversing the GitHub contribution calendar.
Replaces the lion with the classic purple/green Snake eating contribution tiles.
"""

# Snake Head, Body, and Tail SVG elements (scale-ready for contribution cells)
SNAKE_VECTORS = """
<g id="snake-head">
    <!-- Snake Head Body -->
    <rect x="0" y="0" width="11" height="11" rx="4" ry="4" fill="#7c3aed"/>
    <!-- Inner Highlight -->
    <rect x="1.5" y="1.5" width="8" height="8" rx="2.5" ry="2.5" fill="#8b5cf6"/>
    <!-- Snake Eyes -->
    <circle cx="3.5" cy="3.5" r="1.2" fill="#ffffff"/>
    <circle cx="3.5" cy="3.5" r="0.6" fill="#000000"/>
    <circle cx="7.5" cy="3.5" r="1.2" fill="#ffffff"/>
    <circle cx="7.5" cy="3.5" r="0.6" fill="#000000"/>
    <!-- Snake Tongue -->
    <path d="M 5.5 11 L 5.5 14 M 5.5 14 L 3.5 16 M 5.5 14 L 7.5 16" stroke="#ef4444" stroke-width="1" stroke-linecap="round"/>
</g>

<g id="snake-body-1">
    <rect x="0" y="0" width="11" height="11" rx="3.5" ry="3.5" fill="#8b5cf6"/>
    <rect x="2" y="2" width="7" height="7" rx="2" ry="2" fill="#a78bfa"/>
</g>

<g id="snake-body-2">
    <rect x="0" y="0" width="11" height="11" rx="3.5" ry="3.5" fill="#7c3aed"/>
    <rect x="2" y="2" width="7" height="7" rx="2" ry="2" fill="#9333ea"/>
</g>

<g id="snake-tail">
    <rect x="1" y="1" width="9" height="9" rx="4.5" ry="4.5" fill="#6d28d9"/>
</g>
"""

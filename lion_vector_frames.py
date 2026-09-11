"""
Lion SVG Vector Paths & Frames Module
Contains SVG path definitions for a 6-frame smooth lion run cycle animation.
Designed to be embedded into SVG <defs> and animated via CSS @keyframes.
"""

LION_FRAMES = [
    # Frame 0: Extended Leap
    """<g id="lion-frame-0">
        <ellipse cx="60" cy="65" rx="35" ry="3" fill="rgba(0,0,0,0.15)"/>
        <path d="M 25 32 C 15 28 8 20 5 15 C 3 12 5 10 7 12 C 10 16 16 22 23 27 Z" fill="#b87b28"/>
        <path d="M 4 14 C 2 10 1 8 4 6 C 7 5 9 9 7 13 Z" fill="#3a1e06"/>
        <path d="M 32 35 L 20 48 L 12 56 L 18 58 L 26 48 L 36 38 Z" fill="#c48320"/>
        <path d="M 38 33 L 26 48 L 18 58 L 25 60 L 33 50 L 42 37 Z" fill="#e5a93c"/>
        <path d="M 30 30 C 40 25 55 24 70 28 C 78 30 82 34 80 40 C 70 44 50 45 35 42 C 28 40 26 34 30 30 Z" fill="#e5a93c"/>
        <path d="M 38 41 C 50 43 66 42 75 38 C 72 41 55 45 38 43 Z" fill="#f7cf88"/>
        <path d="M 68 33 L 78 45 L 86 52 L 92 51 L 83 43 L 73 31 Z" fill="#c48320"/>
        <path d="M 62 20 C 58 12 70 5 82 12 C 86 16 88 22 84 28 C 78 32 66 30 62 20 Z" fill="#5c3008"/>
        <path d="M 74 32 L 88 44 L 98 52 L 105 51 L 93 41 L 80 30 Z" fill="#e5a93c"/>
        <path d="M 65 18 C 60 8 72 2 86 8 C 94 14 96 24 90 34 C 80 38 68 32 65 18 Z" fill="#7a4413"/>
        <path d="M 68 22 C 65 15 74 8 84 14 C 90 18 91 26 86 32 C 78 35 70 30 68 22 Z" fill="#9e5818"/>
        <path d="M 84 16 C 90 14 98 16 102 20 C 105 23 104 27 98 29 C 94 30 88 28 85 24 Z" fill="#e5a93c"/>
        <path d="M 98 20 C 103 21 106 23 104 26 C 101 28 97 27 96 24 Z" fill="#d49428"/>
        <circle cx="103" cy="22" r="1.5" fill="#221105"/>
        <circle cx="94" cy="20" r="1.2" fill="#221105"/>
        <path d="M 93 18 L 96 18" stroke="#5c3008" stroke-width="0.8"/>
        <path d="M 83 14 C 82 10 86 10 87 14 Z" fill="#7a4413"/>
    </g>""",

    # Frame 1: Recoil / Touchdown
    """<g id="lion-frame-1">
        <ellipse cx="60" cy="65" rx="38" ry="3.5" fill="rgba(0,0,0,0.15)"/>
        <path d="M 23 34 C 13 32 6 26 3 20 C 1 17 4 15 6 17 C 8 21 14 27 21 29 Z" fill="#b87b28"/>
        <path d="M 2 19 C 0 15 0 12 3 11 C 6 10 7 14 5 18 Z" fill="#3a1e06"/>
        <path d="M 30 37 L 22 47 L 18 56 L 24 58 L 28 49 L 34 40 Z" fill="#c48320"/>
        <path d="M 35 35 L 28 46 L 23 57 L 30 59 L 34 48 L 40 39 Z" fill="#e5a93c"/>
        <path d="M 28 32 C 38 28 54 27 68 30 C 76 32 80 37 78 42 C 68 46 48 46 33 43 C 26 41 24 35 28 32 Z" fill="#e5a93c"/>
        <path d="M 36 42 C 48 44 64 43 73 39 C 70 42 53 46 36 44 Z" fill="#f7cf88"/>
        <path d="M 66 35 L 72 47 L 76 57 L 82 57 L 78 47 L 71 33 Z" fill="#c48320"/>
        <path d="M 60 22 C 56 14 68 7 80 14 C 84 18 86 24 82 30 C 76 34 64 32 60 22 Z" fill="#5c3008"/>
        <path d="M 72 34 L 78 46 L 82 58 L 89 58 L 84 46 L 78 32 Z" fill="#e5a93c"/>
        <path d="M 63 20 C 58 10 70 4 84 10 C 92 16 94 26 88 36 C 78 40 66 34 63 20 Z" fill="#7a4413"/>
        <path d="M 66 24 C 63 17 72 10 82 16 C 88 20 89 28 84 34 C 76 37 68 32 66 24 Z" fill="#9e5818"/>
        <path d="M 82 18 C 88 16 96 18 100 22 C 103 25 102 29 96 31 C 92 32 86 30 83 26 Z" fill="#e5a93c"/>
        <path d="M 96 22 C 101 23 104 25 102 28 C 99 30 95 29 94 26 Z" fill="#d49428"/>
        <circle cx="101" cy="24" r="1.5" fill="#221105"/>
        <circle cx="92" cy="22" r="1.2" fill="#221105"/>
        <path d="M 81 16 C 80 12 84 12 85 16 Z" fill="#7a4413"/>
    </g>""",

    # Frame 2: Compression / Gathered
    """<g id="lion-frame-2">
        <ellipse cx="60" cy="65" rx="32" ry="4" fill="rgba(0,0,0,0.15)"/>
        <path d="M 22 36 C 12 36 5 32 2 26 C 0 23 3 21 5 23 C 7 27 13 32 20 32 Z" fill="#b87b28"/>
        <path d="M 1 25 C -1 21 -1 18 2 17 C 5 16 6 20 4 24 Z" fill="#3a1e06"/>
        <path d="M 28 38 L 32 47 L 30 57 L 36 58 L 38 48 L 33 39 Z" fill="#c48320"/>
        <path d="M 33 36 L 38 46 L 36 57 L 43 58 L 44 47 L 38 37 Z" fill="#e5a93c"/>
        <path d="M 26 34 C 34 26 50 25 64 29 C 72 31 76 37 74 42 C 64 47 46 47 31 43 C 24 41 22 36 26 34 Z" fill="#e5a93c"/>
        <path d="M 34 43 C 46 45 60 44 69 40 C 66 43 50 47 34 45 Z" fill="#f7cf88"/>
        <path d="M 62 36 L 56 46 L 52 56 L 58 57 L 62 47 L 67 35 Z" fill="#c48320"/>
        <path d="M 58 24 C 54 16 66 9 78 16 C 82 20 84 26 80 32 C 74 36 62 34 58 24 Z" fill="#5c3008"/>
        <path d="M 68 35 L 62 46 L 58 56 L 65 57 L 68 47 L 74 34 Z" fill="#e5a93c"/>
        <path d="M 61 22 C 56 12 68 6 82 12 C 90 18 92 28 86 38 C 76 42 64 36 61 22 Z" fill="#7a4413"/>
        <path d="M 64 26 C 61 19 70 12 80 18 C 86 22 87 30 82 36 C 74 39 66 34 64 26 Z" fill="#9e5818"/>
        <path d="M 80 20 C 86 18 94 20 98 24 C 101 27 100 31 94 33 C 90 34 84 32 81 28 Z" fill="#e5a93c"/>
        <path d="M 94 24 C 99 25 102 27 100 30 C 97 32 93 31 92 28 Z" fill="#d49428"/>
        <circle cx="99" cy="26" r="1.5" fill="#221105"/>
        <circle cx="90" cy="24" r="1.2" fill="#221105"/>
        <path d="M 79 18 C 78 14 82 14 83 18 Z" fill="#7a4413"/>
    </g>""",

    # Frame 3: Propulsion Push-off
    """<g id="lion-frame-3">
        <ellipse cx="60" cy="65" rx="30" ry="3" fill="rgba(0,0,0,0.12)"/>
        <path d="M 24 33 C 14 30 7 23 4 17 C 2 14 5 12 7 14 C 9 18 15 24 22 28 Z" fill="#b87b28"/>
        <path d="M 3 16 C 1 12 1 9 4 8 C 7 7 8 11 6 15 Z" fill="#3a1e06"/>
        <path d="M 30 35 L 18 46 L 10 54 L 16 56 L 24 47 L 34 38 Z" fill="#c48320"/>
        <path d="M 36 33 L 24 45 L 16 55 L 23 57 L 30 47 L 40 36 Z" fill="#e5a93c"/>
        <path d="M 28 29 C 38 23 54 23 68 26 C 76 28 80 32 78 38 C 68 42 48 43 33 39 C 26 37 24 32 28 29 Z" fill="#e5a93c"/>
        <path d="M 36 39 C 48 41 64 40 73 36 C 70 39 53 43 36 41 Z" fill="#f7cf88"/>
        <path d="M 65 31 L 76 41 L 84 48 L 90 47 L 81 40 L 71 29 Z" fill="#c48320"/>
        <path d="M 60 18 C 56 10 68 3 80 10 C 84 14 86 20 82 26 C 76 30 64 28 60 18 Z" fill="#5c3008"/>
        <path d="M 71 30 L 84 40 L 94 48 L 101 47 L 89 38 L 77 28 Z" fill="#e5a93c"/>
        <path d="M 63 16 C 58 6 70 0 84 6 C 92 12 94 22 88 32 C 78 36 66 30 63 16 Z" fill="#7a4413"/>
        <path d="M 66 20 C 63 13 72 6 82 12 C 88 16 89 24 84 30 C 76 33 68 28 66 20 Z" fill="#9e5818"/>
        <path d="M 82 14 C 88 12 96 14 100 18 C 103 21 102 25 96 27 C 92 28 86 26 83 22 Z" fill="#e5a93c"/>
        <path d="M 96 18 C 101 19 104 21 102 24 C 99 26 95 25 94 22 Z" fill="#d49428"/>
        <circle cx="101" cy="20" r="1.5" fill="#221105"/>
        <circle cx="92" cy="18" r="1.2" fill="#221105"/>
        <path d="M 81 12 C 80 8 84 8 85 12 Z" fill="#7a4413"/>
    </g>""",

    # Frame 4: High Flight / Apex
    """<g id="lion-frame-4">
        <ellipse cx="60" cy="65" rx="25" ry="2.5" fill="rgba(0,0,0,0.08)"/>
        <path d="M 26 29 C 16 25 9 18 6 12 C 4 9 7 7 9 9 C 11 13 17 20 24 24 Z" fill="#b87b28"/>
        <path d="M 5 11 C 3 7 3 4 6 3 C 9 2 10 6 8 10 Z" fill="#3a1e06"/>
        <path d="M 33 31 L 20 40 L 10 46 L 15 48 L 25 41 L 37 34 Z" fill="#c48320"/>
        <path d="M 39 29 L 26 39 L 16 46 L 22 48 L 31 40 L 43 32 Z" fill="#e5a93c"/>
        <path d="M 31 25 C 41 19 57 19 71 23 C 79 25 83 29 81 35 C 71 39 51 40 36 36 C 29 34 27 29 31 25 Z" fill="#e5a93c"/>
        <path d="M 39 36 C 51 38 67 37 76 33 C 73 36 56 40 39 38 Z" fill="#f7cf88"/>
        <path d="M 68 28 L 80 37 L 90 43 L 96 42 L 86 35 L 74 26 Z" fill="#c48320"/>
        <path d="M 63 14 C 59 6 71 -1 83 6 C 87 10 89 16 85 22 C 79 26 67 24 63 14 Z" fill="#5c3008"/>
        <path d="M 74 27 L 88 36 L 100 42 L 106 41 L 93 33 L 80 25 Z" fill="#e5a93c"/>
        <path d="M 66 12 C 61 2 73 -4 87 2 C 95 8 97 18 91 28 C 81 32 69 26 66 12 Z" fill="#7a4413"/>
        <path d="M 69 16 C 66 9 75 2 85 8 C 91 12 92 20 87 26 C 79 29 71 24 69 16 Z" fill="#9e5818"/>
        <path d="M 85 10 C 91 8 99 10 103 14 C 106 17 105 21 99 23 C 95 24 89 22 86 18 Z" fill="#e5a93c"/>
        <path d="M 99 14 C 104 15 107 17 105 20 C 102 22 98 21 97 18 Z" fill="#d49428"/>
        <circle cx="104" cy="16" r="1.5" fill="#221105"/>
        <circle cx="95" cy="14" r="1.2" fill="#221105"/>
        <path d="M 84 8 C 83 4 87 4 88 8 Z" fill="#7a4413"/>
    </g>""",

    # Frame 5: Descent Prepare
    """<g id="lion-frame-5">
        <ellipse cx="60" cy="65" rx="30" ry="3" fill="rgba(0,0,0,0.12)"/>
        <path d="M 25 31 C 15 27 8 20 5 14 C 3 11 6 9 8 11 C 10 15 16 22 23 26 Z" fill="#b87b28"/>
        <path d="M 4 13 C 2 9 2 6 5 5 C 8 4 9 8 7 12 Z" fill="#3a1e06"/>
        <path d="M 31 33 L 19 44 L 11 52 L 17 54 L 25 45 L 35 36 Z" fill="#c48320"/>
        <path d="M 37 31 L 25 43 L 17 53 L 24 55 L 31 45 L 41 34 Z" fill="#e5a93c"/>
        <path d="M 29 27 C 39 21 55 21 69 25 C 77 27 81 31 79 37 C 69 41 49 42 34 38 C 27 36 25 31 29 27 Z" fill="#e5a93c"/>
        <path d="M 37 38 C 49 40 65 39 74 35 C 71 38 54 42 37 40 Z" fill="#f7cf88"/>
        <path d="M 66 30 L 77 42 L 83 51 L 89 50 L 81 41 L 72 28 Z" fill="#c48320"/>
        <path d="M 61 16 C 57 8 69 1 81 8 C 85 12 87 18 83 24 C 77 28 65 26 61 16 Z" fill="#5c3008"/>
        <path d="M 72 29 L 85 41 L 93 51 L 100 50 L 90 39 L 78 27 Z" fill="#e5a93c"/>
        <path d="M 64 14 C 59 4 71 -2 85 4 C 93 10 95 20 89 30 C 79 34 67 28 64 14 Z" fill="#7a4413"/>
        <path d="M 67 18 C 64 11 73 4 83 10 C 89 14 90 22 85 28 C 77 31 69 26 67 18 Z" fill="#9e5818"/>
        <path d="M 83 12 C 89 10 97 12 101 16 C 104 19 103 23 97 25 C 93 26 87 24 84 20 Z" fill="#e5a93c"/>
        <path d="M 97 16 C 102 17 105 19 103 22 C 100 24 96 23 95 20 Z" fill="#d49428"/>
        <circle cx="102" cy="18" r="1.5" fill="#221105"/>
        <circle cx="93" cy="16" r="1.2" fill="#221105"/>
        <path d="M 82 10 C 81 6 85 6 86 10 Z" fill="#7a4413"/>
    </g>"""
]

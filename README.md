# स्व-परिवार · SW-PARIVAR — Indian Social Work Knowledge Base

A searchable, filterable HTML reference built for UGC-NET Social Work aspirants, CSR practitioners, and social work field professionals.

<!-- TODO: Add screenshot -->

## Features

- **Full-text search** across all entries
- **Category filters** — Acts / Schemes / Judgments / Constitution / Frameworks (color-coded)
- **Importance filter** — High / Medium / Supplementary priority tiers
- **Exam mode toggle** — show only UGC-NET relevant items
- **Bookmarks** — save favourites via `localStorage` (persists across sessions)
- **Dark / Light theme** — toggle with one click
- **Card / List view** — switch between visual and compact layouts
- **Detail modal** — click any entry for full text; copy-to-clipboard on key content
- **Keyboard shortcuts** — quick navigation without reaching for the mouse
- **Responsive mobile-first design** — works on phone, tablet, and desktop

## Data covered

| Category | Items | Description |
|---|---|---|
| ⚖️ Acts | 25 | Social welfare legislation (POSH, PESA, FRA, MGNREGA, JJ Act, etc.) |
| 🏛️ Schemes | 24 | Government welfare programs (Ayushman Bharat, PMAY, SBM, etc.) |
| 📋 Judgments | 19 | Landmark Supreme Court rulings on social justice |
| 📕 Constitution | 33 | FRs, DPSPs, Schedules relevant to social work |
| 🌐 Frameworks | 14 | CSR law (Companies Act), SDGs, UN Conventions, ILO |

## How to use

Open `index.html` in any modern browser via a local server (Live Server, Python `http.server`, GitHub Pages, etc.). Works offline after the first load — no backend required.

## Zero-install

Single HTML file + 5 JSON data files. No build step, no npm, no bundler, no database.

## Project structure

```
sw-parivar/
├── index.html              # Single-file app (~1500 lines CSS + JS + HTML)
├── data/
│   ├── acts.json           # Social welfare acts
│   ├── schemes.json        # Government schemes
│   ├── judgments.json      # Landmark judgments
│   ├── constitution.json   # Constitutional provisions
│   └── frameworks.json     # CSR & international frameworks
├── images/                 # Static assets
├── README.md
├── LICENSE
└── .gitignore
```

## Roadmap

- MCQ quiz mode for exam practice
- Comparison view (side-by-side entries)
- PDF / print export
- Citation generator (APA/MLA)
- Community PRs for new entries and corrections

## License

MIT — see [LICENSE](LICENSE).

## Author

**Rituparno Majumdar** — CSR Project Coordinator at TRCSC / Tata Steel UISL, Jamshedpur. UGC-NET (Social Work) qualified.

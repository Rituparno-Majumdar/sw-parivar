<div align="center">

# 📚 स्व-परिवार · SW-PARIVAR

**Indian Social Work Knowledge Base — Laws, Schemes, Judgments & Frameworks**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/Rituparno-Majumdar/sw-parivar/releases)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Made for](https://img.shields.io/badge/UGC--NET-Social%20Work-ff6f00.svg)](https://www.ugcnet.nta.nic.in)
![Zero-install](https://img.shields.io/badge/install-zero-1abc9c.svg)
![Offline-first](https://img.shields.io/badge/offline-first-2ecc71.svg)
![File size](https://img.shields.io/badge/size-380KB-e74c3c.svg)

---

A **self-contained, offline-first** HTML knowledge base for UGC-NET Social Work aspirants,
CSR practitioners, NGO professionals, and social work educators.
Zero dependencies. Open and use — no internet needed.

</div>

---

## ✨ Features

| | Feature | Detail |
|---|---|---|
| 🔍 | **Full-text search** | Instant search across all 231 entries with real-time results |
| 🏷️ | **5 category filters** | Acts · Schemes · Judgments · Constitution · Frameworks (color-coded pills) |
| 🎯 | **3 importance tiers** | High / Medium / Supplementary — prioritise your study |
| 🗺️ | **State filter** | Central · Jharkhand · Odisha — state-specific schemes & acts |
| 👥 | **Target group filter** | Women, Children, SC/ST, Elderly, Persons with Disabilities, and more |
| 📖 | **Exam mode** | Toggle to show only UGC-NET relevant items |
| ⭐ | **Bookmarks** | Save favourites to `localStorage` — persists across sessions |
| 🌙 | **Dark / Light theme** | Toggle with one click — preference saved |
| 📱 | **Responsive design** | Mobile-first layout works on phone, tablet, desktop |
| ⌨️ | **Keyboard shortcuts** | `Ctrl+F` to search, `Esc` to close modals |
| 🔄 | **Remote updates** | Pull latest entries from GitHub with one click |
| 🚀 | **Zero install** | No build step, no npm, no bundler, no database |

---

## 📊 Data at a Glance

| Category | Emoji | Count | Focus Area |
|---|---|---|---|
| **Acts** | ⚖️ | 25 | Social welfare legislation — POSH, PESA, FRA, MGNREGA, JJ Act & more |
| **Schemes** | 🏛️ | 24 | Government programs — Ayushman Bharat, PMAY, SBM, PM-KISAN & more |
| **Judgments** | 📋 | 19 | Landmark Supreme Court rulings on social justice |
| **Constitution** | 📕 | 33 | Fundamental Rights, DPSPs, Schedules relevant to social work |
| **Frameworks** | 🌐 | 14 | CSR law, SDGs, UN Conventions, ILO standards |

**Total: 231 entries** covering central & state (Jharkhand, Odisha) policies.

---

## 🚀 Quick Start

### Option 1: Open in browser (basic)

```bash
python3 serve.py
```

This starts a local server at `http://localhost:8080` and opens your browser automatically.
Works on macOS, Windows, and Linux.

### Option 2: Self-contained (double-click)

Just open `index.html` in any browser. The full database is embedded in the file.
*Note: search and update features work best with the local server.*

### Option 3: Add to your data

```bash
# Edit data.json, then rebuild the embedded database:
python3 build.py

# Or build and launch in one go:
python3 build.py --serve
```

---

## 🧰 Project Structure

```
sw-parivar/
├── index.html              # Self-contained app (all CSS + JS + data embedded)
├── data.json               # Standalone database (same content as embedded)
├── serve.py                # Cross-platform local server launcher
├── build.py                # Build script: embeds data.json into index.html
├── data/
│   ├── acts.json           # Social welfare acts (source)
│   ├── schemes.json        # Government schemes (source)
│   ├── judgments.json      # Landmark judgments (source)
│   ├── constitution.json   # Constitutional provisions (source)
│   └── frameworks.json     # CSR & international frameworks (source)
├── README.md               # This file
├── LICENSE                 # MIT license
└── .gitignore
```

---

## 🎯 Who is this for?

| Audience | How it helps |
|---|---|
| **UGC-NET aspirants** | Exam mode + importance tiers for focused revision |
| **CSR professionals** | Acts & frameworks for compliance reference |
| **Social workers** | Offline field reference for schemes, entitlements & legal provisions |
| **Educators** | Ready-made teaching resource for social work classrooms |
| **NGO staff** | Quick lookup of beneficiary eligibility & government programs |

---

## 🗺️ Roadmap

- [ ] MCQ quiz mode for exam practice
- [ ] Comparison view (side-by-side entries)
- [ ] PDF / print export
- [ ] Citation generator (APA/MLA)
- [ ] Community contributions for new entries

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add an entry, fix an error, or improve the UI:

1. Fork the repository
2. Edit `data.json` (or the individual file in `data/`)
3. Run `python3 build.py` to update `index.html`
4. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

[MIT](LICENSE) — free to use, modify, and distribute.

## 👤 Author

**Rituparno Majumdar** — CSR Project Coordinator at TRCSC / Tata Steel UISL, Jamshedpur. UGC-NET (Social Work) qualified.

- GitHub: [@Rituparno-Majumdar](https://github.com/Rituparno-Majumdar)

---

<div align="center">
  <sub>Built with ❤️ for the Indian social work community</sub>
</div>

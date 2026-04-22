# MILFIT — 52-Week Military Calisthenics Program

## Setup & Run

### Requirements
- Python 3.8+
- pip

### Install & Launch

```bash
# 1. Install Flask
pip install flask

# 2. Run the app
cd milfit
python app.py

# 3. Open browser at:
# http://localhost:5000
```

## Features
- **52-week full program** — 4 training phases: Conditioning → Strength → Endurance → Power → Elite
- **Deload weeks** every 4th week (scheduled recovery)
- **Start date** — set your deployment date, app tracks your active week automatically
- **Pause/Resume** — freeze the week timer if life intervenes; paused days are excluded from calculation
- **Navigation** — Previous/Next week buttons, Jump-to-Week modal, click any dot on the program map
- **Visual charts** — Volume progression bar chart, muscle group doughnut chart
- **Intensity meter** — per-week visual difficulty indicator
- **Exercise reference** — stick-figure illustrations + exercise stats per movement

## Program Structure
| Phase | Weeks | Focus |
|-------|-------|-------|
| Conditioning | 1–12 | Foundation, form, baseline fitness |
| Power | 13–20 | Explosive strength development |
| Advanced Strength | 21–28 | Complex movements, near-max effort |
| Peak Conditioning | 29–36 | High intensity, combat circuits |
| Specialization | 37–44 | Military-specific: rucking, obstacle prep |
| Integration | 45–48 | All qualities combined |
| Elite Graduation | 49–52 | Mission-ready — APFT final test |

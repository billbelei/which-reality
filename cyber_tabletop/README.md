# Operation Dark Horizon — Cyber Tabletop Exercise

A Python/Flask web application delivering an **Oregon Trail–style cyber tabletop exercise** that simulates a sophisticated nation-state cyber attack against a commercial Earth-observation satellite.

## Overview

Players take the role of a ground-station operations officer defending **SENTINEL-7** through 5 escalating stages of attack. At each stage they are presented with real-world observable indicators and must choose from three response options. The game adapts based on their decisions, tracking defender and attacker scores and subsystem health across all four space-vehicle subsystem groupings.

## Features

| Feature | Details |
|---|---|
| 🎮 Oregon Trail gameplay | 5 stages, 3 choices each, branching outcomes |
| 🛰️ Realistic indicators | Ground-station IoCs drawn from actual space-vehicle attack patterns |
| 🚀 SPARTA references | Reconnaissance through Impact techniques |
| 🎯 MITRE ATT&CK references | Phishing, Valid Accounts, Command Execution, Data Manipulation, and more |
| 📋 NIST SP 800-53 Rev 5 | Relevant control families highlighted per decision |
| 🛡️ Subsystem tracking | Command & Control · Communications · Flight Software · Payload |
| 📊 After-Action Report | Full lessons-learned summary at game end |

## Running the Application

```bash
cd cyber_tabletop
pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5000** in a web browser.

## File Structure

```
cyber_tabletop/
├── app.py             # Flask application & routing
├── game_data.py       # Scenarios, SPARTA/MITRE/NIST reference data
├── requirements.txt
├── templates/
│   ├── base.html      # Shared layout
│   ├── index.html     # Mission briefing / intro
│   ├── game.html      # Stage display with indicators & choices
│   ├── outcome.html   # Post-choice analysis (SPARTA, MITRE, NIST)
│   └── summary.html   # After-action report & lessons learned
└── static/
    └── style.css      # Space-ops dark-theme UI
```

## Exercise Scenario

**"Operation Dark Horizon"** — A nation-state actor (*Celestial Dragon*) launches a multi-stage cyber campaign against SENTINEL-7:

| Stage | Scenario | Key Techniques |
|---|---|---|
| 1 | Spear-phishing & credential harvesting | SPARTA REC-0002, MITRE T1566 |
| 2 | Ground station breach via stolen credentials | SPARTA IA-0002, MITRE T1078/T1059 |
| 3 | Unauthorized commands uplinked to spacecraft | SPARTA EXE-0001, MITRE T1601 |
| 4 | Data exfiltration & communications jamming | SPARTA EXF-0001/IMP-0002, MITRE T1498 |
| 5 | Final firmware attack / recovery decision | SPARTA PER-0001, MITRE T1601 |

## Frameworks Referenced

- **[SPARTA](https://sparta.aerospace.org/)** — Space Attack Research and Tactic Analysis
- **[MITRE ATT&CK®](https://attack.mitre.org/)** — Adversarial Tactics, Techniques & Common Knowledge
- **[NIST SP 800-53 Rev 5](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)** — Security and Privacy Controls for Information Systems

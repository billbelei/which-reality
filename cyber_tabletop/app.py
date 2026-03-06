"""
Cyber Tabletop Exercise — Flask Web Application
Oregon Trail-style game simulating a cyber attack on a space vehicle.
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session

from game_data import (
    STAGES,
    SUBSYSTEMS,
    DEGRADATION_LEVELS,
    SPARTA_TECHNIQUES,
    MITRE_TECHNIQUES,
    NIST_CONTROLS,
    LESSONS_LEARNED,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def init_game():
    """Initialize (or reset) the game state stored in the session."""
    session["stage"] = 1
    session["defender_score"] = 0
    session["attacker_score"] = 0
    session["history"] = []      # list of {stage_id, choice_id, outcome_text, …}
    session["subsystems"] = {k: 0 for k in SUBSYSTEMS}


def get_stage(stage_id: int):
    for s in STAGES:
        if s["id"] == stage_id:
            return s
    return None


def determine_outcome():
    """Decide whether the defender won, attacker won, or it was mixed."""
    d = session.get("defender_score", 0)
    a = session.get("attacker_score", 0)
    # Count how many subsystems are fully compromised
    fully_compromised = sum(
        1 for v in session.get("subsystems", {}).values() if v >= 2
    )
    if d >= 12 and fully_compromised == 0:
        return "defender_wins"
    elif a >= 12 or fully_compromised >= 3:
        return "attacker_wins"
    else:
        return "mixed"


def build_technique_refs(sparta_ids, mitre_ids, nist_ids):
    """Return dicts of referenced technique objects."""
    sparta = {k: SPARTA_TECHNIQUES[k] for k in sparta_ids if k in SPARTA_TECHNIQUES}
    mitre = {k: MITRE_TECHNIQUES[k] for k in mitre_ids if k in MITRE_TECHNIQUES}
    nist = {k: NIST_CONTROLS[k] for k in nist_ids if k in NIST_CONTROLS}
    return sparta, mitre, nist


def apply_choice(choice):
    """Update session state based on a player's choice."""
    session["defender_score"] = session.get("defender_score", 0) + choice["defender_score"]
    session["attacker_score"] = session.get("attacker_score", 0) + choice["attacker_score"]

    # Update subsystem degradation levels (capped at 2)
    subsystems = dict(session.get("subsystems", {k: 0 for k in SUBSYSTEMS}))
    for sys_key, delta in choice.get("subsystem_impacts", {}).items():
        subsystems[sys_key] = min(2, subsystems.get(sys_key, 0) + delta)
    session["subsystems"] = subsystems

    # Record history entry
    sparta, mitre, nist = build_technique_refs(
        choice.get("sparta_refs", []),
        choice.get("mitre_refs", []),
        choice.get("nist_refs", []),
    )
    history = list(session.get("history", []))
    history.append(
        {
            "stage_id": session["stage"],
            "choice_id": choice["id"],
            "outcome_text": choice["outcome_text"],
            "sparta": sparta,
            "mitre": mitre,
            "nist": nist,
            "is_best": choice["is_best"],
        }
    )
    session["history"] = history


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Landing / intro page."""
    return render_template("index.html")


@app.route("/start")
def start():
    """Start a new game."""
    init_game()
    return redirect(url_for("game"))


@app.route("/game", methods=["GET"])
def game():
    """Display the current stage."""
    if "stage" not in session:
        return redirect(url_for("index"))

    stage_id = session["stage"]
    if stage_id > len(STAGES):
        return redirect(url_for("summary"))

    stage = get_stage(stage_id)
    subsystem_state = {
        k: {**SUBSYSTEMS[k], **DEGRADATION_LEVELS[session["subsystems"][k]]}
        for k in SUBSYSTEMS
    }
    return render_template(
        "game.html",
        stage=stage,
        subsystems=subsystem_state,
        defender_score=session["defender_score"],
        attacker_score=session["attacker_score"],
        total_stages=len(STAGES),
    )


@app.route("/choose", methods=["POST"])
def choose():
    """Process the player's choice and advance the game."""
    if "stage" not in session:
        return redirect(url_for("index"))

    choice_id = request.form.get("choice_id")
    stage_id = session["stage"]
    stage = get_stage(stage_id)
    if not stage:
        return redirect(url_for("summary"))

    chosen = next((c for c in stage["choices"] if c["id"] == choice_id), None)
    if not chosen:
        return redirect(url_for("game"))

    apply_choice(chosen)
    session["stage"] = stage_id + 1

    # Build refs for the outcome display page
    sparta, mitre, nist = build_technique_refs(
        chosen.get("sparta_refs", []),
        chosen.get("mitre_refs", []),
        chosen.get("nist_refs", []),
    )

    subsystem_state = {
        k: {**SUBSYSTEMS[k], **DEGRADATION_LEVELS[session["subsystems"][k]]}
        for k in SUBSYSTEMS
    }

    return render_template(
        "outcome.html",
        stage=stage,
        choice=chosen,
        sparta=sparta,
        mitre=mitre,
        nist=nist,
        subsystems=subsystem_state,
        defender_score=session["defender_score"],
        attacker_score=session["attacker_score"],
        is_final=(session["stage"] > len(STAGES)),
        total_stages=len(STAGES),
    )


@app.route("/summary")
def summary():
    """Display end-of-game summary and lessons learned."""
    if "stage" not in session:
        return redirect(url_for("index"))

    outcome_key = determine_outcome()
    outcome = LESSONS_LEARNED[outcome_key]
    lessons = LESSONS_LEARNED["general_lessons"]

    subsystem_state = {
        k: {**SUBSYSTEMS[k], **DEGRADATION_LEVELS[session["subsystems"][k]]}
        for k in SUBSYSTEMS
    }

    # Collect all unique technique references from the run
    all_sparta, all_mitre, all_nist = {}, {}, {}
    for entry in session.get("history", []):
        all_sparta.update(entry.get("sparta", {}))
        all_mitre.update(entry.get("mitre", {}))
        all_nist.update(entry.get("nist", {}))

    return render_template(
        "summary.html",
        outcome=outcome,
        lessons=lessons,
        subsystems=subsystem_state,
        defender_score=session["defender_score"],
        attacker_score=session["attacker_score"],
        history=session.get("history", []),
        all_sparta=all_sparta,
        all_mitre=all_mitre,
        all_nist=all_nist,
        total_stages=len(STAGES),
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, port=5000)

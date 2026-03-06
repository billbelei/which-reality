"""
Cyber Tabletop Exercise - Game Data
Space Vehicle Cyber Attack Scenario: "Operation Dark Horizon"

Covers SPARTA, MITRE ATT&CK, and NIST SP 800-53 Rev 5 references.
"""

# ---------------------------------------------------------------------------
# Subsystem definitions
# ---------------------------------------------------------------------------
SUBSYSTEMS = {
    "c2": {
        "label": "Command & Control",
        "icon": "📡",
        "description": "Ground-to-space uplink/downlink systems and mission control software",
    },
    "comms": {
        "label": "Communications",
        "icon": "📻",
        "description": "Transponders, encryption modules, and communication protocols",
    },
    "flight_sw": {
        "label": "Flight Software",
        "icon": "💾",
        "description": "Onboard flight computers, attitude control software, and firmware",
    },
    "payload": {
        "label": "Payload",
        "icon": "🛰️",
        "description": "Sensors, cameras, and mission-specific instruments",
    },
}

# Degradation levels
DEGRADATION_LEVELS = {
    0: {"label": "Nominal", "css": "nominal", "icon": "🟢"},
    1: {"label": "Degraded", "css": "degraded", "icon": "🟡"},
    2: {"label": "Compromised", "css": "compromised", "icon": "🔴"},
}

# ---------------------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------------------

SPARTA_TECHNIQUES = {
    "REC-0001": {
        "name": "Gather Victim Identity Information",
        "tactic": "Reconnaissance",
        "description": "Adversary collects identity info about personnel with access to space systems.",
    },
    "REC-0002": {
        "name": "Phishing for Information",
        "tactic": "Reconnaissance",
        "description": "Spear-phishing emails crafted to extract credentials from ground station staff.",
    },
    "IA-0002": {
        "name": "Valid Accounts",
        "tactic": "Initial Access",
        "description": "Using stolen or default credentials to access ground control systems.",
    },
    "IA-0001": {
        "name": "Supply Chain Compromise",
        "tactic": "Initial Access",
        "description": "Compromising hardware or software before delivery to the space program.",
    },
    "EXE-0001": {
        "name": "Native API / Command Execution",
        "tactic": "Execution",
        "description": "Issuing unauthorized commands through the satellite's native command interface.",
    },
    "EXE-0004": {
        "name": "Scripted Automated Commands",
        "tactic": "Execution",
        "description": "Automated command scripts sent to alter spacecraft configuration.",
    },
    "PER-0001": {
        "name": "Implant in Boot Firmware",
        "tactic": "Persistence",
        "description": "Malicious code embedded in flight software that survives reboots.",
    },
    "IMP-0002": {
        "name": "Denial of Service",
        "tactic": "Impact",
        "description": "Flooding command channels or jamming communication links to deny operator access.",
    },
    "IMP-0006": {
        "name": "Replay Attack on Commands",
        "tactic": "Impact",
        "description": "Re-transmitting previously captured valid commands to cause unintended spacecraft actions.",
    },
    "EXF-0001": {
        "name": "Exfiltration Over C2 Channel",
        "tactic": "Exfiltration",
        "description": "Stealing payload data or mission plans through the command uplink/downlink.",
    },
}

MITRE_TECHNIQUES = {
    "T1566": {
        "name": "Phishing",
        "tactic": "Initial Access",
        "description": "Sending deceptive emails to ground station employees to gain initial footholds.",
    },
    "T1589": {
        "name": "Gather Victim Identity Information",
        "tactic": "Reconnaissance",
        "description": "Collecting employee names, emails, and organizational data from public sources.",
    },
    "T1078": {
        "name": "Valid Accounts",
        "tactic": "Defense Evasion / Persistence",
        "description": "Using legitimate credentials to blend in and avoid detection.",
    },
    "T1059": {
        "name": "Command and Scripting Interpreter",
        "tactic": "Execution",
        "description": "Executing commands through scripting interfaces on ground control systems.",
    },
    "T1190": {
        "name": "Exploit Public-Facing Application",
        "tactic": "Initial Access",
        "description": "Targeting vulnerabilities in internet-facing ground segment applications.",
    },
    "T1486": {
        "name": "Data Encrypted for Impact",
        "tactic": "Impact",
        "description": "Ransomware-style encryption of ground control workstations.",
    },
    "T1499": {
        "name": "Endpoint Denial of Service",
        "tactic": "Impact",
        "description": "Overloading ground station systems to prevent command transmission.",
    },
    "T1601": {
        "name": "Modify System Image",
        "tactic": "Defense Evasion",
        "description": "Altering the spacecraft's onboard software image to change behavior.",
    },
    "T1565": {
        "name": "Data Manipulation",
        "tactic": "Impact",
        "description": "Modifying telemetry data so operators receive false readings.",
    },
    "T1498": {
        "name": "Network Denial of Service",
        "tactic": "Impact",
        "description": "Overwhelming network links between ground stations and the spacecraft.",
    },
}

NIST_CONTROLS = {
    "AC-2": {
        "name": "Account Management",
        "family": "Access Control",
        "description": "Manage information system accounts, including establishing, activating, modifying, and removing accounts.",
    },
    "AC-17": {
        "name": "Remote Access",
        "family": "Access Control",
        "description": "Establish and document usage restrictions and implementation guidance for remote access.",
    },
    "AT-2": {
        "name": "Literacy Training and Awareness",
        "family": "Awareness and Training",
        "description": "Provide security awareness training to all personnel to recognize social engineering.",
    },
    "AU-2": {
        "name": "Event Logging",
        "family": "Audit and Accountability",
        "description": "Identify events that require logging to support security investigations.",
    },
    "AU-6": {
        "name": "Audit Record Review, Analysis, and Reporting",
        "family": "Audit and Accountability",
        "description": "Review and analyze audit records for indications of unusual activity.",
    },
    "CM-7": {
        "name": "Least Functionality",
        "family": "Configuration Management",
        "description": "Configure systems to provide only essential capabilities; disable unused functions.",
    },
    "IA-2": {
        "name": "Identification and Authentication (Org. Users)",
        "family": "Identification and Authentication",
        "description": "Uniquely identify and authenticate organizational users accessing information systems.",
    },
    "IA-5": {
        "name": "Authenticator Management",
        "family": "Identification and Authentication",
        "description": "Manage system authenticators (passwords, tokens, certificates) throughout their lifecycle.",
    },
    "IR-4": {
        "name": "Incident Handling",
        "family": "Incident Response",
        "description": "Implement an incident handling capability for security incidents including preparation, detection, and recovery.",
    },
    "IR-6": {
        "name": "Incident Reporting",
        "family": "Incident Response",
        "description": "Require personnel to report suspected security incidents.",
    },
    "SC-7": {
        "name": "Boundary Protection",
        "family": "System and Communications Protection",
        "description": "Monitor and control communications at the external boundary and key internal boundaries.",
    },
    "SC-8": {
        "name": "Transmission Confidentiality and Integrity",
        "family": "System and Communications Protection",
        "description": "Implement cryptographic mechanisms to protect transmission confidentiality and integrity.",
    },
    "SI-3": {
        "name": "Malicious Code Protection",
        "family": "System and Information Integrity",
        "description": "Deploy malicious code protection mechanisms at information system entry and exit points.",
    },
    "SI-4": {
        "name": "System Monitoring",
        "family": "System and Information Integrity",
        "description": "Monitor the information system to detect attacks and indicators of potential attacks.",
    },
}

# ---------------------------------------------------------------------------
# Scenario stages
# ---------------------------------------------------------------------------
# Each stage has:
#   id, title, narrative, indicators, choices[]
#   Each choice has: id, text, outcome_text, defender_score, attacker_score,
#                    subsystem_impacts (dict), sparta_refs, mitre_refs, is_best

STAGES = [
    # -----------------------------------------------------------------------
    # STAGE 1 — Reconnaissance & Spear Phishing
    # -----------------------------------------------------------------------
    {
        "id": 1,
        "title": "Stage 1: Strange Emails & Odd Login Attempts",
        "background": (
            "Your team operates the ground control center for SENTINEL-7, a commercial "
            "Earth-observation satellite providing critical weather and disaster-response data. "
            "On a Monday morning, two satellite operators report receiving suspicious emails "
            "that appear to come from the satellite manufacturer asking them to 'verify their "
            "portal credentials.' The IT help desk also flags three failed login attempts on "
            "the mission control workstations over the weekend."
        ),
        "indicators": [
            "Two employees received spear-phishing emails mimicking the satellite manufacturer",
            "Three failed login attempts on mission control workstations (Saturday 02:14 UTC)",
            "Unusual LinkedIn scraping activity noticed on the organization's public profiles",
            "One employee admits they may have clicked the email link before realizing it was fake",
        ],
        "choices": [
            {
                "id": "1a",
                "text": "Immediately force a password reset for all mission control accounts and notify the security team.",
                "outcome_text": (
                    "Smart move! Forcing password resets cuts off any credentials the attacker "
                    "may have captured. The security team launches an investigation and discovers "
                    "the phishing campaign was designed to harvest VPN credentials. Your early "
                    "action prevents the adversary from gaining initial access."
                ),
                "defender_score": 3,
                "attacker_score": 0,
                "subsystem_impacts": {},
                "sparta_refs": ["REC-0002", "REC-0001"],
                "mitre_refs": ["T1566", "T1589"],
                "nist_refs": ["AC-2", "IA-5", "AT-2"],
                "is_best": True,
            },
            {
                "id": "1b",
                "text": "Warn employees via an all-hands email to be careful with suspicious messages but take no immediate system action.",
                "outcome_text": (
                    "Raising awareness helps, but warning alone is insufficient. That evening, "
                    "the adversary successfully uses the harvested credentials to log into the "
                    "remote maintenance VPN from an IP address in an unrecognized country. "
                    "The intrusion goes undetected until morning."
                ),
                "defender_score": 1,
                "attacker_score": 2,
                "subsystem_impacts": {"c2": 1},
                "sparta_refs": ["REC-0002", "IA-0002"],
                "mitre_refs": ["T1566", "T1078"],
                "nist_refs": ["AT-2", "AU-2"],
                "is_best": False,
            },
            {
                "id": "1c",
                "text": "Assume it's spam and log the incident for the weekly security review meeting.",
                "outcome_text": (
                    "Delaying action proves costly. The attacker uses the captured credentials "
                    "overnight to establish a persistent foothold on the ground control network. "
                    "By morning, they have mapped your internal systems and identified the "
                    "satellite command workstation."
                ),
                "defender_score": 0,
                "attacker_score": 3,
                "subsystem_impacts": {"c2": 2},
                "sparta_refs": ["REC-0001", "REC-0002", "IA-0002"],
                "mitre_refs": ["T1589", "T1566", "T1078"],
                "nist_refs": ["AU-6", "IR-4", "IR-6"],
                "is_best": False,
            },
        ],
    },
    # -----------------------------------------------------------------------
    # STAGE 2 — Ground Station Breach
    # -----------------------------------------------------------------------
    {
        "id": 2,
        "title": "Stage 2: Unauthorized Access Detected",
        "background": (
            "Your security monitoring system triggers an alert: a workstation on the mission "
            "control network is executing PowerShell commands during off-hours. A new local "
            "administrator account named 'svc_backup2' was created without a change request. "
            "Meanwhile, the SENTINEL-7 telemetry feed shows no anomalies — the spacecraft "
            "appears to be operating normally."
        ),
        "indicators": [
            "Workstation 'MCC-WS-04' executing unusual PowerShell scripts at 03:40 UTC",
            "New local admin account 'svc_backup2' created without a change management ticket",
            "Outbound connection from mission network to unrecognized IP (185.220.x.x)",
            "Increased CPU usage on the Command Planning System server",
        ],
        "choices": [
            {
                "id": "2a",
                "text": "Isolate the affected workstation from the network immediately and activate the incident response plan.",
                "outcome_text": (
                    "Excellent! Isolating the compromised workstation stops lateral movement. "
                    "The incident response team discovers a Remote Access Trojan (RAT) installed "
                    "via the phishing link. The attacker's foothold is contained. The fake admin "
                    "account is removed and the system is reimaged."
                ),
                "defender_score": 3,
                "attacker_score": 0,
                "subsystem_impacts": {},
                "sparta_refs": ["IA-0002", "EXE-0001"],
                "mitre_refs": ["T1078", "T1059"],
                "nist_refs": ["IR-4", "SI-4", "SC-7"],
                "is_best": True,
            },
            {
                "id": "2b",
                "text": "Disable the suspicious admin account but keep the workstation online to monitor the attacker's activity.",
                "outcome_text": (
                    "Disabling the account slows the attacker, but leaving the workstation "
                    "online allows a secondary backdoor (installed earlier) to remain active. "
                    "The adversary pivots to a second machine on the network and begins "
                    "accessing the command planning system."
                ),
                "defender_score": 1,
                "attacker_score": 2,
                "subsystem_impacts": {"c2": 1, "flight_sw": 1},
                "sparta_refs": ["IA-0002", "EXE-0004"],
                "mitre_refs": ["T1078", "T1059"],
                "nist_refs": ["AC-2", "SI-4", "AU-6"],
                "is_best": False,
            },
            {
                "id": "2c",
                "text": "Schedule a security scan for the workstation during the next maintenance window in two days.",
                "outcome_text": (
                    "Two days is far too long. The attacker gains full control of the command "
                    "planning system and begins staging unauthorized command sequences targeting "
                    "SENTINEL-7. The spacecraft's attitude control system receives its first "
                    "unauthorized command packet."
                ),
                "defender_score": 0,
                "attacker_score": 3,
                "subsystem_impacts": {"c2": 2, "flight_sw": 2},
                "sparta_refs": ["IA-0002", "EXE-0001", "EXE-0004"],
                "mitre_refs": ["T1078", "T1059", "T1190"],
                "nist_refs": ["IR-4", "CM-7", "SI-3"],
                "is_best": False,
            },
        ],
    },
    # -----------------------------------------------------------------------
    # STAGE 3 — Command System Compromise
    # -----------------------------------------------------------------------
    {
        "id": 3,
        "title": "Stage 3: Unauthorized Commands Uplinked",
        "background": (
            "SENTINEL-7 telemetry suddenly shows anomalies. The satellite's attitude has shifted "
            "two degrees off its nominal nadir-pointing position. Communications windows with the "
            "ground are becoming shorter and less reliable. Your flight operations team notices "
            "that the command logs show 14 commands were sent during a time window when no "
            "operator was scheduled on console. The commands appear syntactically valid."
        ),
        "indicators": [
            "SENTINEL-7 attitude shifted 2° from nadir — ground antenna tracking degraded",
            "14 commands executed with no corresponding operator entries in the mission log",
            "Telemetry downlink signal strength dropped 8 dB",
            "The onboard Command Management System reports an unexpected mode change to 'Safe Hold'",
            "Ground encryption key management system shows a key query at an unexpected time",
        ],
        "choices": [
            {
                "id": "3a",
                "text": "Invoke spacecraft safe mode procedures, revoke current command encryption keys, and generate fresh keys.",
                "outcome_text": (
                    "The right call under pressure! Commanding the spacecraft into a known-safe "
                    "configuration halts the attacker's ability to issue further harmful commands. "
                    "Revoking and regenerating the command encryption keys locks out any key "
                    "material the adversary captured. Recovery operations begin successfully."
                ),
                "defender_score": 3,
                "attacker_score": 0,
                "subsystem_impacts": {},
                "sparta_refs": ["EXE-0001", "IMP-0006"],
                "mitre_refs": ["T1601", "T1565"],
                "nist_refs": ["SC-8", "IR-4", "CM-7"],
                "is_best": True,
            },
            {
                "id": "3b",
                "text": "Send corrective attitude maneuver commands to return the satellite to its nominal position.",
                "outcome_text": (
                    "Your corrective commands are received, but the adversary intercepts and "
                    "replays them out of sequence to further confuse the spacecraft's attitude "
                    "control logic. The satellite enters a spin that cannot easily be corrected "
                    "remotely. Communications windows degrade further."
                ),
                "defender_score": 1,
                "attacker_score": 2,
                "subsystem_impacts": {"comms": 1, "flight_sw": 2},
                "sparta_refs": ["IMP-0006", "EXE-0001"],
                "mitre_refs": ["T1601", "T1499"],
                "nist_refs": ["SC-8", "SI-4", "AU-6"],
                "is_best": False,
            },
            {
                "id": "3c",
                "text": "Continue nominal operations and assume the anomaly is a software glitch, filing a trouble ticket.",
                "outcome_text": (
                    "Treating a cyber attack as a software glitch is exactly what the adversary "
                    "counted on. While your team waits for a software engineer to review the "
                    "ticket, the attacker uploads a modified firmware patch that embeds a "
                    "persistent backdoor into the flight computer."
                ),
                "defender_score": 0,
                "attacker_score": 3,
                "subsystem_impacts": {"flight_sw": 2, "c2": 1, "comms": 1},
                "sparta_refs": ["EXE-0001", "PER-0001", "IMP-0006"],
                "mitre_refs": ["T1601", "T1059", "T1565"],
                "nist_refs": ["IR-6", "IR-4", "SI-3"],
                "is_best": False,
            },
        ],
    },
    # -----------------------------------------------------------------------
    # STAGE 4 — Escalation: Communications Jamming & Data Exfiltration
    # -----------------------------------------------------------------------
    {
        "id": 4,
        "title": "Stage 4: The Adversary Escalates",
        "background": (
            "After their foothold in the ground segment, the adversary escalates operations. "
            "Your network security appliance logs a massive spike of outbound traffic — it "
            "appears satellite imagery (your payload data) is being exfiltrated to an external "
            "server. Simultaneously, SENTINEL-7's downlink is intermittently disrupted: the "
            "signal quality alternates between normal and degraded every 90 seconds, suggesting "
            "some form of interference synchronized with your communication schedule."
        ),
        "indicators": [
            "2.4 TB of data exfiltrated to external IP via encrypted tunnel over 6 hours",
            "Downlink signal disrupted in 90-second intervals matching your comm window schedule",
            "Payload imaging system shows unauthorized mode changes to 'continuous capture'",
            "Ground station firewall logs show attempted connections to 7 new external IPs",
            "Operator consoles display telemetry, but values appear identical for 40 minutes (frozen/replayed feed)",
        ],
        "choices": [
            {
                "id": "4a",
                "text": "Block all outbound traffic to unrecognized IPs, activate out-of-band communications with the spacecraft, and contact national CERT.",
                "outcome_text": (
                    "Excellent response! Blocking exfiltration stops the data loss. Switching to "
                    "out-of-band communications bypasses the compromised primary ground link, "
                    "restoring a trusted command path. CERT engagement brings additional forensic "
                    "and attribution capabilities. The adversary is effectively evicted."
                ),
                "defender_score": 3,
                "attacker_score": 0,
                "subsystem_impacts": {},
                "sparta_refs": ["EXF-0001", "IMP-0002"],
                "mitre_refs": ["T1498", "T1565"],
                "nist_refs": ["SC-7", "IR-4", "IR-6"],
                "is_best": True,
            },
            {
                "id": "4b",
                "text": "Focus on the spacecraft anomaly first — send commands to reset the payload to its default mode.",
                "outcome_text": (
                    "Focusing only on the spacecraft leaves the ground network wide open. "
                    "Exfiltration continues uninterrupted, and the adversary uses the command "
                    "channel to initiate a Denial of Service attack against the ground station's "
                    "command routing servers, blinding operators to spacecraft state."
                ),
                "defender_score": 1,
                "attacker_score": 2,
                "subsystem_impacts": {"payload": 1, "comms": 2},
                "sparta_refs": ["EXF-0001", "IMP-0002", "IMP-0006"],
                "mitre_refs": ["T1498", "T1499", "T1565"],
                "nist_refs": ["SI-4", "AU-6", "SC-7"],
                "is_best": False,
            },
            {
                "id": "4c",
                "text": "Continue monitoring to gather evidence before acting — you need to understand the full scope first.",
                "outcome_text": (
                    "Waiting costs you dearly. The exfiltration completes, and the adversary "
                    "pivots to a destructive phase: encrypted ransomware is deployed across ground "
                    "station workstations, the payload is commanded to a power-intensive mode "
                    "that risks thermal damage, and the comm system is jammed."
                ),
                "defender_score": 0,
                "attacker_score": 3,
                "subsystem_impacts": {"payload": 2, "comms": 2, "flight_sw": 1},
                "sparta_refs": ["EXF-0001", "IMP-0002", "IMP-0006"],
                "mitre_refs": ["T1486", "T1498", "T1499", "T1565"],
                "nist_refs": ["IR-4", "SC-7", "SI-4"],
                "is_best": False,
            },
        ],
    },
    # -----------------------------------------------------------------------
    # STAGE 5 — Resolution
    # -----------------------------------------------------------------------
    {
        "id": 5,
        "title": "Stage 5: Final Stand — Recovery or Defeat",
        "background": (
            "Your incident response team has been working for 18 hours straight. The adversary "
            "has one last card to play: they attempt to upload a final malicious firmware patch "
            "to SENTINEL-7's flight computer that would permanently brick the spacecraft. "
            "You have a narrow window of approximately 20 minutes before the next scheduled "
            "uplink pass to act. Your choices now will determine whether SENTINEL-7 survives."
        ),
        "indicators": [
            "Command queue shows a 47 KB file staged for uplink — no operator authorized this",
            "The file has a valid (but stolen) command authentication code",
            "SENTINEL-7 will be in uplink range in 18 minutes",
            "Ground network segmentation has partially limited attacker movement",
            "Out-of-band backup comm system is operational but has limited bandwidth",
        ],
        "choices": [
            {
                "id": "5a",
                "text": "Use the out-of-band backup system to uplink an emergency command that disables the primary command receiver until keys are rotated.",
                "outcome_text": (
                    "Brilliant! By disabling the primary receiver via the trusted backup channel, "
                    "you deny the attacker's final upload. The rogue firmware patch never reaches "
                    "SENTINEL-7. With the spacecraft secured, your team begins full recovery: "
                    "new keys are issued, the spacecraft is restored from a known-good software "
                    "baseline, and SENTINEL-7 resumes operations within 48 hours. "
                    "The adversary's campaign has failed."
                ),
                "defender_score": 3,
                "attacker_score": 0,
                "subsystem_impacts": {},
                "sparta_refs": ["PER-0001", "EXE-0001"],
                "mitre_refs": ["T1601", "T1059"],
                "nist_refs": ["SC-8", "CM-7", "IR-4"],
                "is_best": True,
            },
            {
                "id": "5b",
                "text": "Alert your spacecraft manufacturer and attempt to have them remotely authenticate and block the file.",
                "outcome_text": (
                    "Reaching out to the manufacturer is a good instinct, but the 18-minute "
                    "window is too short for the coordination required. The manufacturer's "
                    "on-call team is reached with 4 minutes to spare — not enough time. "
                    "The malicious patch is uploaded. SENTINEL-7 enters a permanent fault state. "
                    "Mission operations are suspended indefinitely."
                ),
                "defender_score": 1,
                "attacker_score": 3,
                "subsystem_impacts": {"flight_sw": 2, "c2": 2, "payload": 2, "comms": 2},
                "sparta_refs": ["PER-0001", "EXE-0001", "IMP-0002"],
                "mitre_refs": ["T1601", "T1499"],
                "nist_refs": ["IR-4", "IR-6"],
                "is_best": False,
            },
            {
                "id": "5c",
                "text": "Physically disconnect the ground station uplink antenna to prevent the upload from happening.",
                "outcome_text": (
                    "A decisive physical action! Disconnecting the antenna prevents the "
                    "malicious upload — but also cuts off all legitimate contact with the "
                    "spacecraft for the next 6 hours. SENTINEL-7 enters autonomous safe mode "
                    "as designed. Although mission operations are delayed, the spacecraft "
                    "is physically undamaged and key rotation begins. A partial victory: "
                    "the spacecraft survives, but recovery takes weeks."
                ),
                "defender_score": 2,
                "attacker_score": 1,
                "subsystem_impacts": {"comms": 1},
                "sparta_refs": ["IMP-0002", "PER-0001"],
                "mitre_refs": ["T1601", "T1499"],
                "nist_refs": ["SC-7", "IR-4", "CM-7"],
                "is_best": False,
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Lessons learned (shown at game end)
# ---------------------------------------------------------------------------
LESSONS_LEARNED = {
    "defender_wins": {
        "headline": "🛡️ Mission Saved — Defender Victory!",
        "summary": (
            "SENTINEL-7 survives the attack. Through timely detection, coordinated response, "
            "and sound decision-making, your team successfully thwarted a sophisticated "
            "nation-state cyber attack on a space asset."
        ),
    },
    "attacker_wins": {
        "headline": "☠️ Mission Lost — Attacker Victory!",
        "summary": (
            "SENTINEL-7 has been compromised. The adversary successfully degraded or destroyed "
            "the spacecraft's operations. This exercise highlights the consequences of delayed "
            "detection and reactive (rather than proactive) security postures."
        ),
    },
    "mixed": {
        "headline": "⚖️ Contested Outcome — Partial Defense",
        "summary": (
            "SENTINEL-7 sustained significant damage but survived in a degraded state. "
            "Some defender actions limited the attack scope, but gaps in security posture "
            "allowed the adversary to achieve several objectives."
        ),
    },
    "general_lessons": [
        {
            "title": "The Value of SPARTA and MITRE ATT&CK Frameworks",
            "body": (
                "SPARTA (Space Attack Research and Tactic Analysis) extends MITRE ATT&CK "
                "to space systems. Together, they give defenders a common vocabulary to "
                "describe adversary behavior — from reconnaissance all the way to impact. "
                "Understanding these frameworks allows operators to recognize attack patterns "
                "early, rather than treating each anomaly in isolation."
            ),
        },
        {
            "title": "Recognizing Indicators of Compromise (IoCs)",
            "body": (
                "This exercise showed how cyber attacks on space vehicles produce observable "
                "indicators at the ground segment: anomalous logins, unexpected command "
                "executions, attitude anomalies, and telemetry irregularities. Building "
                "playbooks around these indicators — and training operators to recognize "
                "them — is critical to early detection."
            ),
        },
        {
            "title": "Subsystem Degradation and the Attack Kill Chain",
            "body": (
                "Attacks rarely impact all subsystems at once. The adversary typically "
                "begins at Command & Control (the ground-space interface), then pivots to "
                "Communications (disrupting the command path), Flight Software (for "
                "persistence and reconfiguration), and finally the Payload (the mission "
                "objective). Understanding this progression helps prioritize what to "
                "protect first and detect earliest."
            ),
        },
        {
            "title": "Key Cyber Protections That Would Have Helped",
            "body": (
                "• Multi-Factor Authentication (MFA) on all mission-critical accounts (AC-2, IA-2)\n"
                "• Anomaly-based monitoring of command logs and network traffic (SI-4, AU-6)\n"
                "• Strict boundary protection between IT and mission networks (SC-7)\n"
                "• Encrypted and authenticated command channels with frequent key rotation (SC-8)\n"
                "• Regular phishing awareness training for all ground station personnel (AT-2)\n"
                "• Tested incident response plans with defined roles (IR-4, IR-6)\n"
                "• Least-privilege access to command systems (CM-7, AC-2)"
            ),
        },
        {
            "title": "NIST SP 800-53 Rev 5 Controls That Address These Threats",
            "body": (
                "The following control families are most relevant to space vehicle cybersecurity:\n\n"
                "• **Access Control (AC):** AC-2 (Account Management), AC-17 (Remote Access)\n"
                "• **Awareness & Training (AT):** AT-2 (Security Awareness Training)\n"
                "• **Audit & Accountability (AU):** AU-2 (Event Logging), AU-6 (Log Review)\n"
                "• **Configuration Management (CM):** CM-7 (Least Functionality)\n"
                "• **Identification & Authentication (IA):** IA-2 (Multi-Factor Auth), IA-5 (Credential Mgmt)\n"
                "• **Incident Response (IR):** IR-4 (Incident Handling), IR-6 (Incident Reporting)\n"
                "• **System & Comms Protection (SC):** SC-7 (Boundary Protection), SC-8 (Transmission Security)\n"
                "• **System & Info Integrity (SI):** SI-3 (Malware Protection), SI-4 (System Monitoring)"
            ),
        },
    ],
}

from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)

PROGRAM = {
    1: {
        "title": "FOUNDATION ZERO",
        "phase": "CONDITIONING",
        "theme": "Build the base. No shortcuts.",
        "description": "Week 1 establishes baseline movement patterns and body awareness. Focus on form over speed. Military readiness begins with mastering the fundamentals — every elite soldier was once a raw recruit performing these exact movements.",
        "exercises": [
            {"name": "Push-Ups", "sets": 3, "reps": "10", "rest": "60s", "muscle": "Chest / Triceps / Shoulders",
             "icon": "💪"},
            {"name": "Bodyweight Squats", "sets": 3, "reps": "15", "rest": "60s",
             "muscle": "Quads / Glutes / Hamstrings", "icon": "🦵"},
            {"name": "Plank Hold", "sets": 3, "reps": "20s", "rest": "45s", "muscle": "Core / Shoulders", "icon": "🛡"},
            {"name": "Jumping Jacks", "sets": 3, "reps": "30", "rest": "45s", "muscle": "Full Body / Cardio",
             "icon": "⚡"},
            {"name": "Glute Bridges", "sets": 3, "reps": "12", "rest": "45s", "muscle": "Glutes / Lower Back",
             "icon": "🔥"},
        ],
        "tips": "Breathe: exhale on exertion, inhale on return. Never hold your breath.",
        "weekly_goal": "Complete 3 training sessions with 1 rest day between each.",
        "intensity": 2,
        "volume": 135,
    },
    2: {
        "title": "BASELINE COMMAND",
        "phase": "CONDITIONING",
        "theme": "Establish your rhythm. Pain is weakness leaving the body.",
        "description": "Increase volume from Week 1. Your muscles are adapting — push them further. Military recruits are tested on volume in week 2 to gauge recovery capacity. Train, recover, repeat.",
        "exercises": [
            {"name": "Push-Ups", "sets": 3, "reps": "15", "rest": "60s", "muscle": "Chest / Triceps", "icon": "💪"},
            {"name": "Bodyweight Squats", "sets": 3, "reps": "20", "rest": "60s", "muscle": "Quads / Glutes",
             "icon": "🦵"},
            {"name": "Plank Hold", "sets": 3, "reps": "30s", "rest": "45s", "muscle": "Core", "icon": "🛡"},
            {"name": "Mountain Climbers", "sets": 3, "reps": "20", "rest": "45s", "muscle": "Core / Cardio",
             "icon": "⚡"},
            {"name": "Reverse Lunges", "sets": 3, "reps": "10 each", "rest": "60s",
             "muscle": "Quads / Glutes / Balance", "icon": "🔥"},
            {"name": "Superman Hold", "sets": 3, "reps": "15s", "rest": "30s", "muscle": "Lower Back / Glutes",
             "icon": "🌟"},
        ],
        "tips": "Control the descent on every rep. Slow negatives build more strength.",
        "weekly_goal": "3 sessions. Track your total push-up count for the week.",
        "intensity": 3,
        "volume": 195,
    },
    3: {
        "title": "IRON DISCIPLINE",
        "phase": "CONDITIONING",
        "theme": "Discipline is the bridge between goals and accomplishment.",
        "description": "Enter the first progression phase. New movement patterns challenge coordination and balance. Military training at this stage tests mental resolve — the body can do far more than the mind believes.",
        "exercises": [
            {"name": "Diamond Push-Ups", "sets": 3, "reps": "10", "rest": "60s", "muscle": "Triceps / Inner Chest",
             "icon": "💎"},
            {"name": "Jump Squats", "sets": 3, "reps": "15", "rest": "60s", "muscle": "Explosive Legs / Power",
             "icon": "⚡"},
            {"name": "Side Plank", "sets": 3, "reps": "20s each", "rest": "45s", "muscle": "Obliques / Core",
             "icon": "🛡"},
            {"name": "Burpees", "sets": 3, "reps": "8", "rest": "90s", "muscle": "Full Body / Conditioning",
             "icon": "🔥"},
            {"name": "Walking Lunges", "sets": 3, "reps": "20 steps", "rest": "60s", "muscle": "Legs / Stability",
             "icon": "🦵"},
        ],
        "tips": "Burpees are your enemy and your ally. Embrace them.",
        "weekly_goal": "3 sessions. Introduce burpees without stopping mid-set.",
        "intensity": 4,
        "volume": 180,
    },
    4: {
        "title": "DELOAD & CONSOLIDATE",
        "phase": "CONDITIONING",
        "theme": "Rest is not weakness. It is strategy.",
        "description": "Every 4th week is a deload. Military operators know that recovery is part of the mission. Reduce volume by 40%, maintain intensity. Let the adaptations consolidate.",
        "exercises": [
            {"name": "Push-Ups", "sets": 2, "reps": "12", "rest": "90s", "muscle": "Chest / Triceps", "icon": "💪"},
            {"name": "Bodyweight Squats", "sets": 2, "reps": "15", "rest": "90s", "muscle": "Quads / Glutes",
             "icon": "🦵"},
            {"name": "Plank Hold", "sets": 2, "reps": "45s", "rest": "60s", "muscle": "Core", "icon": "🛡"},
            {"name": "Yoga Flow / Mobility", "sets": 1, "reps": "10 min", "rest": "0s",
             "muscle": "Full Body / Recovery", "icon": "🌿"},
        ],
        "tips": "Prioritize sleep (8h+) and hydration (3L+ water) this week.",
        "weekly_goal": "2 light sessions only. Active recovery on other days.",
        "intensity": 1,
        "volume": 90,
    },
    5: {
        "title": "STRENGTH INITIATIVE",
        "phase": "STRENGTH",
        "theme": "Phase 2 begins. You are no longer a recruit.",
        "description": "Phase 2 shifts from conditioning to raw strength. Lower rep ranges, longer rest periods. Military strength standards require functional power — the ability to carry loads, climb obstacles, and endure under pressure.",
        "exercises": [
            {"name": "Wide Push-Ups", "sets": 4, "reps": "12", "rest": "75s", "muscle": "Outer Chest / Shoulders",
             "icon": "💪"},
            {"name": "Pistol Squat Assist", "sets": 4, "reps": "6 each", "rest": "90s", "muscle": "Quads / Balance",
             "icon": "🎯"},
            {"name": "Pike Push-Ups", "sets": 4, "reps": "10", "rest": "75s", "muscle": "Shoulders / Triceps",
             "icon": "⚡"},
            {"name": "Bulgarian Split Squat", "sets": 4, "reps": "8 each", "rest": "90s",
             "muscle": "Quads / Glutes / Balance", "icon": "🦵"},
            {"name": "Hollow Body Hold", "sets": 3, "reps": "30s", "rest": "60s", "muscle": "Core / Hip Flexors",
             "icon": "🛡"},
        ],
        "tips": "Slow down your tempo: 3 seconds down, 1 second pause, 1 second up.",
        "weekly_goal": "4 training sessions this week. Push for clean form.",
        "intensity": 5,
        "volume": 240,
    },
    6: {
        "title": "FORCE MULTIPLIER",
        "phase": "STRENGTH",
        "theme": "Compounding effort. Every rep adds to your arsenal.",
        "description": "Introduce pulling movements. A complete military physique requires balanced push/pull strength. Improvised pulling — using tables, bars, tree branches — is the field soldier's gym.",
        "exercises": [
            {"name": "Decline Push-Ups", "sets": 4, "reps": "12", "rest": "75s", "muscle": "Upper Chest / Shoulders",
             "icon": "💪"},
            {"name": "Table/Bar Rows", "sets": 4, "reps": "12", "rest": "75s", "muscle": "Back / Biceps", "icon": "🎯"},
            {"name": "Jump Squats", "sets": 4, "reps": "12", "rest": "60s", "muscle": "Explosive Power", "icon": "⚡"},
            {"name": "Dips (Chair)", "sets": 4, "reps": "10", "rest": "75s", "muscle": "Triceps / Chest", "icon": "💎"},
            {"name": "L-Sit Tuck Hold", "sets": 3, "reps": "15s", "rest": "60s", "muscle": "Core / Hip Flexors",
             "icon": "🛡"},
        ],
        "tips": "For table rows: keep your body straight as a plank throughout the pull.",
        "weekly_goal": "4 sessions. Introduce pulling exercises with strict form.",
        "intensity": 6,
        "volume": 280,
    },
    7: {
        "title": "BATTLE TEMPO",
        "phase": "STRENGTH",
        "theme": "Sustained effort is the mark of a professional.",
        "description": "Higher rep endurance sets combined with strength work. Military fitness tests measure both max strength and sustained endurance. Train both in the same session to simulate operational demands.",
        "exercises": [
            {"name": "Push-Up Ladder (1-10)", "sets": 1, "reps": "55 total", "rest": "30s between rungs",
             "muscle": "Chest / Triceps / Endurance", "icon": "💪"},
            {"name": "Squat Holds", "sets": 4, "reps": "45s hold", "rest": "60s", "muscle": "Quads / Endurance",
             "icon": "🦵"},
            {"name": "Burpee Broad Jump", "sets": 4, "reps": "8", "rest": "90s", "muscle": "Full Body / Power",
             "icon": "🔥"},
            {"name": "Plank to Push-Up", "sets": 3, "reps": "10", "rest": "60s", "muscle": "Core / Shoulders",
             "icon": "🛡"},
            {"name": "Sprint Intervals", "sets": 6, "reps": "20s sprint / 40s walk", "rest": "0s",
             "muscle": "Cardio / Legs", "icon": "⚡"},
        ],
        "tips": "During sprint intervals, run at 90% — not all-out, not easy.",
        "weekly_goal": "4 sessions. Complete the push-up ladder without stopping.",
        "intensity": 7,
        "volume": 320,
    },
    8: {
        "title": "TACTICAL DELOAD II",
        "phase": "STRENGTH",
        "theme": "Reload your magazine. You will need it.",
        "description": "Second scheduled deload. Your nervous system has been under stress for 3 weeks. Smart operators don't run equipment without maintenance. This week is your maintenance window.",
        "exercises": [
            {"name": "Easy Push-Ups", "sets": 2, "reps": "15", "rest": "90s", "muscle": "Chest", "icon": "💪"},
            {"name": "Bodyweight Squats", "sets": 2, "reps": "20", "rest": "90s", "muscle": "Legs", "icon": "🦵"},
            {"name": "Long Plank", "sets": 2, "reps": "60s", "rest": "90s", "muscle": "Core", "icon": "🛡"},
            {"name": "Stretching / Foam Roll", "sets": 1, "reps": "15 min", "rest": "0s", "muscle": "Recovery",
             "icon": "🌿"},
        ],
        "tips": "Map out your training for weeks 9-12. Visualize your progress.",
        "weekly_goal": "2 easy sessions. Focus on mobility and sleep quality.",
        "intensity": 1,
        "volume": 90,
    },
    9: {
        "title": "ENDURANCE ENGINE",
        "phase": "ENDURANCE",
        "theme": "Phase 3: The long game. Where most fail.",
        "description": "Phase 3 is pure endurance. High volume, moderate intensity, minimal rest. The APFT (Army Physical Fitness Test) demands max push-ups and sit-ups in 2 minutes. Train that capacity now.",
        "exercises": [
            {"name": "Max Push-Ups (APFT style)", "sets": 3, "reps": "max in 2min", "rest": "2min",
             "muscle": "Full Upper Body Endurance", "icon": "💪"},
            {"name": "Sit-Ups (APFT style)", "sets": 3, "reps": "max in 2min", "rest": "2min",
             "muscle": "Core Endurance", "icon": "🛡"},
            {"name": "2-Mile Run Pace Work", "sets": 1, "reps": "20 min easy", "rest": "0s", "muscle": "Cardio / Legs",
             "icon": "⚡"},
            {"name": "Mountain Climbers", "sets": 4, "reps": "40", "rest": "45s", "muscle": "Core / Conditioning",
             "icon": "🔥"},
        ],
        "tips": "Track your push-up count from each max set. Aim to improve next week.",
        "weekly_goal": "3-4 sessions. Log your max push-up and sit-up scores.",
        "intensity": 7,
        "volume": 400,
    },
    10: {
        "title": "IRON MILE",
        "phase": "ENDURANCE",
        "theme": "The body does not know the difference between training and combat.",
        "description": "Run-focused week. Military fitness is measured significantly by running capacity. Whether it's a 2-mile APFT run or a 12-mile ruck, cardio is non-negotiable. Pair with calisthenics in circuits.",
        "exercises": [
            {"name": "Interval Run", "sets": 8, "reps": "400m fast / 400m walk", "rest": "0s",
             "muscle": "Cardio / Legs", "icon": "⚡"},
            {"name": "Push-Up Burnout", "sets": 4, "reps": "max", "rest": "90s", "muscle": "Chest / Triceps",
             "icon": "💪"},
            {"name": "Bodyweight Squat Circuit", "sets": 4, "reps": "25", "rest": "45s", "muscle": "Legs / Endurance",
             "icon": "🦵"},
            {"name": "Flutter Kicks", "sets": 4, "reps": "40", "rest": "45s", "muscle": "Core / Hip Flexors",
             "icon": "🛡"},
            {"name": "Bear Crawl", "sets": 4, "reps": "20m", "rest": "60s", "muscle": "Full Body / Coordination",
             "icon": "🔥"},
        ],
        "tips": "Bear crawls build tactical movement — keep hips low and move with purpose.",
        "weekly_goal": "4 sessions. Complete all 8 interval run sets.",
        "intensity": 8,
        "volume": 450,
    },
    11: {
        "title": "COMBAT CIRCUITS",
        "phase": "ENDURANCE",
        "theme": "No isolation. Every muscle fires every session.",
        "description": "Circuit training mimics the chaotic demands of actual operations. No isolation exercises — full body circuits where heart rate stays elevated throughout. Welcome to the pain cave.",
        "exercises": [
            {"name": "CIRCUIT: Push-Ups → Squats → Burpees → Sit-Ups → Sprint", "sets": 5, "reps": "15/15/10/15/30s",
             "rest": "60s between circuits", "muscle": "Full Body / Conditioning", "icon": "🔥"},
            {"name": "Pull-Ups (or Table Rows)", "sets": 4, "reps": "max", "rest": "90s", "muscle": "Back / Biceps",
             "icon": "🎯"},
            {"name": "Plank Circuit", "sets": 3, "reps": "Front 45s / Sides 30s each", "rest": "45s",
             "muscle": "Full Core", "icon": "🛡"},
        ],
        "tips": "During circuits, the only acceptable rest is between full rounds — not between exercises.",
        "weekly_goal": "4 sessions. Complete all 5 circuit rounds without extended breaks.",
        "intensity": 9,
        "volume": 500,
    },
    12: {
        "title": "DELOAD III — MIDPOINT",
        "phase": "ENDURANCE",
        "theme": "You are now 23% complete. The mission continues.",
        "description": "Quarter-point deload. This is where many programs fail trainees — no recovery built in. You have one. Use it wisely. Reassess your baseline metrics: push-up count, squat depth, plank time.",
        "exercises": [
            {"name": "Easy Jog", "sets": 1, "reps": "20 min easy", "rest": "0s", "muscle": "Cardio / Recovery",
             "icon": "⚡"},
            {"name": "Push-Ups (comfortable pace)", "sets": 3, "reps": "15", "rest": "90s", "muscle": "Chest",
             "icon": "💪"},
            {"name": "Deep Squat Hold", "sets": 3, "reps": "60s", "rest": "60s", "muscle": "Mobility / Legs",
             "icon": "🦵"},
            {"name": "Full Stretch Routine", "sets": 1, "reps": "20 min", "rest": "0s", "muscle": "Full Body Recovery",
             "icon": "🌿"},
        ],
        "tips": "Test your current max push-ups and sit-ups. Record baseline for comparison at week 52.",
        "weekly_goal": "2 light sessions. Write down your Week 12 fitness stats.",
        "intensity": 1,
        "volume": 80,
    },
}

# Generate weeks 13-52 programmatically with escalating difficulty
PHASES = {
    range(13, 17): ("POWER", "Explosive power development — plyometrics and strength combined."),
    range(17, 21): ("POWER", "Advanced power training — peak explosive output."),
    range(21, 25): ("ADVANCED STRENGTH", "Near-max strength cycles with complex movement patterns."),
    range(25, 29): ("ADVANCED STRENGTH", "Strength consolidation — own every movement."),
    range(29, 33): ("PEAK CONDITIONING", "High intensity — push your absolute limits."),
    range(33, 37): ("PEAK CONDITIONING", "Sustained peak — hold the summit."),
    range(37, 41): ("SPECIALIZATION", "Sport-specific military movements — rucking, obstacle prep."),
    range(41, 45): ("SPECIALIZATION", "Advanced specialization — mission-ready fitness."),
    range(45, 49): ("INTEGRATION", "Full integration — all qualities combined in complex sessions."),
    range(49, 53): ("ELITE GRADUATION", "Final phase — prove you are elite. Week 52 is your test."),
}

EXERCISE_POOLS = {
    "POWER": [
        {"name": "Clap Push-Ups", "muscle": "Explosive Chest", "icon": "💥"},
        {"name": "Box Jumps", "muscle": "Explosive Legs", "icon": "⚡"},
        {"name": "Plyometric Lunges", "muscle": "Power / Legs", "icon": "🦵"},
        {"name": "Medicine Ball Slams (bodyweight sub: slam burpees)", "muscle": "Full Body Power", "icon": "🔥"},
        {"name": "Broad Jumps", "muscle": "Horizontal Power", "icon": "🎯"},
    ],
    "ADVANCED STRENGTH": [
        {"name": "Archer Push-Ups", "muscle": "Chest / Stability", "icon": "🎯"},
        {"name": "Pistol Squats", "muscle": "Unilateral Legs", "icon": "💎"},
        {"name": "Dragon Flags (tuck)", "muscle": "Advanced Core", "icon": "🛡"},
        {"name": "Pike Push-Up → Handstand Hold", "muscle": "Shoulders / Balance", "icon": "⚡"},
        {"name": "Single-Leg Romanian Deadlift", "muscle": "Posterior Chain", "icon": "🦵"},
    ],
    "PEAK CONDITIONING": [
        {"name": "Burpee Pull-Ups", "muscle": "Full Body", "icon": "🔥"},
        {"name": "Tabata Sprints (20s on/10s off x8)", "muscle": "Cardio / Power", "icon": "⚡"},
        {"name": "Devil Press (bodyweight: squat thrust + push-up)", "muscle": "Full Body", "icon": "💥"},
        {"name": "Renegade Rows (floor)", "muscle": "Back / Core", "icon": "🎯"},
        {"name": "V-Ups", "muscle": "Full Core", "icon": "🛡"},
    ],
    "SPECIALIZATION": [
        {"name": "Weighted Ruck March (15kg+ backpack)", "muscle": "Legs / Endurance", "icon": "🎖"},
        {"name": "Rope Climb Simulation (towel over bar)", "muscle": "Back / Grip / Biceps", "icon": "🔥"},
        {"name": "Tire Flip Simulation (heavy bag)", "muscle": "Full Body / Power", "icon": "💥"},
        {"name": "Obstacle Crawl (low crawl 20m)", "muscle": "Full Body / Coordination", "icon": "🎯"},
        {"name": "Combat Swim Prep (dry land strokes)", "muscle": "Shoulders / Core", "icon": "⚡"},
    ],
    "INTEGRATION": [
        {"name": "Full APFT Mock Test", "muscle": "Max Push-Ups / Sit-Ups / 2-Mile Run", "icon": "🏅"},
        {"name": "Complex Circuit (6 exercises, 6 rounds)", "muscle": "Full Body", "icon": "🔥"},
        {"name": "Endurance Push-Up Protocol", "muscle": "Chest / Triceps / Endurance", "icon": "💪"},
        {"name": "Tactical Movement Course", "muscle": "Agility / Full Body", "icon": "🎖"},
        {"name": "Max Effort Plank (beat your record)", "muscle": "Core", "icon": "🛡"},
    ],
    "ELITE GRADUATION": [
        {"name": "Special Forces Selection Simulation Circuit", "muscle": "Full Body / Mental", "icon": "⭐"},
        {"name": "Max Push-Ups (5-min test)", "muscle": "Chest / Endurance", "icon": "💪"},
        {"name": "100 Burpee Challenge", "muscle": "Full Body", "icon": "🔥"},
        {"name": "4-Mile Run Under 32 Minutes", "muscle": "Cardio / Endurance", "icon": "⚡"},
        {"name": "Cold Water Recovery", "muscle": "Recovery / Mental", "icon": "🌊"},
    ],
}

for week_num in range(13, 53):
    if week_num in PROGRAM:
        continue

    phase = "POWER"
    phase_desc = "Power development phase."
    for r, (ph, desc) in PHASES.items():
        if week_num in r:
            phase = ph
            phase_desc = desc
            break

    is_deload = (week_num % 4 == 0)
    intensity = min(10, 3 + (week_num // 5))
    volume = min(600, 100 + week_num * 8)

    exercises = EXERCISE_POOLS.get(phase, EXERCISE_POOLS["PEAK CONDITIONING"])

    if is_deload:
        week_exercises = [
            {"name": "Light Push-Ups", "sets": 2, "reps": "15", "rest": "90s", "muscle": "Chest", "icon": "💪"},
            {"name": "Easy Squats", "sets": 2, "reps": "20", "rest": "90s", "muscle": "Legs", "icon": "🦵"},
            {"name": "Plank", "sets": 2, "reps": "60s", "rest": "90s", "muscle": "Core", "icon": "🛡"},
            {"name": "Recovery Walk/Jog", "sets": 1, "reps": "20 min", "rest": "0s", "muscle": "Cardio Recovery",
             "icon": "🌿"},
        ]
        PROGRAM[week_num] = {
            "title": f"DELOAD — WEEK {week_num}",
            "phase": phase,
            "theme": "Recovery is part of the mission.",
            "description": f"Scheduled deload week. {phase_desc} Volume reduced by 40%. Let adaptations solidify.",
            "exercises": week_exercises,
            "tips": "Prioritize sleep, nutrition, and hydration this week.",
            "weekly_goal": "2 light sessions only.",
            "intensity": 1,
            "volume": 80,
        }
    else:
        sets_count = min(5, 3 + week_num // 10)
        reps_base = max(8, 20 - week_num // 8)
        week_exercises = [
            {
                "name": ex["name"],
                "sets": sets_count,
                "reps": f"{reps_base + i * 2}" if i < 3 else f"max",
                "rest": f"{60 + i * 15}s",
                "muscle": ex["muscle"],
                "icon": ex["icon"]
            }
            for i, ex in enumerate(exercises)
        ]
        PROGRAM[week_num] = {
            "title": f"WEEK {week_num} PROTOCOL",
            "phase": phase,
            "theme": phase_desc,
            "description": f"Week {week_num} of {phase} phase. {phase_desc} The mission demands more every week — meet the demand.",
            "exercises": week_exercises,
            "tips": f"Week {week_num}: push harder than last week. Progress is mandatory.",
            "weekly_goal": f"{'4-5' if week_num > 30 else '4'} sessions. No missed days.",
            "intensity": intensity,
            "volume": volume,
        }

# Override week 52 — Final graduation test
PROGRAM[52] = {
    "title": "ELITE GRADUATION",
    "phase": "ELITE GRADUATION",
    "theme": "52 weeks. No excuses. This is your final test.",
    "description": "Week 52 is your graduation. You have trained for an entire year. Today you prove it. Complete the Full Military Fitness Test: max push-ups in 2 minutes, max sit-ups in 2 minutes, 2-mile run, and the 100 burpee challenge. Compare against your Week 1 baseline and Week 12 midpoint scores. You are now elite.",
    "exercises": [
        {"name": "APFT Push-Up Max (2 min)", "sets": 1, "reps": "MAX in 2 min", "rest": "5 min",
         "muscle": "Full Upper Body — Graduation Test", "icon": "⭐"},
        {"name": "APFT Sit-Up Max (2 min)", "sets": 1, "reps": "MAX in 2 min", "rest": "5 min",
         "muscle": "Core Endurance — Graduation Test", "icon": "🏅"},
        {"name": "2-Mile Run (Best Time)", "sets": 1, "reps": "RACE PACE", "rest": "10 min",
         "muscle": "Cardio — Graduation Test", "icon": "⚡"},
        {"name": "100 Burpee Challenge", "sets": 1, "reps": "100 total", "rest": "Rest as needed",
         "muscle": "Full Body Endurance — Elite Test", "icon": "🔥"},
        {"name": "Victory Reflection & Rest", "sets": 1, "reps": "Well earned", "rest": "Infinite",
         "muscle": "Mind & Body — Mission Complete", "icon": "🎖"},
    ],
    "tips": "Record every score. You will be shocked by how far you have come from Week 1. This is the proof of your discipline.",
    "weekly_goal": "Complete the full graduation test. Then rest. You have earned it.",
    "intensity": 10,
    "volume": 600,
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/week/<int:week>')
def get_week(week):
    if week < 1 or week > 52:
        return jsonify({"error": "Week must be between 1 and 52"}), 400
    data = PROGRAM.get(week, {})
    data["week"] = week
    return jsonify(data)


@app.route('/api/program/overview')
def get_overview():
    overview = []
    for w in range(1, 53):
        d = PROGRAM.get(w, {})
        overview.append({
            "week": w,
            "title": d.get("title", f"WEEK {w}"),
            "phase": d.get("phase", "TRAINING"),
            "intensity": d.get("intensity", 5),
            "volume": d.get("volume", 200),
        })
    return jsonify(overview)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

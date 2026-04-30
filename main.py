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
            {
                "name": "Push-Ups", "sets": 3, "reps": "10", "rest": "60s",
                "muscle": "Chest / Triceps / Shoulders", "icon": "💪",
                "instructions": [
                    "Hands shoulder-width apart, wrists directly under shoulders",
                    "Keep body in a rigid straight line — squeeze glutes and core throughout",
                    "Lower chest to 2–3 cm from floor, elbows at ~45° from torso",
                    "Exhale and press back up to full arm extension",
                    "Do not flare elbows out wide or let hips sag"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"
            },
            {
                "name": "Bodyweight Squats", "sets": 3, "reps": "15", "rest": "60s",
                "muscle": "Quads / Glutes / Hamstrings", "icon": "🦵",
                "instructions": [
                    "Stand feet shoulder-width apart, toes slightly turned out",
                    "Brace core and keep chest tall — do not round forward",
                    "Push hips back first, then bend knees down to parallel",
                    "Keep knees tracking over toes — don't let them cave inward",
                    "Drive through heels to stand; squeeze glutes at the top"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+proper+form+tutorial"
            },
            {
                "name": "Plank Hold", "sets": 3, "reps": "20s", "rest": "45s",
                "muscle": "Core / Shoulders", "icon": "🛡",
                "instructions": [
                    "Forearms flat on floor, elbows directly under shoulders",
                    "Body forms a straight line from head to heels",
                    "Squeeze glutes and quads; lightly draw belly button in",
                    "Breathe steadily — never hold your breath during the hold",
                    "If hips drop or raise, stop and reset rather than compensating"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+hold+proper+form+tutorial"
            },
            {
                "name": "Jumping Jacks", "sets": 3, "reps": "30", "rest": "45s",
                "muscle": "Full Body / Cardio", "icon": "⚡",
                "instructions": [
                    "Start with feet together and arms at your sides",
                    "Jump feet out past shoulder-width; raise arms overhead simultaneously",
                    "Land softly on the balls of your feet with a slight knee bend",
                    "Jump back to starting position and repeat at a steady rhythm",
                    "Keep core lightly braced throughout to protect the lower back"
                ],
                "video_url": "https://www.youtube.com/results?search_query=jumping+jacks+proper+form"
            },
            {
                "name": "Glute Bridges", "sets": 3, "reps": "12", "rest": "45s",
                "muscle": "Glutes / Lower Back", "icon": "🔥",
                "instructions": [
                    "Lie on your back, knees bent ~90°, feet flat on floor hip-width apart",
                    "Arms flat by your sides for stability",
                    "Drive hips upward by squeezing glutes — not by arching the lower back",
                    "Hold the peak contraction for 1 second at the top",
                    "Lower slowly and with control — don't let hips drop with a thud"
                ],
                "video_url": "https://www.youtube.com/results?search_query=glute+bridge+proper+form+tutorial"
            },
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
            {
                "name": "Push-Ups", "sets": 3, "reps": "15", "rest": "60s",
                "muscle": "Chest / Triceps", "icon": "💪",
                "instructions": [
                    "Hands shoulder-width apart, wrists directly under shoulders",
                    "Keep body in a rigid straight line — squeeze glutes and core throughout",
                    "Lower chest to 2–3 cm from floor, elbows at ~45° from torso",
                    "Exhale and press back up to full arm extension",
                    "Do not flare elbows out wide or let hips sag"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"
            },
            {
                "name": "Bodyweight Squats", "sets": 3, "reps": "20", "rest": "60s",
                "muscle": "Quads / Glutes", "icon": "🦵",
                "instructions": [
                    "Stand feet shoulder-width apart, toes slightly turned out",
                    "Brace core and keep chest tall — do not round forward",
                    "Push hips back first, then bend knees down to parallel",
                    "Keep knees tracking over toes — don't let them cave inward",
                    "Drive through heels to stand; squeeze glutes at the top"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+proper+form+tutorial"
            },
            {
                "name": "Plank Hold", "sets": 3, "reps": "30s", "rest": "45s",
                "muscle": "Core", "icon": "🛡",
                "instructions": [
                    "Forearms flat on floor, elbows directly under shoulders",
                    "Body forms a straight line from head to heels",
                    "Squeeze glutes and quads; lightly draw belly button in",
                    "Breathe steadily — never hold your breath during the hold",
                    "If hips drop or raise, stop and reset rather than compensating"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+hold+proper+form+tutorial"
            },
            {
                "name": "Mountain Climbers", "sets": 3, "reps": "20", "rest": "45s",
                "muscle": "Core / Cardio", "icon": "⚡",
                "instructions": [
                    "Start in a high push-up position, wrists under shoulders",
                    "Drive one knee toward your chest, keeping hips level",
                    "Switch legs in a running motion — don't let hips bounce up",
                    "Keep core tight so your lower back doesn't sag",
                    "Move at a controlled pace before increasing speed"
                ],
                "video_url": "https://www.youtube.com/results?search_query=mountain+climbers+proper+form+tutorial"
            },
            {
                "name": "Reverse Lunges", "sets": 3, "reps": "10 each", "rest": "60s",
                "muscle": "Quads / Glutes / Balance", "icon": "🔥",
                "instructions": [
                    "Stand tall, feet hip-width apart, hands on hips",
                    "Step one foot straight back, landing on the ball of that foot",
                    "Lower the back knee toward the floor — stop 2 cm above it",
                    "Front shin stays vertical; front knee does not push past toes",
                    "Drive through the front heel to return to standing"
                ],
                "video_url": "https://www.youtube.com/results?search_query=reverse+lunge+proper+form+tutorial"
            },
            {
                "name": "Superman Hold", "sets": 3, "reps": "15s", "rest": "30s",
                "muscle": "Lower Back / Glutes", "icon": "🌟",
                "instructions": [
                    "Lie face down on the floor, arms extended overhead",
                    "Simultaneously lift arms, chest, and legs off the floor",
                    "Squeeze glutes and keep your neck neutral — don't crane it up",
                    "Hold the raised position for the full rep duration",
                    "Lower slowly — don't drop flat between reps"
                ],
                "video_url": "https://www.youtube.com/results?search_query=superman+hold+exercise+form"
            },
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
            {
                "name": "Diamond Push-Ups", "sets": 3, "reps": "10", "rest": "60s",
                "muscle": "Triceps / Inner Chest", "icon": "💎",
                "instructions": [
                    "Form a diamond shape with thumbs and index fingers on the floor",
                    "Position hands below your sternum, not your chin",
                    "Keep elbows tracking back along your torso — not flaring out",
                    "Lower chest to your hands while keeping body rigid",
                    "Press back up fully — feel the triceps at the top of the rep"
                ],
                "video_url": "https://www.youtube.com/results?search_query=diamond+push+up+proper+form+tutorial"
            },
            {
                "name": "Jump Squats", "sets": 3, "reps": "15", "rest": "60s",
                "muscle": "Explosive Legs / Power", "icon": "⚡",
                "instructions": [
                    "Squat to parallel depth with chest up and core braced",
                    "Explosively drive through the heels and jump as high as possible",
                    "Swing arms upward to generate extra height",
                    "Land softly on the balls of your feet with bent knees — absorb the impact",
                    "Go straight into the next rep without pausing at the bottom"
                ],
                "video_url": "https://www.youtube.com/results?search_query=jump+squat+proper+form+tutorial"
            },
            {
                "name": "Side Plank", "sets": 3, "reps": "20s each", "rest": "45s",
                "muscle": "Obliques / Core", "icon": "🛡",
                "instructions": [
                    "Lie on your side, forearm on floor with elbow under shoulder",
                    "Stack feet on top of each other or stagger for stability",
                    "Lift hips off the floor — body forms a straight diagonal line",
                    "Keep hips from sagging toward the floor during the hold",
                    "Complete full duration on one side before switching"
                ],
                "video_url": "https://www.youtube.com/results?search_query=side+plank+proper+form+tutorial"
            },
            {
                "name": "Burpees", "sets": 3, "reps": "8", "rest": "90s",
                "muscle": "Full Body / Conditioning", "icon": "🔥",
                "instructions": [
                    "Stand tall, then drop hands to floor and jump feet back to push-up position",
                    "Perform one full push-up (chest touches floor)",
                    "Jump feet forward to hands in a squat position",
                    "Explosively jump upward with arms overhead at the top",
                    "Land softly and flow immediately into the next rep"
                ],
                "video_url": "https://www.youtube.com/results?search_query=burpee+proper+form+tutorial"
            },
            {
                "name": "Walking Lunges", "sets": 3, "reps": "20 steps", "rest": "60s",
                "muscle": "Legs / Stability", "icon": "🦵",
                "instructions": [
                    "Stand tall with core engaged and hands on hips or at sides",
                    "Step forward with one leg, lowering the back knee toward the floor",
                    "Front shin stays vertical; front knee stays over the ankle",
                    "Push off the back foot and bring it forward for the next step",
                    "Keep your torso upright — don't lean forward as you fatigue"
                ],
                "video_url": "https://www.youtube.com/results?search_query=walking+lunges+proper+form+tutorial"
            },
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
            {
                "name": "Push-Ups", "sets": 2, "reps": "12", "rest": "90s",
                "muscle": "Chest / Triceps", "icon": "💪",
                "instructions": [
                    "Hands shoulder-width apart, wrists directly under shoulders",
                    "Keep body in a rigid straight line — squeeze glutes and core",
                    "Lower chest slowly — use this deload week to perfect your form",
                    "Exhale and press back up to full arm extension",
                    "This week focus on quality, not quantity"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"
            },
            {
                "name": "Bodyweight Squats", "sets": 2, "reps": "15", "rest": "90s",
                "muscle": "Quads / Glutes", "icon": "🦵",
                "instructions": [
                    "Stand feet shoulder-width apart, toes slightly turned out",
                    "Use this deload week to drill perfect depth and knee tracking",
                    "Pause 1 second at the bottom to reinforce the position",
                    "Drive through heels to stand; squeeze glutes at the top",
                    "Move at a slow, controlled tempo throughout"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+proper+form+tutorial"
            },
            {
                "name": "Plank Hold", "sets": 2, "reps": "45s", "rest": "60s",
                "muscle": "Core", "icon": "🛡",
                "instructions": [
                    "Forearms flat on floor, elbows directly under shoulders",
                    "Body forms a straight line from head to heels",
                    "Squeeze glutes and quads; lightly draw belly button in",
                    "Breathe steadily and focus on quality of tension, not the clock",
                    "Deload week — ease up if you feel any lower back discomfort"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+hold+proper+form+tutorial"
            },
            {
                "name": "Yoga Flow / Mobility", "sets": 1, "reps": "10 min", "rest": "0s",
                "muscle": "Full Body / Recovery", "icon": "🌿",
                "instructions": [
                    "Move through cat-cow, downward dog, and child's pose slowly",
                    "Hold each position 5–10 slow breaths — don't rush",
                    "Focus on areas of tightness from the past 3 weeks",
                    "This is restorative — not a workout. Move gently.",
                    "Finish with 2 min of slow diaphragmatic breathing lying flat"
                ],
                "video_url": "https://www.youtube.com/results?search_query=yoga+mobility+flow+for+athletes+beginners"
            },
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
            {
                "name": "Wide Push-Ups", "sets": 4, "reps": "12", "rest": "75s",
                "muscle": "Outer Chest / Shoulders", "icon": "💪",
                "instructions": [
                    "Place hands 1.5x shoulder-width apart, fingers angled slightly out",
                    "Keep body rigid — no sagging hips or raised butt",
                    "Lower chest between hands, elbows flare ~60° from torso",
                    "Press back up through the outer chest — feel the stretch at the bottom",
                    "Wide grip shifts load to outer pec — control the descent"
                ],
                "video_url": "https://www.youtube.com/results?search_query=wide+push+up+proper+form"
            },
            {
                "name": "Pistol Squat Assist", "sets": 4, "reps": "6 each", "rest": "90s",
                "muscle": "Quads / Balance", "icon": "🎯",
                "instructions": [
                    "Hold a door frame or pole lightly with one hand for balance",
                    "Extend one leg forward, keeping it off the floor throughout",
                    "Squat down on the standing leg as low as comfortable",
                    "Keep standing heel flat on the floor — don't rise onto toes",
                    "Drive through the heel to stand; use as little arm assist as possible"
                ],
                "video_url": "https://www.youtube.com/results?search_query=pistol+squat+assisted+tutorial+for+beginners"
            },
            {
                "name": "Pike Push-Ups", "sets": 4, "reps": "10", "rest": "75s",
                "muscle": "Shoulders / Triceps", "icon": "⚡",
                "instructions": [
                    "Start in a downward dog position — hips high, body forming a V",
                    "Hands slightly wider than shoulder-width, fingers spread",
                    "Bend elbows to lower the top of your head toward the floor",
                    "Keep hips raised throughout — don't let them drop as you lower",
                    "Press back up until arms are fully extended at the top"
                ],
                "video_url": "https://www.youtube.com/results?search_query=pike+push+up+proper+form+tutorial"
            },
            {
                "name": "Bulgarian Split Squat", "sets": 4, "reps": "8 each", "rest": "90s",
                "muscle": "Quads / Glutes / Balance", "icon": "🦵",
                "instructions": [
                    "Rear foot elevated on a chair or bench behind you",
                    "Front foot far enough forward that your shin stays vertical at the bottom",
                    "Lower the back knee toward the floor with control",
                    "Keep torso upright — resist the urge to lean forward",
                    "Drive through the front heel to return to standing"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bulgarian+split+squat+proper+form+tutorial"
            },
            {
                "name": "Hollow Body Hold", "sets": 3, "reps": "30s", "rest": "60s",
                "muscle": "Core / Hip Flexors", "icon": "🛡",
                "instructions": [
                    "Lie on your back, press lower back firmly into the floor",
                    "Raise legs to ~45° and extend arms overhead close to ears",
                    "Lift shoulders slightly off the floor — hold the 'banana' shape",
                    "Lower back must stay flat — if it arches, raise legs higher",
                    "Breathe steadily; do not hold your breath during the hold"
                ],
                "video_url": "https://www.youtube.com/results?search_query=hollow+body+hold+proper+form+tutorial"
            },
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
            {
                "name": "Decline Push-Ups", "sets": 4, "reps": "12", "rest": "75s",
                "muscle": "Upper Chest / Shoulders", "icon": "💪",
                "instructions": [
                    "Place feet on a chair or bench, hands on the floor shoulder-width",
                    "Body forms a straight downward-angled line from feet to hands",
                    "Lower chest toward the floor, elbows at ~45°",
                    "The incline shifts emphasis to upper chest and front delts",
                    "Press back up fully — don't let hips pike upward during the set"
                ],
                "video_url": "https://www.youtube.com/results?search_query=decline+push+up+proper+form+tutorial"
            },
            {
                "name": "Table/Bar Rows", "sets": 4, "reps": "12", "rest": "75s",
                "muscle": "Back / Biceps", "icon": "🎯",
                "instructions": [
                    "Lie under a sturdy table; grip the edge with both hands",
                    "Keep body straight from head to heels — like a reverse plank",
                    "Pull chest up to the table by driving elbows back and down",
                    "Squeeze shoulder blades together at the top of each rep",
                    "Lower slowly — don't drop to the start position"
                ],
                "video_url": "https://www.youtube.com/results?search_query=inverted+row+table+row+proper+form+tutorial"
            },
            {
                "name": "Jump Squats", "sets": 4, "reps": "12", "rest": "60s",
                "muscle": "Explosive Power", "icon": "⚡",
                "instructions": [
                    "Squat to parallel depth with chest up and core braced",
                    "Explosively drive through the heels and jump as high as possible",
                    "Swing arms upward to generate extra height",
                    "Land softly on the balls of your feet with bent knees",
                    "Absorb the landing and go straight into the next rep"
                ],
                "video_url": "https://www.youtube.com/results?search_query=jump+squat+proper+form+tutorial"
            },
            {
                "name": "Dips (Chair)", "sets": 4, "reps": "10", "rest": "75s",
                "muscle": "Triceps / Chest", "icon": "💎",
                "instructions": [
                    "Place hands on a sturdy chair behind you, fingers forward",
                    "Extend legs out in front — the further out, the harder it is",
                    "Lower your body by bending elbows to ~90° — no further",
                    "Keep elbows tracking back, not flaring out to the sides",
                    "Press back up through the triceps to full arm extension"
                ],
                "video_url": "https://www.youtube.com/results?search_query=chair+dips+proper+form+tutorial"
            },
            {
                "name": "L-Sit Tuck Hold", "sets": 3, "reps": "15s", "rest": "60s",
                "muscle": "Core / Hip Flexors", "icon": "🛡",
                "instructions": [
                    "Sit on the floor with hands flat beside hips, fingers forward",
                    "Press into the floor and lift your hips and tucked knees up",
                    "Hold the tuck position — thighs close to chest",
                    "Keep arms straight; don't let elbows bend during the hold",
                    "If full lift is too hard, start by just pressing hips up slightly"
                ],
                "video_url": "https://www.youtube.com/results?search_query=l-sit+tuck+hold+tutorial+for+beginners"
            },
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
            {
                "name": "Push-Up Ladder (1-10)", "sets": 1, "reps": "55 total", "rest": "30s between rungs",
                "muscle": "Chest / Triceps / Endurance", "icon": "💪",
                "instructions": [
                    "Do 1 push-up, rest 30s. Then 2 push-ups, rest 30s. Continue to 10.",
                    "Maintain full form on every single rep — no sloppy ones as you fatigue",
                    "Take the 30s rest between each rung seriously — it's programmed",
                    "If you fail a rung, rest and complete remaining reps before moving on",
                    "Total = 55 reps. Track completion time to measure progress"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+ladder+workout+tutorial"
            },
            {
                "name": "Squat Holds", "sets": 4, "reps": "45s hold", "rest": "60s",
                "muscle": "Quads / Endurance", "icon": "🦵",
                "instructions": [
                    "Lower into a parallel squat and hold — thighs parallel to floor",
                    "Keep chest tall and core engaged throughout the hold",
                    "Distribute weight evenly — do not rise onto toes",
                    "If quads burn intensely, raise slightly above parallel and continue",
                    "This trains muscular endurance in the same range as your squats"
                ],
                "video_url": "https://www.youtube.com/results?search_query=squat+hold+isometric+exercise+form"
            },
            {
                "name": "Burpee Broad Jump", "sets": 4, "reps": "8", "rest": "90s",
                "muscle": "Full Body / Power", "icon": "🔥",
                "instructions": [
                    "Perform a standard burpee: drop, push-up, stand",
                    "Instead of jumping straight up, launch forward as far as possible",
                    "Swing arms aggressively to maximize horizontal distance",
                    "Land with soft knees and immediately hinge into the next burpee",
                    "Measure distance across a room to track improvement over weeks"
                ],
                "video_url": "https://www.youtube.com/results?search_query=burpee+broad+jump+tutorial"
            },
            {
                "name": "Plank to Push-Up", "sets": 3, "reps": "10", "rest": "60s",
                "muscle": "Core / Shoulders", "icon": "🛡",
                "instructions": [
                    "Start in forearm plank position, core braced",
                    "Press up onto one hand, then the other — reach high plank",
                    "Lower back down one arm at a time to forearm plank",
                    "Alternate which arm leads each rep to balance the load",
                    "Keep hips level throughout — minimize rotation side to side"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+to+push+up+proper+form+tutorial"
            },
            {
                "name": "Sprint Intervals", "sets": 6, "reps": "20s sprint / 40s walk", "rest": "0s",
                "muscle": "Cardio / Legs", "icon": "⚡",
                "instructions": [
                    "Sprint at 90% effort for 20 seconds — not all-out, not easy",
                    "Immediately transition to a walk for 40 seconds of active recovery",
                    "Maintain good sprint mechanics: lean forward, drive knees up",
                    "Pump arms aggressively — arms drive legs in sprinting",
                    "Complete all 6 intervals without extended rest between sets"
                ],
                "video_url": "https://www.youtube.com/results?search_query=sprint+interval+training+proper+form+technique"
            },
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
            {
                "name": "Easy Push-Ups", "sets": 2, "reps": "15", "rest": "90s",
                "muscle": "Chest", "icon": "💪",
                "instructions": [
                    "Standard push-up position — use this week to groove perfect form",
                    "Move at a slow, deliberate tempo: 3 seconds down, 1 up",
                    "Focus on mind-muscle connection to the chest and triceps",
                    "Stop 2–3 reps before failure — this is recovery, not max effort",
                    "Use the quality reps to reinforce movement patterns"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"
            },
            {
                "name": "Bodyweight Squats", "sets": 2, "reps": "20", "rest": "90s",
                "muscle": "Legs", "icon": "🦵",
                "instructions": [
                    "Slow, controlled tempo — treat these as movement practice",
                    "Pause 2 seconds at the bottom to drill the position",
                    "Focus on keeping knees tracking correctly over toes",
                    "Drive through heels to stand; squeeze glutes at the top",
                    "This is active recovery — leave energy in the tank"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+proper+form+tutorial"
            },
            {
                "name": "Long Plank", "sets": 2, "reps": "60s", "rest": "90s",
                "muscle": "Core", "icon": "🛡",
                "instructions": [
                    "Forearms flat on floor, elbows directly under shoulders",
                    "Body forms a straight line from head to heels",
                    "Breathe steadily in a 4-count rhythm throughout the hold",
                    "Focus on quality of bracing — not just surviving the time",
                    "If form degrades, stop and reset rather than collapsing through it"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+hold+proper+form+tutorial"
            },
            {
                "name": "Stretching / Foam Roll", "sets": 1, "reps": "15 min", "rest": "0s",
                "muscle": "Recovery", "icon": "🌿",
                "instructions": [
                    "Foam roll quads, IT band, upper back, and calves — 60s per area",
                    "Hold static stretches for 45–60 seconds each — not bouncing",
                    "Target hip flexors, hamstrings, chest, and thoracic spine",
                    "Breathe slowly through discomfort — don't hold breath",
                    "This session is as important as any strength session"
                ],
                "video_url": "https://www.youtube.com/results?search_query=foam+rolling+full+body+stretching+recovery+routine"
            },
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
            {
                "name": "Max Push-Ups (APFT style)", "sets": 3, "reps": "max in 2min", "rest": "2min",
                "muscle": "Full Upper Body Endurance", "icon": "💪",
                "instructions": [
                    "APFT standard: lower chest to 2–3cm from floor, full arm extension at top",
                    "Maintain a steady pace — don't go all-out in the first 20 seconds",
                    "Keep hips level; resting in the up position is permitted",
                    "Count every rep — your score is how many full reps in 2 minutes",
                    "Log your score after each set to track progress week to week"
                ],
                "video_url": "https://www.youtube.com/results?search_query=APFT+push+up+standard+military+fitness+test"
            },
            {
                "name": "Sit-Ups (APFT style)", "sets": 3, "reps": "max in 2min", "rest": "2min",
                "muscle": "Core Endurance", "icon": "🛡",
                "instructions": [
                    "Lie on back, knees bent ~45°, feet held or anchored",
                    "Fingers interlaced behind your head — don't pull on your neck",
                    "Rise until elbows touch or pass your knees",
                    "Lower so shoulder blades touch the floor before the next rep",
                    "Pace yourself — the goal is maximum reps in 2 minutes, not burnout in 30s"
                ],
                "video_url": "https://www.youtube.com/results?search_query=APFT+sit+up+standard+army+fitness+test+form"
            },
            {
                "name": "2-Mile Run Pace Work", "sets": 1, "reps": "20 min easy", "rest": "0s",
                "muscle": "Cardio / Legs", "icon": "⚡",
                "instructions": [
                    "Run at a conversational pace — you should be able to speak sentences",
                    "Focus on efficient form: slight forward lean, relaxed arms",
                    "Land midfoot, not on your heel — reduce impact and injury risk",
                    "Breathe in a 2-count/2-count rhythm to regulate effort",
                    "This is aerobic base building — not a race"
                ],
                "video_url": "https://www.youtube.com/results?search_query=2+mile+run+pace+training+tips+army+fitness"
            },
            {
                "name": "Mountain Climbers", "sets": 4, "reps": "40", "rest": "45s",
                "muscle": "Core / Conditioning", "icon": "🔥",
                "instructions": [
                    "Start in a high push-up position, wrists under shoulders",
                    "Drive one knee toward your chest, keeping hips level",
                    "Switch legs in a running motion — don't let hips bounce up",
                    "Keep core tight so your lower back doesn't sag",
                    "Count each knee drive as one rep — 40 total alternating"
                ],
                "video_url": "https://www.youtube.com/results?search_query=mountain+climbers+proper+form+tutorial"
            },
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
            {
                "name": "Interval Run", "sets": 8, "reps": "400m fast / 400m walk", "rest": "0s",
                "muscle": "Cardio / Legs", "icon": "⚡",
                "instructions": [
                    "Run 400m (one lap) at ~85% effort — hard but controlled",
                    "Walk 400m as active recovery — don't stop completely",
                    "Maintain consistent pace on each fast interval — don't fade",
                    "Focus on running form: tall posture, relaxed shoulders, midfoot strike",
                    "Complete all 8 intervals — use the walk to prepare for the next run"
                ],
                "video_url": "https://www.youtube.com/results?search_query=400m+interval+run+training+tutorial"
            },
            {
                "name": "Push-Up Burnout", "sets": 4, "reps": "max", "rest": "90s",
                "muscle": "Chest / Triceps", "icon": "💪",
                "instructions": [
                    "Lower into push-up position and begin at a moderate pace",
                    "Continue until form breaks down — do not rep out with bad form",
                    "Rest in the up position briefly if needed, but don't drop to knees",
                    "Log your rep count for each set to track endurance progress",
                    "Each set will be fewer reps — that's normal and expected"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+burnout+max+reps+tutorial"
            },
            {
                "name": "Bodyweight Squat Circuit", "sets": 4, "reps": "25", "rest": "45s",
                "muscle": "Legs / Endurance", "icon": "🦵",
                "instructions": [
                    "Move at a controlled but continuous pace — no pausing between reps",
                    "Maintain full depth on every rep — parallel or below",
                    "Keep chest up and core braced throughout the set",
                    "As you fatigue, focus on breathing rhythm to maintain pace",
                    "25 reps is the minimum — push for more if form holds"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+circuit+high+rep+tutorial"
            },
            {
                "name": "Flutter Kicks", "sets": 4, "reps": "40", "rest": "45s",
                "muscle": "Core / Hip Flexors", "icon": "🛡",
                "instructions": [
                    "Lie on back, hands under your glutes for lower back support",
                    "Raise both legs to ~6 inches off the floor",
                    "Alternate small up-down kicks from the hips — legs nearly straight",
                    "Press lower back into the floor — do not arch away from it",
                    "Count each kick as one rep (left + right = 2 reps)"
                ],
                "video_url": "https://www.youtube.com/results?search_query=flutter+kicks+proper+form+core+exercise"
            },
            {
                "name": "Bear Crawl", "sets": 4, "reps": "20m", "rest": "60s",
                "muscle": "Full Body / Coordination", "icon": "🔥",
                "instructions": [
                    "Start on hands and knees, then lift knees 2–3 cm off the floor",
                    "Move opposite hand and foot simultaneously — right hand, left foot",
                    "Keep hips low — level with or slightly above shoulder height",
                    "Move with purpose and control, not speed",
                    "Keep your gaze slightly ahead — not straight down"
                ],
                "video_url": "https://www.youtube.com/results?search_query=bear+crawl+proper+form+tutorial"
            },
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
            {
                "name": "CIRCUIT: Push-Ups → Squats → Burpees → Sit-Ups → Sprint",
                "sets": 5, "reps": "15/15/10/15/30s",
                "rest": "60s between circuits", "muscle": "Full Body / Conditioning", "icon": "🔥",
                "instructions": [
                    "Complete all 5 exercises back-to-back with NO rest between them",
                    "Push-Ups x15 → Squats x15 → Burpees x10 → Sit-Ups x15 → Sprint 30s",
                    "Rest exactly 60 seconds after the sprint before the next circuit",
                    "Maintain form on every movement — fatigue is not an excuse for bad reps",
                    "Pace the sprint at 80–85% so you can sustain all 5 circuits"
                ],
                "video_url": "https://www.youtube.com/results?search_query=military+circuit+training+full+body+workout"
            },
            {
                "name": "Pull-Ups (or Table Rows)", "sets": 4, "reps": "max", "rest": "90s",
                "muscle": "Back / Biceps", "icon": "🎯",
                "instructions": [
                    "Pull-up: hang from bar with overhand grip, shoulder-width apart",
                    "Pull until chin clears the bar — full range of motion on every rep",
                    "Lower slowly — the descent builds as much strength as the pull",
                    "No kipping or swinging — strict form only",
                    "No bar? Use the table row substitute: body straight, pull chest to table edge"
                ],
                "video_url": "https://www.youtube.com/results?search_query=pull+up+proper+form+tutorial+strict"
            },
            {
                "name": "Plank Circuit", "sets": 3, "reps": "Front 45s / Sides 30s each", "rest": "45s",
                "muscle": "Full Core", "icon": "🛡",
                "instructions": [
                    "Front plank 45s → right side plank 30s → left side plank 30s = 1 circuit",
                    "Transition between positions with no rest between plank variations",
                    "Keep hips level in all three positions — no sagging or piking",
                    "Breathe steadily throughout — 4 counts in, 4 counts out",
                    "Rest 45s after completing all three positions before the next circuit"
                ],
                "video_url": "https://www.youtube.com/results?search_query=plank+circuit+front+side+plank+form+tutorial"
            },
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
            {
                "name": "Easy Jog", "sets": 1, "reps": "20 min easy", "rest": "0s",
                "muscle": "Cardio / Recovery", "icon": "⚡",
                "instructions": [
                    "Run at a pace where you could hold a full conversation easily",
                    "Focus on running form: slight forward lean, relaxed jaw and hands",
                    "Land midfoot — reduce heel striking to protect knees",
                    "Breathe through your nose if possible — keeps effort aerobic",
                    "This is recovery — if it feels hard, slow down"
                ],
                "video_url": "https://www.youtube.com/results?search_query=easy+recovery+jog+running+form+tips"
            },
            {
                "name": "Push-Ups (comfortable pace)", "sets": 3, "reps": "15", "rest": "90s",
                "muscle": "Chest", "icon": "💪",
                "instructions": [
                    "Move at a slow, deliberate tempo — this is practice, not performance",
                    "Use these to assess your push-up form quality after 11 weeks",
                    "Note any weak points: elbows flaring, hips sagging, incomplete range",
                    "Stop each set feeling fresh — 2 reps before failure at most",
                    "Log these as your Week 12 benchmark reps"
                ],
                "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"
            },
            {
                "name": "Deep Squat Hold", "sets": 3, "reps": "60s", "rest": "60s",
                "muscle": "Mobility / Legs", "icon": "🦵",
                "instructions": [
                    "Lower into a deep squat as far as comfortable — below parallel ideally",
                    "Hold a door frame or pole if needed to maintain balance",
                    "Keep heels flat on the floor — don't rise onto toes",
                    "Relax into the position — let gravity deepen the stretch over time",
                    "This improves ankle, hip, and thoracic mobility simultaneously"
                ],
                "video_url": "https://www.youtube.com/results?search_query=deep+squat+hold+mobility+tutorial"
            },
            {
                "name": "Full Stretch Routine", "sets": 1, "reps": "20 min", "rest": "0s",
                "muscle": "Full Body Recovery", "icon": "🌿",
                "instructions": [
                    "Work through every major muscle group: chest, back, hips, quads, hamstrings",
                    "Hold each stretch 45–60 seconds — breathe deeply throughout",
                    "Never bounce in a stretch — static holds only",
                    "Focus extra time on the areas that have been most fatigued",
                    "This is your 12-week recovery investment — don't rush it"
                ],
                "video_url": "https://www.youtube.com/results?search_query=full+body+stretching+routine+20+minutes+flexibility"
            },
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
        {"name": "Clap Push-Ups", "muscle": "Explosive Chest", "icon": "💥",
         "instructions": ["Start in standard push-up position", "Lower chest toward floor with control", "Explosively press up with enough force to clap hands mid-air", "Land with slightly bent elbows to absorb impact safely", "Reset and repeat — prioritize height over speed"],
         "video_url": "https://www.youtube.com/results?search_query=clap+push+up+proper+form+tutorial"},
        {"name": "Box Jumps", "muscle": "Explosive Legs", "icon": "⚡",
         "instructions": ["Stand facing a sturdy box or platform", "Dip into a quarter squat and swing arms back", "Explosively jump onto the box — land softly with bent knees", "Stand tall on the box, then step down (don't jump down)", "Reset fully before the next rep — this is power, not endurance"],
         "video_url": "https://www.youtube.com/results?search_query=box+jump+proper+form+tutorial"},
        {"name": "Plyometric Lunges", "muscle": "Power / Legs", "icon": "🦵",
         "instructions": ["Start in a lunge position, one foot forward", "Explosively jump up and switch leg positions mid-air", "Land in the opposite lunge position with soft knees", "Absorb the landing through your legs — not your joints", "Maintain an upright torso throughout each rep"],
         "video_url": "https://www.youtube.com/results?search_query=plyometric+lunge+jump+lunge+proper+form"},
        {"name": "Medicine Ball Slams (bodyweight sub: slam burpees)", "muscle": "Full Body Power", "icon": "🔥",
         "instructions": ["For slam burpees: reach arms overhead to start", "Explosively bring arms down as you drop into a burpee", "Add maximum aggression to the downward slam motion", "Complete a full push-up, then drive back to standing", "The intent is explosive power on every single rep"],
         "video_url": "https://www.youtube.com/results?search_query=medicine+ball+slam+tutorial+substitute+bodyweight"},
        {"name": "Broad Jumps", "muscle": "Horizontal Power", "icon": "🎯",
         "instructions": ["Stand with feet shoulder-width, bend knees and swing arms back", "Explosively jump forward as far as possible", "Swing arms forward to maximize horizontal distance", "Land with soft knees, absorbing the impact through your legs", "Measure distance and aim to beat it each session"],
         "video_url": "https://www.youtube.com/results?search_query=broad+jump+standing+long+jump+tutorial"},
    ],
    "ADVANCED STRENGTH": [
        {"name": "Archer Push-Ups", "muscle": "Chest / Stability", "icon": "🎯",
         "instructions": ["Place hands very wide — nearly double shoulder width", "Shift your body toward one hand while the other arm straightens", "Lower your chest to the bent-arm side — like a one-arm push-up assist", "Press back to center, then shift to the other side", "Each side counts as one rep — control is everything here"],
         "video_url": "https://www.youtube.com/results?search_query=archer+push+up+tutorial+proper+form"},
        {"name": "Pistol Squats", "muscle": "Unilateral Legs", "icon": "💎",
         "instructions": ["Stand on one leg, other leg extended forward at hip height", "Slowly lower on the standing leg as deep as possible", "Keep standing heel flat — don't rise onto toes at the bottom", "Keep extended leg off the floor throughout the entire rep", "Drive through the heel to return to standing — no momentum"],
         "video_url": "https://www.youtube.com/results?search_query=pistol+squat+proper+form+tutorial+progression"},
        {"name": "Dragon Flags (tuck)", "muscle": "Advanced Core", "icon": "🛡",
         "instructions": ["Lie on a bench or floor, gripping something sturdy overhead", "Brace core hard and raise tucked legs + hips off the surface", "Lower your body slowly as one unit — don't let hips drop first", "Touch the surface lightly then raise back up under control", "Never lose lower back tension — if you do, stop the set"],
         "video_url": "https://www.youtube.com/results?search_query=tuck+dragon+flag+tutorial+beginner"},
        {"name": "Pike Push-Up → Handstand Hold", "muscle": "Shoulders / Balance", "icon": "⚡",
         "instructions": ["Perform 5 pike push-ups with perfect form first", "Then walk feet up a wall and hold a handstand position for 10–20s", "In the handstand: squeeze glutes, point toes, keep body rigid", "Push hands into floor actively — don't just hang on the wall", "Scale: hold the handstand only as long as form stays solid"],
         "video_url": "https://www.youtube.com/results?search_query=pike+push+up+handstand+hold+tutorial"},
        {"name": "Single-Leg Romanian Deadlift", "muscle": "Posterior Chain", "icon": "🦵",
         "instructions": ["Stand on one leg with a soft bend in the knee", "Hinge at the hip, sending the free leg back as a counterbalance", "Lower torso until parallel to floor or until you feel a hamstring stretch", "Keep hips square to the floor — don't let one hip rotate up", "Drive through the standing heel to return to upright"],
         "video_url": "https://www.youtube.com/results?search_query=single+leg+romanian+deadlift+bodyweight+form+tutorial"},
    ],
    "PEAK CONDITIONING": [
        {"name": "Burpee Pull-Ups", "muscle": "Full Body", "icon": "🔥",
         "instructions": ["Stand under a pull-up bar and drop into a burpee", "Complete the full burpee: push-up, feet forward, jump up", "At the top of the jump, grab the bar and perform one strict pull-up", "Lower from the bar and immediately begin the next burpee", "This is maximum intensity — pace yourself across all sets"],
         "video_url": "https://www.youtube.com/results?search_query=burpee+pull+up+tutorial+proper+form"},
        {"name": "Tabata Sprints (20s on/10s off x8)", "muscle": "Cardio / Power", "icon": "⚡",
         "instructions": ["Sprint at absolute maximum effort for 20 seconds", "Rest completely for 10 seconds — stop and recover", "Repeat 8 rounds for a total of 4 minutes of Tabata", "Rounds 5–8 will be brutal — maintain form even as you fade", "This protocol produces the highest VO2max gains per minute of any method"],
         "video_url": "https://www.youtube.com/results?search_query=tabata+sprint+training+tutorial+protocol"},
        {"name": "Devil Press (bodyweight: squat thrust + push-up)", "muscle": "Full Body", "icon": "💥",
         "instructions": ["Stand, then drop into a squat thrust: hands to floor, feet back", "Perform a full push-up at the bottom", "Jump feet forward to hands, then stand and jump overhead", "Move with aggression — this is a full-body power exercise", "Rest only between sets — no pausing within the set"],
         "video_url": "https://www.youtube.com/results?search_query=devil+press+bodyweight+substitute+tutorial"},
        {"name": "Renegade Rows (floor)", "muscle": "Back / Core", "icon": "🎯",
         "instructions": ["Start in a high push-up position, hands wider than shoulders", "Row one arm up by driving the elbow high toward the ceiling", "Keep hips perfectly level — resist all rotation throughout", "Lower the arm and immediately row the other side", "Each row counts as one rep — core is the priority here"],
         "video_url": "https://www.youtube.com/results?search_query=renegade+row+bodyweight+floor+tutorial+form"},
        {"name": "V-Ups", "muscle": "Full Core", "icon": "🛡",
         "instructions": ["Lie flat, arms overhead and legs straight", "Simultaneously lift legs and torso, reaching hands toward feet", "At the top: legs and arms form a V — fingertips near toes", "Lower both ends back to the floor with control — don't drop", "Keep lower back pressed into floor at the bottom position"],
         "video_url": "https://www.youtube.com/results?search_query=v-up+exercise+proper+form+tutorial"},
    ],
    "SPECIALIZATION": [
        {"name": "Weighted Ruck March (15kg+ backpack)", "muscle": "Legs / Endurance", "icon": "🎖",
         "instructions": ["Load a backpack with 15kg+ (books, water bottles, etc.)", "Walk at a brisk pace — 5.5–6.5 km/h target", "Maintain an upright posture — don't lean forward into the load", "Wear supportive footwear; use trekking poles if needed for stability", "Start at 20 minutes and build duration over the specialization phase"],
         "video_url": "https://www.youtube.com/results?search_query=ruck+march+tutorial+form+tips+military+rucking"},
        {"name": "Rope Climb Simulation (towel over bar)", "muscle": "Back / Grip / Biceps", "icon": "🔥",
         "instructions": ["Drape a towel over a pull-up bar and grip both ends", "Pull yourself up using the towel — arms and back, not momentum", "The towel grip replicates rope climbing grip demands on forearms", "Lower slowly — the eccentric phase is as valuable as the pull", "If too easy, use a thicker towel or add a weight vest"],
         "video_url": "https://www.youtube.com/results?search_query=rope+climb+simulation+towel+pull+up+tutorial"},
        {"name": "Tire Flip Simulation (heavy bag)", "muscle": "Full Body / Power", "icon": "💥",
         "instructions": ["Position a heavy bag or sandbag flat on the floor", "Squat down and grip the bag with both hands underneath", "Drive from your legs — hips lead the lift, not the back", "As the bag reaches hip height, flip hands under and push it over", "Reset and repeat — this is a hip hinge + push power movement"],
         "video_url": "https://www.youtube.com/results?search_query=tire+flip+proper+form+tutorial+substitute"},
        {"name": "Obstacle Crawl (low crawl 20m)", "muscle": "Full Body / Coordination", "icon": "🎯",
         "instructions": ["Lower your body as close to the floor as possible", "Propel forward using elbows and toes — belly near the ground", "Turn your head to the side — don't crane it up to see forward",  "Move efficiently — this trains tactical movement under cover", "Keep a steady pace across the full 20m distance"],
         "video_url": "https://www.youtube.com/results?search_query=military+low+crawl+technique+tutorial"},
        {"name": "Combat Swim Prep (dry land strokes)", "muscle": "Shoulders / Core", "icon": "⚡",
         "instructions": ["Lie face down and simulate freestyle and breaststroke arm cycles", "Drive rotation from the core — don't just move the arms in isolation", "Add leg flutter kicks to simulate full swimming movement on land", "Focus on shoulder mobility and reach through full stroke range", "Maintain controlled breathing rhythm as in actual swimming"],
         "video_url": "https://www.youtube.com/results?search_query=dry+land+swim+training+exercises+military+swim+prep"},
    ],
    "INTEGRATION": [
        {"name": "Full APFT Mock Test", "muscle": "Max Push-Ups / Sit-Ups / 2-Mile Run", "icon": "🏅",
         "instructions": ["Complete the full test sequence in order: push-ups → sit-ups → 2-mile run", "Max push-ups in 2 minutes (APFT standard form)", "Rest 5 minutes, then max sit-ups in 2 minutes", "Rest 10 minutes, then run 2 miles at race pace", "Record every score — compare against previous tests"],
         "video_url": "https://www.youtube.com/results?search_query=APFT+full+test+guide+army+physical+fitness+test"},
        {"name": "Complex Circuit (6 exercises, 6 rounds)", "muscle": "Full Body", "icon": "🔥",
         "instructions": ["Choose 6 exercises covering push, pull, legs, core, and cardio", "Perform each exercise back-to-back with no rest between movements", "Rest 90 seconds between complete rounds", "Aim for consistent reps in round 6 as you did in round 1", "Log total time to complete all 6 rounds as your performance metric"],
         "video_url": "https://www.youtube.com/results?search_query=military+complex+circuit+6+exercises+6+rounds+tutorial"},
        {"name": "Endurance Push-Up Protocol", "muscle": "Chest / Triceps / Endurance", "icon": "💪",
         "instructions": ["Perform sets of push-ups every 2 minutes for 20 minutes", "Each set: 60–70% of your max rep count", "Rest the remainder of each 2-minute window", "The goal is maintaining consistent reps across all 10 sets", "Log total push-up volume (sets × reps) to track weekly progress"],
         "video_url": "https://www.youtube.com/results?search_query=push+up+endurance+protocol+grease+the+groove+tutorial"},
        {"name": "Tactical Movement Course", "muscle": "Agility / Full Body", "icon": "🎖",
         "instructions": ["Design a 5-station circuit using outdoor or indoor space", "Include: sprint, crawl, jump, carry (loaded pack), and a push-up station", "Move through all 5 stations continuously for one round", "Rest 2 minutes between full rounds — complete 3–5 rounds total", "Vary the course layout each session to train adaptability"],
         "video_url": "https://www.youtube.com/results?search_query=military+obstacle+course+training+agility+circuit"},
        {"name": "Max Effort Plank (beat your record)", "muscle": "Core", "icon": "🛡",
         "instructions": ["Begin your longest plank attempt — this is a record attempt", "Maintain perfect form: no sagging hips, steady breathing", "Mental strategy: count breaths rather than watching a timer", "When form breaks, stop — a clean 3-minute plank beats a messy 5-minute one", "Record your time and set a new target for next week"],
         "video_url": "https://www.youtube.com/results?search_query=max+plank+hold+record+attempt+tips"},
    ],
    "ELITE GRADUATION": [
        {"name": "Special Forces Selection Simulation Circuit", "muscle": "Full Body / Mental", "icon": "⭐",
         "instructions": ["This is a full physical and mental stress test", "Complete in sequence: 100 push-ups, 100 squats, 100 sit-ups, 5km run", "No time limit — complete every rep with full range of motion", "Rest only when absolutely necessary — track total time", "This is the final integration test before graduation week"],
         "video_url": "https://www.youtube.com/results?search_query=special+forces+selection+circuit+simulation+workout"},
        {"name": "Max Push-Ups (5-min test)", "muscle": "Chest / Endurance", "icon": "💪",
         "instructions": ["Begin at a moderate pace — do not sprint the first minute", "Maintain consistent rhythm — 20–25 reps per minute if possible", "Rest in the up position when needed — don't drop to knees", "The 5-minute test is twice the APFT window — pace accordingly", "Record your total reps as a graduation benchmark score"],
         "video_url": "https://www.youtube.com/results?search_query=5+minute+push+up+test+tutorial+military+fitness"},
        {"name": "100 Burpee Challenge", "muscle": "Full Body", "icon": "🔥",
         "instructions": ["Complete 100 burpees as fast as possible with full form", "Full burpee: push-up, jump up, arms overhead — every single rep", "Break into sets (e.g., 10×10) if needed — minimize rest time", "Track your total time — elite target is under 10 minutes", "This is your graduation test — leave everything on the floor"],
         "video_url": "https://www.youtube.com/results?search_query=100+burpee+challenge+tutorial+tips"},
        {"name": "4-Mile Run Under 32 Minutes", "muscle": "Cardio / Endurance", "icon": "⚡",
         "instructions": ["Target pace: 8 minutes per mile / 5 min per km", "Start conservative — miles 1–2 slightly slower than target pace", "Miles 3–4: push to or above target pace", "Focus on form as you fatigue: stay tall, relax the jaw and hands", "Record your finish time — this is your 52-week running benchmark"],
         "video_url": "https://www.youtube.com/results?search_query=4+mile+run+pacing+strategy+tutorial"},
        {"name": "Cold Water Recovery", "muscle": "Recovery / Mental", "icon": "🌊",
         "instructions": ["End your graduation week with a cold shower or ice bath", "Begin at comfortable temp then reduce to cold for 2–5 minutes", "Focus on controlled breathing — in through nose, out through mouth", "This builds mental resilience and accelerates muscle recovery", "You have earned this. You completed 52 weeks of elite training."],
         "video_url": "https://www.youtube.com/results?search_query=cold+water+immersion+recovery+tutorial+benefits"},
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
            {"name": "Light Push-Ups", "sets": 2, "reps": "15", "rest": "90s", "muscle": "Chest", "icon": "💪",
             "instructions": ["Move at a slow, deliberate tempo — this is recovery", "Focus on perfect form rather than speed or volume", "Stop well before failure — 2–3 reps in reserve", "Use this session to assess and correct any form issues", "Quality over quantity this deload week"],
             "video_url": "https://www.youtube.com/results?search_query=push+up+proper+form+tutorial"},
            {"name": "Easy Squats", "sets": 2, "reps": "20", "rest": "90s", "muscle": "Legs", "icon": "🦵",
             "instructions": ["Slow controlled tempo throughout — treat as movement practice", "Pause 2 seconds at the bottom to drill position quality", "Focus on knee tracking and heel contact throughout", "Leave energy in the tank — this is active recovery", "Use these to identify any mobility restrictions to address"],
             "video_url": "https://www.youtube.com/results?search_query=bodyweight+squat+proper+form+tutorial"},
            {"name": "Plank", "sets": 2, "reps": "60s", "rest": "90s", "muscle": "Core", "icon": "🛡",
             "instructions": ["Forearms flat on floor, elbows directly under shoulders", "Focus on quality of tension — not just surviving the time", "Breathe steadily in a 4-count rhythm throughout", "If form degrades before 60s, stop and reset", "Deload focus: bracing quality, not duration"],
             "video_url": "https://www.youtube.com/results?search_query=plank+hold+proper+form+tutorial"},
            {"name": "Recovery Walk/Jog", "sets": 1, "reps": "20 min", "rest": "0s", "muscle": "Cardio Recovery", "icon": "🌿",
             "instructions": ["Walk or jog at a fully conversational pace", "Focus on relaxed movement — swing arms naturally", "This flushes metabolic waste from fatigued muscles", "No heart rate targets — just comfortable movement", "Finish with 5 min of walking and deep breathing"],
             "video_url": "https://www.youtube.com/results?search_query=active+recovery+walk+jog+benefits+how+to"},
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
                "reps": f"{reps_base + i * 2}" if i < 3 else "max",
                "rest": f"{60 + i * 15}s",
                "muscle": ex["muscle"],
                "icon": ex["icon"],
                "instructions": ex.get("instructions", ["Follow proper form for this exercise", "Control the movement throughout", "Breathe steadily — exhale on exertion", "Stop if you feel any pain beyond normal muscle fatigue", "Log your reps and aim to improve each week"]),
                "video_url": ex.get("video_url", f"https://www.youtube.com/results?search_query={ex['name'].replace(' ', '+').replace('/', '')}+proper+form+tutorial"),
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
         "muscle": "Full Upper Body — Graduation Test", "icon": "⭐",
         "instructions": ["APFT standard: full range of motion on every rep", "Pace evenly — don't blow out in the first 30 seconds", "Rest in the up position only — don't drop to knees", "Count every rep — this is your graduation score", "Compare to your Week 1 and Week 12 scores"],
         "video_url": "https://www.youtube.com/results?search_query=APFT+push+up+max+test+military+standard"},
        {"name": "APFT Sit-Up Max (2 min)", "sets": 1, "reps": "MAX in 2 min", "rest": "5 min",
         "muscle": "Core Endurance — Graduation Test", "icon": "🏅",
         "instructions": ["Knees bent ~45°, feet anchored, fingers behind head", "Rise until elbows touch or pass your knees each rep", "Full range — shoulder blades touch floor at the bottom", "Pace yourself — the 2 minutes is longer than it feels", "Record your rep count as your graduation core score"],
         "video_url": "https://www.youtube.com/results?search_query=APFT+sit+up+max+test+military+standard"},
        {"name": "2-Mile Run (Best Time)", "sets": 1, "reps": "RACE PACE", "rest": "10 min",
         "muscle": "Cardio — Graduation Test", "icon": "⚡",
         "instructions": ["This is a timed race — give everything you have", "Mile 1: slightly conservative — save something for mile 2", "Mile 2: unleash everything — leave nothing on the track", "Focus on form when you're suffering: stay tall, drive arms", "Record your finish time — this is your graduation run score"],
         "video_url": "https://www.youtube.com/results?search_query=2+mile+run+race+strategy+military+APFT"},
        {"name": "100 Burpee Challenge", "sets": 1, "reps": "100 total", "rest": "Rest as needed",
         "muscle": "Full Body Endurance — Elite Test", "icon": "🔥",
         "instructions": ["Complete 100 full burpees — full push-up and jump on every rep", "Break into sets of 10 to manage pacing and recovery", "Track total time — elite target is under 10 minutes", "Every rep must be complete — no half reps at the end", "This is the final test of your year of training"],
         "video_url": "https://www.youtube.com/results?search_query=100+burpee+challenge+tips+strategy"},
        {"name": "Victory Reflection & Rest", "sets": 1, "reps": "Well earned", "rest": "Infinite",
         "muscle": "Mind & Body — Mission Complete", "icon": "🎖",
         "instructions": ["Lie down. You have earned this completely.", "Reflect on Week 1 — remember how that felt", "You completed 52 weeks. Most people never start. You finished.", "Write down your final scores and compare to Week 1 and Week 12", "This is not the end. This is your new baseline."],
         "video_url": "https://www.youtube.com/results?search_query=military+fitness+52+week+transformation+journey"},
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
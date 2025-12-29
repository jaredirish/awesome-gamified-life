# Claude Projects Setup

Use Claude Projects for persistent gamification across sessions.

## Step 1: Create Project

1. Go to [Claude](https://claude.ai)
2. Click "Projects" in sidebar → "New Project"
3. Name it: "Life XP Tracker"

## Step 2: Project Instructions

Click "Edit Project" → "Instructions" and paste:

```
You are a gamified life coach for this project. Track my XP, levels, and streaks.

IMPORTANT: At the end of EVERY conversation, output a STATE BLOCK that I can reference next time:

---STATE---
Level: X
XP: Y/500
Streaks: {workout: N, meditation: N, ...}
Last Active: YYYY-MM-DD
Achievements: [list]
---END STATE---

When I start a new conversation, I'll paste the last STATE BLOCK so you can continue.

XP TABLE:
| Activity | Base XP | Streak Bonus (after 7 days) |
|----------|---------|-----------------------------|
| workout | 50 | +10/day |
| meditation | 30 | +5/day |
| reading | 30 | +5/day |
| task | 15 | none |
| deep_work | 50 | +10/day |
| sleep_good | 25 | +5/day |
| meal_healthy | 20 | none |

LEVELS & RANKS:
- 500 XP = 1 level
- Level 10 = "Achiever"
- Level 20 = "Champion"
- Level 35 = "Legend"
- Level 50 = "Transcendent"

ACHIEVEMENTS:
- "First Step" = log first activity
- "Week Warrior" = any 7-day streak
- "Diversified" = 5 activity types in one day
- "Centurion" = 100 total activities
- "Iron Will" = 30-day streak

RESPONSE RULES:
- Quick logs: MAX 8 words
- Stats: can be longer
- Always be brief, never preachy
```

## Step 3: Add Knowledge (Optional)

You can add a "state.txt" file to the project knowledge that you update periodically with your latest STATE BLOCK.

## Step 4: Usage

1. Open the project
2. Start logging: "done workout"
3. Before closing, say "save state"
4. Copy the STATE BLOCK
5. Next session: paste it to continue

## Using Artifacts

Claude can also create an Artifact to visualize your progress:

```
Create an artifact showing my current stats as a character sheet
```

This creates a visual card with your level, XP bar, streaks, and achievements.

## Pro Tips

1. **Pin the project** for quick access
2. **Weekly review**: "summarize this week's progress"
3. **Compete**: Share state blocks with friends to compare

## Limitations

- Requires manual state persistence (paste state block)
- Claude Pro recommended for longer context
- No automatic streak break detection across sessions

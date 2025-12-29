# Notion Integration

Track your gamified life in Notion with AI assistance.

## Option 1: Notion AI (Simplest)

### Setup
1. Create a new Notion page called "Life XP Tracker"
2. Add a database with these properties:
   - Date (date)
   - Activity (select: workout, meditation, reading, task, deep_work, meal, sleep)
   - XP (number)
   - Notes (text)

3. Add a "Stats" section at the top with:
   - Level: 1
   - Total XP: 0
   - Current Streaks: {}

### Using Notion AI
When logging, ask Notion AI:
```
Add a workout entry for today worth 50 XP. Update my total XP and check if I leveled up (500 XP per level).
```

### Limitations
- Manual XP tracking
- Notion AI doesn't auto-calculate streaks well
- Good for logging, weak for gamification

---

## Option 2: Notion + ChatGPT (Recommended)

### Setup
1. Create Notion database (same as above)
2. Use ChatGPT with Notion plugin enabled
3. Use this custom prompt:

```
You are a gamified life coach connected to my Notion "Life XP Tracker" database.

When I log activities:
1. Add entry to the Notion database
2. Calculate XP (workout:50, meditation:30, task:15, reading:30, deep_work:50, meal:20, sleep:25)
3. Update my "Stats" section with new totals
4. Check for level ups (500 XP = 1 level)
5. Track streaks (consecutive days)

Respond minimally: "+50 XP. Level 3. Workout streak: 5."

When I say "stats", query Notion and summarize my progress.
```

### Usage
```
You: done workout
AI: Adding to Notion... +50 XP. Level 3. Streak: 5 days.

You: stats
AI: Level 3 | 1,247 XP | Streaks: workout 5, meditation 12
```

---

## Option 3: Notion API + Script

For developers who want full automation.

### Prerequisites
- Notion account with API access
- Python 3.8+
- Notion integration token

### Setup

1. Create Notion integration at https://www.notion.so/my-integrations
2. Share your database with the integration
3. Install dependencies:
```bash
pip install notion-client
```

4. Create `notion_xp.py`:
```python
import os
from notion_client import Client
from datetime import datetime, timedelta

notion = Client(auth=os.environ["NOTION_TOKEN"])
DATABASE_ID = "your-database-id"

XP_TABLE = {
    "workout": 50,
    "meditation": 30,
    "reading": 30,
    "task": 15,
    "deep_work": 50,
    "meal": 20,
    "sleep": 25
}

def log_activity(activity: str, notes: str = ""):
    xp = XP_TABLE.get(activity, 15)

    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Date": {"date": {"start": datetime.now().isoformat()}},
            "Activity": {"select": {"name": activity}},
            "XP": {"number": xp},
            "Notes": {"rich_text": [{"text": {"content": notes}}]}
        }
    )

    total_xp = get_total_xp()
    level = total_xp // 500 + 1
    streak = get_streak(activity)

    return f"+{xp} XP. Level {level}. {activity} streak: {streak}."

def get_total_xp():
    results = notion.databases.query(database_id=DATABASE_ID)
    return sum(p["properties"]["XP"]["number"] or 0 for p in results["results"])

def get_streak(activity: str):
    results = notion.databases.query(
        database_id=DATABASE_ID,
        filter={"property": "Activity", "select": {"equals": activity}},
        sorts=[{"property": "Date", "direction": "descending"}]
    )

    streak = 0
    expected_date = datetime.now().date()

    for page in results["results"]:
        date_str = page["properties"]["Date"]["date"]["start"]
        entry_date = datetime.fromisoformat(date_str).date()

        if entry_date == expected_date:
            streak += 1
            expected_date -= timedelta(days=1)
        elif entry_date < expected_date:
            break

    return streak

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = log_activity(sys.argv[1], " ".join(sys.argv[2:]))
        print(result)
```

5. Usage:
```bash
export NOTION_TOKEN="your-token"
python notion_xp.py workout "leg day"
# +50 XP. Level 3. workout streak: 5.
```

---

## Notion Templates

### Database Properties
| Property | Type | Options |
|----------|------|---------|
| Date | Date | - |
| Activity | Select | workout, meditation, reading, task, deep_work, meal, sleep |
| XP | Number | - |
| Notes | Text | - |
| Streak Day | Formula | (calculated) |

### Stats Section Template
```
# 🎮 Life XP Tracker

## Current Stats
- **Level:** 1
- **Total XP:** 0 / 500
- **Rank:** Novice

## Active Streaks
- 🏋️ Workout: 0 days
- 🧘 Meditation: 0 days
- 📚 Reading: 0 days

## Achievements
- [ ] First Step (log first activity)
- [ ] Week Warrior (7-day streak)
- [ ] Iron Will (30-day streak)
```

---

## Tips

1. **Use Notion's mobile app** for quick logging
2. **Create a dashboard** with rollups showing weekly XP
3. **Set reminders** for streak maintenance
4. **Share with accountability partner** for motivation

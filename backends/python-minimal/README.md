# Python Minimal Backend

A ~50 line gamified life tracker with SQLite and REST API.

## Quick Start

```bash
pip install flask
python server.py
```

## API

### Log Activity
```bash
curl -X POST http://localhost:8000/log \
  -H "Content-Type: application/json" \
  -d '{"activity": "workout"}'
```

Response:
```json
{
  "ack": "+50 XP",
  "streak": 3,
  "level": 2,
  "xp": 847,
  "xp_to_next": 153
}
```

### Get Stats
```bash
curl http://localhost:8000/stats
```

Response:
```json
{
  "level": 2,
  "xp": 847,
  "xp_to_next": 153
}
```

## XP Values

| Activity | XP |
|----------|-----|
| workout | 50 |
| meditation | 30 |
| reading | 30 |
| task | 15 |
| deep_work | 50 |
| meal | 20 |
| sleep | 25 |

## Extending

### Add achievements
```python
ACHIEVEMENTS = {
    "first_step": lambda stats: stats["total_activities"] >= 1,
    "week_warrior": lambda stats: any(s >= 7 for s in stats["streaks"].values()),
}
```

### Add user authentication
```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@app.route("/log", methods=["POST"])
@auth.login_required
def log():
    ...
```

### Connect to HOMIE
This backend can be called from HOMIE's LLM via function calling:
```python
# In HOMIE's tool definitions
tools = [{
    "name": "log_activity",
    "description": "Log a completed activity for XP",
    "parameters": {"activity": {"type": "string", "enum": ["workout", "meditation", ...]}}
}]
```

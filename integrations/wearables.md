# Wearable Integrations

Log activities from your wrist, glasses, or any wearable.

---

## Apple Watch / Siri

### Method 1: iOS Shortcuts (Works NOW)

Create a Shortcut that calls the LifeXP API:

1. Open **Shortcuts** app on iPhone
2. Create new Shortcut
3. Add actions:

```
Shortcut: "Log Workout"

Actions:
1. Get contents of URL
   - URL: https://api.lifexp.io/log
   - Method: POST
   - Headers: Authorization: Bearer YOUR_API_KEY
   - Request Body: JSON
     {
       "activity": "workout",
       "user_id": "your-id"
     }

2. Get Dictionary Value (key: "ack") from Shortcuts Input

3. Speak Text: [Dictionary Value]
```

4. Name it "Log Workout"
5. Enable for Siri: "Hey Siri, Log Workout"
6. Enable for Apple Watch

### Usage

- **iPhone**: "Hey Siri, log workout" → "Plus 50 XP"
- **Apple Watch**: Tap complication or say "Log workout"
- **AirPods**: Double-tap + "Log workout"

### Other Shortcuts to Create

| Shortcut Name | Activity | Voice Trigger |
|---------------|----------|---------------|
| Log Workout | workout | "I worked out" |
| Log Meditation | meditation | "I meditated" |
| Log Reading | reading | "I read" |
| Log Task | task | "Task done" |
| Check Stats | (GET /stats) | "My stats" |

---

## Meta Ray-Ban / Oakley Glasses

### Current Status (2024-2025)

Meta doesn't yet support custom "Hey Meta" voice commands. But there are workarounds:

### Method 1: Siri Relay

Your Meta glasses can trigger Siri on your paired iPhone:

1. Set up iOS Shortcuts (above)
2. Say: "Hey Siri, log workout"
3. Siri runs Shortcut → calls LifeXP API
4. Response plays through glasses speakers

**Limitation**: Requires saying "Hey Siri" instead of "Hey Meta"

### Method 2: Messenger Hack

There's a [community workaround](https://github.com/dcrebbin/meta-glasses-api) that intercepts Messenger:

1. Say "Hey Meta, send message to LifeXP"
2. Browser extension catches it
3. Routes to your LifeXP backend
4. Response comes back as message

**Limitation**: Requires browser extension running on computer

### Method 3: Companion App (2026)

When Meta releases the [Wearables Device Access Toolkit](https://developers.meta.com/wearables/faq/):

1. LifeXP companion app on iOS/Android
2. Glasses detect workout end (accelerometer)
3. Auto-prompt: "Log this workout?"
4. Voice confirm: "Yes" → +50 XP

**Timeline**: Limited developer preview now, broad availability 2026

---

## Garmin Watches

Garmin has excellent APIs and the new [Oakley Meta Vanguard](https://www.wareable.com/wearable-tech/oakley-meta-vanguard-smart-glasses-price-pre-order-specs-features) has deep Garmin integration.

### Method 1: Garmin Connect Webhook

1. Garmin watch completes workout
2. Garmin Connect syncs to cloud
3. Webhook fires to LifeXP API
4. Auto-log workout with duration/type

Setup:
```bash
# Garmin Connect IQ → Webhooks (via Zapier or custom)
Trigger: Activity Completed
Action: POST to https://api.lifexp.io/log
Body: {
  "activity": "workout",
  "source": "garmin",
  "type": "{{activity_type}}",
  "duration_min": "{{duration}}"
}
```

### Method 2: Connect IQ App (Future)

A native Garmin app that:
- Shows current XP/level on watch face
- Quick-log buttons for activities
- Streak widget

---

## Wear OS (Samsung, Pixel, etc.)

### Method 1: Tasker Automation

1. Install Tasker on phone
2. Install AutoWear plugin
3. Create task:

```
Profile: AutoWear Command "log workout"
Task:
  1. HTTP POST to LifeXP API
  2. AutoWear Voice: "Plus 50 XP"
```

4. Trigger from watch: "OK Google, log workout"

### Method 2: Tile App (Future)

A simple Wear OS Tile:
- Tap activity icon → log it
- Shows current streak
- XP progress ring

---

## Brilliant Monocle / Mentra Glass

If you're building with open hardware like Brilliant Labs or Mentra:

### Full AR Integration

Since you control the stack:

```python
# On activity log, push to glasses display
def on_xp_earned(user, activity, xp):
    monocle.display(f"+{xp} XP", duration=3)
    if check_level_up(user):
        monocle.display("LEVEL UP!", animation="celebration")
    if check_streak_milestone(user, activity):
        monocle.display(f"🔥 {streak} day streak!")
```

### Voice Integration

```python
# Whisper running locally on glasses
def on_voice_detected(text):
    if matches_activity_pattern(text):
        activity = classify_activity(text)
        result = log_activity(user, activity)
        speak(result.ack)  # "Plus 50 XP"
```

---

## Fitbit

### Method: IFTTT Integration

1. Connect Fitbit to IFTTT
2. Create applet:
   - Trigger: "New exercise logged"
   - Action: Webhook to LifeXP API

```
Webhook URL: https://api.lifexp.io/log
Method: POST
Body: {"activity": "workout", "source": "fitbit", "type": "{{ExerciseType}}"}
```

---

## Whoop

### Method: Whoop API (Requires Whoop 4.0+)

```python
# Poll Whoop API for completed workouts
def sync_whoop():
    workouts = whoop.get_workouts(since=last_sync)
    for workout in workouts:
        lifexp.log({
            "activity": "workout",
            "source": "whoop",
            "strain": workout.strain,
            "duration_min": workout.duration
        })
```

---

## Generic: Any Wearable with Bluetooth

If your wearable can trigger your phone:

```
Wearable → Bluetooth → Phone → Tasker/Shortcuts → LifeXP API
```

Most wearables can:
- Send notifications
- Trigger phone assistant
- Run companion app actions

---

## Integration Priority Roadmap

| Device | Priority | Status | ETA |
|--------|----------|--------|-----|
| iOS Shortcuts (Watch/Siri) | P0 | Ready Now | - |
| Garmin Webhook | P1 | Ready Now | - |
| Wear OS Tasker | P2 | Ready Now | - |
| Meta Glasses SDK | P1 | Waiting on Meta | 2026 |
| Native Watch Apps | P2 | Backlog | Q3 2025 |
| Brilliant/Mentra | P1 | When you have HW | - |

---

## API Endpoints for Wearables

All wearables hit the same simple API:

```bash
# Log activity
POST https://api.lifexp.io/log
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json

{
  "activity": "workout",
  "source": "garmin",           # optional: for analytics
  "duration_min": 45,           # optional
  "notes": "leg day"            # optional
}

# Response
{
  "ack": "+50 XP",
  "streak": 5,
  "level": 12,
  "xp": 5847,
  "xp_to_next": 153
}
```

```bash
# Get stats (for watch face)
GET https://api.lifexp.io/stats
Authorization: Bearer YOUR_API_KEY

# Response
{
  "level": 12,
  "xp": 5847,
  "xp_to_next": 153,
  "rank": "Champion",
  "streaks": {
    "workout": 5,
    "meditation": 12
  }
}
```

---

## Voice Command Cheat Sheet

| Platform | Wake Word | Command |
|----------|-----------|---------|
| Apple | "Hey Siri" | "Log workout" |
| Google | "OK Google" | "Log workout" |
| Meta | "Hey Meta" | (2026: "LifeXP log workout") |
| Alexa | "Alexa" | "Tell LifeXP I worked out" |
| HOMIE | "Hey Jarvis" | "Done workout" |

---

## Sources

- [Meta Wearables Device Access Toolkit](https://developers.meta.com/wearables/faq/)
- [Meta glasses pseudo-API hack](https://github.com/dcrebbin/meta-glasses-api)
- [Oakley Meta Vanguard Garmin integration](https://www.wareable.com/wearable-tech/oakley-meta-vanguard-smart-glasses-price-pre-order-specs-features)
- [Garmin Connect IQ](https://developer.garmin.com/connect-iq/)

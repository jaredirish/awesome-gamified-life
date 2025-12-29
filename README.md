# 🎮 Awesome Gamified Life

> Turn your daily habits into an RPG. Level up IRL.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ⚡ Try It Now (30 Seconds)

**Step 1:** Open [ChatGPT](https://chat.openai.com)

**Step 2:** Paste this:

```
You are a gamified life coach. Track my XP, levels, and streaks.

RULES:
- Start me at Level 1, 0 XP
- Workout: +50 XP | Meditation: +30 XP | Task: +15 XP | Reading: +30 XP
- 500 XP = level up
- Track streaks for consecutive days
- Respond in MAX 10 words

COMMANDS:
- "done workout" → "+50 XP. Logged."
- "stats" → show level, XP, streaks

Say "Ready." and wait.
```

**Step 3:** Say "done workout" → Get XP 🎮

---

## 📊 What You Get

```
You: done workout
AI: +50 XP. Logged.

You: meditated
AI: +30 XP. Streak: 3 days.

You: stats
AI: Level 2 | 847 XP | Workout: 5 days 🔥
```

---

## 🎯 XP System

| Activity | XP | Streak Bonus (7+ days) |
|----------|-----|------------------------|
| Workout | +50 | +10/day |
| Meditation | +30 | +5/day |
| Deep work | +50 | +10/day |
| Reading | +30 | +5/day |
| Task done | +15 | - |
| Good sleep | +25 | +5/day |

**Levels:** 500 XP each → Level 10 "Achiever" → Level 20 "Champion" → Level 50 "Transcendent"

---

## 📁 More Prompts

| Prompt | Best For |
|--------|----------|
| [Voice Optimized](prompts/voice.md) | Spoken logging (3-5 word responses) |
| [Claude Version](prompts/claude-simple.md) | Claude users |
| [With Persistence](prompts/claude-projects.md) | Multi-day tracking |
| [Universal](prompts/universal.md) | Any LLM (Gemini, Llama, etc.) |

---

## 🔥 30-Day Training Arc Challenge

Ready to go harder? Try our first community challenge:

**The Rules:**
- 30 days, no breaks
- Log at least ONE activity daily
- Reach Level 5 by day 30
- Post your final stats with #LifeXP

[Get the Training Arc Prompt →](prompts/challenges/training-arc.md)

---

## 💾 Want Persistence?

Session-based prompts reset when you close the chat. For multi-day tracking:

| Option | Effort | Persistence |
|--------|--------|-------------|
| [Claude Projects](prompts/claude-projects.md) | Low | Project-scoped |
| [Python Backend](backends/python-minimal/) | Medium | Forever (SQLite) |
| [HOMIE Stack](https://github.com/jaredirish/jarvis-stack) | High | Full voice assistant |

---

## 🔧 Build Your Own

Want to build an app? Start with our minimal backend:

```bash
pip install flask
python backends/python-minimal/server.py
```

```bash
curl -X POST localhost:8000/log -d '{"activity":"workout"}'
# {"ack": "+50 XP", "streak": 3, "level": 2}
```

[Full API docs →](backends/python-minimal/README.md)

---

## 🗺️ Roadmap

- [x] Core prompts (ChatGPT, Claude, Universal)
- [x] Voice-optimized prompt
- [x] Python backend
- [x] 30-day Training Arc challenge
- [ ] iOS Shortcuts integration
- [ ] Wearable guides (Apple Watch, Garmin)
- [ ] More themed challenges

---

## 🤝 Contributing

1. Fork this repo
2. Add your prompt, backend, or integration
3. Submit PR

All contributions welcome!

---

## 📄 License

MIT - Do whatever you want.

---

**⭐ Star this repo if it helped you level up!**

Made with 🎮 by [@jaredirish](https://github.com/jaredirish)

# lablab.ai Submission — Paste Kit

## Title
TANNY — Voice-First JARVIS-Style AI Agent

## Short description (1–2 sentences)
TANNY is a JARVIS-style HUD assistant with a real "Hey Tanny" wake word, live streaming transcription, and true barge-in — built entirely on AssemblyAI's Universal-3.5 Pro streaming API.

## Long description
Most "voice assistants" are chat apps with a mic button bolted on: push-to-talk, no interruption, noticeable lag. TANNY is built the other way around — voice-first from the ground up.

Say "Hey Tanny" and it responds — no button required. Under the hood, your microphone streams directly into AssemblyAI's Universal-3.5 Pro streaming model over WebSocket, which returns live partial transcripts as you talk and a fully formatted final transcript the moment you stop. That final transcript both displays in TANNY's HUD and drives its wake-word matching.

The feature we're proudest of is barge-in: AssemblyAI's `SpeechStarted` event fires the instant you start speaking, even while TANNY is mid-reply, and we use it to cut TANNY's voice output off immediately. It's the difference between a script reading responses at you and something that actually feels like a conversation.

Reasoning is handled by Groq's Llama 3.3 70B behind a local daemon, wrapped in a JARVIS-style persona (think Tony Stark's AI, minus the ego). The whole thing runs inside a from-scratch Iron Man HUD interface — arc reactor boot sequence, live physics/particle/neural/fractal simulations, and system telemetry — because if you're building a voice-first assistant, it should look like one.

Security-wise, the AssemblyAI API key never touches the browser: a small standalone token server mints short-lived temporary tokens server-side, and the browser only ever holds a token good for one session.

## Tags
voice-agent, speech-to-text, real-time, assemblyai, streaming, wake-word, llm, groq, hud, jarvis

## Tech stack
AssemblyAI Universal-3.5 Pro (streaming STT), Groq (Llama 3.3 70B), JavaScript/HTML/CSS (frontend HUD), Python (token server + daemon), Web Speech API (TTS)

## Submission checklist
- [ ] Enrolled on the lablab.ai event page
- [ ] Public GitHub repo pushed (tanny.html, aai_token_server.py, server.py, README.md)
- [ ] Demo Application URL (host the static frontend; note the two local Python processes it depends on — see README)
- [ ] Cover image — cover.png (included)
- [ ] Demo video (≤5 min, MP4) — see VIDEO_SCRIPT.md for the shot list
- [ ] Slide deck (PDF) — slides.pdf (included)
- [ ] Submitted before Sep 30, 2026 cutoff

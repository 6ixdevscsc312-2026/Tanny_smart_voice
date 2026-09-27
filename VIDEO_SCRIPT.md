# TANNY — Demo Video Script (target: 3:30–4:30, hard cap 5:00)

Record with OBS or Windows Game Bar. Screen + mic audio. Keep energy up — judges watch dozens of these.

## 0:00–0:25 — Cold open, no narration yet
- Reload the page so the boot sequence plays in full (arc reactor spin-up, boot lines, the new "LINKING ASSEMBLYAI STREAMING UPLINK..." line).
- Let it breathe for a couple seconds once the HUD is live.

## 0:25–0:55 — You, on camera or voiceover
"Hey, I'm Fortune. This is TANNY — a voice-first AI agent built for the AssemblyAI Voice Agent Hackathon. Most voice assistants are chat apps with a mic button bolted on. TANNY's built the other way around: it's always listening, it streams what you say in real time through AssemblyAI, and you can interrupt it mid-sentence like a real conversation."

## 0:55–1:40 — Wake word + live transcription
- Click the mic once to arm it, then hands-off from here.
- Say: **"Hey Tanny, what can you help me with today?"**
- Let the camera catch the live partial transcript filling in the input box as you talk — pause briefly mid-sentence so the partial-vs-final difference is visible.
- Let TANNY reply in voice + on-screen text.

## 1:40–2:20 — Barge-in (the money shot)
- Ask something that gets a longer reply: **"Hey Tanny, explain what an arc reactor does."**
- While it's still talking, cut in with: **"Tanny, stop — actually, run a physics sim instead."**
- Point out on camera (or in a text overlay) that it stopped talking the instant you spoke — that's AssemblyAI's `SpeechStarted` event driving the interrupt, not a fixed delay.

## 2:20–3:10 — The HUD payoff
- Show the simulation lab running (physics/particle/neural — whichever looks best on camera).
- Optionally trigger the AI-described simulation feature ("simulate a black hole accretion disk") to show the LLM + sim integration.
- Briefly show the topbar telemetry / left-right panels to sell the "built a whole product" feeling.

## 3:10–3:40 — Under the hood (quick technical beat)
- Cut to a code view or the architecture slide from slides.pdf for ~15 seconds while you narrate:
"Under the hood: your mic streams straight into AssemblyAI's Universal-3.5 Pro model over WebSocket. The API key never touches the browser — a small local server mints short-lived tokens. Final transcripts drive both the wake word and the reply; the SpeechStarted event drives barge-in. Groq's Llama 3.3 70B handles the reasoning behind a local daemon."

## 3:40–4:00 — Close
"That's TANNY. Wake word, live streaming, real interruption, all on AssemblyAI. Thanks for watching."

## Notes
- Record 2–3 takes of the wake-word + barge-in section — it's the part that sells the project, worth getting right.
- If mic echo/feedback shows up on the recording, mute system audio playback of your own voice or wear headphones while recording.
- Keep total runtime under 5:00 — trim the sim-lab section first if you're running long, it's the least AssemblyAI-relevant part.

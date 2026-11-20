# Bhashabid — Gemini CLI Context

Follow the project constitution (`specs/00-constitution.md`) and the rules in `CLAUDE.md`; they apply to every agent.

- Stop immediately if `state/STOP` exists.
- Deterministic Bengali (numbers, dates, Unicode, Dari) comes from the engine (`bhashabid` CLI / Python), not from your own guesses.
- Tests: `python -m unittest discover -s eval/unit`.
- **Learning loop:** to improve the system from real Bengali output, follow `docs/LEARNING_LOOP_AGENT_GUIDE.md`.
  You may generate input, run `bhashabid learn scan`, and record recommendations with `bhashabid learn suggest --by "<your model id>"`.
  You must never approve, reject or apply cards unless the human explicitly instructs it for named cards with their own name as reviewer.

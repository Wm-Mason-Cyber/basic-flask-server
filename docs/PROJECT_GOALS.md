Project goals:
- Provide a minimal, well-commented Flask app that demonstrates web vulnerabilities and safe coding patterns.
- Teach reflected XSS, stored XSS, SQL injection, and safe API handling.
- Keep data local and resettable (JSON + SQLite) so labs are repeatable.

Safety & instructor guidance:
- This repository intentionally contains insecure code for teaching. Do not expose it to untrusted networks.
- Use `scripts/reset_data.sh` between lab runs to clear state.
- Encourage students to compare vulnerable vs safe endpoints and to inspect HTML source and network traffic.

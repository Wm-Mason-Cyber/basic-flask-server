# Flask Basics Demo — Student Worksheet
# Flask Basics Demo — Student Worksheet (Step-by-step)

This worksheet guides students through short, focused exercises that show the difference between insecure and secure handling of user input.

Preparation (instructor)
- Run the app locally: create a venv, install deps, and start Flask (see README). Use an isolated machine or VM.
- Reset demo state before the class: `bash scripts/reset_data.sh`.

Exercise 1 — Reflected XSS (10 minutes)

Goal: See how reflecting unsanitized input can execute scripts in the browser.

Steps for students:
1. Open: `/vulnerable_reflected?q=<script>alert(1)</script>`
	- Observe: does the browser show an alert? Open DevTools -> Console.
2. Open: `/safe_reflected?q=<script>alert(1)</script>`
	- Observe: is there an alert? Inspect page source (View → Page Source) and compare how the input appears.

Questions
- Which page executed the script? Why did the other page not execute it?
- Where in the HTML is the user input placed? Is it escaped?

Instructor answer
- `/vulnerable_reflected` executes the script because the server returns the raw input into HTML without escaping.
- `/safe_reflected` does not execute the script because Jinja2 auto-escaping (or explicit escaping) renders the input as text (`&lt;script&gt;...`).

Exercise 2 — Stored XSS (15 minutes)

Goal: Understand persistent stored XSS and why stored data must be escaped when rendered.

Steps:
1. Visit `/stored_vuln`. Submit message: `<script>console.log('stored-xss')</script>`.
	- Then reload or visit the page from a different browser profile. Observe whether the script runs.
2. Visit `/stored_safe`. Submit the same message. Observe whether it executes.

Questions
- What is the difference in behavior between the two endpoints?
- If you were designing a chat app, how would you avoid stored XSS?

Instructor answer
- `/stored_vuln` stores messages and renders them unescaped, so stored scripts execute when the page is viewed.
- `/stored_safe` stores messages but the template displays them escaped; no execution.
- To prevent stored XSS: always escape or sanitize output, use a strict content security policy, and treat user content as untrusted.

Exercise 3 — SQL Injection (15 minutes)

Goal: See why concatenating user input into SQL allows attackers to alter queries.

Steps:
1. Visit `/sql_vuln?name=' OR '1'='1`.
	- Observe results: does it return multiple rows? Inspect the page for the constructed query.
2. Visit `/sql_safe?name=' OR '1'='1`.
	- Observe results: are rows returned unexpectedly?

Questions
- How does the vulnerable query treat the input? What does the injected condition do?
- How does parameterized SQL prevent injection?

Instructor answer
- The vulnerable endpoint concatenates the `name` into the SQL string; an injection like `' OR '1'='1` can make the WHERE clause always true and return all rows.
- The safe endpoint uses parameterized queries (placeholders) so the input is treated as data, not code.

Extra exploration tasks (optional)
- Inspect the `data/messages.json` file after submitting stored messages.
- Try safe encodings (e.g., sending `&lt;script&gt;`) and see how the templates render them.

Resetting and cleanup
- To clear stored messages and the DB: `bash scripts/reset_data.sh`.

Safety reminders
- This repository intentionally contains vulnerable code for educational use. Do not host it on public servers.


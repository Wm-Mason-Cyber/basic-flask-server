# Flask Basics Demo — Student Worksheet

This worksheet walks students through simple web security demos: reflected and stored XSS, and SQL injection.

1) Reflected XSS

1) Reflected XSS
 - Visit `/vulnerable_reflected?q=<script>alert(1)</script>` and observe the behavior.
 - Visit `/safe_reflected?q=<script>alert(1)</script>` and compare.

2) Stored XSS
 - Visit `/stored_vuln` and submit a message containing `<script>alert(1)</script>` then reload the page; note execution.
 - Visit `/stored_safe` and submit a message containing `<script>alert(1)</script>`; it should not execute.

3) SQLi
 - Visit `/sql_vuln?name=' OR '1'='1` and observe results — vulnerable endpoint may return all rows.
 - Visit `/sql_safe?name=' OR '1'='1` and observe that parameterization prevents injection.

Answer key (instructor)
 - Reflected vulnerable page: shows raw script tag; browser executes it. Use developer tools to inspect the HTML.
 - Reflected safe page: shows escaped output; no execution.
 - Stored vulnerable: stored message containing script executes when page is viewed.
 - Stored safe: stored message is escaped and displays as text.
 - SQL vulnerable: concatenation of input into SQL can allow condition bypass (e.g., `' OR '1'='1`).
 - SQL safe: parameterized query prevents injection and does not return unintended rows.

Safety notes for instructors
 - Run this lab on isolated networks or local VMs.
 - Reset data between students using `bash scripts/reset_data.sh`.
 - Do not deploy this application to public-facing servers.


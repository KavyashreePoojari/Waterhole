Student Portal Login Demo — (Educational Only)
A simple Flask demo that looks like a student login portal. It captures a username on one page and a password on the next, then saves the pair to a local SQLite database. For learning only — do not use real credentials.

How it works:
- User submits username via a POST form to /username.
- Server stores the username in the session and redirects to /password.
- User submits password via a POST form to /password.
- Server reads the username from the session and inserts username, password into users.db.

Why this is risky?

Passwords are stored in plain text — anyone who gets the DB can read them. If intercepted (no HTTPS) or if DB is exposed, attackers can reuse credentials elsewhere (account takeover, phishing, resale).

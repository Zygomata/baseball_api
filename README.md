<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Baseball Scouting API README</title>
  <style>
    :root {
      --bg: #0b1020;
      --panel: #121a2b;
      --text: #e8edf7;
      --muted: #a8b3c7;
      --accent: #4db6ac;
      --accent-2: #7dd3fc;
      --border: #27324a;
      --code: #0f172a;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, Segoe UI, Roboto, Arial, sans-serif;
      background: linear-gradient(180deg, var(--bg), #0f172a);
      color: var(--text);
      line-height: 1.6;
    }
    .wrap {
      max-width: 980px;
      margin: 0 auto;
      padding: 40px 20px 72px;
    }
    .card {
      background: rgba(18, 26, 43, 0.92);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 32px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }
    h1, h2, h3 { line-height: 1.2; }
    h1 {
      font-size: 2.3rem;
      margin: 0 0 12px;
    }
    h2 {
      margin-top: 34px;
      padding-top: 10px;
      border-top: 1px solid var(--border);
      color: var(--accent-2);
    }
    p, li { color: var(--text); }
    .lead { color: var(--muted); font-size: 1.05rem; }
    code, pre {
      font-family: Consolas, Monaco, 'Courier New', monospace;
    }
    pre {
      background: var(--code);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      overflow-x: auto;
      color: #dbeafe;
    }
    .inline-code {
      background: var(--code);
      border: 1px solid var(--border);
      padding: 2px 6px;
      border-radius: 6px;
      color: #dbeafe;
    }
    a { color: var(--accent-2); }
    ul { padding-left: 20px; }
    .badge {
      display: inline-block;
      margin-bottom: 10px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(77, 182, 172, 0.12);
      border: 1px solid rgba(77, 182, 172, 0.35);
      color: var(--accent);
      font-size: 0.9rem;
      font-weight: 600;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }
    .mini {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
    }

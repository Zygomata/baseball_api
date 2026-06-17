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
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="badge">Project README</div>
      <h1>Baseball Scouting API</h1>
      <p class="lead">A FastAPI-based baseball scouting app that combines Sports Reference CSV source files, notebook-based data preparation, and a Jinja2 frontend to explore player stats by team and position.</p>

      <h2>Overview</h2>
      <p>This project builds a scouting workflow from raw team CSV files through a cleaned master dataset and into a lightweight web application. The notebook prepares and merges the source files into <span class="inline-code">api_teams_data.csv</span>, while the FastAPI app serves a scouting page and an API endpoint for filtered player data.</p>

      <h2>Features</h2>
      <ul>
        <li>FastAPI backend for serving player data and page routes.</li>
        <li>Jinja2 template rendering through <span class="inline-code">templates/scout.html</span>.</li>
        <li>Team and position filtering through <span class="inline-code">POST /api/players</span>.</li>
        <li>Notebook-based data preparation in <span class="inline-code">lake.ipynb</span>.</li>
        <li>Cleaned aggregate dataset stored in <span class="inline-code">api_teams_data.csv</span>.</li>
        <li>Source CSV workflow using a <span class="inline-code">sources/</span> folder populated with Sports Reference exports.</li>
      </ul>

      <h2>Project Structure</h2>
      <pre><code>.
├── api.py
├── api_teams_data.csv
├── lake.ipynb
├── templates/
│   └── scout.html
└── sources/
    ├── braves.csv
    ├── dodgers.csv
    ├── yankees.csv
    └── ...</code></pre>

      <p>The FastAPI app points Jinja2 at the <span class="inline-code">templates</span> directory and renders <span class="inline-code">scout.html</span> from there. The raw team CSV files in <span class="inline-code">sources/</span> serve as the input layer for the notebook-based data pipeline.</p>

      <h2>How It Works</h2>
      <ol>
        <li>Collect team CSV files from Sports Reference into the <span class="inline-code">sources/</span> folder.</li>
        <li>Use <span class="inline-code">lake.ipynb</span> to load, clean, and merge those files.</li>
        <li>Export the processed data to <span class="inline-code">api_teams_data.csv</span>.</li>
        <li>Run <span class="inline-code">api.py</span> to serve the frontend and API endpoints.</li>
      </ol>

      <h2>API Endpoints</h2>
      <div class="grid">
        <div class="mini">
          <h3>GET /</h3>
          <p>Renders the scouting interface using <span class="inline-code">templates/scout.html</span>.</p>
        </div>
        <div class="mini">
          <h3>POST /api/players</h3>
          <p>Returns filtered player data using request fields such as team, position, and optional metrics.</p>
        </div>
      </div>

      <h2>Example Request</h2>
      <pre><code>{
  "team": "braves",
  "position": "1B",
  "metrics": ["WAR", "OPS", "HR"]
}</code></pre>

      <h2>Running the App</h2>
      <pre><code>uvicorn api:app --reload</code></pre>
      <p>Then open <span class="inline-code">http://127.0.0.1:8000</span> in your browser.</p>

      <h2>Tech Stack</h2>
      <ul>
        <li>Python</li>
        <li>FastAPI</li>
        <li>pandas</li>
        <li>Jinja2</li>
        <li>HTML, CSS, and JavaScript frontend template</li>
      </ul>

      <h2>Data Notes</h2>
      <p>The processed dataset includes player metrics such as team, age, position, WAR, OPS, OBP, SLG, HR, RBI, and related batting fields used for scouting-style filtering. The source workflow is designed around team-level Sports Reference CSV exports that are consolidated into a master table for application use.</p>
    </div>
  </div>
</body>
</html>

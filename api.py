

# scouting reports, rankings, and game  statistics.

# rolling averages, ranking players by position, and generating simple scouting reports for coaches. 


import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

df = pd.read_csv('api_teams_data.csv')
print("Columns found:", df.columns.tolist())  

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("scout.html", {"request": request})

@app.post("/api/players")
async def filter_players(request: Request):
    
    body = await request.json()
    team = body.get("team", "").strip()          
    position = body.get("position", "").strip() 
    metrics = body.get("metrics", [])            
    
    print(f"Filtering: team='{team}' pos='{position}' metrics={metrics}")
    
    filtered = df.copy()
    if team:
        filtered = filtered[filtered['team'] == team]
    if position:
        filtered = filtered[filtered['Pos'] == position]
    
    filtered = filtered.replace([float('inf'), -float('inf')], 0).fillna(0)
    
    print(f"Returning {len(filtered)} players")
    return {"players": filtered.to_dict("records")}

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI on GCP DEMO</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                .container {
                    text-align: center;
                    padding: 2rem;
                    background: rgba(255, 255, 255, 0.1);
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                }
                h1 { font-size: 3rem; margin: 0; }
                p { font-size: 1.5rem; }
                .emoji { font-size: 4rem; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="emoji">🚀</div>
                <h1>FastAPI on GCP VM</h1>
                <p>Deployed with CI/CD Pipeline</p>
                <p><small>API Docs: <a href="/docs" style="color: #fff;">/docs</a></small></p>
            </div>
        </body>
    </html>
    """


@app.get("/api")
def api_root():
    return {"message": "Hello from FastAPI on GCP VM 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}

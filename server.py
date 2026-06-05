from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "sami" and request.password == "123456":
        return {"status": "success", "message": "مرحباً بك في تطبيقك الاحترافي"}
    raise HTTPException(status_code=401, detail="بيانات الدخول خاطئة")

@app.get("/content")
def get_content():
    return {
        "categories": [
            {
                "category_name": "بث مباشر - رياضة وأخبار",
                "items": [
                    {
                        "title": "Red Bull TV (رياضة)",
                        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Red_Bull_TV_logo.svg/512px-Red_Bull_TV_logo.svg.png",
                        "stream_url": "https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8"
                    },
                    {
                        "title": "Al Jazeera (أخبار)",
                        "thumbnail": "https://upload.wikimedia.org/wikipedia/ar/thumb/0/05/Al_Jazeera_logo.svg/256px-Al_Jazeera_logo.svg.png",
                        "stream_url": "https://live-hls-web-aja.getaj.net/AJA/index.m3u8"
                    }
                ]
            },
            {
                "category_name": "عالم السينما والأطفال",
                "items": [
                    {
                        "title": "Big Buck Bunny (فيلم)",
                        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Big_buck_bunny_poster_big.jpg/334px-Big_buck_bunny_poster_big.jpg",
                        "stream_url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8"
                    }
                ]
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
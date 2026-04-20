import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static"
)

projects = [
    {
        "id": 1,
        "title": "블로그 웹앱",
        "desc": "Flask 기반 CRUD 블로그",
        "detail": "사용자 인증, 글 작성/수정/삭제 기능 구현"
    },
    {
        "id": 2,
        "title": "포트폴리오 사이트",
        "desc": "반응형 개인 웹사이트",
        "detail": "Vercel 배포 및 UI/UX 개선"
    }
]

@app.route("/")
def home():
    profile = {
        "name": "홍길동",
        "job": "소프트웨어 개발자",
        "intro": "문제 해결과 사용자 경험을 중요하게 생각하는 개발자입니다.",
        "github": "https://github.com/your-id"
    }
    return render_template("index.html", profile=profile, projects=projects)

@app.route("/project/<int:id>")
def project(id):
    proj = next((p for p in projects if p["id"] == id), None)
    return render_template("project.html", project=proj)

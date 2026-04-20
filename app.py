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
        "detail": "사용자 인증, 글 작성·수정·삭제 기능을 완전히 구현한 풀스택 블로그 플랫폼입니다. JWT 기반 인증과 RESTful API 설계를 통해 확장성을 고려했습니다.",
        "tech": ["Python / Flask", "SQLite / SQLAlchemy", "Jinja2 Templates", "JWT Authentication"]
    },
    {
        "id": 2,
        "title": "포트폴리오 사이트",
        "desc": "반응형 개인 웹사이트",
        "detail": "Vercel 서버리스 환경에서 Flask를 운용하는 포트폴리오 사이트입니다. 반응형 레이아웃과 접근성을 고려한 UI/UX 개선에 집중했습니다.",
        "tech": ["Python / Flask", "Vanilla CSS & JS", "Vercel Serverless", "Intersection Observer API"]
    }
]

profile = {
    "name": "홍길동",
    "job": "소프트웨어 개발자",
    "intro": "문제 해결과 사용자 경험을 중요하게 생각하는 개발자입니다.",
    "github": "https://github.com/your-id",
    "email": "hello@yourdomain.com",
    "skills": [
        {"name": "Python / Flask",      "level": 5},
        {"name": "JavaScript",          "level": 4},
        {"name": "HTML / CSS",          "level": 5},
        {"name": "SQL / Database",      "level": 3},
        {"name": "Git / DevOps",        "level": 4},
        {"name": "UI / UX Design",      "level": 3},
    ]
}

@app.route("/")
def home():
    return render_template("index.html", profile=profile, projects=projects)

@app.route("/project/<int:id>")
def project(id):
    proj = next((p for p in projects if p["id"] == id), None)
    return render_template("project.html", project=proj, profile=profile)

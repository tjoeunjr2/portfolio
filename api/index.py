import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel이 이 변수명을 자동으로 인식합니다
handler = app

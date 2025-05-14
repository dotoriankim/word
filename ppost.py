import requests
import base64
import os
from dotenv import load_dotenv

# .env 파일에서 설정값 불러오기
load_dotenv()

WORDPRESS_USERNAME = os.getenv("WORDPRESS_USERNAME")   # 예: kimkyounghyu@naver.com
WORDPRESS_APP_PASSWORD = os.getenv("WORDPRESS_APP_PASSWORD")  # 예: dhflrhrl1@
SITE_URL = os.getenv("SITE_URL")  # 예: https://emboblocks.wordpress.com

POST_TITLE = "임시 테스트 글입니다"
POST_CONTENT = """
<h2>자동화 테스트 중입니다.</h2>
<p>정상적으로 워드프레스 자동 포스팅이 작동하는지 확인하는 중입니다.</p>
"""

# 인증 처리
credentials = f"{WORDPRESS_USERNAME}:{WORDPRESS_APP_PASSWORD}"
token = base64.b64encode(credentials.encode())
headers = {
    "Authorization": f"Basic {token.decode('utf-8')}",
    "Content-Type": "application/json"
}

# 포스트 요청
post_url = f"{SITE_URL}/wp-json/wp/v2/posts"
payload = {
    "title": POST_TITLE,
    "content": POST_CONTENT,
    "status": "publish"
}

response = requests.post(post_url, headers=headers, json=payload)

if response.status_code == 201:
    print("업로드 성공!")
else:
    print(f"업로드 실패... 상태코드: {response.status_code}")
    print(response.text)

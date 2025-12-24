# 🚀 Trip Connection 설정 가이드

## 📋 목차
1. [사전 준비](#사전-준비)
2. [API 키 발급](#api-키-발급)
3. [백엔드 설정](#백엔드-설정)
4. [프론트엔드 설정](#프론트엔드-설정)
5. [실행 방법](#실행-방법)

---

## 🔧 사전 준비

### 필요한 소프트웨어
- Python 3.11+
- Node.js 20.19.0+
- pip
- npm

---

## 🔑 API 키 발급

### 1. Google Maps API 키 (필수 - 지도 기능용)

1. [Google Cloud Console](https://console.cloud.google.com/) 접속
2. 새 프로젝트 생성 또는 기존 프로젝트 선택
3. **APIs & Services** → **Enable APIs and Services** 클릭
4. 다음 API들을 활성화:
   - Maps JavaScript API
   - Places API (선택사항)
5. **Credentials** → **Create Credentials** → **API Key** 선택
6. API 키 복사 (나중에 사용)

### 2. OpenAI API 키 (선택사항 - AI 추천용)

1. [OpenAI Platform](https://platform.openai.com/) 접속 및 로그인
2. **API Keys** 메뉴로 이동
3. **Create new secret key** 클릭
4. API 키 복사 (나중에 사용)

> ⚠️ **주의**: OpenAI API는 유료입니다. API 키 없이도 룰 기반 추천은 작동합니다.

---

## 🐍 백엔드 설정

### 1. 환경 변수 설정

```bash
cd back
cp .env.example .env
```

`.env` 파일을 열고 다음 내용 입력:

```env
# Django Secret Key
SECRET_KEY=your-django-secret-key-here

# OpenAI API Key (선택사항)
OPENAI_API_KEY=sk-your-openai-api-key-here

# CORS (프로덕션 환경)
# CORS_ALLOWED_ORIGINS=http://localhost:5173,https://yourdomain.com
```

### 2. 가상 환경 생성 및 활성화

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

---

## 🎨 프론트엔드 설정

### 1. 환경 변수 설정

```bash
cd ../front
cp .env.example .env
```

`.env` 파일을 열고 다음 내용 입력:

```env
# Backend API URL
VITE_API_BASE_URL=http://127.0.0.1:8000

# Google Maps API Key
VITE_GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here
```

### 2. 의존성 설치

```bash
npm install
```

---

## ▶️ 실행 방법

### 1. 백엔드 서버 실행 (첫 번째 터미널)

```bash
cd back
python manage.py runserver
```

서버 실행 확인: http://127.0.0.1:8000

### 2. 프론트엔드 서버 실행 (두 번째 터미널)

```bash
cd front
npm run dev
```

앱 접속: http://localhost:5173

---

## 🎯 초기 데이터 추가 (선택사항)

### Django Admin에서 샘플 데이터 추가

1. http://127.0.0.1:8000/admin 접속
2. 생성한 관리자 계정으로 로그인
3. **Places** 모델에 장소 추가:
   - 이름: 예) "경복궁"
   - 카테고리: tourist
   - 주소: "서울특별시 종로구 사직로 161"
   - 위도/경도: 37.5796, 126.9770
   - 평균 가격: 3000
   - 가격 레벨: 1
   - 평점: 4.5

---

## 🐛 문제 해결

### 1. Migration 오류

```bash
python manage.py migrate --run-syncdb
```

### 2. CORS 오류

`back/tc_system/settings.py`에서 CORS 설정 확인:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

### 3. Google Maps가 표시되지 않음

- `.env` 파일에 `VITE_GOOGLE_MAPS_API_KEY` 확인
- API 키가 올바른지 확인
- Google Cloud Console에서 해당 API가 활성화되었는지 확인
- 브라우저 콘솔에서 오류 메시지 확인

### 4. GPT 추천이 작동하지 않음

- `.env` 파일에 `OPENAI_API_KEY` 확인
- OpenAI 계정에 크레딧이 있는지 확인
- API 키 없이도 룰 기반 추천은 작동합니다

---

## 📦 주요 기능

✅ 회원가입/로그인 (JWT)
✅ 여행지 검색 (카테고리, 예산, 태그)
✅ AI 기반 맞춤 추천 (OpenAI GPT)
✅ 지도에 장소 표시 (Google Maps)
✅ 여행 패키지 생성/관리
✅ 리뷰 작성 및 평점
✅ 랜덤 장소 추천

---

## 🎊 완료!

이제 Trip Connection을 사용할 준비가 완료되었습니다! 🚀

문제가 발생하면 GitHub Issues에 등록해주세요.

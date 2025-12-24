"""
AI 기반 여행 추천 시스템
"""
import os
import json
from typing import List, Dict

def get_gpt_recommendation(user_preferences: Dict) -> List[str]:
    """
    GPT를 활용한 여행지 추천

    user_preferences 예시:
    {
        'concept': '액티비티',
        'budget': 100000,
        'duration': 3,
        'companions': '가족',
        'preferences': '자연, 휴식'
    }
    """
    # OpenAI API 키 확인
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        print("⚠️  OpenAI API 키가 없습니다. 룰 기반 추천을 사용합니다.")
        return generate_rule_based_recommendation(user_preferences)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        # 프롬프트 구성
        concept = user_preferences.get('concept', '관광')
        budget = user_preferences.get('budget', 0)
        duration = user_preferences.get('duration', 1)
        companions = user_preferences.get('companions', '혼자')
        preferences = user_preferences.get('preferences', '')

        budget_str = f"{budget:,}원" if budget > 0 else "제한 없음"

        prompt = f"""당신은 한국 여행 전문가입니다. 다음 조건에 맞는 한국 여행지를 추천해주세요:

조건:
- 여행 컨셉: {concept}
- 예산: {budget_str}
- 여행 기간: {duration}일
- 동행인: {companions}
- 선호 사항: {preferences if preferences else '없음'}

요청사항:
1. 위 조건에 가장 적합한 한국 여행지 5개를 추천해주세요
2. 응답은 반드시 JSON 배열 형식으로만 작성해주세요
3. 각 장소명은 간단명료하게 (예: "제주도", "경복궁", "부산 해운대")

응답 형식 예시:
["제주도", "경복궁", "부산 해운대", "전주 한옥마을", "강릉 경포대"]"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "당신은 한국 여행 전문가입니다. 사용자의 조건에 맞는 여행지를 추천하며, 응답은 항상 JSON 배열 형식입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )

        # GPT 응답 파싱
        content = response.choices[0].message.content.strip()

        # JSON 파싱 시도
        try:
            recommendations = json.loads(content)
            if isinstance(recommendations, list):
                return recommendations[:5]
        except json.JSONDecodeError:
            # JSON 파싱 실패 시 간단한 문자열 파싱
            print(f"⚠️  GPT 응답 파싱 실패. 응답: {content}")

        return generate_rule_based_recommendation(user_preferences)

    except ImportError:
        print("⚠️  openai 패키지가 설치되지 않았습니다. 'pip install openai' 실행 필요")
        return generate_rule_based_recommendation(user_preferences)

    except Exception as e:
        print(f"⚠️  GPT API 호출 실패: {str(e)}")
        return generate_rule_based_recommendation(user_preferences)


def generate_rule_based_recommendation(preferences: Dict) -> List[str]:
    """
    룰 기반 추천 시스템 (GPT 대안)
    """
    concept = preferences.get('concept', '')
    budget = preferences.get('budget', 0)

    recommendations = []

    # 컨셉별 추천
    if '액티비티' in concept or 'activity' in concept:
        recommendations.extend(['스키장', '번지점프', '패러글라이딩'])
    elif '휴식' in concept or '자연' in concept:
        recommendations.extend(['제주도', '강릉', '속초'])
    elif '맛집' in concept or 'restaurant' in concept:
        recommendations.extend(['전주', '부산', '서울 명동'])
    elif '쇼핑' in concept or 'shopping' in concept:
        recommendations.extend(['명동', '홍대', '강남'])
    else:
        recommendations.extend(['경복궁', 'N서울타워', '한강공원'])

    # 예산별 필터링
    if budget and budget < 50000:
        recommendations = [r for r in recommendations if '공원' in r or '한강' in r]

    return recommendations[:5]  # 최대 5개 반환


def calculate_optimal_route(places: List[Dict]) -> List[Dict]:
    """
    장소 간 최적 경로 계산 (간단한 알고리즘)
    실제로는 Google Maps Directions API 사용 권장
    """
    # TODO: Google Maps Directions API 연동
    # 현재는 단순히 순서대로 반환
    return places

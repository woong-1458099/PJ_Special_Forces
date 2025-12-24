"""
AI 기반 여행 추천 시스템
"""
import os
import json
from typing import List, Dict

# OpenAI GPT를 사용하는 경우 (선택사항)
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
    # TODO: OpenAI API 연동 시 아래 코드 활성화
    # import openai
    # openai.api_key = os.getenv('OPENAI_API_KEY')

    # prompt = f"""
    # 다음 조건에 맞는 한국 여행지를 추천해주세요:
    # - 컨셉: {user_preferences.get('concept', '관광')}
    # - 예산: {user_preferences.get('budget', 0)}원
    # - 기간: {user_preferences.get('duration', 1)}일
    # - 동행인: {user_preferences.get('companions', '혼자')}
    # - 선호: {user_preferences.get('preferences', '')}

    # 추천 장소 이름만 JSON 배열로 반환해주세요.
    # """

    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )

    # return json.loads(response.choices[0].message.content)

    # 현재는 더미 추천 반환
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

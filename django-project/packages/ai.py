import os
import re
from openai import OpenAI
from places.models import Place

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_places_from_prompt(prompt: str):
    """
    GPT에게 여행 추천 요청 → 장소 이름 리스트 반환
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "너는 여행 추천 전문가다. 장소 이름만 리스트로 답해라."
                },
                {
                    "role": "user",
                    "content": f"다음 요청에 맞는 여행 장소 5곳 추천해줘: {prompt}"
                }
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content

        # 줄 단위로 파싱
        place_names = [
            re.sub(r'^[0-9\.\-\s]+', '', line).strip()
            for line in content.split("\n")
            if line.strip()
        ]

        return place_names

    except Exception as e:
        # 실패 시 빈 리스트 반환 (서버 안정성)
        print("GPT 호출 실패:", e)
        return []


def map_place_names_to_places(place_names):
    """
    GPT가 준 장소 이름 → DB Place 매핑
    """
    places = []
    for name in place_names:
        place = Place.objects.filter(name__icontains=name).first()
        if place:
            places.append(place)
    return places

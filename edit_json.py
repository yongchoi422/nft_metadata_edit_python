import json

# JSON 파일 로드
with open('_metadata.json', 'r') as file:
    data = json.load(file)

# 설정값
contract_address = "0x3cA07ca8D5cb17f03af4FFb246d57fAA6aE6acE9"
chain_id = "8453"

# 각 아이템에 대해 animation_url 및 image URL 추가
for i, item in enumerate(data):
    token_id = i  # tokenId는 0부터 시작
    item["animation_url"] = f"https://iframe-tokenbound.vercel.app/{contract_address}/{token_id}/{chain_id}"
    item["image"] = f"https://bafybeib7z7oh5rjv4u4m7rpu6pejxukkqtx3ok6f46kzl6kencwqibveyi.ipfs.w3s.link/2024.11.20%20doldole%26sundole_nft.jpg"

# 변경된 데이터를 다시 JSON 파일로 저장
with open('_metadata.json', 'w') as file:
    json.dump(data, file, indent=4)

# 실행: python edit_json.py

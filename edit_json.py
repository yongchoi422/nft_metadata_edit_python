import json

# JSON 파일 로드
with open('_metadata.json', 'r') as file:
    data = json.load(file)

# 설정값
contract_address = "contract_address"
chain_id = "chain_id"

# 각 아이템에 대해 animation_url 추가
for i, item in enumerate(data):
    token_id = i  # tokenId는 0부터 시작
    item["animation_url"] = f"https://iframe-tokenbound.vercel.app/{contract_address}/{token_id}/{chain_id}"

# 변경된 데이터를 다시 JSON 파일로 저장
with open('_metadata.json', 'w') as file:
    json.dump(data, file, indent=4)


# python edit_json.py to excute
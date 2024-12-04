import json
from datetime import datetime, timedelta

def generate_metadata(base_name, description, image_url, animation_base_url, start_edition, total_count, attributes_list):
    """
    Generate metadata for a series of NFTs.

    :param base_name: Base name for the NFTs.
    :param description: Description for the NFTs.
    :param image_url: URL of the NFT image.
    :param animation_base_url: Base URL for the animation links.
    :param start_edition: Starting edition number.
    :param total_count: Total number of NFTs to generate.
    :param attributes_list: List of attribute dictionaries for the NFTs.
    :return: List of NFT metadata.
    """
    metadata = []
    base_date = datetime.now()

    for i in range(total_count):
        edition_number = start_edition + i
        nft = {
            "name": f"{base_name} #{edition_number}",
            "description": description,
            "image": image_url,
            "edition": edition_number,
            "date": int((base_date + timedelta(seconds=i)).timestamp() * 1000),
            "attributes": attributes_list[i % len(attributes_list)],  # Rotate attributes if fewer than total_count
            "compiler": "HashLips Art Engine",
            "animation_url": f"{animation_base_url}/{edition_number}/8453"  # Incremented animation number
        }
        metadata.append(nft)

    return metadata

# Example Usage
base_name = "YongSanCats & Heemang"
description = """**From Heemang to Ami: A Journey of Resilience and Love**

When I first met Heemang—then unknowingly calling her Pika—I didn’t realize the neighbors had already given her a far more fitting name: Heemang, meaning "Hope." She was a small, lonely cat, out of place among the stray groups in the area. Vulnerable and hungry, she often sneaked into the *DoldolE Clan*’s feeding shelter, a quiet outlier among the bustling feline community. Unlike other strays who would cautiously feed under the cover of night, HOPE would appear during the daytime, from noon to 4 PM, a sign of her fragility and need.

This was especially difficult for her because another stray, DolsunE, was also pregnant at the same time. DolsunE later brought all four of her kittens to the *DoldolE Clan*’s shelter, while HOPE remained on the outskirts, uncertain and struggling. Recognizing her quiet desperation, I began feeding her separately. But even with a full belly, she seemed so fragile, her eyes carrying the weight of loneliness and loss.

A few months ago, I discovered that HOPE had given birth, though her kittens were nowhere to be seen, hidden from the world. As nearby reconstruction forced me to plan the relocation of the *DoldolE Clan*, I knew I couldn’t leave HOPE behind. I held onto the hope that her kittens were safe and wanted to give them all a chance at a better life.

Then came the heartbreaking news. A neighbor told me that her kittens hadn’t survived. HOPE’s silent grief was palpable, yet even through her pain, she began to show signs of resilience. Slowly, she started regaining her strength. Her cautious, reserved demeanor speaks to the hardships she has endured on the streets. Yet, beneath her wary exterior lies a gentle, loving soul—a soul that one neighbor recognized long ago when they named her Heemang, "Hope," with the wish for a brighter future.

Today, HOPE’s story has taken a remarkable turn. She has found a family who sees her pain and her past as part of her strength, embracing her with compassion and rewriting her story into one of real hope and joy. For the first time, she is loved and cared for, her once-fragile spirit now blossoming in a safe and nurturing home.

Thank you for hearing her voice and being part of the journey that transformed HOPE’s life. Her name is not just a wish anymore—it’s her reality. Cheers Ami."""
image_url = "https://bafybeigapsqebtl6ftdonnwex2lgjngs7sk4bxuqdk2ilxynvme5fqqopi.ipfs.w3s.link/2024.11.20%20heemang_nft.jpg"
animation_base_url = "https://iframe-tokenbound.vercel.app/0x0d87321De65aa82D9B3f53172a3cF24faF817692"
start_edition = 0
total_count = 3000

# Define the custom attributes
attributes_list = [
    [
        {"trait_type": "Coat Color", "value": "Calico"},
        {"trait_type": "Eye Color", "value": "Green"},
        {"trait_type": "Body Size", "value": "Small"},
        {"trait_type": "Age", "value": "1+"},
        {"trait_type": "Facial Feature", "value": "Sharp"},
        {"trait_type": "Coat Length", "value": "Short"},
        {"trait_type": "Meaning of the Name in Korean", "value": "Hope"},
        {"trait_type": "Core Personality", "value": "A quiet yet unyielding spirit."},
        {"trait_type": "Fun Fact", "value": "When Heemang finally used the litter box for the first time in her new home, her pee formed the unmistakable shape of a middle finger—a hilariously defiant symbol of her resilience."},
        {"trait_type": "Rescued At", "value": "Itaewon, Yongsangu, Seoul, South Korea"},
        {"trait_type": "Rescued Date", "value": "2024.11.16"}
    ]
]

metadata = generate_metadata(base_name, description, image_url, animation_base_url, start_edition, total_count, attributes_list)

# Save to a JSON file
with open("_metadata.json", "w") as f:
    json.dump(metadata, f, indent=4)

print("NFT metadata has been saved to _metadata.json")

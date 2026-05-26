from dotenv import load_dotenv
from openai import OpenAI
import os
import requests

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
base_url = "https://openrouter.ai/api/v1"

if not api_key:
    raise SystemExit("OPENROUTER_API_KEY kosong. Cek file .env dulu.")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

models = requests.get(f"{base_url}/models", timeout=30).json()["data"]

free_models = []
for m in models:
    model_id = m.get("id", "")
    pricing = m.get("pricing", {})
    prompt_price = float(pricing.get("prompt", 999))
    completion_price = float(pricing.get("completion", 999))

    if model_id.endswith(":free") or (prompt_price == 0 and completion_price == 0):
        free_models.append(model_id)

print(f"Ketemu {len(free_models)} model gratis.")
print("Mencoba model gratis satu per satu...\n")

for model in free_models:
    try:
        print(f"Testing: {model}")
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": "Jawab tepat satu kalimat dalam bahasa Indonesia: koneksi berhasil."
                }
            ],
            max_tokens=80,
            temperature=0.2,
            timeout=45
        )

        content = response.choices[0].message.content

        if content:
            print("\nMODEL BERHASIL ?")
            print("PAKAI MODEL INI:")
            print(model)
            print("\nJawaban:")
            print(content)
            break
        else:
            print("Gagal: response kosong / None\n")

    except Exception as e:
        print(f"Gagal: {str(e)[:220]}\n")
else:
    print("Belum ada model gratis yang berhasil. Coba ulang beberapa menit lagi.")

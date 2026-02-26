import sys, os, time, json
sys.path.append(r'e:\Antigravity\EduMate')
from utils.ai_service import generate_quiz
from utils.ai_service import st

# Reset cache to force real call
st.cache_data.clear()

for i in range(10):
    print(f"Attempt {i+1}...")
    res = generate_quiz("Python basics")
    if "API Quota Exceeded" in res or "429" in res:
        print("Quota hit. waiting 15s...")
        time.sleep(15)
        continue
        
    print("GOT RESPONSE:")
    print(repr(res))
    
    res_clean = res.strip()
    if res_clean.startswith("```json"):
        res_clean = res_clean[7:-3].strip()
    elif res_clean.startswith("```"):
        res_clean = res_clean[3:-3].strip()
        
    try:
        data = json.loads(res_clean)
        print("✅ JSON PARSED SUCCESSFULLY")
    except Exception as e:
        print("❌ JSON PARSE FAILED:", e)
    break

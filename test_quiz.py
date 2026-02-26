import sys, os
sys.path.append(r'e:\Antigravity\EduMate')
from utils.ai_service import generate_quiz
res = generate_quiz("Python basics")
print("<<RAW START>>")
print(repr(res))
print("<<RAW END>>")

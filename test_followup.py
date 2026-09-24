from src.self_rag import run_self_rag

r1 = run_self_rag("payments CPU high", "t2")
print("Q1 route:", r1["route"])

r2 = run_self_rag("aur checkout API ka kya?", "t2")
print("Q2 route:", r2["route"])
print("\nTRACE:")
for t in r2["trace"]:
    print("  -", t)
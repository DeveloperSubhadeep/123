import itertools

tags = [
    'CAM', 'CAMRip', 'TS', 'TSRip', 'Telesync', 'HD-TS', 'HD-CAM',
    'S Print', 'Screen Print', 'HQ S Print', 'High-Quality Screen Print',
    'HC', 'Hardcoded', 'WP', 'Workprint', 'HEVC'
]

combinations = []
for r in range(2, len(tags)+1):  # 2 theke sobar combination
    for combo in itertools.combinations(tags, r):
        combinations.append(' '.join(combo))

print(f"Total combinations: {len(combinations)}")
print(combinations[:50])  # প্রথম ৩০টা দেখাও

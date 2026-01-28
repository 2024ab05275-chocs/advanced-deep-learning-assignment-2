import os
import random

# ===== CONFIG =====
DATA_DIR = "data/img_align_celeba"
KEEP_COUNT = 20000
IMAGE_EXTS = (".jpg", ".jpeg", ".png")

# ==================

# List all image files
files = [
    f for f in os.listdir(DATA_DIR)
    if f.lower().endswith(IMAGE_EXTS)
]

total_files = len(files)

if total_files <= KEEP_COUNT:
    print(f"Only {total_files} files found. Nothing to delete.")
    exit()

# Randomly select files to keep
keep_files = set(random.sample(files, KEEP_COUNT))

deleted = 0
for f in files:
    if f not in keep_files:
        os.remove(os.path.join(DATA_DIR, f))
        deleted += 1

print("===================================")
print(f"Initial files : {total_files}")
print(f"Kept files    : {KEEP_COUNT}")
print(f"Deleted files : {deleted}")
print("===================================")

# METHOD 1: Using huggingface_hub (RECOMMENDED)
#POTETNTIALLY FINETUNE EXISTING MODEL
# %%
from huggingface_hub import snapshot_download

# Download entire dataset
# %%
snapshot_download(
    repo_id="yann111/GlobalGeoTree",
    repo_type="dataset",
    local_dir="./GlobalGeoTree-6M",
    allow_patterns="GlobalGeoTree-6M/*"  # Only files in this folder
)

print("Download complete!")

# %%
import tarfile
import json
import pandas as pd

tar_path = "GlobalGeoTree-6M/GlobalGeoTree-6M/GGT-0.2M_0.5M-000000.tar"

small_sample = []

with tarfile.open(tar_path, "r") as tar:
    for member in tar:
        if member.isfile() and member.name.endswith(".json"):
            f = tar.extractfile(member)
            if f:
                obj = json.loads(f.read().decode("utf-8"))
                small_sample.append(obj)

                if len(small_sample) >= 1000:
                    break

df = pd.DataFrame(small_sample)
print(df.head())
print(df.shape)

# %%
1+1
# %%

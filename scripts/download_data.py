import os

import requests

BASE_URL = "https://huggingface.co/datasets/cannlytics/cannabis_results/resolve/main/data/{}/{}-results-latest.xlsx"

os.makedirs("data/raw/test-results", exist_ok=True)


def download_test_results():
    """Download test results for all states."""
    for state in [
        "ca",
        "co",
        "ct",
        "fl",
        "hi",
        "ma",
        "md",
        "mi",
        "nv",
        "ny",
        "or",
        "ri",
        "ut",
        "wa",
    ]:
        url = BASE_URL.format(state, state)
        print(f"Downloading {url}")
        r = requests.get(url)
        with open(f"data/raw/test-results/{state}-results.xlsx", "wb") as f:
            f.write(r.content)


if __name__ == "__main__":
    download_test_results()
    download_test_results()

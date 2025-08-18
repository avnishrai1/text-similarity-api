
"""
batch_infer.py
--------------
Run similarity over the provided dataset CSV and save results.

Usage:
    python batch_infer.py --input DataNeuron_Text_Similarity.csv --output scored.csv
"""

import argparse
import pandas as pd
from tqdm import tqdm
from model import get_similarity

def guess_columns(df: pd.DataFrame):
    # Prefer standard names
    lower_cols = [c.lower() for c in df.columns]
    if "text1" in lower_cols and "text2" in lower_cols:
        i1 = lower_cols.index("text1")
        i2 = lower_cols.index("text2")
        return df.columns[i1], df.columns[i2]
    # Else assume first two columns are the pairs
    if len(df.columns) >= 2:
        return df.columns[0], df.columns[1]
    raise ValueError("Input CSV must have at least two text columns.")

def main(args):
    df = pd.read_csv(args.input)
    c1, c2 = guess_columns(df)

    scores = []
    for t1, t2 in tqdm(zip(df[c1].astype(str), df[c2].astype(str)), total=len(df)):
        scores.append(get_similarity(t1, t2))

    out = df.copy()
    out["similarity score"] = scores
    out.to_csv(args.output, index=False)
    print(f"Saved {len(out)} rows to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Path to input CSV")
    parser.add_argument("--output", type=str, default="scored.csv", help="Output CSV path")
    args = parser.parse_args()
    main(args)

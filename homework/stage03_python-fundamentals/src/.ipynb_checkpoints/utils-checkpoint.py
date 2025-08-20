from pathlib import Path
import pandas as pd
import numpy as np

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    num = df.select_dtypes(include=[np.number])
    desc = num.describe().T
    desc['n_missing'] = num.isna().sum()
    desc['pct_missing'] = num.isna().mean()
    return desc

def choose_group_col(df: pd.DataFrame) -> str | None:
    if 'category' in df.columns:
        return 'category'
    candidates = [c for c in df.columns if df[c].dtype == 'object' or str(df[c].dtype).startswith('category')]
    candidates = [c for c in candidates if df[c].nunique() > 1 and df[c].nunique() < df.shape[0]]
    if not candidates:
        return None
    best = min(candidates, key=lambda c: df[c].nunique())
    return best

def group_by_and_agg(df: pd.DataFrame, group_col: str = None) -> pd.DataFrame:
    col = group_col or choose_group_col(df)
    if col is None:
        return pd.DataFrame() 
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if not numeric_cols:
        return pd.DataFrame()
    agg = df.groupby(col)[numeric_cols].agg(['mean', 'std', 'count'])
    agg.columns = ['_'.join(col).strip() for col in agg.columns.values]
    return agg.reset_index()

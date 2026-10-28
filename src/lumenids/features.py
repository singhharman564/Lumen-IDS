import numpy as np
import pandas as pd


def zeek_to_common(conn: pd.DataFrame) -> pd.DataFrame:
    """Map Zeek connection records to the common Lumen IDS feature schema."""
    d = conn.copy()

    numeric_cols = [
        "duration", "orig_bytes", "resp_bytes",
        "orig_pkts", "resp_pkts", "id.resp_p"
    ]

    for col in numeric_cols:
        d[col] = pd.to_numeric(d[col], errors="coerce")

    d[numeric_cols] = d[numeric_cols].fillna(0)

    hist = d["history"].fillna("").astype(str)
    total_s = d["duration"].replace(0, np.nan)

    out = pd.DataFrame({
        "dst_port": d["id.resp_p"],
        "duration_us": d["duration"] * 1_000_000,
        "fwd_pkts": d["orig_pkts"],
        "bwd_pkts": d["resp_pkts"],
        "fwd_bytes": d["orig_bytes"],
        "bwd_bytes": d["resp_bytes"],
        "bytes_per_s": (
            (d["orig_bytes"] + d["resp_bytes"]) / total_s
        ).fillna(0),
        "pkts_per_s": (
            (d["orig_pkts"] + d["resp_pkts"]) / total_s
        ).fillna(0),
        "syn_count": hist.str.count("[SsHh]"),
        "rst_count": hist.str.count("[Rr]"),
        "fin_count": hist.str.count("[Ff]"),
    })

    return out

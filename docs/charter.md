Problem

Signature-based IDS tools such as Snort and Suricata miss unknown attacks, and

many ML-based detectors are black boxes that analysts cannot trust or verify.



Goal

Build an ML layer on top of Zeek network logs that detects malicious traffic and

explains every alert in plain terms, with a one-command Docker setup anyone can

run.



In scope for v1.0

Flow-based detection from Zeek logs and PCAP replay

Four attack families: port scan, brute force, DoS, web

attacks

Supervised model plus an anomaly model

Per-alert explanations (SHAP)

Simple dashboard and JSON alert output

Honest cross-dataset evaluation report



Out of scope for v1.0

Blocking traffic (IPS mode)

Inspecting encrypted payloads

Deep learning on raw packets

Host-based detection

Multi-sensor or distributed deployment


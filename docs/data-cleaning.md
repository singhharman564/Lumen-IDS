\# Lumen IDS — CIC-IDS2017 Data Cleaning



\## Dataset

The CIC-IDS2017 MachineLearningCVE CSV files were combined and reduced to the 11 shared network traffic features.



\## Label mapping

The original labels were grouped into benign, portscan, bruteforce, dos, web, and other. The other category was excluded from the first version.



\## Cleaning procedure

1\. Converted shared features to numeric values.

2\. Replaced infinite values with missing values.

3\. Removed other attack categories.

4\. Removed rows with missing values.

5\. Removed duplicate feature-and-label rows.

6\. Checked for identical feature combinations with conflicting labels.

7\. Added the binary is\_attack label.



\## Cleaning results

\- Initial rows: TO FILL

\- Other-class rows removed: TO FILL

\- Missing/infinite rows removed: TO FILL

\- Duplicate rows removed: TO FILL

\- Final rows: TO FILL

\- Conflicting feature combinations: TO FILL



\## Train/test split limitation

The MachineLearningCVE files used in this stage do not provide the timestamps required for a time-based split. The initial random train/test split may produce optimistic results because near-identical flows can appear in both sets.



Later evaluation will use timestamped GeneratedLabelledFlows data and cross-dataset testing.



\## Output

The cleaned dataset is saved locally as data/processed/cic\_common.pkl.


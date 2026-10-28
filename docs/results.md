Lumen IDS — Random Forest Baseline Results



1\. Experimental setup



Dataset: CIC-IDS2017 MachineLearningCVE



Model: Random Forest



Train/test split: 70% training, 30% testing



Random state: 42



Stratification: Enabled



Evaluation: Five-class classification



The split is random, so results may be optimistic because similar flows from the same attacks can appear in both training and test sets.



2\. Results



Overall metrics



False alarm rate: 0.36% (1,985 of 558,225 benign test flows)



Attack detection rate: 99.46%



Per-class results



Class



Precision



Recall



Notes



Benign



FILL IN



FILL IN



Review confusion matrix



Brute force



FILL IN



FILL IN



Strong reported performance



DoS



FILL IN



FILL IN



Strong reported performance



PortScan



FILL IN



FILL IN



Strong reported performance



Web attacks



0.16



0.35



Weak performance



Note: Verify these figures against the final classification report generated after removing is\_attack from the model inputs.



3\. Web attack limitation



Web attack detection is weak. Of 627 web attack test flows, 217 were correctly classified, while 404 were classified as benign. The model also incorrectly classified 1,149 benign flows as web attacks.



The 11 flow-level features do not include HTTP payload content, which may limit the model's ability to distinguish web attacks from benign web traffic.



The project target of at least 90% recall for every attack family is not met for web attacks. This limitation must be reported honestly.



4\. False alarms and real-world base rates



The measured false alarm rate is below the project's 1% target on this test set. However, a real network may have a much larger proportion of benign traffic, so the real-world alert precision may be lower.



5\. Feature importance and leakage correction



An initial experiment included is\_attack, a label derived from family. This was target leakage. The model was retrained after removing is\_attack from the input features.



Record the final top features and the results of the ablation tests here after verification.



6\. Limitations and next steps



Random splitting may produce optimistic results.



Evaluate on separately captured lab traffic.



Test performance without syn\_count, rst\_count, and fin\_count.



Test performance without dst\_port.



Compare results using cross-dataset evaluation in Phase 4.



The model is an initial baseline and has not yet been demonstrated to generalise to unseen network environments.


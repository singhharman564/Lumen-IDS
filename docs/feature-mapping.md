Lumen IDS — Feature Mapping (D1)



Purpose



This document describes how common network-flow features are mapped between CIC-IDS2017 and Zeek conn.log for the first Lumen IDS baseline.



Feature mapping



Common feature



CIC-IDS2017 source



Zeek source / calculation



Known difference



dst\_port



Destination Port



id.resp\_p



Check flow direction and destination-port consistency.



duration\_us



Flow Duration



duration \* 1,000,000



CIC uses microseconds; Zeek duration is in seconds.



fwd\_pkts



Total Fwd Packets



orig\_pkts



Flow direction may differ between sources.



bwd\_pkts



Total Backward Packets



resp\_pkts



Flow direction may differ between sources.



fwd\_bytes



Total Length of Fwd Packets



orig\_bytes



Confirm byte-count definitions.



bwd\_bytes



Total Length of Bwd Packets



resp\_bytes



Confirm byte-count definitions.



bytes\_per\_s



Flow Bytes/s



(orig\_bytes + resp\_bytes) / duration



Zero duration must be handled; definitions may differ.



pkts\_per\_s



Flow Packets/s



(orig\_pkts + resp\_pkts) / duration



Zero duration must be handled; definitions may differ.



syn\_count



SYN Flag Count



Approximate from Zeek history



History is not an exact packet count.



rst\_count



RST Flag Count



Approximate from Zeek history



History is not an exact packet count.



fin\_count



FIN Flag Count



Approximate from Zeek history



History is not an exact packet count.



Missing values and conversion rules



Convert numeric Zeek fields to numbers and replace missing values with zero where appropriate.



Convert Zeek duration from seconds to microseconds.



Handle zero-duration flows when calculating rates to avoid division by zero.



Replace infinite rate values in CIC data with missing values before further processing.



Known limitations



Zeek conn.log does not directly provide all CIC-IDS2017 flow features. In particular, inter-arrival times, packet-length statistics (minimum, maximum, mean and standard deviation), TCP window sizes, and active/idle times are not directly available from the connection log.



The SYN, RST and FIN values derived from history are approximations, not guaranteed equivalents to CIC packet-flag counts.



Validation status



The mappings above are the initial D1 proposal. The feature comparisons in notebooks/03\_feature\_mapping.ipynb must be run and reviewed before the mapping is considered validated.



Record any mismatches discovered in the notebook and update this document with the final decisions.


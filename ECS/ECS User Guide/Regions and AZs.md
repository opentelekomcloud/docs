## Regions and AZs

A region is a geographic area where resources used by your ECSs are located.

ECSs in the same region can communicate with each other over an intranet, but
ECSs in different regions cannot.

Public cloud data centers are deployed worldwide in places, such as North
America, Europe, and Asia. Creating ECSs in different regions can better suit
certain user requirements. For example, applications can be designed to meet
user requirements in specific regions or comply with local laws or regulations.
ECS pricing also changes based on region.

Each region contains many availability zones (AZs) where power and networks are
physically isolated. AZs in the same region can communicate with each other over
an intranet. Each AZ provides cost-effective and low-latency network connections
that are unaffected by faults that may occur in other AZs.

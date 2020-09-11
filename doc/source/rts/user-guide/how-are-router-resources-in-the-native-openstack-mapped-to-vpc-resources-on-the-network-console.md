# How Are Router Resources in the Native OpenStack Mapped to VPC Resources on the Network Console?<a name="EN-US_TOPIC_0078604096"></a>

## Symptom<a name="section5894531922323"></a>

The router ID cannot be found on the network console when you create a VPC stack using a template.

## Solution<a name="section5588912223250"></a>

RTS uses the localized OpenStack network model, including routers, networks, and subnets. The router, router ID, network, and network ID are respectively mapped to the VPC, VPC ID, subnet, and network ID of the VPC service on the network console.


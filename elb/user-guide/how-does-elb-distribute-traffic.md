# How Does ELB Distribute Traffic?<a name="EN-US_TOPIC_0115500495"></a>

For public network load balancers, Linux Virtual Server \(LVS\) uses FullNAT to forward the packets. As shown in the following figures, for Layer-4 protocols, packets are forwarded through LVS. For Layer-7 protocols, packets are forwarded to LVS and then to Nginx.

**Figure  1**  Load balancing at Layer 4<a name="en-us_topic_0100578533_fig41212694173712"></a>  
![](figures/load-balancing-at-layer-4.jpg "load-balancing-at-layer-4")

**Figure  2**  Load balancing at Layer 7<a name="en-us_topic_0100578533_fig15312593173922"></a>  
![](figures/load-balancing-at-layer-7.jpg "load-balancing-at-layer-7")


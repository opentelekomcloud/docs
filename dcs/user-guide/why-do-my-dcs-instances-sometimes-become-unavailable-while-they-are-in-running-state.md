# Why Do My DCS Instances Sometimes Become Unavailable While They Are in Running State?<a name="EN-US_TOPIC_0237964751"></a>

The most probable cause is a network fault. To locate the fault, perform the following steps:

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  Click the name of the unavailable DCS instance. On the  **Summary**  tab page, click  **View**  next to  **Monitoring Metrics**.
6.  View monitoring metrics of the DCS instance.
    -   If monitoring metrics change dramatically over a certain period of time, a network fault has occurred. After the network administrator rectifies the problem, reconnect to the DCS instance or perform management operations on the DCS instance again.
    -   If all monitoring metrics fall within the acceptable range, contact technical support.



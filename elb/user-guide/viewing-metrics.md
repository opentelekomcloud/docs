# Viewing Metrics<a name="EN-US_TOPIC_0107378003"></a>

## Scenarios<a name="en-us_topic_0107076897_section55018171144953"></a>

Cloud Eye is a monitoring service, which allows you to monitor your resources, including load balancers.

There is a short time delay between transmission and display of monitoring data, so the status of each load balancer displayed on the Cloud Eye dashboard at any given time is not its real-time status. For a newly created load balancer, you need to wait for about 5 minutes to 10 minutes before you can view its metrics.

## Prerequisites<a name="en-us_topic_0107076897_section13866854145025"></a>

-   The load balancer to be monitored is running properly.

    If backend servers are stopped, faulty, or deleted, no monitoring data is displayed. 

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Cloud Eye stops monitoring a load balancer and removes it from the monitored object list if its backend servers have been deleted or are in stopped or faulty state for over 24 hours. However, the configured alarm rules will not be automatically deleted.  

-   You have interconnected ELB with Cloud Eye by configuring an alarm rule for the load balancer to be monitored on the Cloud Eye console.

    Without alarm rules configured, there is no monitoring data. For details, see  [Setting an Alarm Rule](setting-an-alarm-rule.md).


## Procedure<a name="en-us_topic_0107076897_section12778912145219"></a>

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Cloud Eye**.
3.  In the navigation pane on the left, choose  **Cloud Service Monitoring**  \>  **Elastic Load Balancing**.
4.  Locate the target load balancer and click  **View Metric**.


# Viewing Metrics<a name="en-us_elb_08_0003"></a>

## Scenarios<a name="en-us_topic_0107076897_section55018171144953"></a>

You can view the metrics of load balancers on the Cloud Eye dashboard.

There is a short time delay between transmitting and displaying data from monitored metrics, so the status of each load balancer displayed on the Cloud Eye dashboard at any given time is not its real-time status. For a newly created load balancer, you need to wait for about 5 minutes to 10 minutes before you can wait its monitoring data.

## Prerequisites<a name="en-us_topic_0107076897_section13866854145025"></a>

-   The target load balancer is running properly.

    No stopped, faulty, or deleted load balancers are displayed on Cloud Eye.

    > ![](public_sys-resources/icon-note.gif) **NOTE:** 

    > Cloud Eye stops monitoring load balancers that remain in stopped or faulty state for over 24 hours and removes them from the monitored object list. However, the alarm rules for those removed load balancers will not be automatically deleted.

-   You have configured alarm rules for the load balancer.

    Monitoring data is unavailable without alarm rules configured in Cloud Eye. For details, see  [Setting an Alarm Rule](setting-an-alarm-rule.md).


## Procedure<a name="en-us_topic_0107076897_section12778912145219"></a>

1.  Log in to the management console.
2.  Under  **Management & Deployment**, click  **Cloud Eye**.
3.  In the navigation pane on the left, choose  **Cloud Service Monitoring**  \>  **Elastic Load Balance**  in the  **Operation**  column.
4.  Locate the target load balancer and click  **View Monitoring Graph**.


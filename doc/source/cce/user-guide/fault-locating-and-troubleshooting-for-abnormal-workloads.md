# Fault Locating and Troubleshooting for Abnormal Workloads<a name="cce_faq_00134"></a>

If a workload is running improperly, you can view events to determine the cause and rectify the fault by referring to  [Common Issues and Solutions](#en-us_topic_0242566249_en-us_topic_0179003348_section1110784004410).

On the CCE console, choose  **Workloads**  \>  **Deployments**  or  **StatefulSets**  in the navigation pane and click the name of the faulty workload. On the workload details page, view the workload events.

## Viewing events<a name="en-us_topic_0242566249_section13566155892120"></a>

1.  Log in to the CCE console. In the navigation pane on the left, choose  **Workloads**  \>  **Deployments**  or  **Workloads**  \>  **StatefulSets**.
2.  In the workload list, click the name of the abnormal workload.
3.  On the  **Pods**  tab page, view the latest workload events.

## Common Issues and Solutions<a name="en-us_topic_0242566249_en-us_topic_0179003348_section1110784004410"></a>

-   [Failed to Schedule an Instance](failed-to-schedule-an-instance.md#cce_faq_00098)
-   [Failed to Pull an Image](failed-to-pull-an-image.md#cce_faq_00015)
-   [Failed to Restart a Container](failed-to-restart-a-container.md#cce_faq_00018)
-   [What Should I Do If An Evicted Pod Exists?](what-should-i-do-if-an-evicted-pod-exists.md#cce_faq_00209)
-   [Instance Eviction Exception](instance-eviction-exception.md#cce_faq_00140)
-   [What Should I Do If Pods in the Terminating State Cannot Be Deleted?](what-should-i-do-if-pods-in-the-terminating-state-cannot-be-deleted.md#cce_faq_00210)
-   [What Should I Do If a Workload Is Stopped Caused by Pod Deletion?](what-should-i-do-if-a-workload-is-stopped-caused-by-pod-deletion.md#cce_faq_00012)
-   [What Should I Do If Sandbox-Related Errors Are Reported When the Pod Remains in the Creating State?](what-should-i-do-if-sandbox-related-errors-are-reported-when-the-pod-remains-in-the-creating-state.md#cce_faq_00005)
-   [What Should I Do If a Pod Is in the Evicted State?](what-should-i-do-if-a-pod-is-in-the-evicted-state.md#cce_faq_00199)
-   [What Should I Do If the OOM Killer Is Triggered When a Container Uses Memory Resources More Than Limited?](what-should-i-do-if-the-oom-killer-is-triggered-when-a-container-uses-memory-resources-more-than-lim.md#cce_faq_00002)


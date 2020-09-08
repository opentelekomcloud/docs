# What Should I Do If a Workload Is Stopped Caused by Pod Deletion?<a name="cce_faq_00012"></a>

## Cause:<a name="en-us_topic_0242566256_section119544513389"></a>

The  **metadata.enable**  field in the YAML file of the workload is  **false**. As a result, the pod of the workload is deleted and the workload is in the stopped status.

![](figures/metadata-enable.png)

## Problem<a name="en-us_topic_0242566256_section1987919184112"></a>

The workload status is  **Stopped**.

## Solution<a name="en-us_topic_0242566256_section3431151713415"></a>

Delete the  **enable**  field or set it to  **true**.


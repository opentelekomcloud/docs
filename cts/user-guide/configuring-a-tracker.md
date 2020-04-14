# Configuring a Tracker<a name="en-us_topic_0059288681"></a>

## Scenarios<a name="section44745431173049"></a>

You can configure the OBS storage for a created tracker.

If you configure an OBS bucket for a tracker, CTS will automatically add a policy to the configured OBS bucket so that trace files can be delivered to the OBS bucket for storage. A prefix can be customized to mark trace files to be dumped. This prefix is automatically added in front of the name of a dumped file, helping you quickly filter out files.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You must select a standard OBS bucket because CTS needs to frequently access the OBS bucket that stores traces.  

After a tracker is configured, new rules take effect immediately.

This section describes how to configure a tracker.

## Prerequisites<a name="section13948718173426"></a>

CTS has been enabled.

## Procedure<a name="section3571284110915"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Click  **Tracker**  in the left pane.
5.  Click  **Configure**  in the  **Operation**  column.

    You must select an OBS bucket for storing trace files and specify the file prefix.

6.  Click  **OK**.

    After the tracker is configured, you can view its details on the  **Tracker**  page.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Traces recorded by CTS are periodically delivered to the OBS bucket for storage. If you configure an OBS bucket for the tracker, traces generated during the current period \(generally several minutes\) will be delivered to the configured OBS bucket. For example, if the current period is from 12:00 to 12:05 and you configure an OBS bucket for the tracker at 12:02, traces received from 12:00 to 12:02 will be delivered to the configured OBS bucket for storage at 12:05.  



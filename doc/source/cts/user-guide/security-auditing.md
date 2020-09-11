# Security Auditing<a name="en-us_topic_0043371377"></a>

## Scenarios<a name="section29070389181456"></a>

This section describes how to query records matching a specified characteristic and to perform security analysis on records of operations to check whether the operations are performed by authorized users.

## Prerequisites<a name="section15151415181756"></a>

You have enabled CTS and the tracker is normal. For details about how to enable CTS, see  [Enabling CTS](enabling-cts.md).

## Procedure<a name="section48879286181857"></a>

The following steps take the creation and deletion of EVS disks in the last two weeks as an example:

1.  Log in to the management console using the administrator account.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner to select the desired region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  <a name="li8526497437"></a>On the trace list page, click  **Filter**. In the displayed box, specify  **Trace Source**,  **Resource Type**, and  **Search By**, and click  **Query**  to query the specified traces.

    For example, you can select  **EVS**  for  **Trace Source**,  **evs**  for  **Resource Type**, and  **Trace name**  for  **Search By**, select  **createVolume**  or  **deleteVolume**  in the right text box, and click  **Query**  to query all creation or deletion operations performed on EVS in the last seven days.

6.  Choose  **Tracker**  from the left pane to switch to the  **Tracker**  page and obtain the OBS bucket name.
7.  Download archived or all trace files by following the instructions in  [Querying Archived Traces](querying-archived-traces.md).
8.  <a name="li38255771182015"></a>In the trace files, search traces using keywords  **createVolume**  or  **deleteVolume**.
9.  Obtain information about the user who performs the operation from the results in  [5](#li8526497437)  and  [8](#li38255771182015). Check whether the user performs any unauthorized operation or any operation that does not conform to the security operation rules.


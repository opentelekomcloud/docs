# ALM-14010 NameService Service Is Abnormal<a name="EN-US_TOPIC_0125375647"></a>

## Description<a name="sf396ed86a1d341e3a96284ce906f3cbd"></a>

The system checks the NameService service status every 180 seconds. This alarm is generated when the NameService service is unavailable and is cleared when the NameService service recovers.

## Attribute<a name="s53ebce3aa797443ea41308b8f90bd7e4"></a>

<a name="en-us_topic_0035998729_table56165728"></a>
<table><thead align="left"><tr id="en-us_topic_0035998729_row23522831"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998729_p26301173"><a name="en-us_topic_0035998729_p26301173"></a><a name="en-us_topic_0035998729_p26301173"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998729_p50020275"><a name="en-us_topic_0035998729_p50020275"></a><a name="en-us_topic_0035998729_p50020275"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998729_p25110514"><a name="en-us_topic_0035998729_p25110514"></a><a name="en-us_topic_0035998729_p25110514"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998729_row20685786"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998729_p64935954"><a name="en-us_topic_0035998729_p64935954"></a><a name="en-us_topic_0035998729_p64935954"></a>14010</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998729_p25320898"><a name="en-us_topic_0035998729_p25320898"></a><a name="en-us_topic_0035998729_p25320898"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998729_p37726867"><a name="en-us_topic_0035998729_p37726867"></a><a name="en-us_topic_0035998729_p37726867"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s7e216992e431486da8bd099754606604"></a>

<a name="en-us_topic_0035998729_table35977388"></a>
<table><thead align="left"><tr id="en-us_topic_0035998729_row30639779"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998729_p65903005"><a name="en-us_topic_0035998729_p65903005"></a><a name="en-us_topic_0035998729_p65903005"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998729_p36543171"><a name="en-us_topic_0035998729_p36543171"></a><a name="en-us_topic_0035998729_p36543171"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998729_row7206911"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998729_p46888886"><a name="en-us_topic_0035998729_p46888886"></a><a name="en-us_topic_0035998729_p46888886"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998729_p39903442"><a name="en-us_topic_0035998729_p39903442"></a><a name="en-us_topic_0035998729_p39903442"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998729_row23586666"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998729_p31471768"><a name="en-us_topic_0035998729_p31471768"></a><a name="en-us_topic_0035998729_p31471768"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998729_p66185246"><a name="en-us_topic_0035998729_p66185246"></a><a name="en-us_topic_0035998729_p66185246"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998729_row58796306"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998729_p64880336"><a name="en-us_topic_0035998729_p64880336"></a><a name="en-us_topic_0035998729_p64880336"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998729_p20815867"><a name="en-us_topic_0035998729_p20815867"></a><a name="en-us_topic_0035998729_p20815867"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998729_row53125076"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998729_p8163917"><a name="en-us_topic_0035998729_p8163917"></a><a name="en-us_topic_0035998729_p8163917"></a>NSName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998729_p57297510"><a name="en-us_topic_0035998729_p57297510"></a><a name="en-us_topic_0035998729_p57297510"></a>Specifies the name of NameService for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s97dee073270d45c1a9a2c30416331ddd"></a>

HDFS fails to provide services for upper-layer components based on the NameService service, such as HBase and MapReduce. As a result, users cannot read or write files.

## Possible Causes<a name="s8a29f0ca6ddd436792b876b23b015ae1"></a>

-   The JournalNode is faulty.
-   The DataNode is faulty.
-   The disk capacity is insufficient.
-   The NameNode enters safe mode.

## Procedure<a name="s89caee6c4ead4e0fba642244179ef373"></a>

1.  Check the status of the JournalNode instance.
    1.  On the MRS Manager portal, click  **Service**.
    2.  Click  **HDFS**.
    3.  Click  **Instance**.
    4.  Check whether the  **Health Status** of the JournalNode is **Good**.
        -   If yes, go to  [2.a](#lf737e34272ab46a8adcb8a33ae6cfd3c).
        -   If no, go to  [1.e](#lb3ccb889a90041be81a135ecc2522bd5).

    5.  <a name="lb3ccb889a90041be81a135ecc2522bd5"></a>Select the faulty JournalNode and choose  **More**  \>  **Restart Instance**. Check whether the JournalNode successfully restarts.
        -   If yes, go to  [1.f](#lb370a24204ee41feaca303b8983cf35e).
        -   If no, go to  [5](#lffb881ae8d2045898cff4e02160c32d2).

    6.  <a name="lb370a24204ee41feaca303b8983cf35e"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#lf737e34272ab46a8adcb8a33ae6cfd3c).

2.  Check the status of the DataNode instance.
    1.  <a name="lf737e34272ab46a8adcb8a33ae6cfd3c"></a>On the MRS Manager portal, click  **Service**.
    2.  Click  **HDFS**.
    3.  In  **Operation and Health Summary**, check whether the **Health Status** of all DataNodes is **Good**.
        -   If yes, go to  [3.a](#l0574fdcbcb6a43798eafa36eb0262ca7).
        -   If no, go to  [2.d](#la045be2dc22a49a2b8f5ca4fe2e099e9).

    4.  <a name="la045be2dc22a49a2b8f5ca4fe2e099e9"></a>Click  **Instance**. On the DataNode management page, select the faulty DataNode, and choose **More**  \>  **Restart Instance**. Check whether the DataNode successfully restarts.
        -   If yes, go to  [2.e](#l21fa368ed5df44d98ac5362ce11630b9).
        -   If no, go to  [3.a](#l0574fdcbcb6a43798eafa36eb0262ca7).

    5.  <a name="l21fa368ed5df44d98ac5362ce11630b9"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#en-us_topic_0035998729_step28).

3.  Check disk status.
    1.  <a name="l0574fdcbcb6a43798eafa36eb0262ca7"></a>On the MRS Manager portal, click  **Host**.
    2.  In the  **Disk Usage**  column, check whether disk space is insufficient.
        -   If yes, go to  [3.c](#la97aa975be0a47d18dff504b6940c846).
        -   If no, go to  [4.a](#en-us_topic_0035998729_step28).

    3.  <a name="la97aa975be0a47d18dff504b6940c846"></a>Expand the disk capacity.
    4.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#en-us_topic_0035998729_step28).

4.  Check whether NameNode is in safe mode.
    1.  <a name="en-us_topic_0035998729_step28"></a>Use the client on the cluster node, and run the  **hdfs dfsadmin -safemode get** command to check whether **Safe mode is ON**  is displayed.

        Information after  **Safe mode is ON**  is alarm information and is displayed based on actual conditions.

        -   If yes, go to  [4.b](#en-us_topic_0035998729_li66373591).
        -   If no, go to  [5](#lffb881ae8d2045898cff4e02160c32d2).

    2.  <a name="en-us_topic_0035998729_li66373591"></a>Use the client on the cluster node and run the  **hdfs dfsadmin -safemode leave**  command.
    3.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#lffb881ae8d2045898cff4e02160c32d2).

5.  <a name="lffb881ae8d2045898cff4e02160c32d2"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s3477ef344abd4082a61873c12734c4f9"></a>

N/A


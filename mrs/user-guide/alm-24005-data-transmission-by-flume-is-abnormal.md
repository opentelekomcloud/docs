# ALM-24005 Data Transmission by Flume Is Abnormal<a name="EN-US_TOPIC_0125375498"></a>

## Description<a name="sa924c77a6c754720bd983b4a1c602436"></a>

The alarm module monitors the capacity of Flume channels. This alarm is generated when the duration that a channel is full or the number of times that a source fails to send data to the channel exceeds the threshold.

Users can set the threshold as required by modifying the  **channelfullcount**  parameter.

This alarm is cleared when the channel space is released.

## Attribute<a name="s17042fec9cd3462ebde11b7754b70466"></a>

<a name="t327f51589b8b48979303e96e02f536ca"></a>
<table><thead align="left"><tr id="r9c002133f3fe4ca0b9ded73415ffc4b6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a42d5a157bc924bd4b87bb6bad5c9d052"><a name="a42d5a157bc924bd4b87bb6bad5c9d052"></a><a name="a42d5a157bc924bd4b87bb6bad5c9d052"></a><strong id="a94eb0521aab64a57b4c0e711b8e90a5a"><a name="a94eb0521aab64a57b4c0e711b8e90a5a"></a><a name="a94eb0521aab64a57b4c0e711b8e90a5a"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a79afc991abf84975a111bf426f016935"><a name="a79afc991abf84975a111bf426f016935"></a><a name="a79afc991abf84975a111bf426f016935"></a><strong id="aa1cd744921fd4dec8192ee52d3fcb3d4"><a name="aa1cd744921fd4dec8192ee52d3fcb3d4"></a><a name="aa1cd744921fd4dec8192ee52d3fcb3d4"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="aa684215dcf934b009a52933c11d12f37"><a name="aa684215dcf934b009a52933c11d12f37"></a><a name="aa684215dcf934b009a52933c11d12f37"></a><strong id="abaf40e5d41e2475e89a90566084a8768"><a name="abaf40e5d41e2475e89a90566084a8768"></a><a name="abaf40e5d41e2475e89a90566084a8768"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra3d0ea5611954e988a9e89c151aa3012"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a73538f346ef0426e9a0f54c1ffe79394"><a name="a73538f346ef0426e9a0f54c1ffe79394"></a><a name="a73538f346ef0426e9a0f54c1ffe79394"></a>24005</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a76d9bc9557264b4ca7fe393a893e6e62"><a name="a76d9bc9557264b4ca7fe393a893e6e62"></a><a name="a76d9bc9557264b4ca7fe393a893e6e62"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a0c8a2bbabfc7430c9903a0a5e912ff5f"><a name="a0c8a2bbabfc7430c9903a0a5e912ff5f"></a><a name="a0c8a2bbabfc7430c9903a0a5e912ff5f"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s63b0b7620fe047c69e0b92442b1db2cd"></a>

<a name="t9fd0a555813448489155204854db5e3a"></a>
<table><thead align="left"><tr id="rf43cf0d863fb4ee2af9c7e454f9b057d"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a9e72ae4c5c7b431a8cf56102d33a20b3"><a name="a9e72ae4c5c7b431a8cf56102d33a20b3"></a><a name="a9e72ae4c5c7b431a8cf56102d33a20b3"></a><strong id="adc75e1faa6554903ad1bc4d63fb4cdea"><a name="adc75e1faa6554903ad1bc4d63fb4cdea"></a><a name="adc75e1faa6554903ad1bc4d63fb4cdea"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="afc54c398691b4ac88a3244637448ad02"><a name="afc54c398691b4ac88a3244637448ad02"></a><a name="afc54c398691b4ac88a3244637448ad02"></a><strong id="a1b984b53728f442198fcbf446e7f3785"><a name="a1b984b53728f442198fcbf446e7f3785"></a><a name="a1b984b53728f442198fcbf446e7f3785"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r85a1073f49bc42a8a05bf9bd785ace7c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a98e6f5bab40e4cfda1e020c50badc35d"><a name="a98e6f5bab40e4cfda1e020c50badc35d"></a><a name="a98e6f5bab40e4cfda1e020c50badc35d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5701b5334f3a43d6bf1b6addb93e76a8"><a name="a5701b5334f3a43d6bf1b6addb93e76a8"></a><a name="a5701b5334f3a43d6bf1b6addb93e76a8"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9ac5d06fc7a04a5882fa3d71eedd7b88"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3e9edc5aa7884f66b9d09b407505df4d"><a name="a3e9edc5aa7884f66b9d09b407505df4d"></a><a name="a3e9edc5aa7884f66b9d09b407505df4d"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a50050912cec74250915889a0f8a846a0"><a name="a50050912cec74250915889a0f8a846a0"></a><a name="a50050912cec74250915889a0f8a846a0"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r844458e7f40c4eb5a97de961df024bbd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a55c832143ab843ebba1395dc95184d8b"><a name="a55c832143ab843ebba1395dc95184d8b"></a><a name="a55c832143ab843ebba1395dc95184d8b"></a>ComponentType</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a44a2e3b7c7f94633a758ab6bc9ee26ae"><a name="a44a2e3b7c7f94633a758ab6bc9ee26ae"></a><a name="a44a2e3b7c7f94633a758ab6bc9ee26ae"></a>Specifies the component type for which the alarm is generated.</p>
</td>
</tr>
<tr id="ree5b87d5e38c46728aa90b910f1e9215"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1e3a5a07b598457bb36bf146d708c3b7"><a name="a1e3a5a07b598457bb36bf146d708c3b7"></a><a name="a1e3a5a07b598457bb36bf146d708c3b7"></a>ComponentName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a78e0055ab48948b4807cbf9af6db3883"><a name="a78e0055ab48948b4807cbf9af6db3883"></a><a name="a78e0055ab48948b4807cbf9af6db3883"></a>Specifies the component name for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sf7e57923ab1b4fff971e1bf216abaa58"></a>

If the usage of the Flume channel continues to grow, the data transmission time increases. When the usage reaches 100%, the Flume agent process is suspended.

## Possible Causes<a name="s08dd3188c73e4fc5820a2ccbbb1e1304"></a>

-   The Flume sink is faulty.
-   The network is faulty.

## Procedure<a name="s7c87a920e8524443b8d55c17f33a5c0d"></a>

1.  Check whether the Flume sink is normal.
    1.  Check whether the Flume sink is the HDFS type.
        -   If yes, go to  [1.b](#l76b9a08043c046ef800538e90ed61e9a).
        -   If no, go to  [1.c](#l74d734b35d234813a09fe04546618064).

    2.  <a name="l76b9a08043c046ef800538e90ed61e9a"></a>On MRS Manager, check whether alarm ALM-14000 HDFS Service Unavailable is reported and whether the HDFS service is stopped.
        -   If the alarm is reported, clear it according to the handling suggestions of ALM-14000 HDFS Service Unavailable; if the HDFS service is stopped, start it. Then go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).
        -   If the alarm is not reported and the HDFS service is running properly, go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).

    3.  <a name="l74d734b35d234813a09fe04546618064"></a>Check whether the Flume sink is the HBase type.
        -   If yes, go to  [1.d](#l15f0135409854225bf17204b6e042dfc).
        -   If no, go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).

    4.  <a name="l15f0135409854225bf17204b6e042dfc"></a>On MRS Manager, check whether alarm ALM-19000 HBase Service Unavailable is reported and whether the HBase service is stopped.
        -   If the alarm is reported, clear it according to the handling suggestions of ALM-19000 HBase Service Unavailable; if the HBase service is stopped, start it. Then go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).
        -   If the alarm is not reported and the HBase service is running properly, go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).

    5.  Check whether the Flume sink is the Kafka type.
        -   If yes, go to  [1.f](#lfd9b68b40cd249a3a587664869efdbfa).
        -   If no, go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).

    6.  <a name="lfd9b68b40cd249a3a587664869efdbfa"></a>On MRS Manager, check whether alarmALM-38000 Kafka Service Unavailable is reported and whether the Kafka service is stopped.
        -   If the alarm is reported, clear it according to the handling suggestions of ALM-38000 Kafka Service Unavailable; if the Kafka service is stopped, start it. Then go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).
        -   If the alarm is not reported and the Kafka service is running properly, go to  [1.g](#l8b76fe1bbc1f40bf8cb64d7d1996866f).

    7.  <a name="l8b76fe1bbc1f40bf8cb64d7d1996866f"></a>On MRS Manager, choose  **Service**  \>  **Flume**  \>  **Instance**.
    8.  Click the Flume instance of the faulty node and check whether the value of the  **Sink Speed Metrics**  is 0.
        -   If yes, go to  [2.a](#l954d20e3b27b4706b3cadfde3a84e4bb).
        -   If no, no further action is required.

2.  Check the status of the network between the Flume sink and faulty node.
    1.  <a name="l954d20e3b27b4706b3cadfde3a84e4bb"></a>Check whether the Flume sink is the avro type.
        -   If yes, go to  [2.c](#l9eb7b59e9cce4e29b3239caaba3c583c).
        -   If no, go to  [3.a](#l3872a25c900442d78c15cb10ac30b3dc).

    2.  Log in to the host where the faulty node resides. Run the following command to switch to user  **root**:

        **sudo su - root**

    3.  <a name="l9eb7b59e9cce4e29b3239caaba3c583c"></a>Run the  **ping** _Flume sink IP address_  command to check whether the Flume sink can be pinged.
        -   If yes, go to  [3.a](#l3872a25c900442d78c15cb10ac30b3dc).
        -   If no, go to  [2.d](#l2b536f6ada734d4ab2c4d00bb4e0e662).

    4.  <a name="l2b536f6ada734d4ab2c4d00bb4e0e662"></a>Contact the network administrator to repair the network.
    5.  Wait for a while and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#l3872a25c900442d78c15cb10ac30b3dc).

3.  Collect fault information.
    1.  <a name="l3872a25c900442d78c15cb10ac30b3dc"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sc26e0a8003e242d1b659d255122ab5a3"></a>

N/A


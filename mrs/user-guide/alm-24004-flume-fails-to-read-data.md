# ALM-24004 Flume Fails to Read Data<a name="EN-US_TOPIC_0125375594"></a>

## Description<a name="s5864b67762bf4f448daf03c830fafc2e"></a>

The alarm module monitors the Flume source status. This alarm is generated when the duration that Flume source fails to read data exceeds the threshold.

Users can modify the threshold as required.

This alarm is cleared when the source reads data successfully.

## Attribute<a name="sd803fab299df494eb52d6e556b80ad93"></a>

<a name="t83b9448095224911b2e3933b3a61cf56"></a>
<table><thead align="left"><tr id="rf72faddc47b0493781b89857d84750d6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a04d9432feaa74677b5dcd10aab95c6af"><a name="a04d9432feaa74677b5dcd10aab95c6af"></a><a name="a04d9432feaa74677b5dcd10aab95c6af"></a><strong id="aff0d287403fe405fa1c7fbd7b74b2980"><a name="aff0d287403fe405fa1c7fbd7b74b2980"></a><a name="aff0d287403fe405fa1c7fbd7b74b2980"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aef15d41ec5c94425a27579451a27be85"><a name="aef15d41ec5c94425a27579451a27be85"></a><a name="aef15d41ec5c94425a27579451a27be85"></a><strong id="a027a9f369a2e472a95dc140f0048c091"><a name="a027a9f369a2e472a95dc140f0048c091"></a><a name="a027a9f369a2e472a95dc140f0048c091"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ac13abcb7e79a47a398dce2f216e55dab"><a name="ac13abcb7e79a47a398dce2f216e55dab"></a><a name="ac13abcb7e79a47a398dce2f216e55dab"></a><strong id="a35ec327d1d41415395334e33942a375a"><a name="a35ec327d1d41415395334e33942a375a"></a><a name="a35ec327d1d41415395334e33942a375a"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r64ff0791cbcf459a900689d8e71920b9"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a3ca1f2505f8c44b79303a98a7a961a53"><a name="a3ca1f2505f8c44b79303a98a7a961a53"></a><a name="a3ca1f2505f8c44b79303a98a7a961a53"></a>24004</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a22bcf0be23e44e5e80ac1eff9387b87a"><a name="a22bcf0be23e44e5e80ac1eff9387b87a"></a><a name="a22bcf0be23e44e5e80ac1eff9387b87a"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="aa041fdfd0ae3466387c9b32156a65922"><a name="aa041fdfd0ae3466387c9b32156a65922"></a><a name="aa041fdfd0ae3466387c9b32156a65922"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s7db98ae9763848e085d958d789f99602"></a>

<a name="t78e7a9dae33b47cca0f5704bfb7529ab"></a>
<table><thead align="left"><tr id="ra9d0c3e29fc2490281e4082684b21894"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a028f07e9fa8c4bc7bee065e8a933ae09"><a name="a028f07e9fa8c4bc7bee065e8a933ae09"></a><a name="a028f07e9fa8c4bc7bee065e8a933ae09"></a><strong id="ad3a0f72d45b14a97a3dfcfd21f279597"><a name="ad3a0f72d45b14a97a3dfcfd21f279597"></a><a name="ad3a0f72d45b14a97a3dfcfd21f279597"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a74633cadf21b49bb9453cdaea0e83429"><a name="a74633cadf21b49bb9453cdaea0e83429"></a><a name="a74633cadf21b49bb9453cdaea0e83429"></a><strong id="ac3fa2d1457ba4e458339102206a78cec"><a name="ac3fa2d1457ba4e458339102206a78cec"></a><a name="ac3fa2d1457ba4e458339102206a78cec"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5a717a0c508c4f71ae7053b0105fc213"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6ea9ca1f6503417c9b52435646685fd9"><a name="a6ea9ca1f6503417c9b52435646685fd9"></a><a name="a6ea9ca1f6503417c9b52435646685fd9"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a512446f6bb014ff88571c19f4c62f3b3"><a name="a512446f6bb014ff88571c19f4c62f3b3"></a><a name="a512446f6bb014ff88571c19f4c62f3b3"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd7f7e46fbc6b42fb83d5f9144ab821d7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a04a831655747472f9e9cfe4664bbfcea"><a name="a04a831655747472f9e9cfe4664bbfcea"></a><a name="a04a831655747472f9e9cfe4664bbfcea"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aee5c574c89f04123acb4f93d34df6923"><a name="aee5c574c89f04123acb4f93d34df6923"></a><a name="aee5c574c89f04123acb4f93d34df6923"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb53d7f0b9e5143358becfd476eb35546"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7bf49b37e8764ce6bb15d7d0e821040b"><a name="a7bf49b37e8764ce6bb15d7d0e821040b"></a><a name="a7bf49b37e8764ce6bb15d7d0e821040b"></a>ComponentType</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a828e4b9759974180a7b2c1d4dbc38133"><a name="a828e4b9759974180a7b2c1d4dbc38133"></a><a name="a828e4b9759974180a7b2c1d4dbc38133"></a>Specifies the component type for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf5454eace6a34639b791e5a177f4c75e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a32f2b63ffa134d65bb3b9d9170fd29b0"><a name="a32f2b63ffa134d65bb3b9d9170fd29b0"></a><a name="a32f2b63ffa134d65bb3b9d9170fd29b0"></a>ComponentName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aead7f3b6cbde4675ab9c0bec0a0317be"><a name="aead7f3b6cbde4675ab9c0bec0a0317be"></a><a name="aead7f3b6cbde4675ab9c0bec0a0317be"></a>Specifies the component name for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sc5e8548109744d409487e258cb6f4c92"></a>

Data collection is stopped.

## Possible Causes<a name="s414423cc0b0f4441b79606a5133d6284"></a>

-   The Flume source is faulty.
-   The network is faulty.

## Procedure<a name="sa9a6706cde254aa6ba51643054ea9dc6"></a>

1.  Check whether the Flume source is normal.
    1.  Check whether the Flume source is the spoolDir type.
        -   If yes, go to  [1.b](#lc94625f4197d42c0b4e48ffc727c9295).
        -   If no, go to  [1.c](#l1042861de2b3420fa56cd7fce29ed986).

    2.  <a name="lc94625f4197d42c0b4e48ffc727c9295"></a>Query the  **spoolDir**  directory and check whether all files have been sent.
        -   If yes, no further action is required.
        -   If no, go to  [1.e](#l9b58accdda3548689e4b58aa9038a8ed).

    3.  <a name="l1042861de2b3420fa56cd7fce29ed986"></a>Check whether the Flume source is the Kafka type.
        -   If yes, go to  [1.d](#l597cb2d4a0a545bfa2f1c817f00a15e9).
        -   If no, go to  [1.e](#l9b58accdda3548689e4b58aa9038a8ed).

    4.  <a name="l597cb2d4a0a545bfa2f1c817f00a15e9"></a>Log in to the Kafka client and run the following commands to check whether all topic data configured for the Kafka source has been consumed.

        **cd /opt/client/Kafka/kafka/bin**

        **./kafka-consumer-groups.sh --bootstrap-server** _Kafka cluster IP address_**:21007** **--new-consumer --describe --group example-group1 --command-config**

        **../config/consumer.properties**

        -   If yes, no further action is required.
        -   If no, go to  [1.e](#l9b58accdda3548689e4b58aa9038a8ed).

    5.  <a name="l9b58accdda3548689e4b58aa9038a8ed"></a>On MRS Manager, choose  **Service**  \>  **Flume**  \>  **Instance**.
    6.  Click the Flume instance of the faulty node and check whether the value of the  **Source Speed Metrics**  is 0.
        -   If yes, go to  [2.a](#l677a2c3f373a453d8e7e6399f82c1085).
        -   If no, no further action is required.

2.  Check the status of the network between the Flume source and faulty node.
    1.  <a name="l677a2c3f373a453d8e7e6399f82c1085"></a>Check whether the Flume source is the avro type.
        -   If yes, go to  [2.c](#l9c6f11e4a33e4feda85d8eeab00fc8cc).
        -   If no, go to  [3.a](#l9898ecad8c1344f9a9294fdc9b05e833).

    2.  Log in to the host where the faulty node resides. Run the following command to switch to user  **root**:

        **sudo su - root**

    3.  <a name="l9c6f11e4a33e4feda85d8eeab00fc8cc"></a>Run the  **ping** _Flume source IP address_  command to check whether the Flume source can be pinged.
        -   If yes, go to  [3.a](#l9898ecad8c1344f9a9294fdc9b05e833).
        -   If no, go to  [2.d](#l691eae4336fe4abe8290e269c614fef7).

    4.  <a name="l691eae4336fe4abe8290e269c614fef7"></a>Contact the network administrator to repair the network.
    5.  Wait for a while and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#l9898ecad8c1344f9a9294fdc9b05e833).

3.  Collect fault information.
    1.  <a name="l9898ecad8c1344f9a9294fdc9b05e833"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sc26f6d630149467b9608c3282a69e06f"></a>

N/A


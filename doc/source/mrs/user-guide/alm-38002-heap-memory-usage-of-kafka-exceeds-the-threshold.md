# ALM-38002 Heap Memory Usage of Kafka Exceeds the Threshold<a name="EN-US_TOPIC_0125375934"></a>

## Description<a name="sa1e13cbd3ecb442e93d43c47444598be"></a>

The system checks the heap memory usage of Kafka every 30 seconds. This alarm is generated when the heap memory usage of Kafka exceeds the threshold \(80%\).

This alarm is cleared when the heap memory usage is lower than the threshold.

## Attribute<a name="s5d78a92c190d4a45944ce7438b06d068"></a>

<a name="t88bf4b3533fa4287bc90a6e0e9bd602e"></a>
<table><thead align="left"><tr id="r20f1437181474bd98613529fe4f6522b"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ab536d18c5049423e99fdb707bb9cb234"><a name="ab536d18c5049423e99fdb707bb9cb234"></a><a name="ab536d18c5049423e99fdb707bb9cb234"></a><strong id="en-us_topic_0053790971_b339495175629"><a name="en-us_topic_0053790971_b339495175629"></a><a name="en-us_topic_0053790971_b339495175629"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aac906056cdff40cc9ce0c346010d25ee"><a name="aac906056cdff40cc9ce0c346010d25ee"></a><a name="aac906056cdff40cc9ce0c346010d25ee"></a><strong id="a61925dd628e1459da30b1301948436ce"><a name="a61925dd628e1459da30b1301948436ce"></a><a name="a61925dd628e1459da30b1301948436ce"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ac18faae725a64d82b1954228a1fb5441"><a name="ac18faae725a64d82b1954228a1fb5441"></a><a name="ac18faae725a64d82b1954228a1fb5441"></a><strong id="a5896f040467146f9a7ca59e2dbd62591"><a name="a5896f040467146f9a7ca59e2dbd62591"></a><a name="a5896f040467146f9a7ca59e2dbd62591"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r27839346a49e4a9f91499da6f92bf809"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a3a51523c694e45ffb094f3921aa08779"><a name="a3a51523c694e45ffb094f3921aa08779"></a><a name="a3a51523c694e45ffb094f3921aa08779"></a>38002</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a8e0a53859b524626813f3f4ac97f0355"><a name="a8e0a53859b524626813f3f4ac97f0355"></a><a name="a8e0a53859b524626813f3f4ac97f0355"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="ab7258c58cb2b45f2a090ef5d76016e8c"><a name="ab7258c58cb2b45f2a090ef5d76016e8c"></a><a name="ab7258c58cb2b45f2a090ef5d76016e8c"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s3dd022c1a3c349b386696f6334e604cb"></a>

<a name="te0bd9b90a401454faa5e1da316925d39"></a>
<table><thead align="left"><tr id="rbc3bf0f875cf4b6181778391ed8e5c77"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="abdb9b0520d7a48fca0ba509a3013daa6"><a name="abdb9b0520d7a48fca0ba509a3013daa6"></a><a name="abdb9b0520d7a48fca0ba509a3013daa6"></a><strong id="a2aa56ba2fea8433c8e2396e464b01f31"><a name="a2aa56ba2fea8433c8e2396e464b01f31"></a><a name="a2aa56ba2fea8433c8e2396e464b01f31"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ad44c366145ed461883a985c87b4b7e23"><a name="ad44c366145ed461883a985c87b4b7e23"></a><a name="ad44c366145ed461883a985c87b4b7e23"></a><strong id="ae920c047ba90485ebdbff1813e324ebf"><a name="ae920c047ba90485ebdbff1813e324ebf"></a><a name="ae920c047ba90485ebdbff1813e324ebf"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r58332a3ffaf44ea4a7b2a950cab2b41f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a48c83a1733784ec2bb27d5044415fdbf"><a name="a48c83a1733784ec2bb27d5044415fdbf"></a><a name="a48c83a1733784ec2bb27d5044415fdbf"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3219e2ad0d644089afdb1d20d5882d50"><a name="a3219e2ad0d644089afdb1d20d5882d50"></a><a name="a3219e2ad0d644089afdb1d20d5882d50"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r47e5f5784bfa45f69f43a6676fb333bd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1aa19103f7ff40b6a7a40a3df121a7fc"><a name="a1aa19103f7ff40b6a7a40a3df121a7fc"></a><a name="a1aa19103f7ff40b6a7a40a3df121a7fc"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8332fe5a926345a88b800c9fd1e556b2"><a name="a8332fe5a926345a88b800c9fd1e556b2"></a><a name="a8332fe5a926345a88b800c9fd1e556b2"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc550d74c45db4ebaac09bb7b586bb040"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0edc9dbdfc474066bd830b829cf62e9e"><a name="a0edc9dbdfc474066bd830b829cf62e9e"></a><a name="a0edc9dbdfc474066bd830b829cf62e9e"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9ed9fa9ba69e43978da58a50035d917d"><a name="a9ed9fa9ba69e43978da58a50035d917d"></a><a name="a9ed9fa9ba69e43978da58a50035d917d"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r5ebd50a1b10c4dd0b2e454e3716effcd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a13fe970f798744eaba1ac8bbfd4a53f6"><a name="a13fe970f798744eaba1ac8bbfd4a53f6"></a><a name="a13fe970f798744eaba1ac8bbfd4a53f6"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aac366373fd384f39ab512622c112fa19"><a name="aac366373fd384f39ab512622c112fa19"></a><a name="aac366373fd384f39ab512622c112fa19"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s96f046c6dc8e4eddaef67ac5e9f61a03"></a>

Memory overflow may occur, causing service crashes.

## Possible Causes<a name="s47f2a6f09d484b5b8bdde0b3f0614f8d"></a>

The heap memory usage is high or the heap memory is improperly allocated.

## Procedure<a name="s77f4e0ff741c4fae8eff68bffc1fef58"></a>

1.  Check the heap memory usage.
    1.  On MRS Manager, choose  **Alarm\> ALM-38002 Heap Memory Usage of Kafka Exceeds the Threshold \> Location**. Query the IP address of the alarmed instance.
    2.  On MRS Manager, choose  **Service \> Kafka \> Instance \> Broker \(corresponding to the IP address of the alarmed instance\) \> Customize \> Kafka Heap Memory Resource Percentage**.
    3.  Check whether the heap memory usage of Kafka has reached the threshold \(80%\).
        -   If yes, go to  [1.d](#l37f4c25ba72b4124a6a90e44ac961b63).
        -   If no, go to  [2](#lf691dbd8a86a4985aa322c7542ad47af).

    4.  <a name="l37f4c25ba72b4124a6a90e44ac961b63"></a>On MRS Manager, choose  **Service \> Kafka \> Service Configuration \> All \> Broker \> Environment**. Increase the value of **KAFKA\_HEAP\_OPTS**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lf691dbd8a86a4985aa322c7542ad47af).

2.  <a name="lf691dbd8a86a4985aa322c7542ad47af"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s9c7a2a34a1c44fc4a1385d1f292bb8dd"></a>

N/A


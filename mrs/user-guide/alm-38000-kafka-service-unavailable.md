# ALM-38000 Kafka Service Unavailable<a name="EN-US_TOPIC_0125375932"></a>

## Description<a name="s9b052d387a6f4625a5b2b9f1a7044671"></a>

The system checks the Kafka service availability every 30 seconds. This alarm is generated when the Kafka service becomes unavailable.

This alarm is cleared after the Kafka service recovers.

## Attribute<a name="se0aba127030947098e9d39bd5114b1d1"></a>

<a name="tf31b9cadb8484d3c954c79dab8e1b06c"></a>
<table><thead align="left"><tr id="r5ca96410d53b49d29bd092efa5f22a40"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="adc9e0efff4bd4460be56ab9d6272cc38"><a name="adc9e0efff4bd4460be56ab9d6272cc38"></a><a name="adc9e0efff4bd4460be56ab9d6272cc38"></a><strong id="a1a8acd92b06f4f028cfd19b480f3c57e"><a name="a1a8acd92b06f4f028cfd19b480f3c57e"></a><a name="a1a8acd92b06f4f028cfd19b480f3c57e"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="af7d103c7d09d4db5b942de18a15f4040"><a name="af7d103c7d09d4db5b942de18a15f4040"></a><a name="af7d103c7d09d4db5b942de18a15f4040"></a><strong id="a652202ef873549fea57b71559e430d74"><a name="a652202ef873549fea57b71559e430d74"></a><a name="a652202ef873549fea57b71559e430d74"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a8e45acc306c743f280fe5d441e90adb5"><a name="a8e45acc306c743f280fe5d441e90adb5"></a><a name="a8e45acc306c743f280fe5d441e90adb5"></a><strong id="aaf76956bea854dabb8ad72ea7bacfe94"><a name="aaf76956bea854dabb8ad72ea7bacfe94"></a><a name="aaf76956bea854dabb8ad72ea7bacfe94"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r30bf01d5151949c08218600349b7f6ed"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a7d1f727ebec04d53b12b79dc962cff38"><a name="a7d1f727ebec04d53b12b79dc962cff38"></a><a name="a7d1f727ebec04d53b12b79dc962cff38"></a>38000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a7091e3ea086f44ae824a592a64945955"><a name="a7091e3ea086f44ae824a592a64945955"></a><a name="a7091e3ea086f44ae824a592a64945955"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a7274355ac0304a098d7377f1c75e589d"><a name="a7274355ac0304a098d7377f1c75e589d"></a><a name="a7274355ac0304a098d7377f1c75e589d"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s17a35505f45945378a58d9258ab017da"></a>

<a name="t7de1a3442cbf445b82b9a8dc62c91349"></a>
<table><thead align="left"><tr id="rba4ea114d35249e7a7a4fe627c1b8c42"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="aeac8bf8664be48b6bb8b32f13d175d3d"><a name="aeac8bf8664be48b6bb8b32f13d175d3d"></a><a name="aeac8bf8664be48b6bb8b32f13d175d3d"></a><strong id="a04abab9a883e43c4b81da26227564642"><a name="a04abab9a883e43c4b81da26227564642"></a><a name="a04abab9a883e43c4b81da26227564642"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="af6ec9b9d9b8f4c73889ac5e40e990c4e"><a name="af6ec9b9d9b8f4c73889ac5e40e990c4e"></a><a name="af6ec9b9d9b8f4c73889ac5e40e990c4e"></a><strong id="aaff762aa53c0486aa0fa7e12d59da802"><a name="aaff762aa53c0486aa0fa7e12d59da802"></a><a name="aaff762aa53c0486aa0fa7e12d59da802"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rfa84e4f9dd97445e92a688f3822eff73"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a00fde034c87e4f7c97324ada9b66a986"><a name="a00fde034c87e4f7c97324ada9b66a986"></a><a name="a00fde034c87e4f7c97324ada9b66a986"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a54dd855dcd284a668e387da4c38ebdce"><a name="a54dd855dcd284a668e387da4c38ebdce"></a><a name="a54dd855dcd284a668e387da4c38ebdce"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd3f9fa531b8f4b73b4042e8e88572d2f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a64a9fa9e63184491a89f39971d310393"><a name="a64a9fa9e63184491a89f39971d310393"></a><a name="a64a9fa9e63184491a89f39971d310393"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a243f14a736c041ce826013932812489e"><a name="a243f14a736c041ce826013932812489e"></a><a name="a243f14a736c041ce826013932812489e"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc5a3ed78e72746e18e5b1dd35ac5d972"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa739ffd9f36b4221862a41f60339fcfa"><a name="aa739ffd9f36b4221862a41f60339fcfa"></a><a name="aa739ffd9f36b4221862a41f60339fcfa"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0b6f2fd048a14738837db03e669859c9"><a name="a0b6f2fd048a14738837db03e669859c9"></a><a name="a0b6f2fd048a14738837db03e669859c9"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8d87e2fda9ae4bd58533c3c155c1f22a"></a>

The cluster cannot provide the Kafka service and users cannot run new Kafka tasks.

## Possible Causes<a name="s01040495e7cf4b1089a0d36947254348"></a>

-   The KrbServer component is faulty.
-   The ZooKeeper component is faulty or fails to respond.
-   The Broker node in the Kafka cluster is abnormal.

## Procedure<a name="s16ebbbd546454c7ab6eb1f7af3f8684c"></a>

1.  Check the KrbServer component status. For clusters without Kerberos authentication, skip this step and go to  [2](#l8a4f460f221f49469938544acd759b25).
    1.  On MRS Manager, click  **Service**.
    2.  <a name="ldabf0861246743658cff7b77136ea7b1"></a>Check whether the health status of the KrbServer service is  **Good**.
        -   If yes, go to  [2.a](#la8ec7d65b69f4b01b14999309811d288).
        -   If no, go to  [1.c](#l3b4d1dfbef4e40a4b8a9c4aa6df45b73).

    3.  <a name="l3b4d1dfbef4e40a4b8a9c4aa6df45b73"></a>Rectify the fault by following instructions in ALM-25500 KrbServer Service Unavailable.
    4.  Perform  [1.b](#ldabf0861246743658cff7b77136ea7b1)  again.

2.  <a name="l8a4f460f221f49469938544acd759b25"></a>Check the ZooKeeper component status.
    1.  <a name="la8ec7d65b69f4b01b14999309811d288"></a>Check whether the health status of the ZooKeeper service is  **Good**.
        -   If yes, go to  [3.a](#ld15a1010f63547628166e94a76ff9e27).
        -   If no, go to  [2.b](#l2efc138671b84bc79efcf030d286d9bf).

    2.  <a name="l2efc138671b84bc79efcf030d286d9bf"></a>If the ZooKeeper service is stopped, start it. For other problems, follow the instructions in ALM-13000 ZooKeeper Service Unavailable.
    3.  Perform  [2.a](#la8ec7d65b69f4b01b14999309811d288)  again.

3.  Check the Broker status.
    1.  <a name="ld15a1010f63547628166e94a76ff9e27"></a>Choose  **Service**  \>  **Kafka**  \>  **Broker**.
    2.  In  **Role**, check whether all instances are normal.
        -   If yes, go to  [3.d](#lfd8d6faa58af46f3905ce73752d1ccb9).
        -   If no, go to  [3.c](#l0ee8a282f57c4110bebcbe8f7adaf615).

    3.  <a name="l0ee8a282f57c4110bebcbe8f7adaf615"></a>Select all instances of Broker and choose  **More**  \>  **Restart Instance**.
        -   If the restart is successful, go to  [3.d](#lfd8d6faa58af46f3905ce73752d1ccb9).
        -   If the restart fails, go to  [4.a](#l84bbea557e2a43ee925517205d326d2e).

    4.  <a name="lfd8d6faa58af46f3905ce73752d1ccb9"></a>Choose  **Service \> Kafka**. Check whether the health status of Kafka is **Good**.
        -   If yes, go to  [3.e](#ld8b6eb9c98aa4795bbadd8402d64286d).
        -   If no, go to  [4.a](#l84bbea557e2a43ee925517205d326d2e).

    5.  <a name="ld8b6eb9c98aa4795bbadd8402d64286d"></a>Wait 30 seconds and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#l84bbea557e2a43ee925517205d326d2e).

4.  Collect fault information.
    1.  <a name="l84bbea557e2a43ee925517205d326d2e"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s680a6e46f11d423abb2ca5f493446439"></a>

N/A


# Messages of Different Protocols<a name="smn_ug_a3000"></a>

Messages delivered to endpoints using different protocols contain different content.

-   Email or HTTP/HTTPS endpoints will receive the message subject, content, and a link to unsubscribe.
-   SMS endpoints will only receive the message content.
-   DMS messages contain the message subject, content, and topic URN.  [Table 1](#table64014010193925)  describes parameters in DMS messages. The following is an example message:

    ```
    {
       "message":[{
          "body":"{
            "event_version":"1.0",
            "subject":"test",
            "event_source":"smn",
            "event_subscription_urn":"urn:smn:regionId:c5acb70716ec4d489213da33e06b15f6:smn_123:47cff941a17f435ea5f6091d3579664e",
            "message_id":"174a38fb1ef24724bf8043954b7330c9",
            "topic_urn":"urn:smn:regionId:c5acb70716ec4d489213da33e06b15f6:smn_123",
            "type":"notification",
            "message":"Hello",
            "timestamp":"2017-10-24T09:37:02Z"
           }"
      ]}
    }
    ```

    **Table  1**  Parameters in a DMS message

    <a name="table64014010193925"></a>
    <table><thead align="left"><tr id="row5043084193925"><th class="cellrowborder" valign="top" width="31.580000000000002%" id="mcps1.2.4.1.1"><p id="p3010233193925"><a name="p3010233193925"></a><a name="p3010233193925"></a><strong id="b842352706161313_1"><a name="b842352706161313_1"></a><a name="b842352706161313_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.18%" id="mcps1.2.4.1.2"><p id="p24770926201222"><a name="p24770926201222"></a><a name="p24770926201222"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.2.4.1.3"><p id="p42502300193925"><a name="p42502300193925"></a><a name="p42502300193925"></a><strong id="b842352706193020"><a name="b842352706193020"></a><a name="b842352706193020"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38134456201232"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p1883213201232"><a name="p1883213201232"></a><a name="p1883213201232"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p18322579201232"><a name="p18322579201232"></a><a name="p18322579201232"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p7733937201232"><a name="p7733937201232"></a><a name="p7733937201232"></a>Message list</p>
    </td>
    </tr>
    <tr id="row25477149201252"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p50383168201252"><a name="p50383168201252"></a><a name="p50383168201252"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p54504779201252"><a name="p54504779201252"></a><a name="p54504779201252"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p52810983201252"><a name="p52810983201252"></a><a name="p52810983201252"></a>Message body</p>
    </td>
    </tr>
    <tr id="row20261315193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p58939980193925"><a name="p58939980193925"></a><a name="p58939980193925"></a>event_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p23598197201215"><a name="p23598197201215"></a><a name="p23598197201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p9409098193925"><a name="p9409098193925"></a><a name="p9409098193925"></a>Version</p>
    </td>
    </tr>
    <tr id="row1317926194055"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p50798406193925"><a name="p50798406193925"></a><a name="p50798406193925"></a>subject</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p32405782201215"><a name="p32405782201215"></a><a name="p32405782201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p56981802194055"><a name="p56981802194055"></a><a name="p56981802194055"></a>Message subject</p>
    </td>
    </tr>
    <tr id="row3004441719406"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p36752602194017"><a name="p36752602194017"></a><a name="p36752602194017"></a>event_source</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p7622717201215"><a name="p7622717201215"></a><a name="p7622717201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p2613091319406"><a name="p2613091319406"></a><a name="p2613091319406"></a>Message source</p>
    </td>
    </tr>
    <tr id="row19906995194010"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p16210282194017"><a name="p16210282194017"></a><a name="p16210282194017"></a>event_subscription_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p13460303201215"><a name="p13460303201215"></a><a name="p13460303201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p16797703194010"><a name="p16797703194010"></a><a name="p16797703194010"></a>Subscription URN</p>
    </td>
    </tr>
    <tr id="row30182723193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p28881537193925"><a name="p28881537193925"></a><a name="p28881537193925"></a>message_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p16542774201215"><a name="p16542774201215"></a><a name="p16542774201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p32602246194350"><a name="p32602246194350"></a><a name="p32602246194350"></a>Message ID</p>
    </td>
    </tr>
    <tr id="row55463365193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p63347618193925"><a name="p63347618193925"></a><a name="p63347618193925"></a>topic_urn</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p35652403201318"><a name="p35652403201318"></a><a name="p35652403201318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p10499547194350"><a name="p10499547194350"></a><a name="p10499547194350"></a>Topic URN</p>
    </td>
    </tr>
    <tr id="row32546122193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p18990191193925"><a name="p18990191193925"></a><a name="p18990191193925"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p22112674201215"><a name="p22112674201215"></a><a name="p22112674201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p3759826194350"><a name="p3759826194350"></a><a name="p3759826194350"></a>Message type</p>
    </td>
    </tr>
    <tr id="row29792815193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p64407799193925"><a name="p64407799193925"></a><a name="p64407799193925"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p46296183201215"><a name="p46296183201215"></a><a name="p46296183201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p56559005194350"><a name="p56559005194350"></a><a name="p56559005194350"></a>Message content</p>
    </td>
    </tr>
    <tr id="row22594652193925"><td class="cellrowborder" valign="top" width="31.580000000000002%" headers="mcps1.2.4.1.1 "><p id="p18227537193925"><a name="p18227537193925"></a><a name="p18227537193925"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.18%" headers="mcps1.2.4.1.2 "><p id="p59003328201215"><a name="p59003328201215"></a><a name="p59003328201215"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p35514193925"><a name="p35514193925"></a><a name="p35514193925"></a>Timestamp</p>
    </td>
    </tr>
    </tbody>
    </table>



# Querying Name Servers in a Private Zone<a name="EN-US_TOPIC_0057342901"></a>

## Function<a name="section55898385"></a>

Query name servers in a private zone.

## URI<a name="section33323423"></a>

-   URI format

    GET /v2/zones/\{zone\_id\}/nameservers

-   Parameter description

    **Table  1**  Parameter in the URI

    <a name="table14024165"></a><table><thead align="left"><tr id="row26592044"><th class="cellrowborder" valign="top" width="19.03190319031903%" id="mcps1.2.5.1.1"><p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a><strong id="b162774213314533"><a name="b162774213314533"></a><a name="b162774213314533"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.781978197819782%" id="mcps1.2.5.1.2"><p id="p54465313"><a name="p54465313"></a><a name="p54465313"></a><strong id="b593421527191713"><a name="b593421527191713"></a><a name="b593421527191713"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.651565156515652%" id="mcps1.2.5.1.3"><p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a><strong id="b84235270619112"><a name="b84235270619112"></a><a name="b84235270619112"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.53455345534553%" id="mcps1.2.5.1.4"><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a><strong id="b842352706112423"><a name="b842352706112423"></a><a name="b842352706112423"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row41071365"><td class="cellrowborder" valign="top" width="19.03190319031903%" headers="mcps1.2.5.1.1 "><p id="p38446258"><a name="p38446258"></a><a name="p38446258"></a>zone_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.781978197819782%" headers="mcps1.2.5.1.2 "><p id="p27139175"><a name="p27139175"></a><a name="p27139175"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.651565156515652%" headers="mcps1.2.5.1.3 "><p id="p50789581"><a name="p50789581"></a><a name="p50789581"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.53455345534553%" headers="mcps1.2.5.1.4 "><p id="p20315403"><a name="p20315403"></a><a name="p20315403"></a>Zone ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section31475357"></a>

None

## Response<a name="section14842765"></a>

-   Parameter description

    **Table  2**  Parameter in the response

    <a name="table2534644119347"></a><table><thead align="left"><tr id="row2134485619347"><th class="cellrowborder" valign="top" width="18.47%" id="mcps1.2.4.1.1"><p id="p5121175619347"><a name="p5121175619347"></a><a name="p5121175619347"></a><strong id="b162774213314533_1"><a name="b162774213314533_1"></a><a name="b162774213314533_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.33%" id="mcps1.2.4.1.2"><p id="p5451156519347"><a name="p5451156519347"></a><a name="p5451156519347"></a><strong id="b84235270619112_1"><a name="b84235270619112_1"></a><a name="b84235270619112_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.2%" id="mcps1.2.4.1.3"><p id="p5336061019347"><a name="p5336061019347"></a><a name="p5336061019347"></a><strong id="b842352706112423_1"><a name="b842352706112423_1"></a><a name="b842352706112423_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2724213119347"><td class="cellrowborder" valign="top" width="18.47%" headers="mcps1.2.4.1.1 "><p id="p5912903419347"><a name="p5912903419347"></a><a name="p5912903419347"></a>nameservers</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p2472241219347"><a name="p2472241219347"></a><a name="p2472241219347"></a>List data structure</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.2%" headers="mcps1.2.4.1.3 "><p id="p64387025171923"><a name="p64387025171923"></a><a name="p64387025171923"></a>Name server list object</p>
    <p id="p60737358161124"><a name="p60737358161124"></a><a name="p60737358161124"></a>For details, see <a href="#EN-US_TOPIC_0057342901__table3847447219326">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **nameservers**  field

    <a name="table3847447219326"></a><table><thead align="left"><tr id="row3833649519326"><th class="cellrowborder" valign="top" width="18.47%" id="mcps1.2.4.1.1"><p id="p3493722219342"><a name="p3493722219342"></a><a name="p3493722219342"></a><strong id="b162774213314533_2"><a name="b162774213314533_2"></a><a name="b162774213314533_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.33%" id="mcps1.2.4.1.2"><p id="p1134272819342"><a name="p1134272819342"></a><a name="p1134272819342"></a><strong id="b84235270619112_2"><a name="b84235270619112_2"></a><a name="b84235270619112_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="62.2%" id="mcps1.2.4.1.3"><p id="p4634576219342"><a name="p4634576219342"></a><a name="p4634576219342"></a><strong id="b842352706112423_2"><a name="b842352706112423_2"></a><a name="b842352706112423_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3753895719326"><td class="cellrowborder" valign="top" width="18.47%" headers="mcps1.2.4.1.1 "><p id="p4303156518517"><a name="p4303156518517"></a><a name="p4303156518517"></a>address</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p6300470318517"><a name="p6300470318517"></a><a name="p6300470318517"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.2%" headers="mcps1.2.4.1.3 "><p id="p310733418517"><a name="p310733418517"></a><a name="p310733418517"></a>IP address of a DNS server</p>
    </td>
    </tr>
    <tr id="row4963379019326"><td class="cellrowborder" valign="top" width="18.47%" headers="mcps1.2.4.1.1 "><p id="p54724792195629"><a name="p54724792195629"></a><a name="p54724792195629"></a>priority</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.33%" headers="mcps1.2.4.1.2 "><p id="p3523206195629"><a name="p3523206195629"></a><a name="p3523206195629"></a>int</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.2%" headers="mcps1.2.4.1.3 "><p id="p16944280195629"><a name="p16944280195629"></a><a name="p16944280195629"></a>Priority of a name server</p>
    <p id="p63758461163042"><a name="p63758461163042"></a><a name="p63758461163042"></a>For example, if the priority of a DNS server is <strong id="b842352706104533"><a name="b842352706104533"></a><a name="b842352706104533"></a>1</strong>, it is used to resolve domain names in first priority.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "nameservers": [
            {
                "priority": 1, 
                "address": "100.125.0.81"
            }, 
            {
                "priority": 2, 
                "address": "100.125.0.82"
            }
        ]
    }
    
    ```


## **Returned Value**<a name="section66476022"></a>

See  [General Request Return Code](general-request-return-code.md).


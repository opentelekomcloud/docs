# Adding a Listener<a name="EN-US_TOPIC_0096561542"></a>

## Function<a name="en-us_topic_0049139642_section1462819"></a>

This API is used to add a listener to a load balancer.

## API Format<a name="en-us_topic_0049139642_section13165375"></a>

<a name="en-us_topic_0049139642_table61044964112545"></a><table><thead align="left"><tr id="en-us_topic_0049139642_row3386316112545"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0049139642_p56085501112550"><a name="en-us_topic_0049139642_p56085501112550"></a><a name="en-us_topic_0049139642_p56085501112550"></a><strong id="b842352706172312"><a name="b842352706172312"></a><a name="b842352706172312"></a>Method</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0049139642_p46631726112550"><a name="en-us_topic_0049139642_p46631726112550"></a><a name="en-us_topic_0049139642_p46631726112550"></a>URI</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0049139642_p19073427112550"><a name="en-us_topic_0049139642_p19073427112550"></a><a name="en-us_topic_0049139642_p19073427112550"></a><strong id="b842352706192251"><a name="b842352706192251"></a><a name="b842352706192251"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0049139642_row55734486112545"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0049139642_p49833499112550"><a name="en-us_topic_0049139642_p49833499112550"></a><a name="en-us_topic_0049139642_p49833499112550"></a>POST</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0049139642_p9981581112550"><a name="en-us_topic_0049139642_p9981581112550"></a><a name="en-us_topic_0049139642_p9981581112550"></a>/v2.0/lbaas/listeners</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0049139642_p3201748112550"><a name="en-us_topic_0049139642_p3201748112550"></a><a name="en-us_topic_0049139642_p3201748112550"></a>Adds a listener.</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="en-us_topic_0049139642_section51379511"></a>

-   Only the administrator can specify  **connection\_limit**.
-   Parameters  **default\_pool\_id**,  **default\_tls\_container\_ref**, and **sni\_container\_refs**  cannot be specified for creating a listener.
-   The value of parameter  **protocol**  can only be  **TCP**  and HTTP.The value of parameter  **protocol**  can only be  **TCP**,  **UDP**,  **HTTP**, and  **TERMINATED\_HTTPS**.
-   The value of  **admin\_state\_up** must be **true**.
-   When  **protocol** is set to **TCP** and **protocol\_port** to **0**, the listener works in IP mode \(DR mode\).

## Request<a name="section112126467011"></a>

-   Parameter description

    <a name="table122881844161815"></a><table><thead align="left"><tr id="row1528814471819"><th class="cellrowborder" valign="top" width="16.96%" id="mcps1.1.5.1.1"><p id="p02881944101816"><a name="p02881944101816"></a><a name="p02881944101816"></a><strong id="b842352706181819"><a name="b842352706181819"></a><a name="b842352706181819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.47%" id="mcps1.1.5.1.2"><p id="p1628844491814"><a name="p1628844491814"></a><a name="p1628844491814"></a><strong id="b84235270610580"><a name="b84235270610580"></a><a name="b84235270610580"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.83%" id="mcps1.1.5.1.3"><p id="p9288104491819"><a name="p9288104491819"></a><a name="p9288104491819"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.74%" id="mcps1.1.5.1.4"><p id="p112889445184"><a name="p112889445184"></a><a name="p112889445184"></a><strong id="b842352706192251_1"><a name="b842352706192251_1"></a><a name="b842352706192251_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19289114471819"><td class="cellrowborder" valign="top" width="16.96%" headers="mcps1.1.5.1.1 "><p id="p14289344171817"><a name="p14289344171817"></a><a name="p14289344171817"></a>listener</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.47%" headers="mcps1.1.5.1.2 "><p id="p2028964471811"><a name="p2028964471811"></a><a name="p2028964471811"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.1.5.1.3 "><p id="p1928964471819"><a name="p1928964471819"></a><a name="p1928964471819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.74%" headers="mcps1.1.5.1.4 "><p id="p142892443189"><a name="p142892443189"></a><a name="p142892443189"></a>Specifies the listener. For details, see <a href="overview-7.html#en-us_topic_0049139638_table15135360111830">Table 1</a>.</p>
    <p id="p10289644111816"><a name="p10289644111816"></a><a name="p10289644111816"></a>Fields <strong id="b84235270616337"><a name="b84235270616337"></a><a name="b84235270616337"></a>protocol_port</strong>,&nbsp;<strong id="b842352706163313"><a name="b842352706163313"></a><a name="b842352706163313"></a>protocol</strong>, and&nbsp;<strong id="b842352706163318"><a name="b842352706163318"></a><a name="b842352706163318"></a>loadbalancer_id</strong> are mandatory.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST  /v2.0/lbaas/listeners
    {
        "listener": {
            "protocol_port": "80",
            "protocol": "TCP",
            "loadbalancer_id": "0416b6f1-877f-4a51-987e-978b3f084253",
            "name": "listener-test",
            "admin_state_up": true
        }
    }
    ```


## Response<a name="section1393614221812"></a>

-   Parameter description

    <a name="table89971153151815"></a><table><thead align="left"><tr id="row199855361813"><th class="cellrowborder" valign="top" width="16.580000000000002%" id="mcps1.1.5.1.1"><p id="p599818535187"><a name="p599818535187"></a><a name="p599818535187"></a><strong id="b842352706181819_1"><a name="b842352706181819_1"></a><a name="b842352706181819_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.330000000000002%" id="mcps1.1.5.1.2"><p id="p4998165315188"><a name="p4998165315188"></a><a name="p4998165315188"></a><strong id="b84235270610580_1"><a name="b84235270610580_1"></a><a name="b84235270610580_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.53%" id="mcps1.1.5.1.3"><p id="p1799865310184"><a name="p1799865310184"></a><a name="p1799865310184"></a><strong id="b8423527061798_1"><a name="b8423527061798_1"></a><a name="b8423527061798_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.559999999999995%" id="mcps1.1.5.1.4"><p id="p8998175331817"><a name="p8998175331817"></a><a name="p8998175331817"></a><strong id="b842352706192251_2"><a name="b842352706192251_2"></a><a name="b842352706192251_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1599914530183"><td class="cellrowborder" valign="top" width="16.580000000000002%" headers="mcps1.1.5.1.1 "><p id="p0999653151816"><a name="p0999653151816"></a><a name="p0999653151816"></a>listener</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.330000000000002%" headers="mcps1.1.5.1.2 "><p id="p3999165310187"><a name="p3999165310187"></a><a name="p3999165310187"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.53%" headers="mcps1.1.5.1.3 "><p id="p17999953111812"><a name="p17999953111812"></a><a name="p17999953111812"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p799915331810"><a name="p799915331810"></a><a name="p799915331810"></a>Specifies the listener. For details, see <a href="overview-7.html#en-us_topic_0049139638_table15135360111830">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "listener": {
            "protocol_port": 80,
            "protocol": "TCP",
            "description": "",
            "default_tls_container_ref": null,
            "admin_state_up": true,
            "loadbalancers": [
                {
                    "id": "0416b6f1-877f-4a51-987e-978b3f084253"
                }
            ],
            "tenant_id": "145483a5107745e9b3d80f956713e6a3",
            "sni_container_refs": [],
            "connection_limit": -1,
            "default_pool_id": null,
            "id": "b7f32b52-6f17-4b16-9ec8-063d71b653ce",
            "name": "listener-test"
        }
    }
    ```


## Error Codes<a name="en-us_topic_0049139642_section51272187"></a>

For details, see section  [Error Codes for Enhanced Load Balancers](error-codes-for-enhanced-load-balancers.md).


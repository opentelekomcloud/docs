# Starting a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158659"></a>

## Function<a name="section5894231"></a>

This API is used to start a single BMS. 

## URI<a name="section53048087"></a>

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#table15103162717019)  lists the parameters.

**Table  1**  Parameter description

<a name="table15103162717019"></a>
<table><thead align="left"><tr id="row6103127604"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p53294272"><a name="p53294272"></a><a name="p53294272"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p21868813"><a name="p21868813"></a><a name="p21868813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p26543418"><a name="p26543418"></a><a name="p26543418"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row201031271407"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p3865173"><a name="p3865173"></a><a name="p3865173"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p59362130"><a name="p59362130"></a><a name="p59362130"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row111036271506"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56885004"><a name="p56885004"></a><a name="p56885004"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p44282627"><a name="p44282627"></a><a name="p44282627"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>Specifies the <span id="text1001475119"><a name="text1001475119"></a><a name="text1001475119"></a>BMS</span><span id="text9024761115"><a name="text9024761115"></a><a name="text9024761115"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section7670737"></a>

-   Request parameters

    <a name="table48180537"></a>
    <table><thead align="left"><tr id="row15499871"><th class="cellrowborder" valign="top" width="14.05%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.05%" id="mcps1.1.5.1.2"><p id="p17403183919111"><a name="p17403183919111"></a><a name="p17403183919111"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.080000000000002%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.82%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54897010"><td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.1.5.1.1 "><p id="p17472816"><a name="p17472816"></a><a name="p17472816"></a>os-start</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.05%" headers="mcps1.1.5.1.2 "><p id="p74009391212"><a name="p74009391212"></a><a name="p74009391212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.080000000000002%" headers="mcps1.1.5.1.3 "><p id="p17209562"><a name="p17209562"></a><a name="p17209562"></a>null</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.82%" headers="mcps1.1.5.1.4 "><p id="p63522246"><a name="p63522246"></a><a name="p63522246"></a>Specifies the operation of starting the <span id="text5483653171111"><a name="text5483653171111"></a><a name="text5483653171111"></a>BMS</span><span id="text1348315319117"><a name="text1348315319117"></a><a name="text1348315319117"></a></span>. The data structure is empty.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{ECS Endpoint}/v2.1/c685484a8cc2416b97260938705deb65/servers/95bf2490-5428-432c-ad9b-5e3406f869dd/action
    ```

    ```
    {
        "os-start": {}
                        }
    ```


## Response Message<a name="section1927776"></a>

N/A

## Returned Values<a name="section17349988"></a>

Normal values

<a name="table753804619176"></a>
<table><thead align="left"><tr id="row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p19735204616177"><a name="p19735204616177"></a><a name="p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p207355465176"><a name="p207355465176"></a><a name="p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13735144611178"><a name="p13735144611178"></a><a name="p13735144611178"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p81516575011"><a name="p81516575011"></a><a name="p81516575011"></a>The server has processed the request but did not return any content.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).


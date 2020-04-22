# Performing Operations on Instances in Batches<a name="EN-US_TOPIC_0043063053"></a>

## Function<a name="section10263773"></a>

-   Add or remove instances to or from an AS group in batches.
-   Configure instance protection or cancel the configuration for the instances in an AS group in batches.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A batch operation can be performed on a maximum of 10 instances at a time. After instances are added to an AS group, the number of instances in the AS group cannot be greater than the maximum number of instances. After instances are removed from an AS group, the number of instances in the AS group cannot be less than the minimum number of instances.  
>-   Instances can be added to an AS group only when the AS group is in the  **INSERVICE**  state and has no scaling action in progress.  
>-   You can remove instances from an AS group only when no scaling action is in progress.  
>-   To add instances to an AS group, ensure that the AZ of the instances falls within that of the AS group.  
>-   Only instances in  **INSERVICE**  state can be removed from an AS group. Instance protection can be enabled or disabled only for  **INSERVICE**  instances.  
>-   When the capacity of an AS group is automatically decreased, the instances with instance protection enabled will not be removed from the AS group.  
>-   If the listener bound to the instance to be removed is the same as the listener in the AS group, the listener will be unbound from the instance. If the listener bound to the instance to be removed is different from the listener in the AS group, the binding relationship between the listener and instance will be reserved.  

## URI<a name="section25265097"></a>

POST /autoscaling-api/v1/\{project\_id\}/scaling\_group\_instance/\{scaling\_group\_id\}/action

**Table  1**  Parameter description

<a name="table10023380"></a>
<table><thead align="left"><tr id="row17946858"><th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.1"><p id="p44409397"><a name="p44409397"></a><a name="p44409397"></a><strong id="b8993173215524"><a name="b8993173215524"></a><a name="b8993173215524"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="p40391380"><a name="p40391380"></a><a name="p40391380"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p50476336"><a name="p50476336"></a><a name="p50476336"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.44444444444445%" id="mcps1.2.5.1.4"><p id="p62051376"><a name="p62051376"></a><a name="p62051376"></a><strong id="b5329232125216"><a name="b5329232125216"></a><a name="b5329232125216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row60105532"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p36709949"><a name="p36709949"></a><a name="p36709949"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p20715931"><a name="p20715931"></a><a name="p20715931"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p268861"><a name="p268861"></a><a name="p268861"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p36520930"><a name="p36520930"></a><a name="p36520930"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row61782511"><td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.1 "><p id="p38327532"><a name="p38327532"></a><a name="p38327532"></a>scaling_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="p17522377"><a name="p17522377"></a><a name="p17522377"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p10026414"><a name="p10026414"></a><a name="p10026414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.44444444444445%" headers="mcps1.2.5.1.4 "><p id="p6833220"><a name="p6833220"></a><a name="p6833220"></a>Specifies the AS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section26059286"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table60799090"></a>
    <table><thead align="left"><tr id="row8858194"><th class="cellrowborder" valign="top" width="22.54901960784314%" id="mcps1.2.5.1.1"><p id="p46425119"><a name="p46425119"></a><a name="p46425119"></a><strong id="b106339347529"><a name="b106339347529"></a><a name="b106339347529"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.54901960784314%" id="mcps1.2.5.1.2"><p id="p2338313"><a name="p2338313"></a><a name="p2338313"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.64705882352941%" id="mcps1.2.5.1.3"><p id="p55185655"><a name="p55185655"></a><a name="p55185655"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="37.254901960784316%" id="mcps1.2.5.1.4"><p id="p40853074"><a name="p40853074"></a><a name="p40853074"></a><strong id="b589893685218"><a name="b589893685218"></a><a name="b589893685218"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20764673"><td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.1 "><p id="p4216941"><a name="p4216941"></a><a name="p4216941"></a>instances_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.2 "><p id="p6027901"><a name="p6027901"></a><a name="p6027901"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p18497945"><a name="p18497945"></a><a name="p18497945"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.254901960784316%" headers="mcps1.2.5.1.4 "><p id="p21938602"><a name="p21938602"></a><a name="p21938602"></a>Specifies the ECS ID.</p>
    </td>
    </tr>
    <tr id="row3847768616914"><td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.1 "><p id="p1754244916917"><a name="p1754244916917"></a><a name="p1754244916917"></a>instance_delete</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.2 "><p id="p1165227516917"><a name="p1165227516917"></a><a name="p1165227516917"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p431024216917"><a name="p431024216917"></a><a name="p431024216917"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.254901960784316%" headers="mcps1.2.5.1.4 "><p id="p52211517171510"><a name="p52211517171510"></a><a name="p52211517171510"></a>Specifies whether to delete an instance when it is removed from an AS group.</p>
    <p id="p3721426171515"><a name="p3721426171515"></a><a name="p3721426171515"></a>Options:</p>
    <a name="ul39711318155"></a><a name="ul39711318155"></a><ul id="ul39711318155"><li><strong id="b12135723171410"><a name="b12135723171410"></a><a name="b12135723171410"></a>no</strong> (default): The instance will not be deleted.</li><li><strong id="b3803102511216"><a name="b3803102511216"></a><a name="b3803102511216"></a>yes</strong>: The instance will be deleted.</li></ul>
    <p id="p5515899416917"><a name="p5515899416917"></a><a name="p5515899416917"></a>This parameter takes effect only when the <strong>action</strong> is set to <strong>REMOVE</strong>.</p>
    </td>
    </tr>
    <tr id="row416365216942"><td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.1 "><p id="p4883500616945"><a name="p4883500616945"></a><a name="p4883500616945"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.54901960784314%" headers="mcps1.2.5.1.2 "><p id="p6332141216945"><a name="p6332141216945"></a><a name="p6332141216945"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.64705882352941%" headers="mcps1.2.5.1.3 "><p id="p2876071816945"><a name="p2876071816945"></a><a name="p2876071816945"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.254901960784316%" headers="mcps1.2.5.1.4 "><p id="p479207748230"><a name="p479207748230"></a><a name="p479207748230"></a>Specifies an action to be performed on instances in batches. The options are as follows:</p>
    <a name="ul6530813782310"></a><a name="ul6530813782310"></a><ul id="ul6530813782310"><li><strong id="b40625683152531"><a name="b40625683152531"></a><a name="b40625683152531"></a>ADD</strong>: adds instances to the AS group.</li><li><strong id="b41969938152555"><a name="b41969938152555"></a><a name="b41969938152555"></a>REMOVE</strong>: removes instances from the AS group.</li><li><strong id="b842352706155259"><a name="b842352706155259"></a><a name="b842352706155259"></a>PROTECT</strong>: enables instance protection.</li><li><strong id="b842352706155313"><a name="b842352706155313"></a><a name="b842352706155313"></a>UNPROTECT</strong>: disables instance protection.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    This example shows how to remove and delete instances with IDs  **instance\_id\_1**  and  **instance\_id\_2**  from the AS group with ID  **e5d27f5c-dd76-4a61-b4bc-a67c5686719a**  in a batch.

    ```
    POST https://{Endpoint}/autoscaling-api/v1/{project_id}/scaling_group_instance/e5d27f5c-dd76-4a61-b4bc-a67c5686719a/action
    
    {
        "action": "REMOVE",
        "instances_id": [
            "instance_id_1",
            "instance_id_2"
        ],
        "instance_delete": "yes"
    }
    ```


## Response Message<a name="section33206990"></a>

-   Response parameters

    None

-   Example response

    None


## Returned Values<a name="section30427456"></a>

-   Normal

    204

-   Abnormal

    <a name="table46788488"></a>
    <table><thead align="left"><tr id="row8624464"><th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.3.1.1"><p id="p27492955"><a name="p27492955"></a><a name="p27492955"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.2%" id="mcps1.1.3.1.2"><p id="p12336887"><a name="p12336887"></a><a name="p12336887"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59763787"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p9028608"><a name="p9028608"></a><a name="p9028608"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p60228670"><a name="p60228670"></a><a name="p60228670"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row5187119"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>You must enter the username and password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row9367865"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p20599592"><a name="p20599592"></a><a name="p20599592"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p57954280"><a name="p57954280"></a><a name="p57954280"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row51826478"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p37195178"><a name="p37195178"></a><a name="p37195178"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p60019402"><a name="p60019402"></a><a name="p60019402"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row3303707"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p66273709"><a name="p66273709"></a><a name="p66273709"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p66570199"><a name="p66570199"></a><a name="p66570199"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row62260885"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p9966935"><a name="p9966935"></a><a name="p9966935"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p2015430"><a name="p2015430"></a><a name="p2015430"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row18138873"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p59962646"><a name="p59962646"></a><a name="p59962646"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p25136147"><a name="p25136147"></a><a name="p25136147"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row24898733"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p3531486"><a name="p3531486"></a><a name="p3531486"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p17614915"><a name="p17614915"></a><a name="p17614915"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row24316508"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p23480171"><a name="p23480171"></a><a name="p23480171"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p22845731"><a name="p22845731"></a><a name="p22845731"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row4284989"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p11539844"><a name="p11539844"></a><a name="p11539844"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p62312200"><a name="p62312200"></a><a name="p62312200"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row23938892"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p60002101"><a name="p60002101"></a><a name="p60002101"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p28332047"><a name="p28332047"></a><a name="p28332047"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row53661838"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p51641620"><a name="p51641620"></a><a name="p51641620"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p22221662"><a name="p22221662"></a><a name="p22221662"></a>Failed to complete the request because the request is invalid.</p>
    </td>
    </tr>
    <tr id="row65777232"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p26355580"><a name="p26355580"></a><a name="p26355580"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p54427232"><a name="p54427232"></a><a name="p54427232"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row20083047"><td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.3.1.1 "><p id="p16114131"><a name="p16114131"></a><a name="p16114131"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.2%" headers="mcps1.1.3.1.2 "><p id="p30176268"><a name="p30176268"></a><a name="p30176268"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section17669131616110"></a>

See  [Error Codes](error-codes.md).


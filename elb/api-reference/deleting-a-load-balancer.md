# Deleting a Load Balancer<a name="EN-US_TOPIC_0096561500"></a>

## Function<a name="en-us_topic_0020100179_section55835522"></a>

This API is used to delete a load balancer. If the load balancer is a public network load balancer, this API deletes the EIP bound to the load balancer.

## Constraints<a name="section454075584016"></a>

For a public network load balancer, you need to delete the backend ECSs added to all listeners of the load balancer before deleting it.

## URI<a name="en-us_topic_0020100179_section32757653"></a>

DELETE /v1.0/\{project\_id\}/elbaas/loadbalancers/\{loadbalancer\_id\}

**Table  1**  Parameter description

<a name="en-us_topic_0020100179_table21270789"></a>
<table><thead align="left"><tr id="en-us_topic_0020100179_row17130265"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="en-us_topic_0020100179_p45374195"><a name="en-us_topic_0020100179_p45374195"></a><a name="en-us_topic_0020100179_p45374195"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="en-us_topic_0020100179_p51431161"><a name="en-us_topic_0020100179_p51431161"></a><a name="en-us_topic_0020100179_p51431161"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.3"><p id="en-us_topic_0020100179_p42188327171146"><a name="en-us_topic_0020100179_p42188327171146"></a><a name="en-us_topic_0020100179_p42188327171146"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="en-us_topic_0020100179_p5174549"><a name="en-us_topic_0020100179_p5174549"></a><a name="en-us_topic_0020100179_p5174549"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0020100179_row16485292"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100179_p97891027152917"><a name="en-us_topic_0020100179_p97891027152917"></a><a name="en-us_topic_0020100179_p97891027152917"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100179_p47625841"><a name="en-us_topic_0020100179_p47625841"></a><a name="en-us_topic_0020100179_p47625841"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100179_p40660579171146"><a name="en-us_topic_0020100179_p40660579171146"></a><a name="en-us_topic_0020100179_p40660579171146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100179_p32487918"><a name="en-us_topic_0020100179_p32487918"></a><a name="en-us_topic_0020100179_p32487918"></a>Specifies the project ID of the operator.</p>
</td>
</tr>
<tr id="en-us_topic_0020100179_row23955812"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0020100179_p61372619"><a name="en-us_topic_0020100179_p61372619"></a><a name="en-us_topic_0020100179_p61372619"></a>loadbalancer_id</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0020100179_p5126234"><a name="en-us_topic_0020100179_p5126234"></a><a name="en-us_topic_0020100179_p5126234"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0020100179_p46553182171146"><a name="en-us_topic_0020100179_p46553182171146"></a><a name="en-us_topic_0020100179_p46553182171146"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0020100179_p12571834"><a name="en-us_topic_0020100179_p12571834"></a><a name="en-us_topic_0020100179_p12571834"></a>Specifies the load balancer ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0020100179_section26383427"></a>

-   Request parameters

    None


-   Example request

    None


## Response<a name="en-us_topic_0020100179_section36124251"></a>

-   Response parameters

    **Table  2**  Response parameters

    <a name="en-us_topic_0020100179_table64935808154453"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100179_row25512474154453"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.4.1.1"><p id="en-us_topic_0020100179_p53244510154453"><a name="en-us_topic_0020100179_p53244510154453"></a><a name="en-us_topic_0020100179_p53244510154453"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.2.4.1.2"><p id="en-us_topic_0020100179_p40442342173633"><a name="en-us_topic_0020100179_p40442342173633"></a><a name="en-us_topic_0020100179_p40442342173633"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.366336633663366%" id="mcps1.2.4.1.3"><p id="en-us_topic_0020100179_p35598641154453"><a name="en-us_topic_0020100179_p35598641154453"></a><a name="en-us_topic_0020100179_p35598641154453"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100179_row64917647154453"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100179_p23838021154453"><a name="en-us_topic_0020100179_p23838021154453"></a><a name="en-us_topic_0020100179_p23838021154453"></a>uri</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100179_p60866790173633"><a name="en-us_topic_0020100179_p60866790173633"></a><a name="en-us_topic_0020100179_p60866790173633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100179_p37605851154453"><a name="en-us_topic_0020100179_p37605851154453"></a><a name="en-us_topic_0020100179_p37605851154453"></a>Specifies the URI returned by Combined API after the job for deleting a load balancer is issued.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row2908346154453"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0020100179_p34249449154453"><a name="en-us_topic_0020100179_p34249449154453"></a><a name="en-us_topic_0020100179_p34249449154453"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0020100179_p12931069173633"><a name="en-us_topic_0020100179_p12931069173633"></a><a name="en-us_topic_0020100179_p12931069173633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0020100179_p30160485154453"><a name="en-us_topic_0020100179_p30160485154453"></a><a name="en-us_topic_0020100179_p30160485154453"></a>Specifies the unique ID assigned to the task for deleting a load balancer in Combined API.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "uri": "/v1/73cd9140bec7427ab9952b4ed75924e0/jobs/4010b39c4fbb4649014fcfd2ab7903b0",
        "job_id": "4010b39c4fbb4649014fcfd2ab7903b0"
    }
    ```


## Status Code<a name="en-us_topic_0020100179_section56682808"></a>

-   Normal

    200

-   Abnormal

    <a name="en-us_topic_0020100179_table37464071151411"></a>
    <table><thead align="left"><tr id="en-us_topic_0020100179_row39359686151411"><th class="cellrowborder" valign="top" width="12.65%" id="mcps1.1.4.1.1"><p id="en-us_topic_0020100179_p34018037151411"><a name="en-us_topic_0020100179_p34018037151411"></a><a name="en-us_topic_0020100179_p34018037151411"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.11%" id="mcps1.1.4.1.2"><p id="p14710544104718"><a name="p14710544104718"></a><a name="p14710544104718"></a>Message</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.1.4.1.3"><p id="en-us_topic_0020100179_p3997645151411"><a name="en-us_topic_0020100179_p3997645151411"></a><a name="en-us_topic_0020100179_p3997645151411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0020100179_row55373813151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p56093845151411"><a name="en-us_topic_0020100179_p56093845151411"></a><a name="en-us_topic_0020100179_p56093845151411"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p1071013442479"><a name="p1071013442479"></a><a name="p1071013442479"></a>badRequest</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p47307606151411"><a name="en-us_topic_0020100179_p47307606151411"></a><a name="en-us_topic_0020100179_p47307606151411"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row23115274151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p60397919151411"><a name="en-us_topic_0020100179_p60397919151411"></a><a name="en-us_topic_0020100179_p60397919151411"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p1773731184814"><a name="p1773731184814"></a><a name="p1773731184814"></a>unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p60393256151411"><a name="en-us_topic_0020100179_p60393256151411"></a><a name="en-us_topic_0020100179_p60393256151411"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row6668396151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p3269183151411"><a name="en-us_topic_0020100179_p3269183151411"></a><a name="en-us_topic_0020100179_p3269183151411"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p16449268489"><a name="p16449268489"></a><a name="p16449268489"></a>userDisabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p63477242151411"><a name="en-us_topic_0020100179_p63477242151411"></a><a name="en-us_topic_0020100179_p63477242151411"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row34424270151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p36902522151411"><a name="en-us_topic_0020100179_p36902522151411"></a><a name="en-us_topic_0020100179_p36902522151411"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p118004106487"><a name="p118004106487"></a><a name="p118004106487"></a>Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p36314273151411"><a name="en-us_topic_0020100179_p36314273151411"></a><a name="en-us_topic_0020100179_p36314273151411"></a>The requested page does not exist.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row58393007151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p32213149151411"><a name="en-us_topic_0020100179_p32213149151411"></a><a name="en-us_topic_0020100179_p32213149151411"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p1025281964811"><a name="p1025281964811"></a><a name="p1025281964811"></a>authFault</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p59128251151411"><a name="en-us_topic_0020100179_p59128251151411"></a><a name="en-us_topic_0020100179_p59128251151411"></a>System error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0020100179_row62392211151411"><td class="cellrowborder" valign="top" width="12.65%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0020100179_p20604349151411"><a name="en-us_topic_0020100179_p20604349151411"></a><a name="en-us_topic_0020100179_p20604349151411"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.11%" headers="mcps1.1.4.1.2 "><p id="p369852418484"><a name="p369852418484"></a><a name="p369852418484"></a>serviceUnavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0020100179_p58339563151411"><a name="en-us_topic_0020100179_p58339563151411"></a><a name="en-us_topic_0020100179_p58339563151411"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



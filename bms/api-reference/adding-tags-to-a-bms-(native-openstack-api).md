# Adding Tags to a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0060410927"></a>

## Function<a name="section59539732104217"></a>

This API is used to add tags to a BMS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the micro version on the client.

## Constraints<a name="section12956040151655"></a>

A BMS can have a maximum of 50 tags.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   It is recommended that you add the  **\_\_type\_baremetal**  tag to BMSs to distinguish BMSs from ECSs. Otherwise, BMSs will be available only on the ECS console.  
>-   A new tag will overwrite the existing one. If you want to retain the original tag, add it to the list of new tags. You are advised to add  **\_\_type\_baremetal**  to the added tags list each time you add a tag.  

## URI<a name="section52138884104217"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/tags

[Table 1](#table7714219185912)  lists the parameters.

**Table  1**  Parameter description

<a name="table7714219185912"></a>
<table><thead align="left"><tr id="row1271511905917"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p17653616104217"><a name="p17653616104217"></a><a name="p17653616104217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p20656767104217"><a name="p20656767104217"></a><a name="p20656767104217"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p62585419104217"><a name="p62585419104217"></a><a name="p62585419104217"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12715101918599"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p50904119104217"><a name="p50904119104217"></a><a name="p50904119104217"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p29593000104217"><a name="p29593000104217"></a><a name="p29593000104217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48222838104217"><a name="p48222838104217"></a><a name="p48222838104217"></a>Specifies the project ID.</p>
<p id="p9141450142010"><a name="p9141450142010"></a><a name="p9141450142010"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row107151219135910"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p56513487104217"><a name="p56513487104217"></a><a name="p56513487104217"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p14189698104217"><a name="p14189698104217"></a><a name="p14189698104217"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8514927104217"><a name="p8514927104217"></a><a name="p8514927104217"></a>Specifies the <span id="text75201646104311"><a name="text75201646104311"></a><a name="text75201646104311"></a>BMS</span><span id="text5520134614311"><a name="text5520134614311"></a><a name="text5520134614311"></a></span> ID.</p>
<p id="p29791113277"><a name="p29791113277"></a><a name="p29791113277"></a>You can obtain the BMS ID from the <span id="en-us_topic_0113746489_text013014803615"><a name="en-us_topic_0113746489_text013014803615"></a><a name="en-us_topic_0113746489_text013014803615"></a>BMS</span><span id="en-us_topic_0113746489_text10131448133612"><a name="en-us_topic_0113746489_text10131448133612"></a><a name="en-us_topic_0113746489_text10131448133612"></a></span> console or using the <a href="querying-bmss-(native-openstack-api).md">Querying BMSs (Native OpenStack API)</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section18620476104217"></a>

-   Request parameters

    <a name="table40018745105534"></a>
    <table><thead align="left"><tr id="row48164488105534"><th class="cellrowborder" valign="top" width="19.37%" id="mcps1.1.5.1.1"><p id="p19987085"><a name="p19987085"></a><a name="p19987085"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.150000000000002%" id="mcps1.1.5.1.2"><p id="p1275716381498"><a name="p1275716381498"></a><a name="p1275716381498"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.61%" id="mcps1.1.5.1.3"><p id="p4546697"><a name="p4546697"></a><a name="p4546697"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.870000000000005%" id="mcps1.1.5.1.4"><p id="p32738149"><a name="p32738149"></a><a name="p32738149"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6972410105534"><td class="cellrowborder" valign="top" width="19.37%" headers="mcps1.1.5.1.1 "><p id="p27894300105534"><a name="p27894300105534"></a><a name="p27894300105534"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.150000000000002%" headers="mcps1.1.5.1.2 "><p id="p9756153811911"><a name="p9756153811911"></a><a name="p9756153811911"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.1.5.1.3 "><p id="p8634695105534"><a name="p8634695105534"></a><a name="p8634695105534"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.870000000000005%" headers="mcps1.1.5.1.4 "><a name="ul1785812112408"></a><a name="ul1785812112408"></a><ul id="ul1785812112408"><li>Specifies the tags of a BMS. Each tag can contain a maximum of 80 characters.</li><li>The tag cannot start with a period (.).</li><li>A BMS can have a maximum of 50 tags.</li><li>An empty tag cannot be created.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers/53206ed0-56de-4d6b-b7ee-ffc62ca26f43/tags
    ```

    ```
    {
        "tags": [
            "baz",
            "foo",
            "qux"
        ]
    }
    ```


## Response Message<a name="section6196486814321"></a>

-   Response parameters

    <a name="table600597414321"></a>
    <table><thead align="left"><tr id="row5646441114321"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.1.4.1.1"><p id="p2639349142614"><a name="p2639349142614"></a><a name="p2639349142614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.61%" id="mcps1.1.4.1.2"><p id="p13639114902610"><a name="p13639114902610"></a><a name="p13639114902610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.22%" id="mcps1.1.4.1.3"><p id="p1864164972614"><a name="p1864164972614"></a><a name="p1864164972614"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4038057614321"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p4960123314321"><a name="p4960123314321"></a><a name="p4960123314321"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.61%" headers="mcps1.1.4.1.2 "><p id="p5827693814321"><a name="p5827693814321"></a><a name="p5827693814321"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.22%" headers="mcps1.1.4.1.3 "><p id="p2281157214321"><a name="p2281157214321"></a><a name="p2281157214321"></a>Specifies user-defined tags of a BMS.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "tags": [
            "baz",
            "foo",
            "qux"
        ]
    }
    ```


## Returned Values<a name="section7610951"></a>

Normal values

<a name="en-us_topic_0106040941_table753804619176"></a>
<table><thead align="left"><tr id="en-us_topic_0106040941_row10735134615172"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="en-us_topic_0106040941_p19735204616177"><a name="en-us_topic_0106040941_p19735204616177"></a><a name="en-us_topic_0106040941_p19735204616177"></a>Returned Values</p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="en-us_topic_0106040941_p207355465176"><a name="en-us_topic_0106040941_p207355465176"></a><a name="en-us_topic_0106040941_p207355465176"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0106040941_row1473514621713"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0106040941_p13735144611178"><a name="en-us_topic_0106040941_p13735144611178"></a><a name="en-us_topic_0106040941_p13735144611178"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0106040941_p207351246161711"><a name="en-us_topic_0106040941_p207351246161711"></a><a name="en-us_topic_0106040941_p207351246161711"></a>The server has successfully processed the request.</p>
</td>
</tr>
</tbody>
</table>

For details about other returned values, see  [Status Codes](status-codes.md).

## Error Codes<a name="section14752650154917"></a>

See  [Error Codes](error-codes.md).


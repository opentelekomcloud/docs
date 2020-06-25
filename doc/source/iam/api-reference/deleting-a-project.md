# Deleting a Project<a name="en-us_topic_0094012960"></a>

## Function Description<a name="section14840153773114"></a>

This interface is used to delete a project.

## URI<a name="section784163713116"></a>

-   URI format

    DELETE /v3/projects/\{project\_id\}


-   URI parameter description

    <a name="table1765831514339"></a>
    <table><thead align="left"><tr id="row136591215133314"><th class="cellrowborder" valign="top" width="19.3%" id="mcps1.1.5.1.1"><p id="p66598151330"><a name="p66598151330"></a><a name="p66598151330"></a><strong id="a6f95694edbbb43d8a152536754b86c82_1"><a name="a6f95694edbbb43d8a152536754b86c82_1"></a><a name="a6f95694edbbb43d8a152536754b86c82_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.96%" id="mcps1.1.5.1.2"><p id="p1565991583314"><a name="p1565991583314"></a><a name="p1565991583314"></a><strong id="b842352706184228_1"><a name="b842352706184228_1"></a><a name="b842352706184228_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.88%" id="mcps1.1.5.1.3"><p id="p9659315143313"><a name="p9659315143313"></a><a name="p9659315143313"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.86%" id="mcps1.1.5.1.4"><p id="p4659131573319"><a name="p4659131573319"></a><a name="p4659131573319"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row365911520332"><td class="cellrowborder" valign="top" width="19.3%" headers="mcps1.1.5.1.1 "><p id="p965961523316"><a name="p965961523316"></a><a name="p965961523316"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.96%" headers="mcps1.1.5.1.2 "><p id="p20659171513317"><a name="p20659171513317"></a><a name="p20659171513317"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.88%" headers="mcps1.1.5.1.3 "><p id="p5659191514336"><a name="p5659191514336"></a><a name="p5659191514336"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.1.5.1.4 "><p id="p56591315203314"><a name="p56591315203314"></a><a name="p56591315203314"></a>Project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section41023711442"></a>

-   Request header parameter description

    <a name="table6841837173110"></a>
    <table><thead align="left"><tr id="row58413376318"><th class="cellrowborder" valign="top" width="19.27807219278072%" id="mcps1.1.5.1.1"><p id="p584143715313"><a name="p584143715313"></a><a name="p584143715313"></a><strong id="a6f95694edbbb43d8a152536754b86c82_3"><a name="a6f95694edbbb43d8a152536754b86c82_3"></a><a name="a6f95694edbbb43d8a152536754b86c82_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.17818218178182%" id="mcps1.1.5.1.2"><p id="p58421837173119"><a name="p58421837173119"></a><a name="p58421837173119"></a><strong id="b842352706184228_3"><a name="b842352706184228_3"></a><a name="b842352706184228_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.698230176982303%" id="mcps1.1.5.1.3"><p id="p1284203773111"><a name="p1284203773111"></a><a name="p1284203773111"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.84551544845515%" id="mcps1.1.5.1.4"><p id="p1584293703114"><a name="p1584293703114"></a><a name="p1584293703114"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11842637153116"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.5.1.1 "><p id="p68421237153116"><a name="p68421237153116"></a><a name="p68421237153116"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.17818218178182%" headers="mcps1.1.5.1.2 "><p id="p198428375319"><a name="p198428375319"></a><a name="p198428375319"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.698230176982303%" headers="mcps1.1.5.1.3 "><p id="p158426375311"><a name="p158426375311"></a><a name="p158426375311"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.84551544845515%" headers="mcps1.1.5.1.4 "><p id="p784213783118"><a name="p784213783118"></a><a name="p784213783118"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row984253713313"><td class="cellrowborder" valign="top" width="19.27807219278072%" headers="mcps1.1.5.1.1 "><p id="p1484219377311"><a name="p1484219377311"></a><a name="p1484219377311"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.17818218178182%" headers="mcps1.1.5.1.2 "><p id="p484223783118"><a name="p484223783118"></a><a name="p484223783118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.698230176982303%" headers="mcps1.1.5.1.3 "><p id="p1884233733118"><a name="p1884233733118"></a><a name="p1884233733118"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.84551544845515%" headers="mcps1.1.5.1.4 "><p id="p3907950692245"><a name="p3907950692245"></a><a name="p3907950692245"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X DELETE https://172.30.48.180:31943/v3/projects/3291eab70fd743499ef1a09aa3ae67a7
    ```


## Response<a name="section1732319140365"></a>

No response body.

## Status Codes<a name="section20323151411368"></a>

<a name="table8323141453613"></a>
<table><thead align="left"><tr id="row932381403612"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p14323514173615"><a name="p14323514173615"></a><a name="p14323514173615"></a><strong id="b842352706104328"><a name="b842352706104328"></a><a name="b842352706104328"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p10323141463613"><a name="p10323141463613"></a><a name="p10323141463613"></a><strong id="b842352706114032_5"><a name="b842352706114032_5"></a><a name="b842352706114032_5"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row132319142366"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p16323714103613"><a name="p16323714103613"></a><a name="p16323714103613"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5323614133611"><a name="p5323614133611"></a><a name="p5323614133611"></a>The request is successful.</p>
</td>
</tr>
<tr id="row43234147366"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1632321443618"><a name="p1632321443618"></a><a name="p1632321443618"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p432310148363"><a name="p432310148363"></a><a name="p432310148363"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row3323114113619"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p832311411365"><a name="p832311411365"></a><a name="p832311411365"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p14323121419361"><a name="p14323121419361"></a><a name="p14323121419361"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row15323514113619"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p13323131419361"><a name="p13323131419361"></a><a name="p13323131419361"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p12323914143611"><a name="p12323914143611"></a><a name="p12323914143611"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row1832313143362"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p20324171414362"><a name="p20324171414362"></a><a name="p20324171414362"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p33243147365"><a name="p33243147365"></a><a name="p33243147365"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row143245147365"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1732412140368"><a name="p1732412140368"></a><a name="p1732412140368"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p232416145368"><a name="p232416145368"></a><a name="p232416145368"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row83241314123618"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5324181453616"><a name="p5324181453616"></a><a name="p5324181453616"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p232411417363"><a name="p232411417363"></a><a name="p232411417363"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>


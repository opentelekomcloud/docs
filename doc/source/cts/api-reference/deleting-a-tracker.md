# Deleting a Tracker<a name="en-us_topic_0168602223"></a>

## Function<a name="section15349251"></a>

This API is used to delete a tracker. Deleting a tracker has no impact on the operation records generated. When you enable CTS again, you can view those operation records.

## URI<a name="section3925534"></a>

DELETE /v1.0/\{project\_id\}/tracker?tracker\_name=\{tracker\_name\}

For details about the parameters, see  [Deleting a Tracker](deleting-a-tracker.md).

**Table  1**  Parameters in the URI

<a name="table4080300"></a>
<table><thead align="left"><tr id="row23192694"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="p66668934"><a name="p66668934"></a><a name="p66668934"></a><strong id="b842352706115038"><a name="b842352706115038"></a><a name="b842352706115038"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.5.1.2"><p id="p31474554"><a name="p31474554"></a><a name="p31474554"></a><strong id="b842352706115041"><a name="b842352706115041"></a><a name="b842352706115041"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p66410939"><a name="p66410939"></a><a name="p66410939"></a><strong id="b842352706115043"><a name="b842352706115043"></a><a name="b842352706115043"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p10576944"><a name="p10576944"></a><a name="p10576944"></a><strong id="b842352706115045"><a name="b842352706115045"></a><a name="b842352706115045"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row51426113"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p4765656"><a name="p4765656"></a><a name="p4765656"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.2 "><p id="p50473818"><a name="p50473818"></a><a name="p50473818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p61847473"><a name="p61847473"></a><a name="p61847473"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p43589445"><a name="p43589445"></a><a name="p43589445"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row20031075143358"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="p1850775014343"><a name="p1850775014343"></a><a name="p1850775014343"></a>tracker_name</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.5.1.2 "><p id="p2273281814343"><a name="p2273281814343"></a><a name="p2273281814343"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p2941893714343"><a name="p2941893714343"></a><a name="p2941893714343"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p3412371714343"><a name="p3412371714343"></a><a name="p3412371714343"></a>Specifies the tracker name.</p>
<p id="p3867800514343"><a name="p3867800514343"></a><a name="p3867800514343"></a>If this parameter is not specified, all trackers of a user will be deleted.</p>
<p id="p1255772614343"><a name="p1255772614343"></a><a name="p1255772614343"></a>Currently, only tracker "system" is available.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section35329809"></a>

-   Parameters

    None


-   Example request

    ```
    DELETE /v1.0/{project_id}/tracker?tracker_name=system
    ```


## Response<a name="section49532829"></a>

-   Parameters

    None


-   Example response

    None


## Returned Values<a name="section43142284"></a>

-   Normal

    **Table  2**  Return code for successful requests

    <a name="table15748167"></a>
    <table><thead align="left"><tr id="row53117702"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a><strong id="b842352706115056"><a name="b842352706115056"></a><a name="b842352706115056"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p8918541"><a name="p8918541"></a><a name="p8918541"></a><strong id="b842352706115059"><a name="b842352706115059"></a><a name="b842352706115059"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51313205"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a>204</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p47877526"><a name="p47877526"></a><a name="p47877526"></a>Deleted successfully.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    **Table  3**  Return code for failed requests

    <a name="table52874399"></a>
    <table><thead align="left"><tr id="row7652366"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.2.3.1.1"><p id="p15861880"><a name="p15861880"></a><a name="p15861880"></a><strong id="b84235270611513"><a name="b84235270611513"></a><a name="b84235270611513"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.3.1.2"><p id="p9743886"><a name="p9743886"></a><a name="p9743886"></a><strong id="b842352706114437"><a name="b842352706114437"></a><a name="b842352706114437"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row23803959143231"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p24240714143232"><a name="p24240714143232"></a><a name="p24240714143232"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p17340830143232"><a name="p17340830143232"></a><a name="p17340830143232"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row51057338"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p42003681"><a name="p42003681"></a><a name="p42003681"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p46855021"><a name="p46855021"></a><a name="p46855021"></a>The server failed to find the requested resource or deleting some trackers failed.</p>
    </td>
    </tr>
    <tr id="row19042013"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p66008059"><a name="p66008059"></a><a name="p66008059"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p45052529"><a name="p45052529"></a><a name="p45052529"></a>The request failed to be executed or some trackers failed to be deleted.</p>
    </td>
    </tr>
    <tr id="row3547785910342"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p1628033103416"><a name="p1628033103416"></a><a name="p1628033103416"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p64761823103416"><a name="p64761823103416"></a><a name="p64761823103416"></a>Your access request is rejected.</p>
    </td>
    </tr>
    <tr id="row4636840710346"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.2.3.1.1 "><p id="p33837633103416"><a name="p33837633103416"></a><a name="p33837633103416"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.3.1.2 "><p id="p56493743103416"><a name="p56493743103416"></a><a name="p56493743103416"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    </tbody>
    </table>



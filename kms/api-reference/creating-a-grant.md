# Creating a Grant<a name="kms_02_0028"></a>

## Function<a name="en-us_topic_0112992333_section37533920154934"></a>

This API enables you to create a grant to grant permissions on a CMK to a user so that the user can perform operations on the CMK.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>A Default Master Key \(the alias suffix of which is  **/default**\) does not allow permission granting.  

## URI<a name="en-us_topic_0112992333_section37627629154934"></a>

-   URI format

    POST /v1.0/\{project\_id\}/kms/create-grant

-   Parameter description

    **Table  1**  Parameter description

    <a name="en-us_topic_0112992333_table38759358154934"></a>
    <table><thead align="left"><tr id="en-us_topic_0112992333_row60644171154934"><th class="cellrowborder" valign="top" width="22.74%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992333_p13230838154934"><a name="en-us_topic_0112992333_p13230838154934"></a><a name="en-us_topic_0112992333_p13230838154934"></a><strong id="en-us_topic_0112992333_b842352706191249"><a name="en-us_topic_0112992333_b842352706191249"></a><a name="en-us_topic_0112992333_b842352706191249"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992333_p65064970154934"><a name="en-us_topic_0112992333_p65064970154934"></a><a name="en-us_topic_0112992333_p65064970154934"></a><strong id="en-us_topic_0112992333_b842352706191255"><a name="en-us_topic_0112992333_b842352706191255"></a><a name="en-us_topic_0112992333_b842352706191255"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.55%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992333_p35771181154934"><a name="en-us_topic_0112992333_p35771181154934"></a><a name="en-us_topic_0112992333_p35771181154934"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.79%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992333_p11784586154934"><a name="en-us_topic_0112992333_p11784586154934"></a><a name="en-us_topic_0112992333_p11784586154934"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0112992333_row15027399154934"><td class="cellrowborder" valign="top" width="22.74%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p9259788154934"><a name="en-us_topic_0112992333_p9259788154934"></a><a name="en-us_topic_0112992333_p9259788154934"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p11845378154934"><a name="en-us_topic_0112992333_p11845378154934"></a><a name="en-us_topic_0112992333_p11845378154934"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p4386100291125"><a name="en-us_topic_0112992333_p4386100291125"></a><a name="en-us_topic_0112992333_p4386100291125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.79%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p5464351154934"><a name="en-us_topic_0112992333_p5464351154934"></a><a name="en-us_topic_0112992333_p5464351154934"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Requests<a name="en-us_topic_0112992333_section49179167154934"></a>

**Table  2**  Request parameters

<a name="en-us_topic_0112992333_table5096792154934"></a>
<table><thead align="left"><tr id="en-us_topic_0112992333_row37570371154934"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992333_p114081546134418"><a name="en-us_topic_0112992333_p114081546134418"></a><a name="en-us_topic_0112992333_p114081546134418"></a><strong id="en-us_topic_0112992333_b1636075548"><a name="en-us_topic_0112992333_b1636075548"></a><a name="en-us_topic_0112992333_b1636075548"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992333_p9408546124415"><a name="en-us_topic_0112992333_p9408546124415"></a><a name="en-us_topic_0112992333_p9408546124415"></a><strong id="en-us_topic_0112992333_b1693435514"><a name="en-us_topic_0112992333_b1693435514"></a><a name="en-us_topic_0112992333_b1693435514"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992333_p164081146134413"><a name="en-us_topic_0112992333_p164081146134413"></a><a name="en-us_topic_0112992333_p164081146134413"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992333_p10408194611444"><a name="en-us_topic_0112992333_p10408194611444"></a><a name="en-us_topic_0112992333_p10408194611444"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992333_row3735252154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p5492758715522"><a name="en-us_topic_0112992333_p5492758715522"></a><a name="en-us_topic_0112992333_p5492758715522"></a>key_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p530110015522"><a name="en-us_topic_0112992333_p530110015522"></a><a name="en-us_topic_0112992333_p530110015522"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p3346736533"><a name="en-us_topic_0112992333_p3346736533"></a><a name="en-us_topic_0112992333_p3346736533"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p2673593115522"><a name="en-us_topic_0112992333_p2673593115522"></a><a name="en-us_topic_0112992333_p2673593115522"></a>36-byte ID of a CMK that matches the regular expression <span class="parmvalue" id="en-us_topic_0112992333_parmvalue80435593163333"><a name="en-us_topic_0112992333_parmvalue80435593163333"></a><a name="en-us_topic_0112992333_parmvalue80435593163333"></a><b>^[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$</b></span></p>
<p id="en-us_topic_0112992333_p5898392715522"><a name="en-us_topic_0112992333_p5898392715522"></a><a name="en-us_topic_0112992333_p5898392715522"></a>Example: 0d0466b0-e727-4d9c-b35d-f84bb474a37f</p>
</td>
</tr>
<tr id="en-us_topic_0112992333_row2233745154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p4383626015522"><a name="en-us_topic_0112992333_p4383626015522"></a><a name="en-us_topic_0112992333_p4383626015522"></a>grantee_principal</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p4822598815522"><a name="en-us_topic_0112992333_p4822598815522"></a><a name="en-us_topic_0112992333_p4822598815522"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p16572391317"><a name="en-us_topic_0112992333_p16572391317"></a><a name="en-us_topic_0112992333_p16572391317"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p1538695162811"><a name="en-us_topic_0112992333_p1538695162811"></a><a name="en-us_topic_0112992333_p1538695162811"></a>Indicates the ID of the authorized user. The value is between 1 to 64 bytes and meets the regular expression <strong id="en-us_topic_0112992333_b112401647135813"><a name="en-us_topic_0112992333_b112401647135813"></a><a name="en-us_topic_0112992333_b112401647135813"></a>"^[a-zA-Z0-9]{1,64}$"</strong>.</p>
<p id="en-us_topic_0112992333_p5880995015522"><a name="en-us_topic_0112992333_p5880995015522"></a><a name="en-us_topic_0112992333_p5880995015522"></a>Example: 0d0466b00d0466b00d0466b00d0466b0</p>
</td>
</tr>
<tr id="en-us_topic_0112992333_row23632615154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p1108616615530"><a name="en-us_topic_0112992333_p1108616615530"></a><a name="en-us_topic_0112992333_p1108616615530"></a>operations</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p5743624615530"><a name="en-us_topic_0112992333_p5743624615530"></a><a name="en-us_topic_0112992333_p5743624615530"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p1941514414456"><a name="en-us_topic_0112992333_p1941514414456"></a><a name="en-us_topic_0112992333_p1941514414456"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p34245185181036"><a name="en-us_topic_0112992333_p34245185181036"></a><a name="en-us_topic_0112992333_p34245185181036"></a>Permissions that can be granted</p>
<p id="en-us_topic_0112992333_p58016892181046"><a name="en-us_topic_0112992333_p58016892181046"></a><a name="en-us_topic_0112992333_p58016892181046"></a>Values: <span class="parmname" id="en-us_topic_0112992333_parmname711983078104314"><a name="en-us_topic_0112992333_parmname711983078104314"></a><a name="en-us_topic_0112992333_parmname711983078104314"></a><b>create-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname1476402418104314"><a name="en-us_topic_0112992333_parmname1476402418104314"></a><a name="en-us_topic_0112992333_parmname1476402418104314"></a><b>create-datakey-without-plaintext</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname833542488104314"><a name="en-us_topic_0112992333_parmname833542488104314"></a><a name="en-us_topic_0112992333_parmname833542488104314"></a><b>encrypt-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname876101735104314"><a name="en-us_topic_0112992333_parmname876101735104314"></a><a name="en-us_topic_0112992333_parmname876101735104314"></a><b>decrypt-datakey</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname150410567104314"><a name="en-us_topic_0112992333_parmname150410567104314"></a><a name="en-us_topic_0112992333_parmname150410567104314"></a><b>describe-key</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname1533829523104314"><a name="en-us_topic_0112992333_parmname1533829523104314"></a><a name="en-us_topic_0112992333_parmname1533829523104314"></a><b>create-grant</b></span>, <span class="parmname" id="en-us_topic_0112992333_parmname1728175126175753"><a name="en-us_topic_0112992333_parmname1728175126175753"></a><a name="en-us_topic_0112992333_parmname1728175126175753"></a><b>retire-grant</b></span></p>
<p id="en-us_topic_0112992333_p2182438615530"><a name="en-us_topic_0112992333_p2182438615530"></a><a name="en-us_topic_0112992333_p2182438615530"></a><span class="parmvalue" id="en-us_topic_0112992333_parmvalue1365452364619"><a name="en-us_topic_0112992333_parmvalue1365452364619"></a><a name="en-us_topic_0112992333_parmvalue1365452364619"></a><b>create-grant</b></span> cannot be the only value.</p>
</td>
</tr>
<tr id="en-us_topic_0112992333_row20487414155231"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p517669515530"><a name="en-us_topic_0112992333_p517669515530"></a><a name="en-us_topic_0112992333_p517669515530"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p721574715530"><a name="en-us_topic_0112992333_p721574715530"></a><a name="en-us_topic_0112992333_p721574715530"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p16985457636"><a name="en-us_topic_0112992333_p16985457636"></a><a name="en-us_topic_0112992333_p16985457636"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p4760460115530"><a name="en-us_topic_0112992333_p4760460115530"></a><a name="en-us_topic_0112992333_p4760460115530"></a>Name of a grant which can be 1 to 255 characters in length and matches the regular expression <strong id="en-us_topic_0112992333_b842352706104539"><a name="en-us_topic_0112992333_b842352706104539"></a><a name="en-us_topic_0112992333_b842352706104539"></a>^[a-zA-Z0-9:/_-]{1,255}$</strong></p>
</td>
</tr>
<tr id="en-us_topic_0112992333_row7628893155234"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p847179515530"><a name="en-us_topic_0112992333_p847179515530"></a><a name="en-us_topic_0112992333_p847179515530"></a>retiring_principal</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p1731110115530"><a name="en-us_topic_0112992333_p1731110115530"></a><a name="en-us_topic_0112992333_p1731110115530"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p31154020414"><a name="en-us_topic_0112992333_p31154020414"></a><a name="en-us_topic_0112992333_p31154020414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p851655562816"><a name="en-us_topic_0112992333_p851655562816"></a><a name="en-us_topic_0112992333_p851655562816"></a>Indicates the ID of the retiring user. The value is between 1 to 64 bytes and meets the regular expression <strong id="en-us_topic_0112992333_b1580910581588"><a name="en-us_topic_0112992333_b1580910581588"></a><a name="en-us_topic_0112992333_b1580910581588"></a>"^[a-zA-Z0-9]{1,64}$"</strong>.</p>
<p id="en-us_topic_0112992333_p342916081631"><a name="en-us_topic_0112992333_p342916081631"></a><a name="en-us_topic_0112992333_p342916081631"></a>Example: 0d0466b00d0466b00d0466b00d0466b0</p>
</td>
</tr>
<tr id="en-us_topic_0112992333_row4011877155238"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p906222915530"><a name="en-us_topic_0112992333_p906222915530"></a><a name="en-us_topic_0112992333_p906222915530"></a>sequence</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p6594517215530"><a name="en-us_topic_0112992333_p6594517215530"></a><a name="en-us_topic_0112992333_p6594517215530"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p1774218113418"><a name="en-us_topic_0112992333_p1774218113418"></a><a name="en-us_topic_0112992333_p1774218113418"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p2406104219271"><a name="en-us_topic_0112992333_p2406104219271"></a><a name="en-us_topic_0112992333_p2406104219271"></a>36-byte serial number of a request message</p>
<p id="en-us_topic_0112992333_p3995872615530"><a name="en-us_topic_0112992333_p3995872615530"></a><a name="en-us_topic_0112992333_p3995872615530"></a>Example: 919c82d4-8046-4722-9094-35c3c6524cff</p>
</td>
</tr>
</tbody>
</table>

## Responses<a name="en-us_topic_0112992333_section35819930154934"></a>

**Table  3**  Response parameters

<a name="en-us_topic_0112992333_table66429519154934"></a>
<table><thead align="left"><tr id="en-us_topic_0112992333_row58318988154934"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0112992333_p1832914587446"><a name="en-us_topic_0112992333_p1832914587446"></a><a name="en-us_topic_0112992333_p1832914587446"></a><strong id="en-us_topic_0112992333_b2117366585"><a name="en-us_topic_0112992333_b2117366585"></a><a name="en-us_topic_0112992333_b2117366585"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="en-us_topic_0112992333_p932911586447"><a name="en-us_topic_0112992333_p932911586447"></a><a name="en-us_topic_0112992333_p932911586447"></a><strong id="en-us_topic_0112992333_b1472577382"><a name="en-us_topic_0112992333_b1472577382"></a><a name="en-us_topic_0112992333_b1472577382"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="en-us_topic_0112992333_p9329155814416"><a name="en-us_topic_0112992333_p9329155814416"></a><a name="en-us_topic_0112992333_p9329155814416"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="en-us_topic_0112992333_p19329358144416"><a name="en-us_topic_0112992333_p19329358144416"></a><a name="en-us_topic_0112992333_p19329358144416"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992333_row12703112154934"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0112992333_p6454391416846"><a name="en-us_topic_0112992333_p6454391416846"></a><a name="en-us_topic_0112992333_p6454391416846"></a>grant_id</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0112992333_p4593721154934"><a name="en-us_topic_0112992333_p4593721154934"></a><a name="en-us_topic_0112992333_p4593721154934"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0112992333_p6511947417"><a name="en-us_topic_0112992333_p6511947417"></a><a name="en-us_topic_0112992333_p6511947417"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0112992333_p445028111690"><a name="en-us_topic_0112992333_p445028111690"></a><a name="en-us_topic_0112992333_p445028111690"></a>64-byte ID of a grant</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="en-us_topic_0112992333_section194314434818"></a>

The following example shows how to grant the  **describe-key**,  **create-datakey**, and  **encrypt-datakey**  permissions of CMK \(ID:  **bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e**\) to the user whose ID is  **13gg44z4g2sglzk0egw0u726zoyzvrs8**. The authorization name is  **my\_grant**, and the user \(ID:  **13gg44z4g2sglzk0egw0u726zoyzvrs8**\) can retire a grant.

-   Example request

    ```
    {      
        "key_id": "bb6a3d22-dc93-47ac-b5bd-88df7ad35f1e",
        "operations": [
           "describe-key",
           "create-datakey",
           "encrypt-datakey"
         ],
         "grantee_principal":"13gg44z4g2sglzk0egw0u726zoyzvrs8",
         "name":"my_grant",
         "retiring_principal":"13gg44z4g2sglzk0egw0u726zoyzvrs8"
    }
    ```

-   Example response

    ```
    {
        "grant_id": "7c9a3286af4fcca5f0a385ad13e1d21a50e27b6dbcab50f37f30f93b8939827d"
    }
    ```

    or

    ```
    {
        "error": {
            "error_code": "KMS.XXXX",
            "error_msg": "XXX"
        }
    }
    ```


## Status Codes<a name="en-us_topic_0112992333_section3454223421"></a>

[Table 4](#en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_table20596071)  lists the normal status code returned by the response.

**Table  4**  Status codes

<a name="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_table20596071"></a>
<table><thead align="left"><tr id="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_row9746163"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="en-us_topic_0112992333_en-us_topic_0112992294_p57545694203043"><a name="en-us_topic_0112992333_en-us_topic_0112992294_p57545694203043"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_p57545694203043"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0112992333_en-us_topic_0112992294_p4531342288"><a name="en-us_topic_0112992333_en-us_topic_0112992294_p4531342288"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_p4531342288"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.4.1.3"><p id="en-us_topic_0112992333_en-us_topic_0112992294_p30689603203043"><a name="en-us_topic_0112992333_en-us_topic_0112992294_p30689603203043"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_p30689603203043"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_row48621261"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"><a name="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_en-us_topic_0079615001_p46008046"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0112992333_en-us_topic_0112992294_p7538425819"><a name="en-us_topic_0112992333_en-us_topic_0112992294_p7538425819"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_p7538425819"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0112992333_en-us_topic_0112992294_p1885682315512"><a name="en-us_topic_0112992333_en-us_topic_0112992294_p1885682315512"></a><a name="en-us_topic_0112992333_en-us_topic_0112992294_p1885682315512"></a>Request processed successfully.</p>
</td>
</tr>
</tbody>
</table>

Exception status code. For details, see  [Status Codes](status-codes.md#kms_02_0301).


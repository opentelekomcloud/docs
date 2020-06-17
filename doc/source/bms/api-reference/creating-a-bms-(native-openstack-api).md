# Creating a BMS \(Native OpenStack API\)<a name="EN-US_TOPIC_0053158682"></a>

## Function<a name="section1345647716824"></a>

This interface is used to create a BMS.

## Constraints<a name="section621290195310"></a>

-   This interface cannot be used to create BMSs in batches.
-   When you create a BMS using an image that supports Cloud-Init or Cloudbase-Init, only parameter  **key\_name**  can be configured. \(Parameter  **adminPass**  is invalid.\) The password of a Linux BMS can be injected only using parameter  **user\_data**. The password of a Windows BMS can be injected only using metadata  **admin\_pass**.
-   When you create a BMS using an image that does not support Cloud-Init or Cloudbase-Init, both parameters  **adminPass**  and  **key\_name**  are invalid. You need to use the password or certificate of the image to log in to the BMS.
-   File injection is not supported.
-   BMS creation from a system volume is not supported.
-   Parameter  **port**  in the three network parameters \(**port**,  **uuid**, and  **fixed\_ip**\) has the highest priority. If parameter  **fixed\_ip**  is set, you must specify the UUID.
-   After a BMS is created, it is recommended that you attach the  **\_\_type\_baremetal**  tag to the BMS. This tag specifies that the created server is a BMS. Otherwise, the BMS may not be displayed in the BMS list on the management console.
-   A BMS can have a maximum of two VPCs, in which case the first VPC will be used by the primary NIC.

## URI<a name="section1187785216824"></a>

POST /v2.1/\{project\_id\}/servers

[Table 1](#table193302233354)  lists the parameters.

**Table  1**  Parameter description

<a name="table193302233354"></a>
<table><thead align="left"><tr id="row1331182318359"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p6708685516824"><a name="p6708685516824"></a><a name="p6708685516824"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p152354631985"><a name="p152354631985"></a><a name="p152354631985"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p5692883616824"><a name="p5692883616824"></a><a name="p5692883616824"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1633142311354"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p4926689916824"><a name="p4926689916824"></a><a name="p4926689916824"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p3119585316824"><a name="p3119585316824"></a><a name="p3119585316824"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4383614716824"><a name="p4383614716824"></a><a name="p4383614716824"></a>Specifies the project ID.</p>
<p id="p13397185821014"><a name="p13397185821014"></a><a name="p13397185821014"></a>For how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section5898101116824"></a>

-   Request parameters

    <a name="table63027372115233"></a>
    <table><thead align="left"><tr id="row53764762115233"><th class="cellrowborder" valign="top" width="18.418158184181582%" id="mcps1.1.5.1.1"><p id="p59978491115233"><a name="p59978491115233"></a><a name="p59978491115233"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.22847715228477%" id="mcps1.1.5.1.2"><p id="p523875318499"><a name="p523875318499"></a><a name="p523875318499"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.617838216178384%" id="mcps1.1.5.1.3"><p id="p26419641115233"><a name="p26419641115233"></a><a name="p26419641115233"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.73552644735527%" id="mcps1.1.5.1.4"><p id="p64181866115233"><a name="p64181866115233"></a><a name="p64181866115233"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31348653115233"><td class="cellrowborder" valign="top" width="18.418158184181582%" headers="mcps1.1.5.1.1 "><p id="p56212973115233"><a name="p56212973115233"></a><a name="p56212973115233"></a>server</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.22847715228477%" headers="mcps1.1.5.1.2 "><p id="p17214453174914"><a name="p17214453174914"></a><a name="p17214453174914"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.617838216178384%" headers="mcps1.1.5.1.3 "><p id="p56956945115233"><a name="p56956945115233"></a><a name="p56956945115233"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.73552644735527%" headers="mcps1.1.5.1.4 "><p id="p207899819655"><a name="p207899819655"></a><a name="p207899819655"></a>Specifies the BMS information, see <a href="#table3034272816824">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **server**  field data structure description

    <a name="table3034272816824"></a>
    <table><thead align="left"><tr id="row4067332316824"><th class="cellrowborder" valign="top" width="25.05%" id="mcps1.2.5.1.1"><p id="p1645824224414"><a name="p1645824224414"></a><a name="p1645824224414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.9%" id="mcps1.2.5.1.2"><p id="p846014425445"><a name="p846014425445"></a><a name="p846014425445"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.61%" id="mcps1.2.5.1.3"><p id="p24652042124419"><a name="p24652042124419"></a><a name="p24652042124419"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="34.44%" id="mcps1.2.5.1.4"><p id="p15467342154412"><a name="p15467342154412"></a><a name="p15467342154412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3747029116824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p1519475416824"><a name="p1519475416824"></a><a name="p1519475416824"></a>imageRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p3612083716824"><a name="p3612083716824"></a><a name="p3612083716824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p47173149172743"><a name="p47173149172743"></a><a name="p47173149172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p5488522316258"><a name="p5488522316258"></a><a name="p5488522316258"></a>Specifies the ID of the image used by the BMS or the image resource uniform resource locator (URL).</p>
    <a name="en-us_topic_0057972661_ul25957356102658"></a><a name="en-us_topic_0057972661_ul25957356102658"></a><ul id="en-us_topic_0057972661_ul25957356102658"><li>Example image ID: 3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2</li><li>Example image URL: http://glance.openstack.example.com/images/3b8d6fef-af77-42ab-b8b7-5a7f0f0af8f2</li></ul>
    <div class="note" id="note137413351178"><a name="note137413351178"></a><a name="note137413351178"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul185629592115"></a><a name="ul185629592115"></a><ul id="ul185629592115"><li>BMSs using certain flavors do not support all public images provided by the public cloud. To obtain the images supported by a BMS flavor, log in to the management console, view the images displayed on the <strong id="en-us_topic_0068473331_b842352706185454"><a name="en-us_topic_0068473331_b842352706185454"></a><a name="en-us_topic_0068473331_b842352706185454"></a>Create ECS</strong> page, and obtain the image IDs on the <strong id="en-us_topic_0068473331_b842352706185522"><a name="en-us_topic_0068473331_b842352706185522"></a><a name="en-us_topic_0068473331_b842352706185522"></a>Image Management Service</strong> page.</li><li>If the creation fails, modify the parameter settings.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row2541566816824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p4540324216824"><a name="p4540324216824"></a><a name="p4540324216824"></a>flavorRef</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p6153613516824"><a name="p6153613516824"></a><a name="p6153613516824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p29487937172743"><a name="p29487937172743"></a><a name="p29487937172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p1837107116824"><a name="p1837107116824"></a><a name="p1837107116824"></a>Specifies the ID or URL of the flavor used by the BMS.</p>
    </td>
    </tr>
    <tr id="row3112191316824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p3784704016824"><a name="p3784704016824"></a><a name="p3784704016824"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p1163818816824"><a name="p1163818816824"></a><a name="p1163818816824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p21870220172743"><a name="p21870220172743"></a><a name="p21870220172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p316918516824"><a name="p316918516824"></a><a name="p316918516824"></a>Specifies the BMS name. It contains 0 to 255 characters.</p>
    </td>
    </tr>
    <tr id="row66460276162716"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p14573312162716"><a name="p14573312162716"></a><a name="p14573312162716"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p5448288619840"><a name="p5448288619840"></a><a name="p5448288619840"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p38590274172743"><a name="p38590274172743"></a><a name="p38590274172743"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p22885804162716"><a name="p22885804162716"></a><a name="p22885804162716"></a>Specifies the BMS metadata. The maximum size for each metadata key and value pair is 255 bytes. For details, see <a href="#table2549048917552">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row3208149162756"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p15946101162759"><a name="p15946101162759"></a><a name="p15946101162759"></a>user_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p34065362162759"><a name="p34065362162759"></a><a name="p34065362162759"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p13695788172743"><a name="p13695788172743"></a><a name="p13695788172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p34042936162759"><a name="p34042936162759"></a><a name="p34042936162759"></a>Specifies the user data to be injected during the BMS creation.</p>
    <p id="p7968474162759"><a name="p7968474162759"></a><a name="p7968474162759"></a>Text, text files, and .gzip files can be injected. The content to be injected cannot be greater than 32 KB in size. The content to be injected must be encoded with base64.</p>
    </td>
    </tr>
    <tr id="row50298416824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p4074174916824"><a name="p4074174916824"></a><a name="p4074174916824"></a>adminPass</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p1201460516824"><a name="p1201460516824"></a><a name="p1201460516824"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p52117854172743"><a name="p52117854172743"></a><a name="p52117854172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p3365895216824"><a name="p3365895216824"></a><a name="p3365895216824"></a>Specifies the initial login password of the BMS administrator account. This parameter is invalid for a Linux BMS. The administrator account of a Windows BMS is <strong id="b84235270617157"><a name="b84235270617157"></a><a name="b84235270617157"></a>Administrator</strong>.</p>
    <p id="p3449511316824"><a name="p3449511316824"></a><a name="p3449511316824"></a>Password complexity requirements:</p>
    <a name="ul4202056716824"></a><a name="ul4202056716824"></a><ul id="ul4202056716824"><li>The password contains 8 to 26 characters.</li><li>The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?).</li><li>The password cannot contain the username or the username in reverse.</li><li>The Windows BMS password cannot contain the username, the username in reverse order, or more than two consecutive characters in the username.</li></ul>
    <p id="p23106383195337"><a name="p23106383195337"></a><a name="p23106383195337"></a>Note: If this parameter is not specified, a random password will be generated.</p>
    <p id="p13457623114921"><a name="p13457623114921"></a><a name="p13457623114921"></a>Special characters: !@$%^-_=+[{}]:,./?</p>
    </td>
    </tr>
    <tr id="row46738163204556"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p17990285204556"><a name="p17990285204556"></a><a name="p17990285204556"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p471257501996"><a name="p471257501996"></a><a name="p471257501996"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p58977744172743"><a name="p58977744172743"></a><a name="p58977744172743"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p43848996204556"><a name="p43848996204556"></a><a name="p43848996204556"></a>Specifies the security group of a BMS. The default value is <strong id="b84235270617200"><a name="b84235270617200"></a><a name="b84235270617200"></a>default</strong>. This parameter is valid when you specify parameter <strong id="b842352706172025"><a name="b842352706172025"></a><a name="b842352706172025"></a>network</strong>. You are not allowed to specify multiple security groups. For details, see <a href="#table42731625205411">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row13145434164550"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p58147228164550"><a name="p58147228164550"></a><a name="p58147228164550"></a>networks</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p5087468419915"><a name="p5087468419915"></a><a name="p5087468419915"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p45102428172743"><a name="p45102428172743"></a><a name="p45102428172743"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p10421164510143"><a name="p10421164510143"></a><a name="p10421164510143"></a>Specifies the BMS NICs. For details, see <a href="#table36009093171737">Table 5</a>.</p>
    <p id="p1238293164550"><a name="p1238293164550"></a><a name="p1238293164550"></a>You can specify a maximum of four networks for a BMS, including two VXLAN networks and two GENEVE networks. The first network in the parameter must be a VXLAN network. The network is used as by the primary NIC of the BMS. If multiple groups of network parameters are specified, ensure that the parameters of each group belong to the same VPC.</p>
    </td>
    </tr>
    <tr id="row5645252416824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p925172616824"><a name="p925172616824"></a><a name="p925172616824"></a>key_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p3416339516824"><a name="p3416339516824"></a><a name="p3416339516824"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p63436109172743"><a name="p63436109172743"></a><a name="p63436109172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p1577162316824"><a name="p1577162316824"></a><a name="p1577162316824"></a>Specifies the name of a key pair. This is an extended attribute.</p>
    </td>
    </tr>
    <tr id="row3144662616824"><td class="cellrowborder" valign="top" width="25.05%" headers="mcps1.2.5.1.1 "><p id="p6414881716824"><a name="p6414881716824"></a><a name="p6414881716824"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.2.5.1.2 "><p id="p4070804916824"><a name="p4070804916824"></a><a name="p4070804916824"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.61%" headers="mcps1.2.5.1.3 "><p id="p6916701172743"><a name="p6916701172743"></a><a name="p6916701172743"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.44%" headers="mcps1.2.5.1.4 "><p id="p1015603112849"><a name="p1015603112849"></a><a name="p1015603112849"></a>Specifies information about the AZ to which the BMS belongs. You are not allowed to specify host information.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **metadata**  field data structure description

    <a name="table2549048917552"></a>
    <table><thead align="left"><tr id="row5894027817552"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.1"><p id="p11219135318446"><a name="p11219135318446"></a><a name="p11219135318446"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.2"><p id="p522225319444"><a name="p522225319444"></a><a name="p522225319444"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p1822675317442"><a name="p1822675317442"></a><a name="p1822675317442"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.73%" id="mcps1.2.5.1.4"><p id="p202271853144411"><a name="p202271853144411"></a><a name="p202271853144411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2346131617552"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p2131841817552"><a name="p2131841817552"></a><a name="p2131841817552"></a>User-defined field key and value pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p4907026417552"><a name="p4907026417552"></a><a name="p4907026417552"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p47081973172826"><a name="p47081973172826"></a><a name="p47081973172826"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.73%" headers="mcps1.2.5.1.4 "><p id="p5719410617654"><a name="p5719410617654"></a><a name="p5719410617654"></a>Specifies the key and value pair of the metadata.</p>
    <p id="p4498490617654"><a name="p4498490617654"></a><a name="p4498490617654"></a>The maximum size for each metadata key and value pair is 255 bytes.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **security\_groups**  field data structure description

    <a name="table42731625205411"></a>
    <table><thead align="left"><tr id="row34164732205411"><th class="cellrowborder" valign="top" width="18.36816318368163%" id="mcps1.2.5.1.1"><p id="p255117254512"><a name="p255117254512"></a><a name="p255117254512"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.2"><p id="p055313224510"><a name="p055313224510"></a><a name="p055313224510"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.348265173482652%" id="mcps1.2.5.1.3"><p id="p2556142104512"><a name="p2556142104512"></a><a name="p2556142104512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.95520447955205%" id="mcps1.2.5.1.4"><p id="p1556115294517"><a name="p1556115294517"></a><a name="p1556115294517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6461164205411"><td class="cellrowborder" valign="top" width="18.36816318368163%" headers="mcps1.2.5.1.1 "><p id="p53592277205411"><a name="p53592277205411"></a><a name="p53592277205411"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.2 "><p id="p46007215205411"><a name="p46007215205411"></a><a name="p46007215205411"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.348265173482652%" headers="mcps1.2.5.1.3 "><p id="p35596962205411"><a name="p35596962205411"></a><a name="p35596962205411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.95520447955205%" headers="mcps1.2.5.1.4 "><p id="p64781653205411"><a name="p64781653205411"></a><a name="p64781653205411"></a>Specifies the name of the security group to which the BMS belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **networks**  field data structure description

    <a name="table36009093171737"></a>
    <table><thead align="left"><tr id="row42632034171737"><th class="cellrowborder" valign="top" width="18.42%" id="mcps1.2.5.1.1"><p id="p133405190458"><a name="p133405190458"></a><a name="p133405190458"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.2"><p id="p16342141912455"><a name="p16342141912455"></a><a name="p16342141912455"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.5.1.3"><p id="p1134521916458"><a name="p1134521916458"></a><a name="p1134521916458"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.73%" id="mcps1.2.5.1.4"><p id="p19349141944517"><a name="p19349141944517"></a><a name="p19349141944517"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18447984171737"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p1742148417187"><a name="p1742148417187"></a><a name="p1742148417187"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p39942372171737"><a name="p39942372171737"></a><a name="p39942372171737"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p51432231171829"><a name="p51432231171829"></a><a name="p51432231171829"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.73%" headers="mcps1.2.5.1.4 "><p id="p48960383171839"><a name="p48960383171839"></a><a name="p48960383171839"></a>Specifies the UUID of the network port.</p>
    </td>
    </tr>
    <tr id="row16127665171737"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p1668674617187"><a name="p1668674617187"></a><a name="p1668674617187"></a>uuid</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p50041644171737"><a name="p50041644171737"></a><a name="p50041644171737"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p47350914171829"><a name="p47350914171829"></a><a name="p47350914171829"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.73%" headers="mcps1.2.5.1.4 "><p id="p57312447171839"><a name="p57312447171839"></a><a name="p57312447171839"></a>Specifies the network UUID.</p>
    </td>
    </tr>
    <tr id="row38645887171737"><td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.2.5.1.1 "><p id="p1793378117187"><a name="p1793378117187"></a><a name="p1793378117187"></a>fixed_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.2 "><p id="p18378580171737"><a name="p18378580171737"></a><a name="p18378580171737"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.5.1.3 "><p id="p24860872171829"><a name="p24860872171829"></a><a name="p24860872171829"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.73%" headers="mcps1.2.5.1.4 "><p id="p39060604171839"><a name="p39060604171839"></a><a name="p39060604171839"></a>Specifies the fixed IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{ECS Endpoint}/v2.1/bbf1946d374b44a0a2a95533562ba954/servers
    ```

    ```
    {
        "server": {
            "imageRef": "1a6635d8-afea-4f2b-abb6-27a202bad319",
            "flavorRef": "physical.o2.medium",
            "name": "bms_name01",
            "availability_zone": "az-dc-1",
            "networks": [
                {
                    "uuid": "8470310b-bfa2-4edf-8f64-d15196b2b2c9"
                }
            ]
        }
    }
    ```


## Response Message<a name="section1328768116824"></a>

-   Response parameters

    <a name="table4738922173128"></a>
    <table><thead align="left"><tr id="row63581626173128"><th class="cellrowborder" valign="top" width="23.169999999999998%" id="mcps1.1.4.1.1"><p id="p11743123884519"><a name="p11743123884519"></a><a name="p11743123884519"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.240000000000002%" id="mcps1.1.4.1.2"><p id="p574616386455"><a name="p574616386455"></a><a name="p574616386455"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.59%" id="mcps1.1.4.1.3"><p id="p1775253812450"><a name="p1775253812450"></a><a name="p1775253812450"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15621585173128"><td class="cellrowborder" valign="top" width="23.169999999999998%" headers="mcps1.1.4.1.1 "><p id="p57388852173128"><a name="p57388852173128"></a><a name="p57388852173128"></a>server</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.240000000000002%" headers="mcps1.1.4.1.2 "><p id="p31166714191051"><a name="p31166714191051"></a><a name="p31166714191051"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.59%" headers="mcps1.1.4.1.3 "><p id="p25133623173128"><a name="p25133623173128"></a><a name="p25133623173128"></a>Specifies the BMS information. For details, see <a href="#table25637149173128">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **server**  field data structure description

    <a name="table25637149173128"></a>
    <table><thead align="left"><tr id="row56523333173128"><th class="cellrowborder" valign="top" width="23.47%" id="mcps1.2.4.1.1"><p id="p4470165411451"><a name="p4470165411451"></a><a name="p4470165411451"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="25.900000000000002%" id="mcps1.2.4.1.2"><p id="p947114542454"><a name="p947114542454"></a><a name="p947114542454"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.629999999999995%" id="mcps1.2.4.1.3"><p id="p144807542455"><a name="p144807542455"></a><a name="p144807542455"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12983931173128"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p45065510173128"><a name="p45065510173128"></a><a name="p45065510173128"></a>security_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.900000000000002%" headers="mcps1.2.4.1.2 "><p id="p52236047191059"><a name="p52236047191059"></a><a name="p52236047191059"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p60269405173128"><a name="p60269405173128"></a><a name="p60269405173128"></a>Specifies information about the BMS security group. For details, see <a href="#table1647050183630">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row19129447174652"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p5981336174652"><a name="p5981336174652"></a><a name="p5981336174652"></a>OS-DCF:diskConfig</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.900000000000002%" headers="mcps1.2.4.1.2 "><p id="p14726202174652"><a name="p14726202174652"></a><a name="p14726202174652"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p29459773174827"><a name="p29459773174827"></a><a name="p29459773174827"></a>Specifies the disk configuration. The value can be:</p>
    <a name="ul63811370174827"></a><a name="ul63811370174827"></a><ul id="ul63811370174827"><li><strong id="en-us_topic_0113746489_b842352706201852"><a name="en-us_topic_0113746489_b842352706201852"></a><a name="en-us_topic_0113746489_b842352706201852"></a>MANUAL</strong>: The API uses the partitioning scheme in the image and the file system to create a <span id="en-us_topic_0113746489_text5742455133714"><a name="en-us_topic_0113746489_text5742455133714"></a><a name="en-us_topic_0113746489_text5742455133714"></a>BMS</span><span id="en-us_topic_0113746489_text674310553373"><a name="en-us_topic_0113746489_text674310553373"></a><a name="en-us_topic_0113746489_text674310553373"></a></span>. If the target flavor has a large disk, the API does not partition the remaining disk space.</li><li><strong id="en-us_topic_0113746489_b11108728193415"><a name="en-us_topic_0113746489_b11108728193415"></a><a name="en-us_topic_0113746489_b11108728193415"></a>AUTO</strong>: The API uses a single partition with the same size as the disk of the target flavor to create a <span id="en-us_topic_0113746489_text1759675920373"><a name="en-us_topic_0113746489_text1759675920373"></a><a name="en-us_topic_0113746489_text1759675920373"></a>BMS</span><span id="en-us_topic_0113746489_text1159611597371"><a name="en-us_topic_0113746489_text1159611597371"></a><a name="en-us_topic_0113746489_text1159611597371"></a></span>. The API automatically adjusts the file system to adapt to the entire partition.</li></ul>
    </td>
    </tr>
    <tr id="row44983361174653"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p19773625174653"><a name="p19773625174653"></a><a name="p19773625174653"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.900000000000002%" headers="mcps1.2.4.1.2 "><p id="p58159806174653"><a name="p58159806174653"></a><a name="p58159806174653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p13323831174653"><a name="p13323831174653"></a><a name="p13323831174653"></a>Specifies the BMS ID.</p>
    </td>
    </tr>
    <tr id="row50254960174653"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p44119923174653"><a name="p44119923174653"></a><a name="p44119923174653"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.900000000000002%" headers="mcps1.2.4.1.2 "><p id="p64107320191132"><a name="p64107320191132"></a><a name="p64107320191132"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p21662468183429"><a name="p21662468183429"></a><a name="p21662468183429"></a>Specifies the shortcut links of the BMS. For details, see <a href="#table3029270918355">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row46057069174654"><td class="cellrowborder" valign="top" width="23.47%" headers="mcps1.2.4.1.1 "><p id="p39635070174654"><a name="p39635070174654"></a><a name="p39635070174654"></a>adminPass</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.900000000000002%" headers="mcps1.2.4.1.2 "><p id="p56324096174654"><a name="p56324096174654"></a><a name="p56324096174654"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.629999999999995%" headers="mcps1.2.4.1.3 "><p id="p65957914174654"><a name="p65957914174654"></a><a name="p65957914174654"></a>Specifies the initial login password of the BMS administrator account.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **security\_groups**  field data structure description

    <a name="table1647050183630"></a>
    <table><thead align="left"><tr id="row15268237183630"><th class="cellrowborder" valign="top" width="22.99%" id="mcps1.2.4.1.1"><p id="p209000120462"><a name="p209000120462"></a><a name="p209000120462"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.479999999999997%" id="mcps1.2.4.1.2"><p id="p59031412184610"><a name="p59031412184610"></a><a name="p59031412184610"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.529999999999994%" id="mcps1.2.4.1.3"><p id="p12910131213460"><a name="p12910131213460"></a><a name="p12910131213460"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1777918183630"><td class="cellrowborder" valign="top" width="22.99%" headers="mcps1.2.4.1.1 "><p id="p9793636183630"><a name="p9793636183630"></a><a name="p9793636183630"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.479999999999997%" headers="mcps1.2.4.1.2 "><p id="p55087051183630"><a name="p55087051183630"></a><a name="p55087051183630"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.529999999999994%" headers="mcps1.2.4.1.3 "><p id="p44911546183630"><a name="p44911546183630"></a><a name="p44911546183630"></a>Specifies the name of the security group to which the BMS belongs.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **links**  field data structure description

    <a name="table3029270918355"></a>
    <table><thead align="left"><tr id="row4237903718355"><th class="cellrowborder" valign="top" width="23.630000000000003%" id="mcps1.2.4.1.1"><p id="p467412584614"><a name="p467412584614"></a><a name="p467412584614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.36%" id="mcps1.2.4.1.2"><p id="p66760255468"><a name="p66760255468"></a><a name="p66760255468"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.01%" id="mcps1.2.4.1.3"><p id="p10682192534612"><a name="p10682192534612"></a><a name="p10682192534612"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2915424618355"><td class="cellrowborder" valign="top" width="23.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1268376418355"><a name="p1268376418355"></a><a name="p1268376418355"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.36%" headers="mcps1.2.4.1.2 "><p id="p2075197418355"><a name="p2075197418355"></a><a name="p2075197418355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.01%" headers="mcps1.2.4.1.3 "><p id="p318835718355"><a name="p318835718355"></a><a name="p318835718355"></a>Specifies the shortcut link marker name. The value can be:</p>
    <a name="ul207311644172510"></a><a name="ul207311644172510"></a><ul id="ul207311644172510"><li><strong id="en-us_topic_0131326852_b320113110516"><a name="en-us_topic_0131326852_b320113110516"></a><a name="en-us_topic_0131326852_b320113110516"></a>self</strong>: resource link that contains the version number. It is used when immediate tracing is required.</li><li><strong id="en-us_topic_0131326852_b84171947711"><a name="en-us_topic_0131326852_b84171947711"></a><a name="en-us_topic_0131326852_b84171947711"></a>bookmark</strong>: resource link that can be stored for a long time.</li></ul>
    </td>
    </tr>
    <tr id="row2869521618355"><td class="cellrowborder" valign="top" width="23.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p4261119718355"><a name="p4261119718355"></a><a name="p4261119718355"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.36%" headers="mcps1.2.4.1.2 "><p id="p2895492218355"><a name="p2895492218355"></a><a name="p2895492218355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.01%" headers="mcps1.2.4.1.3 "><p id="p6364732718355"><a name="p6364732718355"></a><a name="p6364732718355"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "server": {
            "security_groups": [
                {
                    "name": "default"
                }
            ],
            "OS-DCF:diskConfig": "MANUAL",
            "links": [
                {
                    "rel": "self",
                    "href": "https://openstack.example.com/v2/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                },
                {
                    "rel": "bookmark",
                    "href": "https://openstack.example.com/c685484a8cc2416b97260938705deb65/servers/9ab74d89-61e7-4259-8546-465fdebe4944"
                }
            ],
            "id": "9ab74d89-61e7-4259-8546-465fdebe4944",
            "adminPass": "RjdD3h8U2DBe"
        }
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


# Creating an ECS <a name="EN-US_TOPIC_0020212668"></a>

## Function<a name="section61372619"></a>

This API is used to create one or more ECSs.

Before calling this API, you need to obtain  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

Logging in to an ECS can be authenticated using either a key pair or password. For security purposes, you are advised to use key pair authentication.

-   Key pair

    A key pair is used for ECS login authentication.

    Method of calling APIs: Use the  **key\_name**  field to specify the key file used for logging in to the ECS.

-   Password

    If you choose the initial password for authentication in an ECS, you can log in to an ECS using the username and its initial password. The initial password of user  **root**  is used for authentication in Linux, while that of user  **Administrator**  is used for authentication in Windows.

    Method of calling the API: Use the  **adminPass** field to specify the initial login password of the administrator account. For details about how to use the  **adminPass**  field, see  [Table 3](#table761103195216). If an encrypted password is required for logging in to a Linux ECS that is created using an image with Cloud-Init installed, you can use the  **user\_data**  field to inject the password. For details, see  [Table 3](#table761103195216).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the  **user\_data**  field is specified for a Linux ECS that is created using an image with Cloud-Init installed, the  **adminPass**  field becomes invalid.  


## URI<a name="section15482662"></a>

POST /v1/\{project\_id\}/cloudservers

[Table 1](#table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table55945983"></a>
<table><thead align="left"><tr id="row11302482"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p43085863"><a name="p43085863"></a><a name="p43085863"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p294000"><a name="p294000"></a><a name="p294000"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p23814038"><a name="p23814038"></a><a name="p23814038"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row49888896"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="p14468758"><a name="p14468758"></a><a name="p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="p31118786"><a name="p31118786"></a><a name="p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section5126234"></a>

**Request parameters**

[Table 2](#en-us_topic_0057972661_table40519951)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057972661_table40519951"></a>
<table><thead align="left"><tr id="en-us_topic_0057972661_row35619075"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972661_p66572856"><a name="en-us_topic_0057972661_p66572856"></a><a name="en-us_topic_0057972661_p66572856"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057972661_p23692278"><a name="en-us_topic_0057972661_p23692278"></a><a name="en-us_topic_0057972661_p23692278"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972661_p40026340"><a name="en-us_topic_0057972661_p40026340"></a><a name="en-us_topic_0057972661_p40026340"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972661_p20908074"><a name="en-us_topic_0057972661_p20908074"></a><a name="en-us_topic_0057972661_p20908074"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972661_row15832433"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972661_p7358688"><a name="en-us_topic_0057972661_p7358688"></a><a name="en-us_topic_0057972661_p7358688"></a>server</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972661_p59182880"><a name="en-us_topic_0057972661_p59182880"></a><a name="en-us_topic_0057972661_p59182880"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p29083993"><a name="en-us_topic_0057972661_p29083993"></a><a name="en-us_topic_0057972661_p29083993"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972661_p6993202"><a name="en-us_topic_0057972661_p6993202"></a><a name="en-us_topic_0057972661_p6993202"></a>Specifies the ECS information. For details, see <a href="#table761103195216">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Parameters for creating an ECS

<a name="table761103195216"></a>
<table><thead align="left"><tr id="row6501318520"><th class="cellrowborder" valign="top" width="16.666666666666668%" id="mcps1.2.5.1.1"><p id="p107278674213"><a name="p107278674213"></a><a name="p107278674213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.666666666666668%" id="mcps1.2.5.1.2"><p id="p13742669429"><a name="p13742669429"></a><a name="p13742669429"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.76470588235294%" id="mcps1.2.5.1.3"><p id="p1874212611429"><a name="p1874212611429"></a><a name="p1874212611429"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.90196078431373%" id="mcps1.2.5.1.4"><p id="p77581261423"><a name="p77581261423"></a><a name="p77581261423"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row145143105220"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p450031105218"><a name="p450031105218"></a><a name="p450031105218"></a>imageRef</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p25133117527"><a name="p25133117527"></a><a name="p25133117527"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p155173185218"><a name="p155173185218"></a><a name="p155173185218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p15183125212"><a name="p15183125212"></a><a name="p15183125212"></a>Specifies the ID of the system image used for creating ECSs. The ID is in Universally Unique Identifier (UUID) format.</p>
<div class="note" id="note20483193115317"><a name="note20483193115317"></a><a name="note20483193115317"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="en-us_topic_0068473331_ul185629592115"></a><a name="en-us_topic_0068473331_ul185629592115"></a><ul id="en-us_topic_0068473331_ul185629592115"><li>Certain ECS flavors cannot support all public images provided on the public cloud platform. To obtain the images supported by an ECS flavor, log in to the management console, view the images displayed on the <strong id="b842352706185454"><a name="b842352706185454"></a><a name="b842352706185454"></a>Create ECS</strong> page, and obtain the image IDs on the <strong id="b842352706185522"><a name="b842352706185522"></a><a name="b842352706185522"></a>Image Management Service</strong> page.</li><li>If the creation fails, modify the parameter settings.</li></ul>
</div></div>
</td>
</tr>
<tr id="row155233165214"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p5515317522"><a name="p5515317522"></a><a name="p5515317522"></a>flavorRef</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p45113165219"><a name="p45113165219"></a><a name="p45113165219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p5510313525"><a name="p5510313525"></a><a name="p5510313525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p124996526158"><a name="p124996526158"></a><a name="p124996526158"></a>Specifies the flavor ID of the ECS to be created.</p>
<p id="p14521031105216"><a name="p14521031105216"></a><a name="p14521031105216"></a>For details about the flavors that have been released, see "ECS Types and Specifications" in <em id="i842352697151722"><a name="i842352697151722"></a><a name="i842352697151722"></a>Elastic Cloud Server User Guide</em>.</p>
</td>
</tr>
<tr id="row1652163155219"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p852153118529"><a name="p852153118529"></a><a name="p852153118529"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p652123195218"><a name="p652123195218"></a><a name="p652123195218"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p352203120525"><a name="p352203120525"></a><a name="p352203120525"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p12521231135217"><a name="p12521231135217"></a><a name="p12521231135217"></a>Specifies the ECS name.</p>
<p id="p195216316527"><a name="p195216316527"></a><a name="p195216316527"></a>Value requirements:</p>
<a name="ul652163175211"></a><a name="ul652163175211"></a><ul id="ul652163175211"><li>Consists of 1 to 64 characters, including letters, digits, underscores (_), hyphens (-), periods (.).</li><li>If more than one ECS is to be created (the <strong id="b842352706144014"><a name="b842352706144014"></a><a name="b842352706144014"></a>count</strong> value is greater than <strong id="b842352706144025"><a name="b842352706144025"></a><a name="b842352706144025"></a>1</strong>), the system automatically adds a hyphen followed by a four-digit incremental number, such as <strong id="b842352706104944"><a name="b842352706104944"></a><a name="b842352706104944"></a>-0000</strong>, to the end of each ECS name. In this case, the ECS name contains a maximum of 59 characters.<div class="note" id="note1631304619446"><a name="note1631304619446"></a><a name="note1631304619446"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1313546134412"><a name="p1313546134412"></a><a name="p1313546134412"></a>ECS hostnames comply with <a href="https://tools.ietf.org/html/rfc952" target="_blank" rel="noopener noreferrer">RFC952</a> and <a href="https://tools.ietf.org/html/rfc1123" target="_blank" rel="noopener noreferrer">RFC1123</a> naming rules. It is recommended that you configure hostnames using digits, letters (case sensitive), and hyphens (-). Underscores (_) are converted into hyphens (-) by default.</p>
</div></div>
</li></ul>
</td>
</tr>
<tr id="row17782101981517"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p1148283018154"><a name="p1148283018154"></a><a name="p1148283018154"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p248253012159"><a name="p248253012159"></a><a name="p248253012159"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p34981630181517"><a name="p34981630181517"></a><a name="p34981630181517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p968256115212"><a name="p968256115212"></a><a name="p968256115212"></a>Specifies the user data to be injected during the ECS creation process. Text and text files can be injected.</p>
<p id="p151383081516"><a name="p151383081516"></a><a name="p151383081516"></a>For more information about the user data to be injected, see "Injecting User Data into ECSs" in <em id="i24557219106"><a name="i24557219106"></a><a name="i24557219106"></a>Elastic Cloud Server User Guide</em>.</p>
<p id="p135138305157"><a name="p135138305157"></a><a name="p135138305157"></a>Constraints:</p>
<a name="ul20513113015159"></a><a name="ul20513113015159"></a><ul id="ul20513113015159"><li>The content to be injected must be encoded with base64. The maximum size of the content to be injected (before encoding) is 32 KB.</li><li>This parameter can be used to inject the user-defined initial password for user <strong id="b84235270616491"><a name="b84235270616491"></a><a name="b84235270616491"></a>root</strong> when you create a Linux ECS using password authentication. For details, see <a href="#section61372619">Function</a>.</li></ul>
<p id="p1356123019157"><a name="p1356123019157"></a><a name="p1356123019157"></a>Examples (before base64 encoding):</p>
<a name="ul18511102323114"></a><a name="ul18511102323114"></a><ul id="ul18511102323114"><li>Linux<pre class="screen" id="screen193519572312"><a name="screen193519572312"></a><a name="screen193519572312"></a>#! /bin/bash
echo user_test &gt;&gt; /home/user.txt </pre>
</li><li>Windows<pre class="screen" id="screen14888143719322"><a name="screen14888143719322"></a><a name="screen14888143719322"></a>rem cmd
echo 111 &gt; c:\aaa.tx</pre>
</li></ul>
</td>
</tr>
<tr id="row155573112522"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p165493165214"><a name="p165493165214"></a><a name="p165493165214"></a>adminPass</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p20541531105217"><a name="p20541531105217"></a><a name="p20541531105217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p64471619514"><a name="p64471619514"></a><a name="p64471619514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p12995174416219"><a name="p12995174416219"></a><a name="p12995174416219"></a>Specifies the initial login password of the administrator account for logging in to an ECS using password authentication. The Linux administrator is <strong id="b8423527068404"><a name="b8423527068404"></a><a name="b8423527068404"></a>root</strong>, and the Windows administrator is <strong id="b84235270684012"><a name="b84235270684012"></a><a name="b84235270684012"></a>Administrator</strong>. For details, see <a href="#section61372619">Function</a>.</p>
<div class="p" id="p1152014504224"><a name="p1152014504224"></a><a name="p1152014504224"></a>Password complexity requirements:<a name="ul52104519219"></a><a name="ul52104519219"></a><ul id="ul52104519219"><li>Consists of 8 to 26 characters.</li><li>The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?~#*).</li><li>The password cannot contain the username or the username in reverse.</li><li>The Windows ECS password cannot contain the username, the username in reverse, or more than two consecutive characters in the username.</li></ul>
</div>
</td>
</tr>
<tr id="row155573175215"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p855531175218"><a name="p855531175218"></a><a name="p855531175218"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p16551131155216"><a name="p16551131155216"></a><a name="p16551131155216"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p1455163111526"><a name="p1455163111526"></a><a name="p1455163111526"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p055153115217"><a name="p055153115217"></a><a name="p055153115217"></a>Specifies the name of the SSH key used for logging in to the ECS.</p>
<p id="p01371615133414"><a name="p01371615133414"></a><a name="p01371615133414"></a>Keys can be created using the key creating API (<a href="creating-and-importing-an-ssh-key-pair.md">Creating and Importing an SSH Key Pair</a>) or queried using the SSH key query API (<a href="querying-ssh-key-pairs.md">Querying SSH Key Pairs</a>).</p>
</td>
</tr>
<tr id="row13551231195216"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p14551831185218"><a name="p14551831185218"></a><a name="p14551831185218"></a>vpcid</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p2551031195211"><a name="p2551031195211"></a><a name="p2551031195211"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p55543155218"><a name="p55543155218"></a><a name="p55543155218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p5551731125218"><a name="p5551731125218"></a><a name="p5551731125218"></a>Specifies the ID of the VPC to which the ECS belongs. The value is in the format of the UUID.</p>
<p id="p56133115171910"><a name="p56133115171910"></a><a name="p56133115171910"></a>You can obtain the VPC ID from the management console or by following the instructions provided in "Querying VPCs" in <em id="i4550823153416"><a name="i4550823153416"></a><a name="i4550823153416"></a>Virtual Private Cloud API Reference</em>.</p>
</td>
</tr>
<tr id="row156133118524"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p1055123135212"><a name="p1055123135212"></a><a name="p1055123135212"></a>nics</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p35518315528"><a name="p35518315528"></a><a name="p35518315528"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p856731205215"><a name="p856731205215"></a><a name="p856731205215"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p1756731175216"><a name="p1756731175216"></a><a name="p1756731175216"></a>Specifies the NIC information of the ECS. For details, see <a href="#table9120223">Table 4</a>.</p>
<p id="p13561731175218"><a name="p13561731175218"></a><a name="p13561731175218"></a>Constraints:</p>
<a name="ul14713548182"></a><a name="ul14713548182"></a>
<a name="ul125617317523"></a><a name="ul125617317523"></a><ul id="ul125617317523"><li>A maximum of 12 NICs can be attached to an ECS.</li></ul>
</td>
</tr>
<tr id="row45603125217"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p95618318528"><a name="p95618318528"></a><a name="p95618318528"></a>publicip</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p7563318521"><a name="p7563318521"></a><a name="p7563318521"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p75611317526"><a name="p75611317526"></a><a name="p75611317526"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p17561731155214"><a name="p17561731155214"></a><a name="p17561731155214"></a>Specifies the EIP of the ECS, which can be configured in the following three ways:</p>
<a name="ul1456133105216"></a><a name="ul1456133105216"></a><ul id="ul1456133105216"><li>Do not use: In such a case, this field is unavailable.</li><li>Automatically assign: The system will automatically assign an EIP to your ECS.</li><li>Use existing: You need to specify an existing EIP for your ECS.</li></ul>
<p id="p76591419152310"><a name="p76591419152310"></a><a name="p76591419152310"></a>For details, see <a href="data-structure-for-creating-ecss.md#table2785183710710">Table 1</a>.</p>
</td>
</tr>
<tr id="row1457831155216"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p165613120523"><a name="p165613120523"></a><a name="p165613120523"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p175711312521"><a name="p175711312521"></a><a name="p175711312521"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p105793165216"><a name="p105793165216"></a><a name="p105793165216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p1157203120522"><a name="p1157203120522"></a><a name="p1157203120522"></a>Specifies the number of ECSs to be created.</p>
<p id="p195712318525"><a name="p195712318525"></a><a name="p195712318525"></a>Constraints:</p>
<a name="ul557183145214"></a><a name="ul557183145214"></a><ul id="ul557183145214"><li>If this parameter is not specified, the default value is <strong id="b842352706165622"><a name="b842352706165622"></a><a name="b842352706165622"></a>1</strong>.</li><li>If the quota is sufficient, the maximum value is <strong id="b842352706165647"><a name="b842352706165647"></a><a name="b842352706165647"></a>500</strong>.</li></ul>
</td>
</tr>
<tr id="row25753155216"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p1457531155213"><a name="p1457531155213"></a><a name="p1457531155213"></a>root_volume</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p857031115213"><a name="p857031115213"></a><a name="p857031115213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p157331165217"><a name="p157331165217"></a><a name="p157331165217"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p17571031115215"><a name="p17571031115215"></a><a name="p17571031115215"></a>Specifies ECS system disk configurations.</p>
<p id="p59971231202312"><a name="p59971231202312"></a><a name="p59971231202312"></a>For details, see <a href="#table53188122">Table 5</a>.</p>
</td>
</tr>
<tr id="row1458183112527"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p1557203125216"><a name="p1557203125216"></a><a name="p1557203125216"></a>data_volumes</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p4571931185219"><a name="p4571931185219"></a><a name="p4571931185219"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p25733117524"><a name="p25733117524"></a><a name="p25733117524"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p4581031115217"><a name="p4581031115217"></a><a name="p4581031115217"></a>Specifies ECS data disk configurations. Each data structure represents a data disk to be created.</p>
<p id="p45833113521"><a name="p45833113521"></a><a name="p45833113521"></a>An ECS can be attached with a maximum of 59 data disks (certain flavors support only 23 data disks).</p>
<p id="p269855113235"><a name="p269855113235"></a><a name="p269855113235"></a>For details, see <a href="#table66739923">Table 6</a>.</p>
</td>
</tr>
<tr id="row1659631185215"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p10581312525"><a name="p10581312525"></a><a name="p10581312525"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p2581931185218"><a name="p2581931185218"></a><a name="p2581931185218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p145813185212"><a name="p145813185212"></a><a name="p145813185212"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p1059123112521"><a name="p1059123112521"></a><a name="p1059123112521"></a>Specifies the security groups of the ECS.</p>
<p id="p1159831155218"><a name="p1159831155218"></a><a name="p1159831155218"></a>Constraints: If this parameter is left blank, the default security group is bound to the ECS by default.</p>
<p id="p118678147244"><a name="p118678147244"></a><a name="p118678147244"></a>For details, see <a href="data-structure-for-creating-ecss.md#table1698566599">Table 2</a>.</p>
</td>
</tr>
<tr id="row185993115219"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p155933145215"><a name="p155933145215"></a><a name="p155933145215"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p1959143115529"><a name="p1959143115529"></a><a name="p1959143115529"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p2059133165210"><a name="p2059133165210"></a><a name="p2059133165210"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p1059113114525"><a name="p1059113114525"></a><a name="p1059113114525"></a>Specifies the name of the AZ where the ECS is located.</p>
<p id="p15187154018230"><a name="p15187154018230"></a><a name="p15187154018230"></a>See <a href="querying-azs.md">Querying AZs</a>.</p>
</td>
</tr>
<tr id="row1259123185210"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p1959193111524"><a name="p1959193111524"></a><a name="p1959193111524"></a>extendparam</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p459931115218"><a name="p459931115218"></a><a name="p459931115218"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p559143112527"><a name="p559143112527"></a><a name="p559143112527"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p759143185217"><a name="p759143185217"></a><a name="p759143185217"></a>Provides the supplementary information about the ECS to be created.</p>
<p id="p1763154062412"><a name="p1763154062412"></a><a name="p1763154062412"></a>For details, see <a href="data-structure-for-creating-ecss.md#table1137234112314">Table 6</a>.</p>
</td>
</tr>
<tr id="row160631105219"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p5595317524"><a name="p5595317524"></a><a name="p5595317524"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p460131185220"><a name="p460131185220"></a><a name="p460131185220"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p1662104714508"><a name="p1662104714508"></a><a name="p1662104714508"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p1460173115527"><a name="p1460173115527"></a><a name="p1460173115527"></a>Specifies the metadata of ECS to be created.</p>
<p id="p57411157124216"><a name="p57411157124216"></a><a name="p57411157124216"></a>You can use metadata to customize key-value pairs.</p>
<p id="p7572223145718"><a name="p7572223145718"></a><a name="p7572223145718"></a>For details, see <a href="data-structure-for-creating-ecss.md#table2373623012315">Table 8</a>.</p>
</td>
</tr>
<tr id="row1460731155214"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p66010319528"><a name="p66010319528"></a><a name="p66010319528"></a>os:scheduler_hints</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p8601331145214"><a name="p8601331145214"></a><a name="p8601331145214"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p176073116528"><a name="p176073116528"></a><a name="p176073116528"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p116011319521"><a name="p116011319521"></a><a name="p116011319521"></a>Schedules ECSs, for example, by configuring an ECS group.</p>
<p id="p2052872152610"><a name="p2052872152610"></a><a name="p2052872152610"></a>For details, see <a href="data-structure-for-creating-ecss.md#table24430409172542">Table 9</a>.</p>
</td>
</tr>
<tr id="row361143135218"><td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.1 "><p id="p106083115213"><a name="p106083115213"></a><a name="p106083115213"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="16.666666666666668%" headers="mcps1.2.5.1.2 "><p id="p186193120522"><a name="p186193120522"></a><a name="p186193120522"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.76470588235294%" headers="mcps1.2.5.1.3 "><p id="p661153112520"><a name="p661153112520"></a><a name="p661153112520"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="54.90196078431373%" headers="mcps1.2.5.1.4 "><p id="p20611731185211"><a name="p20611731185211"></a><a name="p20611731185211"></a>Specifies ECS tags.</p>
<p id="p9613318525"><a name="p9613318525"></a><a name="p9613318525"></a>A tag is in the format of "key.value", where the maximum lengths of <strong id="b84235270692310"><a name="b84235270692310"></a><a name="b84235270692310"></a>key</strong> and <strong id="b84235270692313"><a name="b84235270692313"></a><a name="b84235270692313"></a>value</strong> are 36 and 43 characters, respectively.</p>
<p id="p166173115522"><a name="p166173115522"></a><a name="p166173115522"></a>When adding a tag to an ECS, ensure that the tag complies with the following requirements:</p>
<a name="ul10612319523"></a><a name="ul10612319523"></a><ul id="ul10612319523"><li>The key of the tag can contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</li><li>The value of the tag can contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</li></ul>
<div class="note" id="note126123110526"><a name="note126123110526"></a><a name="note126123110526"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul5578110122215"></a><a name="ul5578110122215"></a><ul id="ul5578110122215"><li>When you create ECSs, one ECS supports up to 10 tags.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  4** **nics**  field description

<a name="table9120223"></a>
<table><thead align="left"><tr id="row45607220"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.1"><p id="p1577344054216"><a name="p1577344054216"></a><a name="p1577344054216"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p97891040194210"><a name="p97891040194210"></a><a name="p97891040194210"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.5.1.3"><p id="p1478994020422"><a name="p1478994020422"></a><a name="p1478994020422"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.45544554455446%" id="mcps1.2.5.1.4"><p id="p0804144018428"><a name="p0804144018428"></a><a name="p0804144018428"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56761457"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p34275314"><a name="p34275314"></a><a name="p34275314"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p24837051"><a name="p24837051"></a><a name="p24837051"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p65644149"><a name="p65644149"></a><a name="p65644149"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p52170790174229"><a name="p52170790174229"></a><a name="p52170790174229"></a>Specifies the subnet of the ECS.</p>
<p id="p43287089174217"><a name="p43287089174217"></a><a name="p43287089174217"></a>The value must be the ID of the subnet created in the VPC specified by <strong id="b84235270617196"><a name="b84235270617196"></a><a name="b84235270617196"></a>vpcid</strong> and in the format of the UUID.</p>
</td>
</tr>
<tr id="row11285618104313"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p34461706104313"><a name="p34461706104313"></a><a name="p34461706104313"></a>ip_address</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p39934810104313"><a name="p39934810104313"></a><a name="p39934810104313"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p13494158104313"><a name="p13494158104313"></a><a name="p13494158104313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p28930193174245"><a name="p28930193174245"></a><a name="p28930193174245"></a>Specifies the IP address of the NIC used by the ECS. The value is an IPv4 address.</p>
<p id="p59045150174245"><a name="p59045150174245"></a><a name="p59045150174245"></a>Constraints:</p>
<a name="ul61644302174245"></a><a name="ul61644302174245"></a><ul id="ul61644302174245"><li>If this parameter is left blank or set to <strong id="b842352706173944"><a name="b842352706173944"></a><a name="b842352706173944"></a>""</strong>, an unused IP address in the subnet is automatically assigned as the IP address of the NIC.</li><li>If this parameter is specified, its value must be an unused IP address in the network segment of the subnet.</li></ul>
</td>
</tr>
<tr id="row48292797201232"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p31981994201232"><a name="p31981994201232"></a><a name="p31981994201232"></a>binding:profile</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p40404711201232"><a name="p40404711201232"></a><a name="p40404711201232"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p95441454989"><a name="p95441454989"></a><a name="p95441454989"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p55491053202324"><a name="p55491053202324"></a><a name="p55491053202324"></a>Allows you to customize data. Configure this parameter when creating a HANA ECS.</p>
<p id="p9341758182610"><a name="p9341758182610"></a><a name="p9341758182610"></a>For details, see <a href="data-structure-for-creating-ecss.md#table42451440577">Table 10</a>.</p>
</td>
</tr>
<tr id="row16036609201232"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p10111755201232"><a name="p10111755201232"></a><a name="p10111755201232"></a>extra_dhcp_opts</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p13745865201232"><a name="p13745865201232"></a><a name="p13745865201232"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p019211151690"><a name="p019211151690"></a><a name="p019211151690"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p65187435417"><a name="p65187435417"></a><a name="p65187435417"></a>Indicates extended DHCP options.</p>
<p id="p145881020172710"><a name="p145881020172710"></a><a name="p145881020172710"></a>For details, see <a href="data-structure-for-creating-ecss.md#table93959401279">Table 11</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **root\_volume**  field description

<a name="table53188122"></a>
<table><thead align="left"><tr id="row56379492"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.1"><p id="p748555484218"><a name="p748555484218"></a><a name="p748555484218"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.5.1.2"><p id="p1948517542420"><a name="p1948517542420"></a><a name="p1948517542420"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.2.5.1.3"><p id="p55012544426"><a name="p55012544426"></a><a name="p55012544426"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.45544554455446%" id="mcps1.2.5.1.4"><p id="p1451675411422"><a name="p1451675411422"></a><a name="p1451675411422"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row3514615"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p16248438"><a name="p16248438"></a><a name="p16248438"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p41055134"><a name="p41055134"></a><a name="p41055134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p37131542"><a name="p37131542"></a><a name="p37131542"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p54864902"><a name="p54864902"></a><a name="p54864902"></a>Specifies the ECS system disk type. The disk type must match the available disk type.</p>
<a name="ul32900150164116"></a><a name="ul32900150164116"></a><ul id="ul32900150164116"><li>SATA: common I/O disk type</li><li>SAS: high I/O disk type</li><li>SSD: ultra-high I/O disk type</li><li>co-p1: high I/O (performance-optimized I) disk type</li><li>uh-l1: ultra-high I/O (latency-optimized) disk type</li></ul>
<div class="note" id="note1189393515548"><a name="note1189393515548"></a><a name="note1189393515548"></a><span class="notetitle"> NOTE: </span><div class="notebody"></div></div>
</td>
</tr>
<tr id="row60160519142638"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p11049419142649"><a name="p11049419142649"></a><a name="p11049419142649"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p22587748142649"><a name="p22587748142649"></a><a name="p22587748142649"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p17668334142649"><a name="p17668334142649"></a><a name="p17668334142649"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p21848977142649"><a name="p21848977142649"></a><a name="p21848977142649"></a>Specifies the system disk size, in GB. The value ranges from 1 to 1024.</p>
<p id="p9898211364"><a name="p9898211364"></a><a name="p9898211364"></a>Constraints:</p>
<a name="ul13190271969"></a><a name="ul13190271969"></a><ul id="ul13190271969"><li>The system disk size must be greater than or equal to the minimum system disk size supported by the image (<strong id="b842352706191837"><a name="b842352706191837"></a><a name="b842352706191837"></a>min_disk</strong> attribute of the image).</li><li>If this parameter is not specified or is set to <strong id="b842352706191921"><a name="b842352706191921"></a><a name="b842352706191921"></a>0</strong>, the default system disk size is the minimum value of the system disk in the image (<strong id="b842352706191942"><a name="b842352706191942"></a><a name="b842352706191942"></a>min_disk</strong> attribute of the image).<div class="note" id="note995775414129"><a name="note995775414129"></a><a name="note995775414129"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1427920232184"><a name="p1427920232184"></a><a name="p1427920232184"></a>To obtain the minimum system disk size (<strong id="b84235270613130"><a name="b84235270613130"></a><a name="b84235270613130"></a>min_disk</strong>) of an image, click the image on the management console for its details. Alternatively, call the native OpenStack API for querying details about an image. For details, see "Querying Image Details (Native OpenStack)" in <em id="i842352697142054"><a name="i842352697142054"></a><a name="i842352697142054"></a>Image Management Service API Reference</em>.</p>
</div></div>
</li></ul>
</td>
</tr>
<tr id="row1960625122419"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p9710802420"><a name="p9710802420"></a><a name="p9710802420"></a>hw:passthrough</p>
</td>
<td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.5.1.2 "><p id="p107208152412"><a name="p107208152412"></a><a name="p107208152412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.2.5.1.3 "><p id="p147212852417"><a name="p147212852417"></a><a name="p147212852417"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.2.5.1.4 "><p id="p157213814240"><a name="p157213814240"></a><a name="p157213814240"></a>Pay attention to this parameter if your ECS is SDI-compliant. If the value of this parameter is <strong id="b2211171682615"><a name="b2211171682615"></a><a name="b2211171682615"></a>true</strong>, the created disk is of SCSI type.</p>
<div class="note" id="note187211802410"><a name="note187211802410"></a><a name="note187211802410"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p167298132410"><a name="p167298132410"></a><a name="p167298132410"></a>This parameter is of boolean type. If a non-boolean character is imported, the parameter value is set to <strong id="b709517254143436"><a name="b709517254143436"></a><a name="b709517254143436"></a>false</strong>.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

**Table  6** **data\_volumes**  field description

<a name="table66739923"></a>
<table><thead align="left"><tr id="row64470080"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.1"><p id="p11191618194312"><a name="p11191618194312"></a><a name="p11191618194312"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p911916181439"><a name="p911916181439"></a><a name="p911916181439"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.5.1.3"><p id="p16135171819439"><a name="p16135171819439"></a><a name="p16135171819439"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.545454545454554%" id="mcps1.2.5.1.4"><p id="p2135131811433"><a name="p2135131811433"></a><a name="p2135131811433"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11410990"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p51874972"><a name="p51874972"></a><a name="p51874972"></a>volumetype</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p41123170"><a name="p41123170"></a><a name="p41123170"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p42642473"><a name="p42642473"></a><a name="p42642473"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p31488280"><a name="p31488280"></a><a name="p31488280"></a>Specifies the disk type of the ECS data disk. The disk type must match the available disk type.</p>
<p id="p2946710911145"><a name="p2946710911145"></a><a name="p2946710911145"></a>Enumerated values of the disk type:</p>
<a name="ul19026230153616"></a><a name="ul19026230153616"></a><ul id="ul19026230153616"><li><strong id="b8423527061044"><a name="b8423527061044"></a><a name="b8423527061044"></a>SATA</strong>: common I/O disk type</li><li><strong id="b8423527061047"><a name="b8423527061047"></a><a name="b8423527061047"></a>SAS</strong>: high I/O disk type</li><li><strong id="b84235270610413"><a name="b84235270610413"></a><a name="b84235270610413"></a>SSD</strong>: ultra-high I/O disk type</li><li><strong id="b84235270610425"><a name="b84235270610425"></a><a name="b84235270610425"></a>co-p1</strong>: high I/O (performance-optimized I) disk type</li><li><strong id="b84235270610432"><a name="b84235270610432"></a><a name="b84235270610432"></a>uh-l1</strong>: ultra-high I/O (latency-optimized) disk type</li></ul>
<div class="note" id="note6222576894254"><a name="note6222576894254"></a><a name="note6222576894254"></a><span class="notetitle"> NOTE: </span><div class="notebody"></div></div>
</td>
</tr>
<tr id="row14959071"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p3725214"><a name="p3725214"></a><a name="p3725214"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p33306906"><a name="p33306906"></a><a name="p33306906"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p13504826"><a name="p13504826"></a><a name="p13504826"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p5562853216262"><a name="p5562853216262"></a><a name="p5562853216262"></a>Specifies the data disk size, in GB. The value ranges from 10 to 32768.</p>
</td>
</tr>
<tr id="row36319805104741"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p58442796104741"><a name="p58442796104741"></a><a name="p58442796104741"></a>shareable</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p36246068104741"><a name="p36246068104741"></a><a name="p36246068104741"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p50250380104741"><a name="p50250380104741"></a><a name="p50250380104741"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p340879331257"><a name="p340879331257"></a><a name="p340879331257"></a>Specifies whether the disk is shared. The value can be <strong id="b1234733726161036"><a name="b1234733726161036"></a><a name="b1234733726161036"></a>true</strong> (specifies a shared disk) or <strong id="b441872521161041"><a name="b441872521161041"></a><a name="b441872521161041"></a>false</strong> (a common EVS disk).</p>
<div class="note" id="note3759105212439"><a name="note3759105212439"></a><a name="note3759105212439"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p277515212439"><a name="p277515212439"></a><a name="p277515212439"></a>This field has been deprecated. Use <strong id="b84235270610834"><a name="b84235270610834"></a><a name="b84235270610834"></a>multiattach</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row5795350214188"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p5181947414188"><a name="p5181947414188"></a><a name="p5181947414188"></a>multiattach</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p3662789014188"><a name="p3662789014188"></a><a name="p3662789014188"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p1406913114188"><a name="p1406913114188"></a><a name="p1406913114188"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p6585779614188"><a name="p6585779614188"></a><a name="p6585779614188"></a>Specifies the shared disk information.</p>
<a name="ul303285995535"></a><a name="ul303285995535"></a><ul id="ul303285995535"><li><strong id="b84235270620220"><a name="b84235270620220"></a><a name="b84235270620220"></a>true</strong>: indicates that the created disk is a shared disk.</li><li><strong id="b84235270620526"><a name="b84235270620526"></a><a name="b84235270620526"></a>false</strong>: indicates that the created disk is a common EVS disk.</li></ul>
<div class="note" id="note6690690095624"><a name="note6690690095624"></a><a name="note6690690095624"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p6529118995624"><a name="p6529118995624"></a><a name="p6529118995624"></a>The <strong id="b84235270620621"><a name="b84235270620621"></a><a name="b84235270620621"></a>shareable</strong> field is not used any more. If both <strong id="b174806763820640"><a name="b174806763820640"></a><a name="b174806763820640"></a>shareable</strong> and <strong id="b8423527062091"><a name="b8423527062091"></a><a name="b8423527062091"></a>multiattach</strong> must be used, ensure that the values of the two fields are the same. If this parameter is not specified, common EVS disks are created by default.</p>
</div></div>
</td>
</tr>
<tr id="row1051569714183"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p2753241214183"><a name="p2753241214183"></a><a name="p2753241214183"></a>hw:passthrough</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p1553286914183"><a name="p1553286914183"></a><a name="p1553286914183"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p5020283814183"><a name="p5020283814183"></a><a name="p5020283814183"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p4088945310517"><a name="p4088945310517"></a><a name="p4088945310517"></a>Indicates whether the data volume uses a SCSI lock.</p>
<a name="en-us_topic_0044524833_ul14462208141855"></a><a name="en-us_topic_0044524833_ul14462208141855"></a><ul id="en-us_topic_0044524833_ul14462208141855"><li>If this parameter is set to <strong id="b84235270620365"><a name="b84235270620365"></a><a name="b84235270620365"></a>true</strong>, the disk device type is SCSI, which allows ECS OSs to directly access the underlying storage media. SCSI reservation command is supported.</li><li>If this parameter is set to <strong id="b203367810216"><a name="b203367810216"></a><a name="b203367810216"></a>false</strong>, the disk device type will be VBD, which supports only simple SCSI read/write commands.</li><li>If this parameter does not appear, the disk device type is VBD.</li></ul>
<div class="note" id="note1279613227324"><a name="note1279613227324"></a><a name="note1279613227324"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p679712229326"><a name="p679712229326"></a><a name="p679712229326"></a>This parameter is of boolean type. If a non-boolean character is imported, the parameter value is set to <strong id="b1987176772"><a name="b1987176772"></a><a name="b1987176772"></a>false</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row62177020217"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p5036340620217"><a name="p5036340620217"></a><a name="p5036340620217"></a>data_image_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p5290411520217"><a name="p5290411520217"></a><a name="p5290411520217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p5737494520217"><a name="p5737494520217"></a><a name="p5737494520217"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p37344069202225"><a name="p37344069202225"></a><a name="p37344069202225"></a>Specifies ID of the data image. The value is in UUID format.</p>
<p id="p844532810467"><a name="p844532810467"></a><a name="p844532810467"></a>If data disks are created using a data disk image, this parameter is mandatory and it does not support metadata.</p>
</td>
</tr>
<tr id="row17444062585"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="p164461462581"><a name="p164461462581"></a><a name="p164461462581"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p174476613587"><a name="p174476613587"></a><a name="p174476613587"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.5.1.3 "><p id="p296112276588"><a name="p296112276588"></a><a name="p296112276588"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="54.545454545454554%" headers="mcps1.2.5.1.4 "><p id="p544756135816"><a name="p544756135816"></a><a name="p544756135816"></a>Specifies the EVS disk metadata. Ensure that <strong id="b1086810651"><a name="b1086810651"></a><a name="b1086810651"></a>key</strong> and <strong id="b1157636134"><a name="b1157636134"></a><a name="b1157636134"></a>value</strong> in the metadata contain at most 255 bytes.</p>
<p id="p5568103611379"><a name="p5568103611379"></a><a name="p5568103611379"></a>This field is used only when an encrypted disk is created.</p>
<p id="p1815264144920"><a name="p1815264144920"></a><a name="p1815264144920"></a>If data disks are created using a data disk image, this field cannot be used.</p>
<p id="p16970151531615"><a name="p16970151531615"></a><a name="p16970151531615"></a>For details, see <a href="data-structure-for-creating-ecss.md#section1228814491353">metadata Field Description for Creating Disks</a>.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section46136113"></a>

<a name="table2824153181913"></a>
<table><thead align="left"><tr id="row11825193111915"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.1"><p id="p135632102272"><a name="p135632102272"></a><a name="p135632102272"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.2"><p id="p156321002716"><a name="p156321002716"></a><a name="p156321002716"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.1.5.1.3"><p id="p55632010102714"><a name="p55632010102714"></a><a name="p55632010102714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.45544554455446%" id="mcps1.1.5.1.4"><p id="p125631410152717"><a name="p125631410152717"></a><a name="p125631410152717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row382615381910"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p1882713151914"><a name="p1882713151914"></a><a name="p1882713151914"></a>job_id</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p156901318203618"><a name="p156901318203618"></a><a name="p156901318203618"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.5.1.3 "><p id="p1182723161913"><a name="p1182723161913"></a><a name="p1182723161913"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.1.5.1.4 "><p id="p12827133121914"><a name="p12827133121914"></a><a name="p12827133121914"></a>Specifies the returned task ID after delivering the task. You can query the task progress using this ID. For details about how to query the task execution status based on <strong id="b176813401213"><a name="b176813401213"></a><a name="b176813401213"></a>job_id</strong>, see <a href="task-status-management.md">Task Status Management</a>.</p>
</td>
</tr>
<tr id="row1659515481837"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p5576801843"><a name="p5576801843"></a><a name="p5576801843"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p165761807410"><a name="p165761807410"></a><a name="p165761807410"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.5.1.3 "><p id="p657611018416"><a name="p657611018416"></a><a name="p657611018416"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.1.5.1.4 "><p id="p17576103410"><a name="p17576103410"></a><a name="p17576103410"></a>Specifies the returned error message when an error occurs.</p>
</td>
</tr>
<tr id="row071913521232"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p185761708416"><a name="p185761708416"></a><a name="p185761708416"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.2 "><p id="p145761401648"><a name="p145761401648"></a><a name="p145761401648"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.1.5.1.3 "><p id="p6576101846"><a name="p6576101846"></a><a name="p6576101846"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.45544554455446%" headers="mcps1.1.5.1.4 "><p id="p1557620647"><a name="p1557620647"></a><a name="p1557620647"></a>Specifies the error code returned when an error occurs.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section755512111436"></a>

The public cloud platform provides various ECS types. The flavor name/ID varies depending on ECS types and specifications. When you use APIs to create ECSs with different specifications, the request bodies are the same. You only need to change the parameter values in the following request example based on the parameters described in  [Request](#section5126234).

-   Example URL request

    ```
    POST https://{endpoint}/v1/{project_id}/cloudservers
    ```


-   An ECS with flavor ID  **m1.larger**  is to be created, where the image ID is  **imageid\_123**, disk type is  **SATA**, and VPC ID is  **0dae26c9-9a70-4392-93f3-87d53115d171**. An example request is as follows:

    ```
    {
        "server": {
            "availability_zone":"az1-dc1",
            "name": "newserver", 
            "imageRef": "imageid_123", 
            "root_volume": {
                "volumetype": "SATA"
            }, 
            "data_volumes": [
                {
                    "volumetype": "SATA", 
                    "size": 100
                }, 
                {
                    "volumetype": "SSD", 
                    "size": 100,
                    "multiattach": true,
                    "hw:passthrough": "true"
                }
            ], 
            "flavorRef": "m1.larger", 
            "vpcid": "0dae26c9-9a70-4392-93f3-87d53115d171", 
            "security_groups": [
                {
                    "id": "507ca48f-814c-4293-8706-300564d54620"
                }
            ], 
            "nics": [
                {
                    "subnet_id": "157ee789-03ea-45b1-a698-76c92660dd83", 
                    "extra_dhcp_opts":[
                         {
                               "opt_value": 8888, 
                               "opt_name": "26",
                         }
                    ]
                }
            ], 
            "publicip": {
                "eip": {
                    "iptype": "5_bgp",
                    "bandwidth": {
                        "size": 10, 
                        "sharetype": "PER"
                    }
                }
            }, 
            "key_name": "sshkey-123", 
            "count": 1 
        }
    }
    ```



## Example Response<a name="section584343712331"></a>

```
{
    "job_id": "93c82933d6b7827d3016b8771f2070873"
}
```

Or

```
{
    "error": {
        "code": "request body is illegal.", 
        "message": "Ecs.0005"
    }
}
```

## Returned Values<a name="section3394154515224"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


# Querying Users in a User Group<a name="en-us_topic_0057845561"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query users in a user group.

## URI<a name="section3019338085013"></a>

-   URI format

    GET /v3/groups/\{group\_id\}/users

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706161530"><a name="b842352706161530"></a><a name="b842352706161530"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.77%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.25%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.620000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b842352706114032_1"><a name="b842352706114032_1"></a><a name="b842352706114032_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.25%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.620000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>ID of a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Query parameter description

    <a name="table38476019164014"></a>
    <table><thead align="left"><tr id="row56436571164014"><th class="cellrowborder" valign="top" width="19.439999999999998%" id="mcps1.1.5.1.1"><p id="p7959515164014"><a name="p7959515164014"></a><a name="p7959515164014"></a><strong id="b1156489731"><a name="b1156489731"></a><a name="b1156489731"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.43%" id="mcps1.1.5.1.2"><p id="p40740988164014"><a name="p40740988164014"></a><a name="p40740988164014"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.64%" id="mcps1.1.5.1.3"><p id="p11685733164014"><a name="p11685733164014"></a><a name="p11685733164014"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.49%" id="mcps1.1.5.1.4"><p id="p7020351164014"><a name="p7020351164014"></a><a name="p7020351164014"></a><strong id="b842352706114032_3"><a name="b842352706114032_3"></a><a name="b842352706114032_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31777586164014"><td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.1.5.1.1 "><p id="p23847653164014"><a name="p23847653164014"></a><a name="p23847653164014"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p52611712164014"><a name="p52611712164014"></a><a name="p52611712164014"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.3 "><p id="p33690284164014"><a name="p33690284164014"></a><a name="p33690284164014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="p44558480164014"><a name="p44558480164014"></a><a name="p44558480164014"></a>ID of the domain to which a user group belongs.</p>
    </td>
    </tr>
    <tr id="row65482007164014"><td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.1.5.1.1 "><p id="p2442371164014"><a name="p2442371164014"></a><a name="p2442371164014"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p63614396164014"><a name="p63614396164014"></a><a name="p63614396164014"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.3 "><p id="p52492457164014"><a name="p52492457164014"></a><a name="p52492457164014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="p24030643164014"><a name="p24030643164014"></a><a name="p24030643164014"></a>Name of a user. The maximum length is 64 characters.</p>
    </td>
    </tr>
    <tr id="row20100318164057"><td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.1.5.1.1 "><p id="p46685139164057"><a name="p46685139164057"></a><a name="p46685139164057"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p66073055164128"><a name="p66073055164128"></a><a name="p66073055164128"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.3 "><p id="p50317259164128"><a name="p50317259164128"></a><a name="p50317259164128"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="p48949399164057"><a name="p48949399164057"></a><a name="p48949399164057"></a>Whether a user is enabled. The value can be <strong id="b842352706182927"><a name="b842352706182927"></a><a name="b842352706182927"></a>true</strong> or <strong id="b842352706182931"><a name="b842352706182931"></a><a name="b842352706182931"></a>false</strong>. <strong id="b1586036687182937"><a name="b1586036687182937"></a><a name="b1586036687182937"></a>true</strong> indicates the user is enabled and <strong id="b77525951182937"><a name="b77525951182937"></a><a name="b77525951182937"></a>false</strong> indicates the user is not enabled.</p>
    </td>
    </tr>
    <tr id="row172741544195812"><td class="cellrowborder" valign="top" width="19.439999999999998%" headers="mcps1.1.5.1.1 "><p id="p122311493521"><a name="p122311493521"></a><a name="p122311493521"></a>password_expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.43%" headers="mcps1.1.5.1.2 "><p id="p1823334995215"><a name="p1823334995215"></a><a name="p1823334995215"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.64%" headers="mcps1.1.5.1.3 "><p id="p623364945219"><a name="p623364945219"></a><a name="p623364945219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="p1123314965211"><a name="p1123314965211"></a><a name="p1123314965211"></a>Password expiration time. The format is <strong id="b842352706153618"><a name="b842352706153618"></a><a name="b842352706153618"></a>password_expires_at=</strong><em id="i842352697153316"><a name="i842352697153316"></a><a name="i842352697153316"></a>operator</em><strong id="b842352706153622"><a name="b842352706153622"></a><a name="b842352706153622"></a>:</strong><em id="i842352697153329"><a name="i842352697153329"></a><a name="i842352697153329"></a>timestamp</em>.</p>
    <p id="p1838112538569"><a name="p1838112538569"></a><a name="p1838112538569"></a>Example:</p>
    <pre class="screen" id="screen85910169576"><a name="screen85910169576"></a><a name="screen85910169576"></a>password_expires_at=lt:2016-12-08T22:02:00Z</pre>
    <a name="ul9511557111910"></a><a name="ul9511557111910"></a><ul id="ul9511557111910"><li>The value of <strong id="b842352706153734"><a name="b842352706153734"></a><a name="b842352706153734"></a>operator</strong> can be <strong id="b842352706153825"><a name="b842352706153825"></a><a name="b842352706153825"></a>lt</strong>, <strong id="b842352706153821"><a name="b842352706153821"></a><a name="b842352706153821"></a>lte</strong>, <strong id="b842352706153814"><a name="b842352706153814"></a><a name="b842352706153814"></a>gt</strong>, <strong id="b84235270615388"><a name="b84235270615388"></a><a name="b84235270615388"></a>gte</strong>, <strong id="b84235270615384"><a name="b84235270615384"></a><a name="b84235270615384"></a>eq</strong>, or <strong id="b84235270615380"><a name="b84235270615380"></a><a name="b84235270615380"></a>neq</strong>.<a name="ul1162653632014"></a><a name="ul1162653632014"></a><ul id="ul1162653632014"><li><strong id="b84235270615395"><a name="b84235270615395"></a><a name="b84235270615395"></a>lt</strong>: The expiration time is earlier than <em id="i842352697154057"><a name="i842352697154057"></a><a name="i842352697154057"></a>timestamp</em>.</li><li><strong id="b842352706154029"><a name="b842352706154029"></a><a name="b842352706154029"></a>lte</strong>: The expiration time is earlier than or equal to <em id="i84235269715416"><a name="i84235269715416"></a><a name="i84235269715416"></a>timestamp</em>.</li><li><strong id="b1045171"><a name="b1045171"></a><a name="b1045171"></a>gt</strong>: The expiration time is later than <em id="i84235269715427"><a name="i84235269715427"></a><a name="i84235269715427"></a>timestamp</em>.</li><li><strong id="b1132875272"><a name="b1132875272"></a><a name="b1132875272"></a>gte</strong>: The expiration time is equal to or later than <em id="i649631542"><a name="i649631542"></a><a name="i649631542"></a>timestamp</em>.</li><li><strong id="b2047639843"><a name="b2047639843"></a><a name="b2047639843"></a>eq</strong>: The expiration time is equal to <em id="i1850266607"><a name="i1850266607"></a><a name="i1850266607"></a>timestamp</em>.</li><li><strong id="b446734727"><a name="b446734727"></a><a name="b446734727"></a>neq</strong>: The expiration time is not equal to <em id="i1816528420"><a name="i1816528420"></a><a name="i1816528420"></a>timestamp</em>.</li></ul>
    </li><li>The <strong id="b842352706154327"><a name="b842352706154327"></a><a name="b842352706154327"></a>timestamp</strong> format is <strong id="b842352706154332"><a name="b842352706154332"></a><a name="b842352706154332"></a>YYYY-MM-DDTHH:mm:ssZ</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.62%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a6f95694edbbb43d8a152536754b86c82_1"><a name="a6f95694edbbb43d8a152536754b86c82_1"></a><a name="a6f95694edbbb43d8a152536754b86c82_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.39%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.5%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_5"><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.49%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b842352706114032_5"><a name="b842352706114032_5"></a><a name="b842352706114032_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row9196329"><td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p6705199"><a name="en-us_topic_0032920307_p6705199"></a><a name="en-us_topic_0032920307_p6705199"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p6250253"><a name="en-us_topic_0032920307_p6250253"></a><a name="en-us_topic_0032920307_p6250253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36508524"><a name="en-us_topic_0032920307_p36508524"></a><a name="en-us_topic_0032920307_p36508524"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p4400500"><a name="en-us_topic_0032920307_p4400500"></a><a name="en-us_topic_0032920307_p4400500"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.62%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.5%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.49%" headers="mcps1.1.5.1.4 "><p id="p6097796794746"><a name="p6097796794746"></a><a name="p6097796794746"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample request

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X GET https://172.30.48.86:31943/v3/groups/00007111583e457389b0d4252643181b/users
    ```


## Response<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="19.541954195419542%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="a6f95694edbbb43d8a152536754b86c82_3"><a name="a6f95694edbbb43d8a152536754b86c82_3"></a><a name="a6f95694edbbb43d8a152536754b86c82_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.58195819581958%" id="mcps1.1.5.1.2"><p id="p182061578189"><a name="p182061578189"></a><a name="p182061578189"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_7"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_7"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.19181918191819%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_7"><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.684268426842685%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b842352706114032_7"><a name="b842352706114032_7"></a><a name="b842352706114032_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570214510010"><td class="cellrowborder" valign="top" width="19.541954195419542%" headers="mcps1.1.5.1.1 "><p id="p5922062510010"><a name="p5922062510010"></a><a name="p5922062510010"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58195819581958%" headers="mcps1.1.5.1.2 "><p id="p182061673183"><a name="p182061673183"></a><a name="p182061673183"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19181918191819%" headers="mcps1.1.5.1.3 "><p id="p12656935926"><a name="p12656935926"></a><a name="p12656935926"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.684268426842685%" headers="mcps1.1.5.1.4 "><p id="p2326866010010"><a name="p2326866010010"></a><a name="p2326866010010"></a>Resource links of users in a user group.</p>
    </td>
    </tr>
    <tr id="row809135110010"><td class="cellrowborder" valign="top" width="19.541954195419542%" headers="mcps1.1.5.1.1 "><p id="p5141972010010"><a name="p5141972010010"></a><a name="p5141972010010"></a>users</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.58195819581958%" headers="mcps1.1.5.1.2 "><p id="p32068771816"><a name="p32068771816"></a><a name="p32068771816"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.19181918191819%" headers="mcps1.1.5.1.3 "><p id="p16554338420"><a name="p16554338420"></a><a name="p16554338420"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.684268426842685%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>List of users in a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the user format

    <a name="en-us_topic_0057845638_table683623312113"></a>
    <table><thead align="left"><tr id="en-us_topic_0057845638_row19845533162112"><th class="cellrowborder" valign="top" width="19.81%" id="mcps1.1.5.1.1"><p id="en-us_topic_0057845638_p484813315212"><a name="en-us_topic_0057845638_p484813315212"></a><a name="en-us_topic_0057845638_p484813315212"></a><strong id="en-us_topic_0057845638_a6f95694edbbb43d8a152536754b86c82_7"><a name="en-us_topic_0057845638_a6f95694edbbb43d8a152536754b86c82_7"></a><a name="en-us_topic_0057845638_a6f95694edbbb43d8a152536754b86c82_7"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.45%" id="mcps1.1.5.1.2"><p id="en-us_topic_0057845638_p88525332215"><a name="en-us_topic_0057845638_p88525332215"></a><a name="en-us_topic_0057845638_p88525332215"></a><strong id="en-us_topic_0057845638_b1670597098"><a name="en-us_topic_0057845638_b1670597098"></a><a name="en-us_topic_0057845638_b1670597098"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.91%" id="mcps1.1.5.1.3"><p id="en-us_topic_0057845638_p14856183320218"><a name="en-us_topic_0057845638_p14856183320218"></a><a name="en-us_topic_0057845638_p14856183320218"></a><strong id="en-us_topic_0057845638_b14476260"><a name="en-us_topic_0057845638_b14476260"></a><a name="en-us_topic_0057845638_b14476260"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.83%" id="mcps1.1.5.1.4"><p id="en-us_topic_0057845638_p286173320218"><a name="en-us_topic_0057845638_p286173320218"></a><a name="en-us_topic_0057845638_p286173320218"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057845638_row3863153311217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p88666332215"><a name="en-us_topic_0057845638_p88666332215"></a><a name="en-us_topic_0057845638_p88666332215"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p386916336212"><a name="en-us_topic_0057845638_p386916336212"></a><a name="en-us_topic_0057845638_p386916336212"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p7871123352112"><a name="en-us_topic_0057845638_p7871123352112"></a><a name="en-us_topic_0057845638_p7871123352112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p6874133172114"><a name="en-us_topic_0057845638_p6874133172114"></a><a name="en-us_topic_0057845638_p6874133172114"></a>Description for a user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row128753339212"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p18877113392115"><a name="en-us_topic_0057845638_p18877113392115"></a><a name="en-us_topic_0057845638_p18877113392115"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p1487933362114"><a name="en-us_topic_0057845638_p1487933362114"></a><a name="en-us_topic_0057845638_p1487933362114"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p1388513334213"><a name="en-us_topic_0057845638_p1388513334213"></a><a name="en-us_topic_0057845638_p1388513334213"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p3888143315211"><a name="en-us_topic_0057845638_p3888143315211"></a><a name="en-us_topic_0057845638_p3888143315211"></a>ID of the tenant that the user belongs to.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row089017338215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p1389315339212"><a name="en-us_topic_0057845638_p1389315339212"></a><a name="en-us_topic_0057845638_p1389315339212"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p3896123318213"><a name="en-us_topic_0057845638_p3896123318213"></a><a name="en-us_topic_0057845638_p3896123318213"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p13899103317210"><a name="en-us_topic_0057845638_p13899103317210"></a><a name="en-us_topic_0057845638_p13899103317210"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p12901113312215"><a name="en-us_topic_0057845638_p12901113312215"></a><a name="en-us_topic_0057845638_p12901113312215"></a>Indicates whether the user is enabled. The value can be <strong id="en-us_topic_0057845638_b0372455203917"><a name="en-us_topic_0057845638_b0372455203917"></a><a name="en-us_topic_0057845638_b0372455203917"></a>true</strong> or <strong id="en-us_topic_0057845638_b4751556173915"><a name="en-us_topic_0057845638_b4751556173915"></a><a name="en-us_topic_0057845638_b4751556173915"></a>false</strong>. The default value is <strong id="en-us_topic_0057845638_b74111258193916"><a name="en-us_topic_0057845638_b74111258193916"></a><a name="en-us_topic_0057845638_b74111258193916"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row29030337213"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p890513302110"><a name="en-us_topic_0057845638_p890513302110"></a><a name="en-us_topic_0057845638_p890513302110"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p189081733112118"><a name="en-us_topic_0057845638_p189081733112118"></a><a name="en-us_topic_0057845638_p189081733112118"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p691093332117"><a name="en-us_topic_0057845638_p691093332117"></a><a name="en-us_topic_0057845638_p691093332117"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p091212333214"><a name="en-us_topic_0057845638_p091212333214"></a><a name="en-us_topic_0057845638_p091212333214"></a>User ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row20913123342114"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p1391415332215"><a name="en-us_topic_0057845638_p1391415332215"></a><a name="en-us_topic_0057845638_p1391415332215"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p391693315216"><a name="en-us_topic_0057845638_p391693315216"></a><a name="en-us_topic_0057845638_p391693315216"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p189191933182113"><a name="en-us_topic_0057845638_p189191933182113"></a><a name="en-us_topic_0057845638_p189191933182113"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p192211334219"><a name="en-us_topic_0057845638_p192211334219"></a><a name="en-us_topic_0057845638_p192211334219"></a>User resource links.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row179247335217"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p119261133192110"><a name="en-us_topic_0057845638_p119261133192110"></a><a name="en-us_topic_0057845638_p119261133192110"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p189291933142116"><a name="en-us_topic_0057845638_p189291933142116"></a><a name="en-us_topic_0057845638_p189291933142116"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p493213315214"><a name="en-us_topic_0057845638_p493213315214"></a><a name="en-us_topic_0057845638_p493213315214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p29351333192112"><a name="en-us_topic_0057845638_p29351333192112"></a><a name="en-us_topic_0057845638_p29351333192112"></a>Username</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row193643316211"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p1393815334212"><a name="en-us_topic_0057845638_p1393815334212"></a><a name="en-us_topic_0057845638_p1393815334212"></a>password_expires_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p1194143312119"><a name="en-us_topic_0057845638_p1194143312119"></a><a name="en-us_topic_0057845638_p1194143312119"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p18943633142112"><a name="en-us_topic_0057845638_p18943633142112"></a><a name="en-us_topic_0057845638_p18943633142112"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p294619332218"><a name="en-us_topic_0057845638_p294619332218"></a><a name="en-us_topic_0057845638_p294619332218"></a>UTC time when the password will expire. <strong id="en-us_topic_0057845638_b1483686226114627"><a name="en-us_topic_0057845638_b1483686226114627"></a><a name="en-us_topic_0057845638_b1483686226114627"></a>null</strong> indicates that the password will not expire.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row294912331214"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p17951143302120"><a name="en-us_topic_0057845638_p17951143302120"></a><a name="en-us_topic_0057845638_p17951143302120"></a>pwd_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p11955533102116"><a name="en-us_topic_0057845638_p11955533102116"></a><a name="en-us_topic_0057845638_p11955533102116"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p29573333214"><a name="en-us_topic_0057845638_p29573333214"></a><a name="en-us_topic_0057845638_p29573333214"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p09601033172120"><a name="en-us_topic_0057845638_p09601033172120"></a><a name="en-us_topic_0057845638_p09601033172120"></a>Password status. <strong id="en-us_topic_0057845638_b355111133319"><a name="en-us_topic_0057845638_b355111133319"></a><a name="en-us_topic_0057845638_b355111133319"></a>true</strong> means that the password needs to be changed, and <strong id="en-us_topic_0057845638_b11550112333"><a name="en-us_topic_0057845638_b11550112333"></a><a name="en-us_topic_0057845638_b11550112333"></a>false</strong> means that the password is normal.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row496283313218"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p179691433202117"><a name="en-us_topic_0057845638_p179691433202117"></a><a name="en-us_topic_0057845638_p179691433202117"></a>pwd_strength</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p15972333142118"><a name="en-us_topic_0057845638_p15972333142118"></a><a name="en-us_topic_0057845638_p15972333142118"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p14974113312218"><a name="en-us_topic_0057845638_p14974113312218"></a><a name="en-us_topic_0057845638_p14974113312218"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p69781233112115"><a name="en-us_topic_0057845638_p69781233112115"></a><a name="en-us_topic_0057845638_p69781233112115"></a>Password strength. The value can be <strong id="en-us_topic_0057845638_b153847174517"><a name="en-us_topic_0057845638_b153847174517"></a><a name="en-us_topic_0057845638_b153847174517"></a>high</strong>, <strong id="en-us_topic_0057845638_b8634162184518"><a name="en-us_topic_0057845638_b8634162184518"></a><a name="en-us_topic_0057845638_b8634162184518"></a>mid</strong>, or <strong id="en-us_topic_0057845638_b107749304513"><a name="en-us_topic_0057845638_b107749304513"></a><a name="en-us_topic_0057845638_b107749304513"></a>low</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row3979173362110"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p16982433112119"><a name="en-us_topic_0057845638_p16982433112119"></a><a name="en-us_topic_0057845638_p16982433112119"></a>mobile</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p179855333218"><a name="en-us_topic_0057845638_p179855333218"></a><a name="en-us_topic_0057845638_p179855333218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p1198913337219"><a name="en-us_topic_0057845638_p1198913337219"></a><a name="en-us_topic_0057845638_p1198913337219"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p299293302113"><a name="en-us_topic_0057845638_p299293302113"></a><a name="en-us_topic_0057845638_p299293302113"></a>Mobile number of the user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row12993103382113"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p89961133152119"><a name="en-us_topic_0057845638_p89961133152119"></a><a name="en-us_topic_0057845638_p89961133152119"></a>email</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p159991333132113"><a name="en-us_topic_0057845638_p159991333132113"></a><a name="en-us_topic_0057845638_p159991333132113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p82153416214"><a name="en-us_topic_0057845638_p82153416214"></a><a name="en-us_topic_0057845638_p82153416214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p94153412215"><a name="en-us_topic_0057845638_p94153412215"></a><a name="en-us_topic_0057845638_p94153412215"></a>Email address of the user.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row1851134102111"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p1671834142117"><a name="en-us_topic_0057845638_p1671834142117"></a><a name="en-us_topic_0057845638_p1671834142117"></a>forceResetPwd</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p2101534142113"><a name="en-us_topic_0057845638_p2101534142113"></a><a name="en-us_topic_0057845638_p2101534142113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p1412133452113"><a name="en-us_topic_0057845638_p1412133452113"></a><a name="en-us_topic_0057845638_p1412133452113"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p1015173472110"><a name="en-us_topic_0057845638_p1015173472110"></a><a name="en-us_topic_0057845638_p1015173472110"></a>Indicates whether password reset is required at the next login.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row1161234152117"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p519173417211"><a name="en-us_topic_0057845638_p519173417211"></a><a name="en-us_topic_0057845638_p519173417211"></a>default_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p18213344218"><a name="en-us_topic_0057845638_p18213344218"></a><a name="en-us_topic_0057845638_p18213344218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p423193420211"><a name="en-us_topic_0057845638_p423193420211"></a><a name="en-us_topic_0057845638_p423193420211"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p1925143462116"><a name="en-us_topic_0057845638_p1925143462116"></a><a name="en-us_topic_0057845638_p1925143462116"></a>ID of the project that is displayed by default when the user logs in to the console.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057845638_row9263348215"><td class="cellrowborder" valign="top" width="19.81%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0057845638_p1330334112110"><a name="en-us_topic_0057845638_p1330334112110"></a><a name="en-us_topic_0057845638_p1330334112110"></a>last_project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.45%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0057845638_p1232193418212"><a name="en-us_topic_0057845638_p1232193418212"></a><a name="en-us_topic_0057845638_p1232193418212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.91%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0057845638_p17361734142110"><a name="en-us_topic_0057845638_p17361734142110"></a><a name="en-us_topic_0057845638_p17361734142110"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.83%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0057845638_p203843472112"><a name="en-us_topic_0057845638_p203843472112"></a><a name="en-us_topic_0057845638_p203843472112"></a>ID of the project that the user lastly accessed before exiting the system.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "users": [{
            "name": "username",
            "links": {
                "self": "https://sample.domain.com/v3/users/6d8b04e3bf99445b8f76300xxx"
            },
            "description": "1234",
            "domain_id": "88b16b6440684467b8825d7xxx",
            "enabled": false,
            "id": "6d8b04e3bf99445b8f763009xxx",
            "default_project_id": "263fd9",
            "password_expires_at": "2016-12-07T00:00:00.000000Z",
            "pwd_status": true,
            "pwd_strength": "high",
            "mobile": "",
            "email": "",
            "forceResetPwd": false,
            "last_project_id": ""
        }],
        "links": {
            "self": "https://sample.domain.com/v3/users?domain_id=88b16b6440684467b882xxx154d8&enabled=false",
            "previous": null,
            "next": null
        }
    }
    ```


## Status Codes<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b54569330171957"><a name="b54569330171957"></a><a name="b54569330171957"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b842352706114032_11"><a name="b842352706114032_11"></a><a name="b842352706114032_11"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0032920307_row24305815"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p22613965"><a name="en-us_topic_0032920307_p22613965"></a><a name="en-us_topic_0032920307_p22613965"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p19791876"><a name="en-us_topic_0032920307_p19791876"></a><a name="en-us_topic_0032920307_p19791876"></a>The request is successful.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row43909159"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p66980994"><a name="en-us_topic_0032920307_p66980994"></a><a name="en-us_topic_0032920307_p66980994"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p56751409"><a name="en-us_topic_0032920307_p56751409"></a><a name="en-us_topic_0032920307_p56751409"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row460808479497"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p120744399497"><a name="p120744399497"></a><a name="p120744399497"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p385055099497"><a name="p385055099497"></a><a name="p385055099497"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="en-us_topic_0032920307_row41000636"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0032920307_p32717189"><a name="en-us_topic_0032920307_p32717189"></a><a name="en-us_topic_0032920307_p32717189"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0032920307_p32846614"><a name="en-us_topic_0032920307_p32846614"></a><a name="en-us_topic_0032920307_p32846614"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row2569718985351"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2994811485351"><a name="p2994811485351"></a><a name="p2994811485351"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p987817085351"><a name="p987817085351"></a><a name="p987817085351"></a>The server could not find the requested page.</p>
</td>
</tr>
</tbody>
</table>


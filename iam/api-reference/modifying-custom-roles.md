# Modifying Custom Roles<a name="EN-US_TOPIC_0147658933"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to modify a custom role.

## URI<a name="section3019338085013"></a>

-   URI format

    PATCH /v3.0/OS-ROLE/roles/\{role\_id\}

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706113951"><a name="b842352706113951"></a><a name="b842352706113951"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.189999999999998%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b7930731103215"><a name="b7930731103215"></a><a name="b7930731103215"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.5%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>role_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.189999999999998%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.5%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>ID of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="table5300449510340"></a>
    <table><thead align="left"><tr id="row1039042410340"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="p4664845010340"><a name="p4664845010340"></a><a name="p4664845010340"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="p2042812910340"><a name="p2042812910340"></a><a name="p2042812910340"></a><strong id="b13634202633213_1"><a name="b13634202633213_1"></a><a name="b13634202633213_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.91%" id="mcps1.1.5.1.3"><p id="p4406574810340"><a name="p4406574810340"></a><a name="p4406574810340"></a><strong id="b1506887119"><a name="b1506887119"></a><a name="b1506887119"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.74%" id="mcps1.1.5.1.4"><p id="p1255584410340"><a name="p1255584410340"></a><a name="p1255584410340"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2072124010340"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p3631800910340"><a name="p3631800910340"></a><a name="p3631800910340"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p5607758210340"><a name="p5607758210340"></a><a name="p5607758210340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.3 "><p id="p4599027110340"><a name="p4599027110340"></a><a name="p4599027110340"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.74%" headers="mcps1.1.5.1.4 "><p id="p3422450210340"><a name="p3422450210340"></a><a name="p3422450210340"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="row3753952210340"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p5227343810340"><a name="p5227343810340"></a><a name="p5227343810340"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p629006210340"><a name="p629006210340"></a><a name="p629006210340"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.1.5.1.3 "><p id="p3973302310340"><a name="p3973302310340"></a><a name="p3973302310340"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.74%" headers="mcps1.1.5.1.4 "><p id="p42128747112955"><a name="p42128747112955"></a><a name="p42128747112955"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request body parameter description

    <a name="table20476227103839"></a>
    <table><thead align="left"><tr id="row27191649103839"><th class="cellrowborder" valign="top" width="19.490000000000002%" id="mcps1.1.5.1.1"><p id="p55039964103839"><a name="p55039964103839"></a><a name="p55039964103839"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.860000000000003%" id="mcps1.1.5.1.2"><p id="p29052075103839"><a name="p29052075103839"></a><a name="p29052075103839"></a><strong id="b1044408467"><a name="b1044408467"></a><a name="b1044408467"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17%" id="mcps1.1.5.1.3"><p id="p4407863103839"><a name="p4407863103839"></a><a name="p4407863103839"></a><strong id="b1128963095"><a name="b1128963095"></a><a name="b1128963095"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.480000000000004%" id="mcps1.1.5.1.4"><p id="p21492583103839"><a name="p21492583103839"></a><a name="p21492583103839"></a><strong id="b1223575483"><a name="b1223575483"></a><a name="b1223575483"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63177635103839"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p17114836103839"><a name="p17114836103839"></a><a name="p17114836103839"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p44124514103839"><a name="p44124514103839"></a><a name="p44124514103839"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p17315892103839"><a name="p17315892103839"></a><a name="p17315892103839"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p60410035103839"><a name="p60410035103839"></a><a name="p60410035103839"></a>Request body of a user group.</p>
    </td>
    </tr>
    <tr id="row6819406103839"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p15501051103839"><a name="p15501051103839"></a><a name="p15501051103839"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p47625608103839"><a name="p47625608103839"></a><a name="p47625608103839"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p32469021103839"><a name="p32469021103839"></a><a name="p32469021103839"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p12745059103839"><a name="p12745059103839"></a><a name="p12745059103839"></a>Displayed name of a role. The value cannot exceed 64 characters.</p>
    </td>
    </tr>
    <tr id="row60192972103433"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p58438405103441"><a name="p58438405103441"></a><a name="p58438405103441"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p35890370103441"><a name="p35890370103441"></a><a name="p35890370103441"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p21438876103441"><a name="p21438876103441"></a><a name="p21438876103441"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p58827386103441"><a name="p58827386103441"></a><a name="p58827386103441"></a>Display mode of a role.</p>
    <a name="ul59684430103441"></a><a name="ul59684430103441"></a><ul id="ul59684430103441"><li><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.<div class="note" id="note6156094517252"><a name="note6156094517252"></a><a name="note6156094517252"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22955343165917"><a name="p22955343165917"></a><a name="p22955343165917"></a>The display mode of a role can only be <strong id="b84235270610383"><a name="b84235270610383"></a><a name="b84235270610383"></a>AX</strong> or <strong id="b84235270610386"><a name="b84235270610386"></a><a name="b84235270610386"></a>XA</strong>. A role cannot be displayed at both the domain and project layers or neither of the two layers. That is, neither <strong id="b842352706104236"><a name="b842352706104236"></a><a name="b842352706104236"></a>AA</strong> nor <strong id="b842352706104526"><a name="b842352706104526"></a><a name="b842352706104526"></a>XX</strong> is allowed.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row5662163914486"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p1766203911486"><a name="p1766203911486"></a><a name="p1766203911486"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p11662103914818"><a name="p11662103914818"></a><a name="p11662103914818"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p19663139124819"><a name="p19663139124819"></a><a name="p19663139124819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p116631239124811"><a name="p116631239124811"></a><a name="p116631239124811"></a>Description of a role. The value cannot exceed 256 characters.</p>
    </td>
    </tr>
    <tr id="row29609315103946"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p65157251103946"><a name="p65157251103946"></a><a name="p65157251103946"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p43245998103946"><a name="p43245998103946"></a><a name="p43245998103946"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p13264962103946"><a name="p13264962103946"></a><a name="p13264962103946"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p720101103946"><a name="p720101103946"></a><a name="p720101103946"></a>Permission policy of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the policy format

    <a name="table91819610348"></a>
    <table><thead align="left"><tr id="row4910255010348"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.1.5.1.1"><p id="p3416513010511"><a name="p3416513010511"></a><a name="p3416513010511"></a><strong id="b515887819"><a name="b515887819"></a><a name="b515887819"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.1.5.1.2"><p id="p1591217110511"><a name="p1591217110511"></a><a name="p1591217110511"></a><strong id="b89386817"><a name="b89386817"></a><a name="b89386817"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="p1381751310511"><a name="p1381751310511"></a><a name="p1381751310511"></a><strong id="b1926003350"><a name="b1926003350"></a><a name="b1926003350"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.269999999999996%" id="mcps1.1.5.1.4"><p id="p4547677910511"><a name="p4547677910511"></a><a name="p4547677910511"></a><strong id="b1234948779"><a name="b1234948779"></a><a name="b1234948779"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1795602910348"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p4515225510348"><a name="p4515225510348"></a><a name="p4515225510348"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.2 "><p id="p3345406210348"><a name="p3345406210348"></a><a name="p3345406210348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p39012936101229"><a name="p39012936101229"></a><a name="p39012936101229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p4611838510348"><a name="p4611838510348"></a><a name="p4611838510348"></a>Version of a policy. The value must be <strong id="b842352706173323"><a name="b842352706173323"></a><a name="b842352706173323"></a>1.1</strong>.</p>
    </td>
    </tr>
    <tr id="row1241228310348"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p6587084810348"><a name="p6587084810348"></a><a name="p6587084810348"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.2 "><p id="p3393848610348"><a name="p3393848610348"></a><a name="p3393848610348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p906005101236"><a name="p906005101236"></a><a name="p906005101236"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p319969910348"><a name="p319969910348"></a><a name="p319969910348"></a>Statement for using the policy to grant permissions. A policy consists of a maximum of eight statements. A <strong id="b842352706173423"><a name="b842352706173423"></a><a name="b842352706173423"></a>Statement</strong> field contains the <strong id="b842352706173420"><a name="b842352706173420"></a><a name="b842352706173420"></a>Effect</strong> and <strong id="b842352706173427"><a name="b842352706173427"></a><a name="b842352706173427"></a>Action</strong> elements.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the statement format

    <a name="table5858327510641"></a>
    <table><thead align="left"><tr id="row234853010641"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.1.5.1.1"><p id="p5601325710641"><a name="p5601325710641"></a><a name="p5601325710641"></a><strong id="b38745935"><a name="b38745935"></a><a name="b38745935"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.58%" id="mcps1.1.5.1.2"><p id="p4077999710641"><a name="p4077999710641"></a><a name="p4077999710641"></a><strong id="b1352329528"><a name="b1352329528"></a><a name="b1352329528"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.48%" id="mcps1.1.5.1.3"><p id="p1484546110641"><a name="p1484546110641"></a><a name="p1484546110641"></a><strong id="b1515870198"><a name="b1515870198"></a><a name="b1515870198"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.11%" id="mcps1.1.5.1.4"><p id="p6163170610641"><a name="p6163170610641"></a><a name="p6163170610641"></a><strong id="b1932279032"><a name="b1932279032"></a><a name="b1932279032"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2611227510641"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p3471952910641"><a name="p3471952910641"></a><a name="p3471952910641"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.1.5.1.2 "><p id="p6081843510641"><a name="p6081843510641"></a><a name="p6081843510641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p51739175101251"><a name="p51739175101251"></a><a name="p51739175101251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.1.5.1.4 "><p id="p44854910641"><a name="p44854910641"></a><a name="p44854910641"></a>The value can be <strong id="b8423527061142"><a name="b8423527061142"></a><a name="b8423527061142"></a>Allow</strong> and <strong id="b8423527061138"><a name="b8423527061138"></a><a name="b8423527061138"></a>Deny</strong>. If both <strong id="b8423527061734_1"><a name="b8423527061734_1"></a><a name="b8423527061734_1"></a>Allow</strong> and <strong id="b8423527061732_1"><a name="b8423527061732_1"></a><a name="b8423527061732_1"></a>Deny</strong> are found in statements, the policy evaluation starts with <strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>Deny</strong>.</p>
    </td>
    </tr>
    <tr id="row403694110641"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p15866909101431"><a name="p15866909101431"></a><a name="p15866909101431"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.1.5.1.2 "><p id="p10151214101431"><a name="p10151214101431"></a><a name="p10151214101431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p90575969132"><a name="p90575969132"></a><a name="p90575969132"></a>StringArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.1.5.1.4 "><p id="p30124746101431"><a name="p30124746101431"></a><a name="p30124746101431"></a>Permission set, which specifies the operation permissions on resources. The number of permission sets cannot exceed 100.</p>
    <p id="p2055674702610"><a name="p2055674702610"></a><a name="p2055674702610"></a>Format:</p>
    <p id="p2687264101431"><a name="p2687264101431"></a><a name="p2687264101431"></a>The value format is <em id="i84235269723526"><a name="i84235269723526"></a><a name="i84235269723526"></a>Service name</em>:<em id="i84235269723639"><a name="i84235269723639"></a><a name="i84235269723639"></a>Resource type</em>:<em id="i84235269723534"><a name="i84235269723534"></a><a name="i84235269723534"></a>Action</em>, for example, <strong id="b842352706165816"><a name="b842352706165816"></a><a name="b842352706165816"></a>vpc:ports:create</strong>.</p>
    <p id="p24185381101431"><a name="p24185381101431"></a><a name="p24185381101431"></a><em id="i84235269711017"><a name="i84235269711017"></a><a name="i84235269711017"></a>Service name</em>: indicates the product name, such as <strong id="b1194612119195"><a name="b1194612119195"></a><a name="b1194612119195"></a>ecs</strong>, <strong id="b9388113991919"><a name="b9388113991919"></a><a name="b9388113991919"></a>evs</strong>, or <strong id="b3519155131912"><a name="b3519155131912"></a><a name="b3519155131912"></a>vpc</strong>. Only lowercase letters are allowed.</p>
    <p id="p16341842101431"><a name="p16341842101431"></a><a name="p16341842101431"></a><em id="i84235269710240"><a name="i84235269710240"></a><a name="i84235269710240"></a>Resource type</em> and <em id="i84235269710254"><a name="i84235269710254"></a><a name="i84235269710254"></a>Action</em>: The values are case-insensitive, and the wildcard (*) is allowed. A wildcard (*) can represent all or part of information about resource types and actions for the specific service.</p>
    </td>
    </tr>
    <tr id="row63666123121"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p1636641216127"><a name="p1636641216127"></a><a name="p1636641216127"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.58%" headers="mcps1.1.5.1.2 "><p id="p83664127126"><a name="p83664127126"></a><a name="p83664127126"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.1.5.1.3 "><p id="p1936616124128"><a name="p1936616124128"></a><a name="p1936616124128"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.11%" headers="mcps1.1.5.1.4 "><a name="ul19197153611218"></a><a name="ul19197153611218"></a><ul id="ul19197153611218"><li>Resources to be managed. After a domain establishes multiple trust relationships between itself and your domain, you can authorize different users to manage resources of the delegating party. Each user can only switch to the specified agencies. You can create custom policies to assign specified permissions to users.</li><li>When creating a custom policy, specify the <strong id="b2091110591413"><a name="b2091110591413"></a><a name="b2091110591413"></a>Action</strong> as <strong id="b1791214591019"><a name="b1791214591019"></a><a name="b1791214591019"></a>iam:agencies:assume</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    -   Format description of the Resource parameter

        <a name="table755284212333"></a>
        <table><thead align="left"><tr id="row855217422337"><th class="cellrowborder" valign="top" width="19.52%" id="mcps1.1.5.1.1"><p id="p5552184233312"><a name="p5552184233312"></a><a name="p5552184233312"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.2"><p id="p6552242193314"><a name="p6552242193314"></a><a name="p6552242193314"></a><strong id="b471407491"><a name="b471407491"></a><a name="b471407491"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="17.79%" id="mcps1.1.5.1.3"><p id="p65531427338"><a name="p65531427338"></a><a name="p65531427338"></a><strong id="b1413283782"><a name="b1413283782"></a><a name="b1413283782"></a>Type</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="43.8%" id="mcps1.1.5.1.4"><p id="p135531542163310"><a name="p135531542163310"></a><a name="p135531542163310"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1955313429331"><td class="cellrowborder" valign="top" width="19.52%" headers="mcps1.1.5.1.1 "><p id="p195532423339"><a name="p195532423339"></a><a name="p195532423339"></a>uri</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.2 "><p id="p2553134203312"><a name="p2553134203312"></a><a name="p2553134203312"></a>Yes</p>
        </td>
        <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p7553642193315"><a name="p7553642193315"></a><a name="p7553642193315"></a>StringArray</p>
        </td>
        <td class="cellrowborder" valign="top" width="43.8%" headers="mcps1.1.5.1.4 "><p id="p1715635317473"><a name="p1715635317473"></a><a name="p1715635317473"></a>URI of a resource, which can contain a maximum of 128 characters.</p>
        <p id="p1355354283311"><a name="p1355354283311"></a><a name="p1355354283311"></a>Format: /iam/agencies/{<em id="i1214010814218"><a name="i1214010814218"></a><a name="i1214010814218"></a>agency ID</em>}</p>
        </td>
        </tr>
        </tbody>
        </table>



-   Sample request \(custom policy for a cloud service\)

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PATCH -d'{"role":{"display_name":"Customed ECS Viewer","policy":{"Version":"1.1","Statement":[{"Action":["ecs:*:get*","ecs:*:list*","ecs:blockDevice:use","ecs:serverGroups:manage","ecs:serverVolumes:use","evs:*:get*","evs:*:list*","vpc:*:get*","vpc:*:list*","ims:*:get*","ims:*:list*"],"Effect":"Allow"}]},"type":"XA","description":"The read-only permissions to all ECS resources,which can be used for statistics ands urvey."}}' https://10.22.44.158:31943/v3.0/OS-ROLE/roles/9698542758bc422088c0c3eabfc30d12
    ```


-   Sample request \(custom policy for an agency\)

    ```
    curl -i -k -H 'Accept:application/json' -H 'Content-Type:application/json;charset=utf8' -H "X-Auth-Token:$token" -X PATCH -d'{"role":{"display_name":"Customed fine-grained agency","policy":{"Version":"1.1","Statement":[{"Action":["iam:agencies:assume"],"Effect":"Allow","Resource":{"uri":["/iam/agencies/3459fd170b924c55add704fa0a3a50ec"]}}]},"type":"AX","description":"Allow sub-user to use agency."}}' https://10.22.44.158:31943/v3.0/OS-ROLE/roles/9698542758bc422088c0c3eabfc30d12
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table152994212185"></a>
    <table><thead align="left"><tr id="row173714281818"><th class="cellrowborder" valign="top" width="19.75%" id="mcps1.1.5.1.1"><p id="p5372426180"><a name="p5372426180"></a><a name="p5372426180"></a><strong id="b1192381399"><a name="b1192381399"></a><a name="b1192381399"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.55%" id="mcps1.1.5.1.2"><p id="p1056617720581"><a name="p1056617720581"></a><a name="p1056617720581"></a><strong id="b1007459660"><a name="b1007459660"></a><a name="b1007459660"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.36%" id="mcps1.1.5.1.3"><p id="p15441142151819"><a name="p15441142151819"></a><a name="p15441142151819"></a><strong id="b930082205"><a name="b930082205"></a><a name="b930082205"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.34%" id="mcps1.1.5.1.4"><p id="p7463424187"><a name="p7463424187"></a><a name="p7463424187"></a><strong id="b131311940"><a name="b131311940"></a><a name="b131311940"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1948142191819"><td class="cellrowborder" valign="top" width="19.75%" headers="mcps1.1.5.1.1 "><p id="p205084221810"><a name="p205084221810"></a><a name="p205084221810"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p556717175819"><a name="p556717175819"></a><a name="p556717175819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.1.5.1.3 "><p id="p195510424182"><a name="p195510424182"></a><a name="p195510424182"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p195619421189"><a name="p195619421189"></a><a name="p195619421189"></a>Details of the role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the role format

    <a name="table11611242141815"></a>
    <table><thead align="left"><tr id="row13671142131817"><th class="cellrowborder" valign="top" width="19.67%" id="mcps1.1.5.1.1"><p id="p16994231814"><a name="p16994231814"></a><a name="p16994231814"></a><strong id="b16646705155652"><a name="b16646705155652"></a><a name="b16646705155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.33%" id="mcps1.1.5.1.2"><p id="p47406710214141"><a name="p47406710214141"></a><a name="p47406710214141"></a><strong id="b183610741"><a name="b183610741"></a><a name="b183610741"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52%" id="mcps1.1.5.1.3"><p id="p47416427185"><a name="p47416427185"></a><a name="p47416427185"></a><strong id="b857629909"><a name="b857629909"></a><a name="b857629909"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.48%" id="mcps1.1.5.1.4"><p id="p1576124212185"><a name="p1576124212185"></a><a name="p1576124212185"></a><strong id="b1964926461"><a name="b1964926461"></a><a name="b1964926461"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2718319318492"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p4332214818492"><a name="p4332214818492"></a><a name="p4332214818492"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p52491180214141"><a name="p52491180214141"></a><a name="p52491180214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p1943313718492"><a name="p1943313718492"></a><a name="p1943313718492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p3058025418492"><a name="p3058025418492"></a><a name="p3058025418492"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row185642121813"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p198724213181"><a name="p198724213181"></a><a name="p198724213181"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p20220752214141"><a name="p20220752214141"></a><a name="p20220752214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p1690194261820"><a name="p1690194261820"></a><a name="p1690194261820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p1193124219186"><a name="p1193124219186"></a><a name="p1193124219186"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row18941242151812"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p169614219187"><a name="p169614219187"></a><a name="p169614219187"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p64755119214141"><a name="p64755119214141"></a><a name="p64755119214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p119974291818"><a name="p119974291818"></a><a name="p119974291818"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p121019429189"><a name="p121019429189"></a><a name="p121019429189"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row1910211424181"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p210417429182"><a name="p210417429182"></a><a name="p210417429182"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p3095987214141"><a name="p3095987214141"></a><a name="p3095987214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p1210874251814"><a name="p1210874251814"></a><a name="p1210874251814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p141091842191813"><a name="p141091842191813"></a><a name="p141091842191813"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row1548265115236"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p5745115415230"><a name="p5745115415230"></a><a name="p5745115415230"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p7745175432314"><a name="p7745175432314"></a><a name="p7745175432314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p147452546233"><a name="p147452546233"></a><a name="p147452546233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p1429292915554"><a name="p1429292915554"></a><a name="p1429292915554"></a>Display mode of a role.</p>
    <a name="ul32219201103535"></a><a name="ul32219201103535"></a><ul id="ul32219201103535"><li><strong id="b388586646"><a name="b388586646"></a><a name="b388586646"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b1249233059"><a name="b1249233059"></a><a name="b1249233059"></a>XA</strong>: A role is displayed at the project layer.</li></ul>
    </td>
    </tr>
    <tr id="row57645998214145"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p59369096214145"><a name="p59369096214145"></a><a name="p59369096214145"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p19319748214145"><a name="p19319748214145"></a><a name="p19319748214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p23075900214145"><a name="p23075900214145"></a><a name="p23075900214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p12999383214145"><a name="p12999383214145"></a><a name="p12999383214145"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row33977091214145"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p65673627214145"><a name="p65673627214145"></a><a name="p65673627214145"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p34536686214145"><a name="p34536686214145"></a><a name="p34536686214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p3673120214145"><a name="p3673120214145"></a><a name="p3673120214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p55700186214145"><a name="p55700186214145"></a><a name="p55700186214145"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row53576771214145"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p48279332214145"><a name="p48279332214145"></a><a name="p48279332214145"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p26134551214145"><a name="p26134551214145"></a><a name="p26134551214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p18445422214145"><a name="p18445422214145"></a><a name="p18445422214145"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p963217214145"><a name="p963217214145"></a><a name="p963217214145"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row28018958214145"><td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.1.5.1.1 "><p id="p5775123214145"><a name="p5775123214145"></a><a name="p5775123214145"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.33%" headers="mcps1.1.5.1.2 "><p id="p40003297214145"><a name="p40003297214145"></a><a name="p40003297214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p47954295214145"><a name="p47954295214145"></a><a name="p47954295214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p43833853214145"><a name="p43833853214145"></a><a name="p43833853214145"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response \(custom policy for a cloud service\)

    ```
    {
      "role": {
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "id": "24e7a89bffe443979760c4e9715c13a5",
          "links": {
            "self": "www.example.com/v3/roles/9698542758bc422088c0c3eabfc30d12"
          },
          "name": "custom_9698542758bc422088c0c3eabfc30d12_0",
          "type": "XA",
          "display_name": "Customed ECS Viewer",
          "catalog": "CUSTOMED",
          "policy": {
            "Version": "1.1",
            "Statement": [
              {
                "Action": [
                  "ecs:*:get*",
                  "ecs:*:list*",
                  "ecs:blockDevice:use",
                  "ecs:serverGroups:manage",
                  "ecs:serverVolumes:use",
                  "evs:*:get*",
                  "evs:*:list*",
                  "vpc:*:get*",
                  "vpc:*:list*",
                  "ims:*:get*",
                  "ims:*:list*"
                ],
                "Effect": "Allow"
              }
            ]
          },
          "description": "The read-only permissions to all ECS resources, which can be used for statistics and survey."
        }
    }
    ```


-   Sample response \(custom policy for an agency\)

    ```
    {
      "role": {
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "id": "5c03c324d4784435baaedb6a9bf01321",
          "links": {
            "self": "www.example.com/v3/roles/9698542758bc422088c0c3eabfc30d12"
          },
          "name": "custom_9698542758bc422088c0c3eabfc30d12_1",
          "type": "AX",
          "display_name": "Customed fine-grained agency",
          "catalog": "CUSTOMED",
          "policy": {
            "Version": "1.1",
            "Statement": [
              {
                "Action": [
                  "iam:agencies:assume"
                ],
                "Effect": "Allow",
                "Resource": {
                "uri": [
                  "/iam/agencies/3459fd170b924c55add704fa0a3a50ec"
                ]
               }
              }
            ]
          },
          "description": "Allow sub-user to use agency."
        }
    }
    ```


-   Error response body parameter description

    <a name="table11369132715418"></a>
    <table><thead align="left"><tr id="row1937712715414"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p1237819270542"><a name="p1237819270542"></a><a name="p1237819270542"></a><strong id="b237608126"><a name="b237608126"></a><a name="b237608126"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p338319273549"><a name="p338319273549"></a><a name="p338319273549"></a><strong id="b352746258"><a name="b352746258"></a><a name="b352746258"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p15386152755413"><a name="p15386152755413"></a><a name="p15386152755413"></a><strong id="b1406939196"><a name="b1406939196"></a><a name="b1406939196"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p538916276547"><a name="p538916276547"></a><a name="p538916276547"></a><strong id="b1056755463"><a name="b1056755463"></a><a name="b1056755463"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row93911227135417"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p339310274543"><a name="p339310274543"></a><a name="p339310274543"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p16394152716546"><a name="p16394152716546"></a><a name="p16394152716546"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p1339662755417"><a name="p1339662755417"></a><a name="p1339662755417"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1397172725415"><a name="p1397172725415"></a><a name="p1397172725415"></a>Response error</p>
    </td>
    </tr>
    <tr id="row18399927115419"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1024473095615"><a name="p1024473095615"></a><a name="p1024473095615"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1740352725417"><a name="p1740352725417"></a><a name="p1740352725417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p84051327155415"><a name="p84051327155415"></a><a name="p84051327155415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p154064276547"><a name="p154064276547"></a><a name="p154064276547"></a>Error details</p>
    </td>
    </tr>
    <tr id="row372143818575"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p157237386575"><a name="p157237386575"></a><a name="p157237386575"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p1723193895712"><a name="p1723193895712"></a><a name="p1723193895712"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p472318381579"><a name="p472318381579"></a><a name="p472318381579"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1172313855711"><a name="p1172313855711"></a><a name="p1172313855711"></a>Status code</p>
    </td>
    </tr>
    <tr id="row12320192018583"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p1132012017585"><a name="p1132012017585"></a><a name="p1132012017585"></a>title</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p9320122095810"><a name="p9320122095810"></a><a name="p9320122095810"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p2032082014581"><a name="p2032082014581"></a><a name="p2032082014581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p681134632"><a name="p681134632"></a><a name="p681134632"></a>Error type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(failed response\)

    ```
    {
      "error": {
        "message": "Authentication failed",
        "code": 401,
        "title": "Unauthorized"
      }
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b23486412155652"><a name="b23486412155652"></a><a name="b23486412155652"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0032920307_p16041657"><a name="en-us_topic_0032920307_p16041657"></a><a name="en-us_topic_0032920307_p16041657"></a><strong id="b20601766145329_9"><a name="b20601766145329_9"></a><a name="b20601766145329_9"></a>Description</strong></p>
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
<tr id="row16927104610415"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p19928204664112"><a name="p19928204664112"></a><a name="p19928204664112"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7928134664115"><a name="p7928134664115"></a><a name="p7928134664115"></a>The server could not find the requested page.</p>
</td>
</tr>
<tr id="row8522852174127"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p26754698174132"><a name="p26754698174132"></a><a name="p26754698174132"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p19646931174132"><a name="p19646931174132"></a><a name="p19646931174132"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>


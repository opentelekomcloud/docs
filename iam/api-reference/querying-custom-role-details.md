# Querying Custom Role Details<a name="EN-US_TOPIC_0147658858"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query custom role details, including the permission policies of a role.

## URI<a name="section3019338085013"></a>

-   URI format

    GET /v3.0/OS-ROLE/roles/\{role\_id\}

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You can also use  **GET /v3/roles/\{role\_id\}**  to query the detailed information about a custom role. For details, see  [Querying Role Details](querying-role-details.md).  

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706113951"><a name="b842352706113951"></a><a name="b842352706113951"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.24%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b7930731103215"><a name="b7930731103215"></a><a name="b7930731103215"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.32%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.080000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>role_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>ID of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.49%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="b13634202633213_1"><a name="b13634202633213_1"></a><a name="b13634202633213_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.299999999999997%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="p15987056112825"><a name="p15987056112825"></a><a name="p15987056112825"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    <tr id="row17416125164010"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p756284913314"><a name="p756284913314"></a><a name="p756284913314"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p1656219494334"><a name="p1656219494334"></a><a name="p1656219494334"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.299999999999997%" headers="mcps1.1.5.1.3 "><p id="p86097153416"><a name="p86097153416"></a><a name="p86097153416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="p95620493339"><a name="p95620493339"></a><a name="p95620493339"></a>Fill <strong id="b1830031716544"><a name="b1830031716544"></a><a name="b1830031716544"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request \(custom policy for a cloud service\)

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3.0/OS-ROLE/roles/24e7a89bffe443979760c4e9715c13a5
    ```


-   Sample request \(custom policy for an agency\)

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3.0/OS-ROLE/roles/5c03c324d4784435baaedb6a9bf01321
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table50419879102853"></a>
    <table><thead align="left"><tr id="row31663644102853"><th class="cellrowborder" valign="top" width="19.75%" id="mcps1.1.5.1.1"><p id="p18286183102853"><a name="p18286183102853"></a><a name="p18286183102853"></a><strong id="b1983936155652"><a name="b1983936155652"></a><a name="b1983936155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.42%" id="mcps1.1.5.1.2"><p id="p4785837102853"><a name="p4785837102853"></a><a name="p4785837102853"></a><strong id="b1693752015"><a name="b1693752015"></a><a name="b1693752015"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.62%" id="mcps1.1.5.1.3"><p id="p52108553102853"><a name="p52108553102853"></a><a name="p52108553102853"></a><strong id="b120012564"><a name="b120012564"></a><a name="b120012564"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.21%" id="mcps1.1.5.1.4"><p id="p60043232102853"><a name="p60043232102853"></a><a name="p60043232102853"></a><strong id="b947989563"><a name="b947989563"></a><a name="b947989563"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43887845102853"><td class="cellrowborder" valign="top" width="19.75%" headers="mcps1.1.5.1.1 "><p id="p14618405102853"><a name="p14618405102853"></a><a name="p14618405102853"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.42%" headers="mcps1.1.5.1.2 "><p id="p43240162102853"><a name="p43240162102853"></a><a name="p43240162102853"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.62%" headers="mcps1.1.5.1.3 "><p id="p12792252102853"><a name="p12792252102853"></a><a name="p12792252102853"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p29539482102853"><a name="p29539482102853"></a><a name="p29539482102853"></a>Details of the role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the role format

    <a name="table11611242141815"></a>
    <table><thead align="left"><tr id="row13671142131817"><th class="cellrowborder" valign="top" width="19.939999999999998%" id="mcps1.1.5.1.1"><p id="p16994231814"><a name="p16994231814"></a><a name="p16994231814"></a><strong id="b16646705155652"><a name="b16646705155652"></a><a name="b16646705155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.1.5.1.2"><p id="p47406710214141"><a name="p47406710214141"></a><a name="p47406710214141"></a><strong id="b1928710115"><a name="b1928710115"></a><a name="b1928710115"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.1.5.1.3"><p id="p47416427185"><a name="p47416427185"></a><a name="p47416427185"></a><strong id="b1774446474"><a name="b1774446474"></a><a name="b1774446474"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.080000000000005%" id="mcps1.1.5.1.4"><p id="p1576124212185"><a name="p1576124212185"></a><a name="p1576124212185"></a><strong id="b71732695"><a name="b71732695"></a><a name="b71732695"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2718319318492"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p4332214818492"><a name="p4332214818492"></a><a name="p4332214818492"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p52491180214141"><a name="p52491180214141"></a><a name="p52491180214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1943313718492"><a name="p1943313718492"></a><a name="p1943313718492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p3058025418492"><a name="p3058025418492"></a><a name="p3058025418492"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row185642121813"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p198724213181"><a name="p198724213181"></a><a name="p198724213181"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p20220752214141"><a name="p20220752214141"></a><a name="p20220752214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1690194261820"><a name="p1690194261820"></a><a name="p1690194261820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p1193124219186"><a name="p1193124219186"></a><a name="p1193124219186"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row18941242151812"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p169614219187"><a name="p169614219187"></a><a name="p169614219187"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p64755119214141"><a name="p64755119214141"></a><a name="p64755119214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p119974291818"><a name="p119974291818"></a><a name="p119974291818"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p121019429189"><a name="p121019429189"></a><a name="p121019429189"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row15685104816190"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p16851348171913"><a name="p16851348171913"></a><a name="p16851348171913"></a>references</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p8685948101920"><a name="p8685948101920"></a><a name="p8685948101920"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p36856483191"><a name="p36856483191"></a><a name="p36856483191"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p0686174891919"><a name="p0686174891919"></a><a name="p0686174891919"></a>Number of references.</p>
    </td>
    </tr>
    <tr id="row1910211424181"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p210417429182"><a name="p210417429182"></a><a name="p210417429182"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p3095987214141"><a name="p3095987214141"></a><a name="p3095987214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p1210874251814"><a name="p1210874251814"></a><a name="p1210874251814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p141091842191813"><a name="p141091842191813"></a><a name="p141091842191813"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row1548265115236"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p5745115415230"><a name="p5745115415230"></a><a name="p5745115415230"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p7745175432314"><a name="p7745175432314"></a><a name="p7745175432314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p147452546233"><a name="p147452546233"></a><a name="p147452546233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p10745554132312"><a name="p10745554132312"></a><a name="p10745554132312"></a>Display mode of a role.</p>
    <a name="ul1146623910286"></a><a name="ul1146623910286"></a><ul id="ul1146623910286"><li><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.<div class="note" id="note6156094517252"><a name="note6156094517252"></a><a name="note6156094517252"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22955343165917"><a name="p22955343165917"></a><a name="p22955343165917"></a>The display mode of a role can only be <strong id="b84235270610383"><a name="b84235270610383"></a><a name="b84235270610383"></a>AX</strong> or <strong id="b84235270610386"><a name="b84235270610386"></a><a name="b84235270610386"></a>XA</strong>. A role cannot be displayed at both the domain and project layers or neither of the two layers. That is, neither <strong id="b842352706104236"><a name="b842352706104236"></a><a name="b842352706104236"></a>AA</strong> nor <strong id="b842352706104526"><a name="b842352706104526"></a><a name="b842352706104526"></a>XX</strong> is allowed.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row57645998214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p59369096214145"><a name="p59369096214145"></a><a name="p59369096214145"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p19319748214145"><a name="p19319748214145"></a><a name="p19319748214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p23075900214145"><a name="p23075900214145"></a><a name="p23075900214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p12999383214145"><a name="p12999383214145"></a><a name="p12999383214145"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row33977091214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p65673627214145"><a name="p65673627214145"></a><a name="p65673627214145"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p34536686214145"><a name="p34536686214145"></a><a name="p34536686214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p3673120214145"><a name="p3673120214145"></a><a name="p3673120214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p55700186214145"><a name="p55700186214145"></a><a name="p55700186214145"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row53576771214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p48279332214145"><a name="p48279332214145"></a><a name="p48279332214145"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p26134551214145"><a name="p26134551214145"></a><a name="p26134551214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p18445422214145"><a name="p18445422214145"></a><a name="p18445422214145"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p963217214145"><a name="p963217214145"></a><a name="p963217214145"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row28018958214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p5775123214145"><a name="p5775123214145"></a><a name="p5775123214145"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p40003297214145"><a name="p40003297214145"></a><a name="p40003297214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.1.5.1.3 "><p id="p47954295214145"><a name="p47954295214145"></a><a name="p47954295214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.080000000000005%" headers="mcps1.1.5.1.4 "><p id="p43833853214145"><a name="p43833853214145"></a><a name="p43833853214145"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the policy format

    <a name="table91819610348"></a>
    <table><thead align="left"><tr id="row4910255010348"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.1.5.1.1"><p id="p3416513010511"><a name="p3416513010511"></a><a name="p3416513010511"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.11%" id="mcps1.1.5.1.2"><p id="p1591217110511"><a name="p1591217110511"></a><a name="p1591217110511"></a><strong id="b1651014773"><a name="b1651014773"></a><a name="b1651014773"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.79%" id="mcps1.1.5.1.3"><p id="p1381751310511"><a name="p1381751310511"></a><a name="p1381751310511"></a><strong id="b1000698017"><a name="b1000698017"></a><a name="b1000698017"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.269999999999996%" id="mcps1.1.5.1.4"><p id="p4547677910511"><a name="p4547677910511"></a><a name="p4547677910511"></a><strong id="b384872084"><a name="b384872084"></a><a name="b384872084"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1795602910348"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p4515225510348"><a name="p4515225510348"></a><a name="p4515225510348"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.1.5.1.2 "><p id="p3345406210348"><a name="p3345406210348"></a><a name="p3345406210348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p39012936101229"><a name="p39012936101229"></a><a name="p39012936101229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p4611838510348"><a name="p4611838510348"></a><a name="p4611838510348"></a>Version of a policy. The value must be <strong id="b842352706173323"><a name="b842352706173323"></a><a name="b842352706173323"></a>1.1</strong>.</p>
    </td>
    </tr>
    <tr id="row1241228310348"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.1.5.1.1 "><p id="p6587084810348"><a name="p6587084810348"></a><a name="p6587084810348"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.1.5.1.2 "><p id="p3393848610348"><a name="p3393848610348"></a><a name="p3393848610348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.79%" headers="mcps1.1.5.1.3 "><p id="p906005101236"><a name="p906005101236"></a><a name="p906005101236"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.269999999999996%" headers="mcps1.1.5.1.4 "><p id="p319969910348"><a name="p319969910348"></a><a name="p319969910348"></a>Statement for using the policy to grant permissions. A policy consists of a maximum of eight statements. A <strong id="b842352706173423"><a name="b842352706173423"></a><a name="b842352706173423"></a>Statement</strong> field contains the <strong id="b842352706173420"><a name="b842352706173420"></a><a name="b842352706173420"></a>Effect</strong> and <strong id="b842352706173427"><a name="b842352706173427"></a><a name="b842352706173427"></a>Action</strong> elements.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the statement format

    <a name="table5858327510641"></a>
    <table><thead align="left"><tr id="row234853010641"><th class="cellrowborder" valign="top" width="19.831983198319833%" id="mcps1.1.5.1.1"><p id="p5601325710641"><a name="p5601325710641"></a><a name="p5601325710641"></a><strong id="b49285753"><a name="b49285753"></a><a name="b49285753"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.95179517951795%" id="mcps1.1.5.1.2"><p id="p4077999710641"><a name="p4077999710641"></a><a name="p4077999710641"></a><strong id="b897392927"><a name="b897392927"></a><a name="b897392927"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.631763176317634%" id="mcps1.1.5.1.3"><p id="p1484546110641"><a name="p1484546110641"></a><a name="p1484546110641"></a><strong id="b351207863"><a name="b351207863"></a><a name="b351207863"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.58445844584458%" id="mcps1.1.5.1.4"><p id="p6163170610641"><a name="p6163170610641"></a><a name="p6163170610641"></a><strong id="b698097166"><a name="b698097166"></a><a name="b698097166"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2611227510641"><td class="cellrowborder" valign="top" width="19.831983198319833%" headers="mcps1.1.5.1.1 "><p id="p3471952910641"><a name="p3471952910641"></a><a name="p3471952910641"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.2 "><p id="p6081843510641"><a name="p6081843510641"></a><a name="p6081843510641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.631763176317634%" headers="mcps1.1.5.1.3 "><p id="p51739175101251"><a name="p51739175101251"></a><a name="p51739175101251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58445844584458%" headers="mcps1.1.5.1.4 "><p id="p44854910641"><a name="p44854910641"></a><a name="p44854910641"></a>The value can be <strong id="b8423527061142"><a name="b8423527061142"></a><a name="b8423527061142"></a>Allow</strong> and <strong id="b8423527061138"><a name="b8423527061138"></a><a name="b8423527061138"></a>Deny</strong>. If both <strong id="b8423527061734_1"><a name="b8423527061734_1"></a><a name="b8423527061734_1"></a>Allow</strong> and <strong id="b8423527061732_1"><a name="b8423527061732_1"></a><a name="b8423527061732_1"></a>Deny</strong> are found in statements, the policy evaluation starts with <strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>Deny</strong>.</p>
    </td>
    </tr>
    <tr id="row403694110641"><td class="cellrowborder" valign="top" width="19.831983198319833%" headers="mcps1.1.5.1.1 "><p id="p15866909101431"><a name="p15866909101431"></a><a name="p15866909101431"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.2 "><p id="p10151214101431"><a name="p10151214101431"></a><a name="p10151214101431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.631763176317634%" headers="mcps1.1.5.1.3 "><p id="p90575969132"><a name="p90575969132"></a><a name="p90575969132"></a>StringArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58445844584458%" headers="mcps1.1.5.1.4 "><p id="p2687264101431"><a name="p2687264101431"></a><a name="p2687264101431"></a></p>
    <p id="p127565452811"><a name="p127565452811"></a><a name="p127565452811"></a>Permission set, which specifies the operation permissions on resources. The number of permission sets cannot exceed 100.</p>
    <p id="p19358101314235"><a name="p19358101314235"></a><a name="p19358101314235"></a>Format:</p>
    <p id="p167617472813"><a name="p167617472813"></a><a name="p167617472813"></a>The value format is <em id="i84235269723526"><a name="i84235269723526"></a><a name="i84235269723526"></a>Service name</em>:<em id="i84235269723639"><a name="i84235269723639"></a><a name="i84235269723639"></a>Resource type</em>:<em id="i84235269723534"><a name="i84235269723534"></a><a name="i84235269723534"></a>Action</em>, for example, <strong id="b842352706165816"><a name="b842352706165816"></a><a name="b842352706165816"></a>vpc:ports:create</strong>.</p>
    <p id="p24185381101431"><a name="p24185381101431"></a><a name="p24185381101431"></a><em id="i84235269711017"><a name="i84235269711017"></a><a name="i84235269711017"></a>Service name</em>: indicates the product name, such as <strong id="b1194612119195"><a name="b1194612119195"></a><a name="b1194612119195"></a>ecs</strong>, <strong id="b9388113991919"><a name="b9388113991919"></a><a name="b9388113991919"></a>evs</strong>, or <strong id="b3519155131912"><a name="b3519155131912"></a><a name="b3519155131912"></a>vpc</strong>. Only lowercase letters are allowed.</p>
    <p id="p16341842101431"><a name="p16341842101431"></a><a name="p16341842101431"></a><em id="i1166771720720"><a name="i1166771720720"></a><a name="i1166771720720"></a>Resource type</em> and <em id="i1166820178714"><a name="i1166820178714"></a><a name="i1166820178714"></a>Action</em>: The values are case-insensitive, and the wildcard (*) is allowed. A wildcard (*) can represent all or part of information about resource types and actions for the specific service.</p>
    </td>
    </tr>
    <tr id="row178631124191018"><td class="cellrowborder" valign="top" width="19.831983198319833%" headers="mcps1.1.5.1.1 "><p id="p38641024201014"><a name="p38641024201014"></a><a name="p38641024201014"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.95179517951795%" headers="mcps1.1.5.1.2 "><p id="p148641024111012"><a name="p148641024111012"></a><a name="p148641024111012"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.631763176317634%" headers="mcps1.1.5.1.3 "><p id="p6864172421014"><a name="p6864172421014"></a><a name="p6864172421014"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.58445844584458%" headers="mcps1.1.5.1.4 "><a name="ul9647547681"></a><a name="ul9647547681"></a><ul id="ul9647547681"><li>Resources to be managed. After a domain establishes multiple trust relationships between itself and your domain, you can authorize different users to manage resources of the delegating party. Each user can only switch to the specified agencies. You can create custom policies to assign specified permissions to users.</li><li>When creating a custom policy, specify the <strong id="b209041648588"><a name="b209041648588"></a><a name="b209041648588"></a>Action</strong> as <strong id="b1490534195818"><a name="b1490534195818"></a><a name="b1490534195818"></a>iam:agencies:assume</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    -   Format description of the Resource parameter

        <a name="table755284212333"></a>
        <table><thead align="left"><tr id="row855217422337"><th class="cellrowborder" valign="top" width="19.52%" id="mcps1.1.5.1.1"><p id="p5552184233312"><a name="p5552184233312"></a><a name="p5552184233312"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.2"><p id="p6552242193314"><a name="p6552242193314"></a><a name="p6552242193314"></a><strong id="b227755034"><a name="b227755034"></a><a name="b227755034"></a>Mandatory</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="17.79%" id="mcps1.1.5.1.3"><p id="p65531427338"><a name="p65531427338"></a><a name="p65531427338"></a><strong id="b807702354"><a name="b807702354"></a><a name="b807702354"></a>Type</strong></p>
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
        <p id="p1355354283311"><a name="p1355354283311"></a><a name="p1355354283311"></a>Format: /iam/agencies/{<em id="i2065201125817"><a name="i2065201125817"></a><a name="i2065201125817"></a>agency ID</em>}</p>
        </td>
        </tr>
        </tbody>
        </table>



-   Sample response \(custom policy for a cloud service\)

    ```
    { 
       "role": {
          "id": "24e7a89bffe443979760c4e9715c13a5",
          "name": "custom_9698542758bc422088c0c3eabfc30d12_0",
          "display_name": "Customed ECS Viewer",
          "description": "The read-only permissions to all ECS resources, which can be used for statistics and survey.",
          "links": {
            "self": "www.example.com/v3/roles/24e7a89bffe443979760c4e9715c13a5"
          },
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "type": "XA",
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
          }
        }
     }
    ```


-   Sample response \(custom policy for an agency\)

    ```
    { 
       "role": {
          "id": "5c03c324d4784435baaedb6a9bf01321",
          "name": "custom_9698542758bc422088c0c3eabfc30d12_1",
          "display_name": "Customed fine-grained agency",
          "description": "Allow sub-user to use agency.",
          "links": {
            "self": "www.example.com/v3/roles/5c03c324d4784435baaedb6a9bf01321"
          },
          "domain_id": "9698542758bc422088c0c3eabfc30d12",
          "type": "AX",
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
                    "/iam/agencies/4eb04341ec2d41f5add4f3846d884f2d"
                  ]
                }
              }
            ]
          }
        }
     }
    ```


-   Error response body parameter description

    <a name="table4649094141930"></a>
    <table><thead align="left"><tr id="row17736093141930"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p27337422141930"><a name="p27337422141930"></a><a name="p27337422141930"></a><strong id="b89569156"><a name="b89569156"></a><a name="b89569156"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p66847539141930"><a name="p66847539141930"></a><a name="p66847539141930"></a><strong id="b806649783"><a name="b806649783"></a><a name="b806649783"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p45941556141930"><a name="p45941556141930"></a><a name="p45941556141930"></a><strong id="b229099984"><a name="b229099984"></a><a name="b229099984"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p30278587141930"><a name="p30278587141930"></a><a name="p30278587141930"></a><strong id="b657706759"><a name="b657706759"></a><a name="b657706759"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36646445141930"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p15572084141930"><a name="p15572084141930"></a><a name="p15572084141930"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p53379320141930"><a name="p53379320141930"></a><a name="p53379320141930"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p28757664141930"><a name="p28757664141930"></a><a name="p28757664141930"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p47669461141930"><a name="p47669461141930"></a><a name="p47669461141930"></a>Response error</p>
    </td>
    </tr>
    <tr id="row26371967141930"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p55754610141930"><a name="p55754610141930"></a><a name="p55754610141930"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p19829541141930"><a name="p19829541141930"></a><a name="p19829541141930"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p62688960141930"><a name="p62688960141930"></a><a name="p62688960141930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p44641004141930"><a name="p44641004141930"></a><a name="p44641004141930"></a>Error details</p>
    </td>
    </tr>
    <tr id="row66224720141930"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p62602071141930"><a name="p62602071141930"></a><a name="p62602071141930"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p37603011141930"><a name="p37603011141930"></a><a name="p37603011141930"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p25945084141930"><a name="p25945084141930"></a><a name="p25945084141930"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p21177065141930"><a name="p21177065141930"></a><a name="p21177065141930"></a>Status code</p>
    </td>
    </tr>
    <tr id="row56375863141930"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p3042190141930"><a name="p3042190141930"></a><a name="p3042190141930"></a>title</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p45090829141930"><a name="p45090829141930"></a><a name="p45090829141930"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p28478557141930"><a name="p28478557141930"></a><a name="p28478557141930"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p25061798141930"><a name="p25061798141930"></a><a name="p25061798141930"></a>Error type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(failed response\)

    ```
    {
        "error": {
            "message": "The request you have made requires authentication.",
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
<tr id="row25486086174056"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2553726917410"><a name="p2553726917410"></a><a name="p2553726917410"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5525289717410"><a name="p5525289717410"></a><a name="p5525289717410"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>


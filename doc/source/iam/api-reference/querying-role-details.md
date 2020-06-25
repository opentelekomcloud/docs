# Querying Role Details<a name="en-us_topic_0057845603"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query role details, including the permission policies of a role. A role is a set of permissions and represents a group of actions.

## URI<a name="section3019338085013"></a>

-   URI format

    GET /v3/roles/\{role\_id\}

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706112217"><a name="b842352706112217"></a><a name="b842352706112217"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.24%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b78961916133210"><a name="b78961916133210"></a><a name="b78961916133210"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.32%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.080000000000005%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
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
    <th class="cellrowborder" valign="top" width="18.86%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="b181381942173110_1"><a name="b181381942173110_1"></a><a name="b181381942173110_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.21%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p6173474111910"><a name="p6173474111910"></a><a name="p6173474111910"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3/roles/19bb93eec4ca4f08aefdc02da76d8f3c
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="19.75%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="b3565951916252"><a name="b3565951916252"></a><a name="b3565951916252"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.55%" id="mcps1.1.5.1.2"><p id="p1056617720581"><a name="p1056617720581"></a><a name="p1056617720581"></a><strong id="b181381942173110_3"><a name="b181381942173110_3"></a><a name="b181381942173110_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.36%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.34%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row809135110010"><td class="cellrowborder" valign="top" width="19.75%" headers="mcps1.1.5.1.1 "><p id="p5141972010010"><a name="p5141972010010"></a><a name="p5141972010010"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.55%" headers="mcps1.1.5.1.2 "><p id="p556717175819"><a name="p556717175819"></a><a name="p556717175819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.34%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>Details of the role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the role format

    <a name="table4865996110948"></a>
    <table><thead align="left"><tr id="row3498648810948"><th class="cellrowborder" valign="top" width="19.939999999999998%" id="mcps1.1.5.1.1"><p id="p1533325610948"><a name="p1533325610948"></a><a name="p1533325610948"></a><strong id="b293392616252"><a name="b293392616252"></a><a name="b293392616252"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.1.5.1.2"><p id="p47406710214141"><a name="p47406710214141"></a><a name="p47406710214141"></a><strong id="b181381942173110_5"><a name="b181381942173110_5"></a><a name="b181381942173110_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52%" id="mcps1.1.5.1.3"><p id="p3403423310948"><a name="p3403423310948"></a><a name="p3403423310948"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.48%" id="mcps1.1.5.1.4"><p id="p530949010948"><a name="p530949010948"></a><a name="p530949010948"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2718319318492"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p4332214818492"><a name="p4332214818492"></a><a name="p4332214818492"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p52491180214141"><a name="p52491180214141"></a><a name="p52491180214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p1943313718492"><a name="p1943313718492"></a><a name="p1943313718492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p3058025418492"><a name="p3058025418492"></a><a name="p3058025418492"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row61939585101142"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p20585353101142"><a name="p20585353101142"></a><a name="p20585353101142"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p20220752214141"><a name="p20220752214141"></a><a name="p20220752214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p56800915101142"><a name="p56800915101142"></a><a name="p56800915101142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p37471393101142"><a name="p37471393101142"></a><a name="p37471393101142"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row66853790101157"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p64813205101157"><a name="p64813205101157"></a><a name="p64813205101157"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p64755119214141"><a name="p64755119214141"></a><a name="p64755119214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p15378285101157"><a name="p15378285101157"></a><a name="p15378285101157"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p37681557101157"><a name="p37681557101157"></a><a name="p37681557101157"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row5718865710123"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p4493586710123"><a name="p4493586710123"></a><a name="p4493586710123"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p3095987214141"><a name="p3095987214141"></a><a name="p3095987214141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p1592658110123"><a name="p1592658110123"></a><a name="p1592658110123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p1498466710123"><a name="p1498466710123"></a><a name="p1498466710123"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row1548265115236"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p5745115415230"><a name="p5745115415230"></a><a name="p5745115415230"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p7745175432314"><a name="p7745175432314"></a><a name="p7745175432314"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p147452546233"><a name="p147452546233"></a><a name="p147452546233"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p10745554132312"><a name="p10745554132312"></a><a name="p10745554132312"></a>Display mode of a role.</p>
    <a name="ul58960622111433"></a><a name="ul58960622111433"></a><ul id="ul58960622111433"><li><strong id="b61484664113035"><a name="b61484664113035"></a><a name="b61484664113035"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b14201912113035"><a name="b14201912113035"></a><a name="b14201912113035"></a>XA</strong>: A role is displayed at the project layer.</li><li><strong id="b9504241113035"><a name="b9504241113035"></a><a name="b9504241113035"></a>AA</strong>: A role is displayed at both the domain and project layers.</li><li><strong id="b31646026113035"><a name="b31646026113035"></a><a name="b31646026113035"></a>XX</strong>: A role is not displayed at the domain or project layer.</li></ul>
    </td>
    </tr>
    <tr id="row57645998214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p59369096214145"><a name="p59369096214145"></a><a name="p59369096214145"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p19319748214145"><a name="p19319748214145"></a><a name="p19319748214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p23075900214145"><a name="p23075900214145"></a><a name="p23075900214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p12999383214145"><a name="p12999383214145"></a><a name="p12999383214145"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row33977091214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p65673627214145"><a name="p65673627214145"></a><a name="p65673627214145"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p34536686214145"><a name="p34536686214145"></a><a name="p34536686214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p3673120214145"><a name="p3673120214145"></a><a name="p3673120214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p55700186214145"><a name="p55700186214145"></a><a name="p55700186214145"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row53576771214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p48279332214145"><a name="p48279332214145"></a><a name="p48279332214145"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p26134551214145"><a name="p26134551214145"></a><a name="p26134551214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p18445422214145"><a name="p18445422214145"></a><a name="p18445422214145"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p963217214145"><a name="p963217214145"></a><a name="p963217214145"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row28018958214145"><td class="cellrowborder" valign="top" width="19.939999999999998%" headers="mcps1.1.5.1.1 "><p id="p5775123214145"><a name="p5775123214145"></a><a name="p5775123214145"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.1.5.1.2 "><p id="p40003297214145"><a name="p40003297214145"></a><a name="p40003297214145"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p47954295214145"><a name="p47954295214145"></a><a name="p47954295214145"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.48%" headers="mcps1.1.5.1.4 "><p id="p43833853214145"><a name="p43833853214145"></a><a name="p43833853214145"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
      "role": {
        "display_name": "Tanent Guest",
        "description": "Tanent Guest",
        "links": {
          "self": "www.example.com/v3/roles/19bb93eec4ca4f08aefdc02da76d8f3c"
        },
        "domain_id": null,
        "catalog": "BASE",
        "policy": {
          "Version": "1.0",
          "Statement": [
            {
              "Action": [
                "::Get",
                "::List"
              ],
              "Effect": "Allow"
            },
            {
              "Action": [
                "identity:*"
              ],
              "Effect": "Deny"
            }
          ]
        },
        "id": "19bb93eec4ca4f08aefdc02da76d8f3c",
        "type": "AA",
        "name": "readonly"
      }
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b535923316124"><a name="b535923316124"></a><a name="b535923316124"></a>Status Code</strong></p>
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
<tr id="row17137612184219"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p20020782184219"><a name="p20020782184219"></a><a name="p20020782184219"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p11070673184219"><a name="p11070673184219"></a><a name="p11070673184219"></a>The server could not find the requested page.</p>
</td>
</tr>
</tbody>
</table>


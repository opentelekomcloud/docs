# Querying a Role List<a name="en-us_topic_0057845591"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query a role list, including the permission policies of a role. A role is a set of permissions and represents a group of actions.

## URI<a name="section3019338085013"></a>

-   URI format

    GET /v3/roles

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706112217"><a name="b842352706112217"></a><a name="b842352706112217"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.19191919191919%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b7930731103215"><a name="b7930731103215"></a><a name="b7930731103215"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.781778177817785%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43.834383438343835%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.781778177817785%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.834383438343835%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row19857248"><td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p64933228"><a name="en-us_topic_0032920307_p64933228"></a><a name="en-us_topic_0032920307_p64933228"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.19191919191919%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p25100141"><a name="en-us_topic_0032920307_p25100141"></a><a name="en-us_topic_0032920307_p25100141"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.781778177817785%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p19845579"><a name="en-us_topic_0032920307_p19845579"></a><a name="en-us_topic_0032920307_p19845579"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="43.834383438343835%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p63988077"><a name="en-us_topic_0032920307_p63988077"></a><a name="en-us_topic_0032920307_p63988077"></a>ID of a domain.</p>
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
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.21%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5809965914567"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="p39507220145612"><a name="p39507220145612"></a><a name="p39507220145612"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="p45968213145612"><a name="p45968213145612"></a><a name="p45968213145612"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="p32437767145612"><a name="p32437767145612"></a><a name="p32437767145612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p10213457145612"><a name="p10213457145612"></a><a name="p10213457145612"></a>Fill <strong id="b842352706161331"><a name="b842352706161331"></a><a name="b842352706161331"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.49%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.21%" headers="mcps1.1.5.1.4 "><p id="p1956316611820"><a name="p1956316611820"></a><a name="p1956316611820"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3/roles?name=readonly
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="19.55%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="b1983936155652"><a name="b1983936155652"></a><a name="b1983936155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.790000000000003%" id="mcps1.1.5.1.2"><p id="p3950172025717"><a name="p3950172025717"></a><a name="p3950172025717"></a><strong id="b13634202633213_3"><a name="b13634202633213_3"></a><a name="b13634202633213_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.52%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.14%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570214510010"><td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.5.1.1 "><p id="p5922062510010"><a name="p5922062510010"></a><a name="p5922062510010"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.1.5.1.2 "><p id="p19505202571"><a name="p19505202571"></a><a name="p19505202571"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p5331155510010"><a name="p5331155510010"></a><a name="p5331155510010"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.1.5.1.4 "><p id="p2326866010010"><a name="p2326866010010"></a><a name="p2326866010010"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row809135110010"><td class="cellrowborder" valign="top" width="19.55%" headers="mcps1.1.5.1.1 "><p id="p5141972010010"><a name="p5141972010010"></a><a name="p5141972010010"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.790000000000003%" headers="mcps1.1.5.1.2 "><p id="p2950620155714"><a name="p2950620155714"></a><a name="p2950620155714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.52%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.14%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>List of roles.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Description for the role format

    <a name="table4865996110948"></a>
    <table><thead align="left"><tr id="row3498648810948"><th class="cellrowborder" valign="top" width="23.27%" id="mcps1.1.5.1.1"><p id="p1533325610948"><a name="p1533325610948"></a><a name="p1533325610948"></a><strong id="b16646705155652"><a name="b16646705155652"></a><a name="b16646705155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.17%" id="mcps1.1.5.1.2"><p id="p34951346212620"><a name="p34951346212620"></a><a name="p34951346212620"></a><strong id="b13634202633213_5"><a name="b13634202633213_5"></a><a name="b13634202633213_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.56%" id="mcps1.1.5.1.3"><p id="p3403423310948"><a name="p3403423310948"></a><a name="p3403423310948"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.1.5.1.4"><p id="p530949010948"><a name="p530949010948"></a><a name="p530949010948"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61939585101142"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p20585353101142"><a name="p20585353101142"></a><a name="p20585353101142"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p8728262212620"><a name="p8728262212620"></a><a name="p8728262212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p56800915101142"><a name="p56800915101142"></a><a name="p56800915101142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p37471393101142"><a name="p37471393101142"></a><a name="p37471393101142"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row66853790101157"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p64813205101157"><a name="p64813205101157"></a><a name="p64813205101157"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p38182884212620"><a name="p38182884212620"></a><a name="p38182884212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p15378285101157"><a name="p15378285101157"></a><a name="p15378285101157"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p37681557101157"><a name="p37681557101157"></a><a name="p37681557101157"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row12296246163915"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p685894713911"><a name="p685894713911"></a><a name="p685894713911"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p58591747193919"><a name="p58591747193919"></a><a name="p58591747193919"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p15860144713394"><a name="p15860144713394"></a><a name="p15860144713394"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p88621476393"><a name="p88621476393"></a><a name="p88621476393"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row5718865710123"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p4493586710123"><a name="p4493586710123"></a><a name="p4493586710123"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p39011830212620"><a name="p39011830212620"></a><a name="p39011830212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p1592658110123"><a name="p1592658110123"></a><a name="p1592658110123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p10388175584213"><a name="p10388175584213"></a><a name="p10388175584213"></a>Name of a role.</p>
    <p id="p1498466710123"><a name="p1498466710123"></a><a name="p1498466710123"></a>This parameter is carried in the token of a user. The cloud service determines whether the user has the access permission based on the role name.</p>
    </td>
    </tr>
    <tr id="row6238021117125"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p2455099017125"><a name="p2455099017125"></a><a name="p2455099017125"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p47903332212620"><a name="p47903332212620"></a><a name="p47903332212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p4247314317125"><a name="p4247314317125"></a><a name="p4247314317125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p1777252017125"><a name="p1777252017125"></a><a name="p1777252017125"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row166333532187"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p66341539183"><a name="p66341539183"></a><a name="p66341539183"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p11634105315184"><a name="p11634105315184"></a><a name="p11634105315184"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p363455312189"><a name="p363455312189"></a><a name="p363455312189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p2397929132215"><a name="p2397929132215"></a><a name="p2397929132215"></a>Display mode of a role.</p>
    <p id="p039712291224"><a name="p039712291224"></a><a name="p039712291224"></a><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</p>
    <p id="p0398102914222"><a name="p0398102914222"></a><a name="p0398102914222"></a><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.</p>
    <p id="p193981329162219"><a name="p193981329162219"></a><a name="p193981329162219"></a><strong id="b911853911303"><a name="b911853911303"></a><a name="b911853911303"></a>AA</strong>: A role is displayed at both the domain and project layers.</p>
    <p id="p1639815292223"><a name="p1639815292223"></a><a name="p1639815292223"></a><strong id="b40422911303"><a name="b40422911303"></a><a name="b40422911303"></a>XX</strong>: A role is not displayed at the domain or project layer.</p>
    </td>
    </tr>
    <tr id="row36980485212115"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p58797236212142"><a name="p58797236212142"></a><a name="p58797236212142"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p54329714212620"><a name="p54329714212620"></a><a name="p54329714212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p19673345212115"><a name="p19673345212115"></a><a name="p19673345212115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p31059936212115"><a name="p31059936212115"></a><a name="p31059936212115"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row1426065517258"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p112602055182513"><a name="p112602055182513"></a><a name="p112602055182513"></a>flag</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p92601558255"><a name="p92601558255"></a><a name="p92601558255"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p726025512255"><a name="p726025512255"></a><a name="p726025512255"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p14260175516254"><a name="p14260175516254"></a><a name="p14260175516254"></a>A tag for indicating an internal fine-grained role.</p>
    </td>
    </tr>
    <tr id="row1484057212111"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p56972052212111"><a name="p56972052212111"></a><a name="p56972052212111"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p20929634212620"><a name="p20929634212620"></a><a name="p20929634212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p15953184212111"><a name="p15953184212111"></a><a name="p15953184212111"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p23853027212111"><a name="p23853027212111"></a><a name="p23853027212111"></a>Policy of a role.</p>
    <a name="ul369294285620"></a><a name="ul369294285620"></a><ul id="ul369294285620"><li><strong id="b8423527069331"><a name="b8423527069331"></a><a name="b8423527069331"></a>Version</strong>: indicates policy version.<a name="ul1969294210568"></a><a name="ul1969294210568"></a><ul id="ul1969294210568"><li><strong id="b84235270618822"><a name="b84235270618822"></a><a name="b84235270618822"></a>1.0</strong>: Preset cloud service permission (non-fine-grained permission)</li><li><strong id="b842352706181223"><a name="b842352706181223"></a><a name="b842352706181223"></a>1.1</strong>: Fine-grained permission</li></ul>
    </li><li>The <strong id="b11933382060574_3"><a name="b11933382060574_3"></a><a name="b11933382060574_3"></a>Statement</strong> field provides detailed information about a policy and contains the <strong id="b84235270605817_3"><a name="b84235270605817_3"></a><a name="b84235270605817_3"></a>Effect</strong> and <strong id="b84235270605820_3"><a name="b84235270605820_3"></a><a name="b84235270605820_3"></a>Action</strong> elements.<a name="ul59455830103212"></a><a name="ul59455830103212"></a><ul id="ul59455830103212"><li><strong id="b8423527069271"><a name="b8423527069271"></a><a name="b8423527069271"></a>Effect</strong>:<p id="p2023241915820"><a name="p2023241915820"></a><a name="p2023241915820"></a>The value can be <strong id="b8423527061142"><a name="b8423527061142"></a><a name="b8423527061142"></a>Allow</strong> and <strong id="b8423527061138"><a name="b8423527061138"></a><a name="b8423527061138"></a>Deny</strong>. If both <strong id="b8423527061734_1"><a name="b8423527061734_1"></a><a name="b8423527061734_1"></a>Allow</strong> and <strong id="b8423527061732_1"><a name="b8423527061732_1"></a><a name="b8423527061732_1"></a>Deny</strong> are found in statements, the policy evaluation starts with <strong id="b842352706102859"><a name="b842352706102859"></a><a name="b842352706102859"></a>Deny</strong>.</p>
    </li><li><em id="i84235269792727"><a name="i84235269792727"></a><a name="i84235269792727"></a>Action</em>:<p id="p21734600113344"><a name="p21734600113344"></a><a name="p21734600113344"></a>The value can be one or more resource authorization items.</p>
    <p id="p1892123013589"><a name="p1892123013589"></a><a name="p1892123013589"></a>The value format is <em id="i84235269793136"><a name="i84235269793136"></a><a name="i84235269793136"></a>Service name</em>:<em id="i84235269793141"><a name="i84235269793141"></a><a name="i84235269793141"></a>Resource type</em>:<em id="i84235269793144"><a name="i84235269793144"></a><a name="i84235269793144"></a>Action</em>.</p>
    <p id="p28955516431"><a name="p28955516431"></a><a name="p28955516431"></a>For example: <strong id="b84235270693022"><a name="b84235270693022"></a><a name="b84235270693022"></a>vpc:ports:create</strong>.</p>
    </li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="row6468263421212"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p3602757621212"><a name="p3602757621212"></a><a name="p3602757621212"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p19103310212620"><a name="p19103310212620"></a><a name="p19103310212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.56%" headers="mcps1.1.5.1.3 "><p id="p1573738521212"><a name="p1573738521212"></a><a name="p1573738521212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.5.1.4 "><p id="p6092064621212"><a name="p6092064621212"></a><a name="p6092064621212"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "links": {
        "self": "www.example.com/v3/roles?name=readonly",
        "previous": null,
        "next": null
      },
      "roles": [
        {
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
      ]
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
</tbody>
</table>


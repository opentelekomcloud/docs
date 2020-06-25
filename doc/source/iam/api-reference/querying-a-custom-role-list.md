# Querying a Custom Role List<a name="EN-US_TOPIC_0147658842"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query a custom role list, including the permissions policies of a role.

## URI<a name="section3019338085013"></a>

URI format

GET /v3.0/OS-ROLE/roles

>![](/images/icon-note.gif) **NOTE:**   
>You can also use  **GET /v3/roles?domain\_id=\{domain\_id\}**  to query the custom role list. For details, see  [Querying a Role List](querying-a-role-list.md).  

## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.490000000000002%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504"><a name="a173ae121cc9e48328ca613e72f2a1504"></a><a name="a173ae121cc9e48328ca613e72f2a1504"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.860000000000003%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="b13634202633213_1"><a name="b13634202633213_1"></a><a name="b13634202633213_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.17%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p63243911"><a name="en-us_topic_0032920307_p63243911"></a><a name="en-us_topic_0032920307_p63243911"></a><strong id="b842352706143526_3"><a name="b842352706143526_3"></a><a name="b842352706143526_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.480000000000004%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p22483156"><a name="en-us_topic_0032920307_p22483156"></a><a name="en-us_topic_0032920307_p22483156"></a><strong id="b20601766145329_3"><a name="b20601766145329_3"></a><a name="b20601766145329_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row39604502"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p53848109"><a name="en-us_topic_0032920307_p53848109"></a><a name="en-us_topic_0032920307_p53848109"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p66729601"><a name="en-us_topic_0032920307_p66729601"></a><a name="en-us_topic_0032920307_p66729601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p36388601"><a name="en-us_topic_0032920307_p36388601"></a><a name="en-us_topic_0032920307_p36388601"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p3519337911274"><a name="p3519337911274"></a><a name="p3519337911274"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    <tr id="row23514384390"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p756284913314"><a name="p756284913314"></a><a name="p756284913314"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.860000000000003%" headers="mcps1.1.5.1.2 "><p id="p1656219494334"><a name="p1656219494334"></a><a name="p1656219494334"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.17%" headers="mcps1.1.5.1.3 "><p id="p86097153416"><a name="p86097153416"></a><a name="p86097153416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p95620493339"><a name="p95620493339"></a><a name="p95620493339"></a>Fill <strong id="b1381912885410"><a name="b1381912885410"></a><a name="b1381912885410"></a>application/json;charset=utf8</strong> in this field.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3.0/OS-ROLE/roles
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="b1983936155652"><a name="b1983936155652"></a><a name="b1983936155652"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p3950172025717"><a name="p3950172025717"></a><a name="p3950172025717"></a><strong id="b13634202633213_3"><a name="b13634202633213_3"></a><a name="b13634202633213_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570214510010"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p5922062510010"><a name="p5922062510010"></a><a name="p5922062510010"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p19505202571"><a name="p19505202571"></a><a name="p19505202571"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p5331155510010"><a name="p5331155510010"></a><a name="p5331155510010"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p2326866010010"><a name="p2326866010010"></a><a name="p2326866010010"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row809135110010"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p5141972010010"><a name="p5141972010010"></a><a name="p5141972010010"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p2950620155714"><a name="p2950620155714"></a><a name="p2950620155714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>List of roles.</p>
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
    <th class="cellrowborder" valign="top" width="15.629999999999999%" id="mcps1.1.5.1.3"><p id="p3403423310948"><a name="p3403423310948"></a><a name="p3403423310948"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.93%" id="mcps1.1.5.1.4"><p id="p530949010948"><a name="p530949010948"></a><a name="p530949010948"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61939585101142"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p20585353101142"><a name="p20585353101142"></a><a name="p20585353101142"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p8728262212620"><a name="p8728262212620"></a><a name="p8728262212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p56800915101142"><a name="p56800915101142"></a><a name="p56800915101142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p37471393101142"><a name="p37471393101142"></a><a name="p37471393101142"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row66853790101157"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p64813205101157"><a name="p64813205101157"></a><a name="p64813205101157"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p38182884212620"><a name="p38182884212620"></a><a name="p38182884212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p15378285101157"><a name="p15378285101157"></a><a name="p15378285101157"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p37681557101157"><a name="p37681557101157"></a><a name="p37681557101157"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row12296246163915"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p685894713911"><a name="p685894713911"></a><a name="p685894713911"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p58591747193919"><a name="p58591747193919"></a><a name="p58591747193919"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p15860144713394"><a name="p15860144713394"></a><a name="p15860144713394"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p88621476393"><a name="p88621476393"></a><a name="p88621476393"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row5718865710123"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p4493586710123"><a name="p4493586710123"></a><a name="p4493586710123"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p39011830212620"><a name="p39011830212620"></a><a name="p39011830212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p1592658110123"><a name="p1592658110123"></a><a name="p1592658110123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p1498466710123"><a name="p1498466710123"></a><a name="p1498466710123"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row6238021117125"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p2455099017125"><a name="p2455099017125"></a><a name="p2455099017125"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p47903332212620"><a name="p47903332212620"></a><a name="p47903332212620"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p4247314317125"><a name="p4247314317125"></a><a name="p4247314317125"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p1777252017125"><a name="p1777252017125"></a><a name="p1777252017125"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row166333532187"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p66341539183"><a name="p66341539183"></a><a name="p66341539183"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p11634105315184"><a name="p11634105315184"></a><a name="p11634105315184"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p363455312189"><a name="p363455312189"></a><a name="p363455312189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p2397929132215"><a name="p2397929132215"></a><a name="p2397929132215"></a>Display mode of a role.</p>
    <a name="ul10474257102533"></a><a name="ul10474257102533"></a><ul id="ul10474257102533"><li><strong id="b4067993711303"><a name="b4067993711303"></a><a name="b4067993711303"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b674061011303"><a name="b674061011303"></a><a name="b674061011303"></a>XA</strong>: A role is displayed at the project layer.<div class="note" id="note6156094517252"><a name="note6156094517252"></a><a name="note6156094517252"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p22955343165917"><a name="p22955343165917"></a><a name="p22955343165917"></a>The display mode of a role can only be <strong id="b84235270610383"><a name="b84235270610383"></a><a name="b84235270610383"></a>AX</strong> or <strong id="b84235270610386"><a name="b84235270610386"></a><a name="b84235270610386"></a>XA</strong>. A role cannot be displayed at both the domain and project layers or neither of the two layers. That is, neither <strong id="b842352706104236"><a name="b842352706104236"></a><a name="b842352706104236"></a>AA</strong> nor <strong id="b842352706104526"><a name="b842352706104526"></a><a name="b842352706104526"></a>XX</strong> is allowed.</p>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row36980485212115"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p58797236212142"><a name="p58797236212142"></a><a name="p58797236212142"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p54329714212620"><a name="p54329714212620"></a><a name="p54329714212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p19673345212115"><a name="p19673345212115"></a><a name="p19673345212115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p31059936212115"><a name="p31059936212115"></a><a name="p31059936212115"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row1484057212111"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p56972052212111"><a name="p56972052212111"></a><a name="p56972052212111"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p20929634212620"><a name="p20929634212620"></a><a name="p20929634212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p15953184212111"><a name="p15953184212111"></a><a name="p15953184212111"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p23853027212111"><a name="p23853027212111"></a><a name="p23853027212111"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row6468263421212"><td class="cellrowborder" valign="top" width="23.27%" headers="mcps1.1.5.1.1 "><p id="p3602757621212"><a name="p3602757621212"></a><a name="p3602757621212"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.17%" headers="mcps1.1.5.1.2 "><p id="p19103310212620"><a name="p19103310212620"></a><a name="p19103310212620"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.629999999999999%" headers="mcps1.1.5.1.3 "><p id="p1573738521212"><a name="p1573738521212"></a><a name="p1573738521212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.93%" headers="mcps1.1.5.1.4 "><p id="p6092064621212"><a name="p6092064621212"></a><a name="p6092064621212"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the policy format

    <a name="table91819610348"></a>
    <table><thead align="left"><tr id="row4910255010348"><th class="cellrowborder" valign="top" width="23.432343234323433%" id="mcps1.1.5.1.1"><p id="p3416513010511"><a name="p3416513010511"></a><a name="p3416513010511"></a><strong id="b37426530113629"><a name="b37426530113629"></a><a name="b37426530113629"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.23162316231623%" id="mcps1.1.5.1.2"><p id="p1591217110511"><a name="p1591217110511"></a><a name="p1591217110511"></a><strong id="b1385362904"><a name="b1385362904"></a><a name="b1385362904"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.441544154415443%" id="mcps1.1.5.1.3"><p id="p1381751310511"><a name="p1381751310511"></a><a name="p1381751310511"></a><strong id="b578448693"><a name="b578448693"></a><a name="b578448693"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.894489448944896%" id="mcps1.1.5.1.4"><p id="p4547677910511"><a name="p4547677910511"></a><a name="p4547677910511"></a><strong id="b14438018113629"><a name="b14438018113629"></a><a name="b14438018113629"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1795602910348"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 "><p id="p4515225510348"><a name="p4515225510348"></a><a name="p4515225510348"></a>Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 "><p id="p3345406210348"><a name="p3345406210348"></a><a name="p3345406210348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p39012936101229"><a name="p39012936101229"></a><a name="p39012936101229"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 "><p id="p4611838510348"><a name="p4611838510348"></a><a name="p4611838510348"></a>Version of a policy. The value must be <strong id="b842352706173323"><a name="b842352706173323"></a><a name="b842352706173323"></a>1.1</strong>.</p>
    </td>
    </tr>
    <tr id="row1241228310348"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 "><p id="p6587084810348"><a name="p6587084810348"></a><a name="p6587084810348"></a>Statement</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 "><p id="p3393848610348"><a name="p3393848610348"></a><a name="p3393848610348"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p906005101236"><a name="p906005101236"></a><a name="p906005101236"></a>JSONArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 "><p id="p319969910348"><a name="p319969910348"></a><a name="p319969910348"></a>Statement for using the policy to grant permissions. A policy consists of a maximum of eight statements. A <strong id="b842352706173423"><a name="b842352706173423"></a><a name="b842352706173423"></a>Statement</strong> field contains the <strong id="b842352706173420"><a name="b842352706173420"></a><a name="b842352706173420"></a>Effect</strong> and <strong id="b842352706173427"><a name="b842352706173427"></a><a name="b842352706173427"></a>Action</strong> elements.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Description for the statement format

    <a name="table5858327510641"></a>
    <table><thead align="left"><tr id="row234853010641"><th class="cellrowborder" valign="top" width="23.432343234323433%" id="mcps1.1.5.1.1"><p id="p5601325710641"><a name="p5601325710641"></a><a name="p5601325710641"></a><strong id="b1139266717"><a name="b1139266717"></a><a name="b1139266717"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.23162316231623%" id="mcps1.1.5.1.2"><p id="p4077999710641"><a name="p4077999710641"></a><a name="p4077999710641"></a><strong id="b1394388815"><a name="b1394388815"></a><a name="b1394388815"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.441544154415443%" id="mcps1.1.5.1.3"><p id="p1484546110641"><a name="p1484546110641"></a><a name="p1484546110641"></a><strong id="b1723677754"><a name="b1723677754"></a><a name="b1723677754"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.894489448944896%" id="mcps1.1.5.1.4"><p id="p6163170610641"><a name="p6163170610641"></a><a name="p6163170610641"></a><strong id="b1502777232"><a name="b1502777232"></a><a name="b1502777232"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2611227510641"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 "><p id="p3471952910641"><a name="p3471952910641"></a><a name="p3471952910641"></a>Effect</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 "><p id="p6081843510641"><a name="p6081843510641"></a><a name="p6081843510641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p51739175101251"><a name="p51739175101251"></a><a name="p51739175101251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 "><p id="p44854910641"><a name="p44854910641"></a><a name="p44854910641"></a>The value can be <strong id="b8423527061142"><a name="b8423527061142"></a><a name="b8423527061142"></a>Allow</strong> and <strong id="b8423527061138"><a name="b8423527061138"></a><a name="b8423527061138"></a>Deny</strong>. If both <strong id="b8423527061734_1"><a name="b8423527061734_1"></a><a name="b8423527061734_1"></a>Allow</strong> and <strong id="b8423527061732_1"><a name="b8423527061732_1"></a><a name="b8423527061732_1"></a>Deny</strong> are found in statements, the policy evaluation starts with <strong id="b842352706101627"><a name="b842352706101627"></a><a name="b842352706101627"></a>Deny</strong>.</p>
    </td>
    </tr>
    <tr id="row403694110641"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 "><p id="p15866909101431"><a name="p15866909101431"></a><a name="p15866909101431"></a>Action</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 "><p id="p10151214101431"><a name="p10151214101431"></a><a name="p10151214101431"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p90575969132"><a name="p90575969132"></a><a name="p90575969132"></a>StringArray</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 "><p id="p2687264101431"><a name="p2687264101431"></a><a name="p2687264101431"></a>Permission set, which specifies the operation permissions on resources. The number of permission sets cannot exceed 100.</p>
    <p id="p19358101314235"><a name="p19358101314235"></a><a name="p19358101314235"></a>Format:</p>
    <p id="p17841114310274"><a name="p17841114310274"></a><a name="p17841114310274"></a>The value format is <em id="i84235269723526"><a name="i84235269723526"></a><a name="i84235269723526"></a>Service name</em>:<em id="i84235269723639"><a name="i84235269723639"></a><a name="i84235269723639"></a>Resource type</em>:<em id="i84235269723534"><a name="i84235269723534"></a><a name="i84235269723534"></a>Action</em>, for example, <strong id="b842352706165816"><a name="b842352706165816"></a><a name="b842352706165816"></a>vpc:ports:create</strong>.</p>
    <p id="p24185381101431"><a name="p24185381101431"></a><a name="p24185381101431"></a><em id="i84235269711017"><a name="i84235269711017"></a><a name="i84235269711017"></a>Service name</em>: indicates the product name, such as <strong id="b1194612119195"><a name="b1194612119195"></a><a name="b1194612119195"></a>ecs</strong>, <strong id="b9388113991919"><a name="b9388113991919"></a><a name="b9388113991919"></a>evs</strong>, or <strong id="b3519155131912"><a name="b3519155131912"></a><a name="b3519155131912"></a>vpc</strong>. Only lowercase letters are allowed.</p>
    <p id="p16341842101431"><a name="p16341842101431"></a><a name="p16341842101431"></a><em id="i84235269710240"><a name="i84235269710240"></a><a name="i84235269710240"></a>Resource type</em> and <em id="i84235269710254"><a name="i84235269710254"></a><a name="i84235269710254"></a>Action</em>: The values are case-insensitive, and the wildcard (*) is allowed. A wildcard (*) can represent all or part of information about resource types and actions for the specific service.</p>
    </td>
    </tr>
    <tr id="row10521161917259"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 ">&nbsp;&nbsp;</td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 ">&nbsp;&nbsp;</td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 ">&nbsp;&nbsp;</td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 ">&nbsp;&nbsp;</td>
    </tr>
    <tr id="row1043019492715"><td class="cellrowborder" valign="top" width="23.432343234323433%" headers="mcps1.1.5.1.1 "><p id="p154301349972"><a name="p154301349972"></a><a name="p154301349972"></a>Resource</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.23162316231623%" headers="mcps1.1.5.1.2 "><p id="p1543115496712"><a name="p1543115496712"></a><a name="p1543115496712"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.441544154415443%" headers="mcps1.1.5.1.3 "><p id="p54311149272"><a name="p54311149272"></a><a name="p54311149272"></a>JSON object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.894489448944896%" headers="mcps1.1.5.1.4 "><a name="ul9647547681"></a><a name="ul9647547681"></a><ul id="ul9647547681"><li>Resources to be managed. After a domain establishes multiple trust relationships between itself and your domain, you can authorize different users to manage resources of the delegating party. Each user can only switch to the specified agencies. You can create custom policies to assign specified permissions to users.</li><li>When creating a custom policy, specify the <strong id="b1527265894720"><a name="b1527265894720"></a><a name="b1527265894720"></a>Action</strong> as <strong id="b1790513384816"><a name="b1790513384816"></a><a name="b1790513384816"></a>iam:agencies:assume</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response \(successful response\)

    ```
    {
      "links": {
        "self": "www.example.com/v3/roles?domain_id=9698542758bc422088c0c3eabfc30d12",
        "previous": null,
        "next": null
      },
      "roles": [
        {
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
        },
        {
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
      ]
    }
        
    ```


-   Error response body parameter description

    <a name="table11176492114346"></a>
    <table><thead align="left"><tr id="row41569007114346"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.5.1.1"><p id="p11646382114346"><a name="p11646382114346"></a><a name="p11646382114346"></a><strong id="b120188107"><a name="b120188107"></a><a name="b120188107"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.1.5.1.2"><p id="p3832874114346"><a name="p3832874114346"></a><a name="p3832874114346"></a><strong id="b764583609"><a name="b764583609"></a><a name="b764583609"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.06%" id="mcps1.1.5.1.3"><p id="p42027338114346"><a name="p42027338114346"></a><a name="p42027338114346"></a><strong id="b141135781"><a name="b141135781"></a><a name="b141135781"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.940000000000005%" id="mcps1.1.5.1.4"><p id="p48771190114346"><a name="p48771190114346"></a><a name="p48771190114346"></a><strong id="b945103355"><a name="b945103355"></a><a name="b945103355"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58152343114346"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p12719381114346"><a name="p12719381114346"></a><a name="p12719381114346"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p23636951114346"><a name="p23636951114346"></a><a name="p23636951114346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p35544902114346"><a name="p35544902114346"></a><a name="p35544902114346"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p60564809114346"><a name="p60564809114346"></a><a name="p60564809114346"></a>Response error</p>
    </td>
    </tr>
    <tr id="row8212374114346"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p61222547114346"><a name="p61222547114346"></a><a name="p61222547114346"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p60079256114346"><a name="p60079256114346"></a><a name="p60079256114346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p34581582114346"><a name="p34581582114346"></a><a name="p34581582114346"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p49644764114346"><a name="p49644764114346"></a><a name="p49644764114346"></a>Error details</p>
    </td>
    </tr>
    <tr id="row44149700114346"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p19355979114346"><a name="p19355979114346"></a><a name="p19355979114346"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p24330429114346"><a name="p24330429114346"></a><a name="p24330429114346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p24607748114346"><a name="p24607748114346"></a><a name="p24607748114346"></a>Int</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p47070600114346"><a name="p47070600114346"></a><a name="p47070600114346"></a>Status code</p>
    </td>
    </tr>
    <tr id="row20982220114346"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.5.1.1 "><p id="p21838261114346"><a name="p21838261114346"></a><a name="p21838261114346"></a>title</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.5.1.2 "><p id="p24068751114346"><a name="p24068751114346"></a><a name="p24068751114346"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.06%" headers="mcps1.1.5.1.3 "><p id="p3411842114346"><a name="p3411842114346"></a><a name="p3411842114346"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.940000000000005%" headers="mcps1.1.5.1.4 "><p id="p7923765114346"><a name="p7923765114346"></a><a name="p7923765114346"></a>Error type</p>
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
<tr id="row11791665174018"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p15600847174018"><a name="p15600847174018"></a><a name="p15600847174018"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p55709105174018"><a name="p55709105174018"></a><a name="p55709105174018"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
</tbody>
</table>


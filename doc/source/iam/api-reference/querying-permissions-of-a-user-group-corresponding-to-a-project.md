# Querying Permissions of a User Group Corresponding to a Project<a name="en-us_topic_0057845640"></a>

## Function Description<a name="section495175389414"></a>

This interface is used to query the permissions of a specified user group corresponding to a project. A role is a set of permissions and represents a group of actions.

## URI<a name="section3019338085013"></a>

-   URI format

    GET /v3/projects/\{project\_id\}/groups/\{group\_id\}/roles

-   URI parameter description

    <a name="en-us_topic_0032920307_table36168141"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row15662289"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p60685926"><a name="en-us_topic_0032920307_p60685926"></a><a name="en-us_topic_0032920307_p60685926"></a><strong id="b842352706112519"><a name="b842352706112519"></a><a name="b842352706112519"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.24%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p16612996"><a name="en-us_topic_0032920307_p16612996"></a><a name="en-us_topic_0032920307_p16612996"></a><strong id="b842352706112524"><a name="b842352706112524"></a><a name="b842352706112524"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.05%" id="mcps1.1.5.1.3"><p id="en-us_topic_0032920307_p3475410"><a name="en-us_topic_0032920307_p3475410"></a><a name="en-us_topic_0032920307_p3475410"></a><strong id="b842352706143526_1"><a name="b842352706143526_1"></a><a name="b842352706143526_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.35%" id="mcps1.1.5.1.4"><p id="en-us_topic_0032920307_p13072760"><a name="en-us_topic_0032920307_p13072760"></a><a name="en-us_topic_0032920307_p13072760"></a><strong id="b20601766145329_1"><a name="b20601766145329_1"></a><a name="b20601766145329_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0032920307_row52260639"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p5253358"><a name="en-us_topic_0032920307_p5253358"></a><a name="en-us_topic_0032920307_p5253358"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p22868878"><a name="en-us_topic_0032920307_p22868878"></a><a name="en-us_topic_0032920307_p22868878"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p40439847"><a name="en-us_topic_0032920307_p40439847"></a><a name="en-us_topic_0032920307_p40439847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p54402144"><a name="en-us_topic_0032920307_p54402144"></a><a name="en-us_topic_0032920307_p54402144"></a>Project ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0032920307_row19857248"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0032920307_p64933228"><a name="en-us_topic_0032920307_p64933228"></a><a name="en-us_topic_0032920307_p64933228"></a>group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.24%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0032920307_p25100141"><a name="en-us_topic_0032920307_p25100141"></a><a name="en-us_topic_0032920307_p25100141"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0032920307_p19845579"><a name="en-us_topic_0032920307_p19845579"></a><a name="en-us_topic_0032920307_p19845579"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.35%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0032920307_p63988077"><a name="en-us_topic_0032920307_p63988077"></a><a name="en-us_topic_0032920307_p63988077"></a>ID of a user group.</p>
    </td>
    </tr>
    </tbody>
    </table>


## **Request**<a name="section1437107585444"></a>

-   Request header parameter description

    <a name="en-us_topic_0032920307_table21736211"></a>
    <table><thead align="left"><tr id="en-us_topic_0032920307_row48433347"><th class="cellrowborder" valign="top" width="19.490000000000002%" id="mcps1.1.5.1.1"><p id="en-us_topic_0032920307_p30787047"><a name="en-us_topic_0032920307_p30787047"></a><a name="en-us_topic_0032920307_p30787047"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_1"><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a><a name="a173ae121cc9e48328ca613e72f2a1504_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.860000000000003%" id="mcps1.1.5.1.2"><p id="en-us_topic_0032920307_p10722842"><a name="en-us_topic_0032920307_p10722842"></a><a name="en-us_topic_0032920307_p10722842"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
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
    <td class="cellrowborder" valign="top" width="44.480000000000004%" headers="mcps1.1.5.1.4 "><p id="p60756946111611"><a name="p60756946111611"></a><a name="p60756946111611"></a>Authenticated token with the <strong id="b750798910387"><a name="b750798910387"></a><a name="b750798910387"></a>Security Administrator</strong> permission.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample request

    ```
    curl -i -k -H "X-Auth-Token:$token" -H 'Content-Type:application/json;charset=utf8' -X GET https://10.22.44.158:31943/v3/projects/073bbf60da374853841cf6624c94de4b/groups/47d79cabc2cf4c35b13493d919a5bb3d/roles
    ```


## **Response**<a name="section422798898594"></a>

-   Response body parameter description

    <a name="table1056195410010"></a>
    <table><thead align="left"><tr id="row2747156110010"><th class="cellrowborder" valign="top" width="19.490000000000002%" id="mcps1.1.5.1.1"><p id="p447620910517"><a name="p447620910517"></a><a name="p447620910517"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_3"><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a><a name="a173ae121cc9e48328ca613e72f2a1504_3"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.85%" id="mcps1.1.5.1.2"><p id="p17765536155914"><a name="p17765536155914"></a><a name="p17765536155914"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.990000000000002%" id="mcps1.1.5.1.3"><p id="p755696810517"><a name="p755696810517"></a><a name="p755696810517"></a><strong id="b842352706143526_5"><a name="b842352706143526_5"></a><a name="b842352706143526_5"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.67%" id="mcps1.1.5.1.4"><p id="p6407638510517"><a name="p6407638510517"></a><a name="p6407638510517"></a><strong id="b20601766145329_5"><a name="b20601766145329_5"></a><a name="b20601766145329_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row570214510010"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p5922062510010"><a name="p5922062510010"></a><a name="p5922062510010"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.1.5.1.2 "><p id="p17658363596"><a name="p17658363596"></a><a name="p17658363596"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p5331155510010"><a name="p5331155510010"></a><a name="p5331155510010"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.67%" headers="mcps1.1.5.1.4 "><p id="p2326866010010"><a name="p2326866010010"></a><a name="p2326866010010"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row809135110010"><td class="cellrowborder" valign="top" width="19.490000000000002%" headers="mcps1.1.5.1.1 "><p id="p5141972010010"><a name="p5141972010010"></a><a name="p5141972010010"></a>roles</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.1.5.1.2 "><p id="p6765836125917"><a name="p6765836125917"></a><a name="p6765836125917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.990000000000002%" headers="mcps1.1.5.1.3 "><p id="p852996010010"><a name="p852996010010"></a><a name="p852996010010"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.67%" headers="mcps1.1.5.1.4 "><p id="p1983818310010"><a name="p1983818310010"></a><a name="p1983818310010"></a>List of roles.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Role parameter description

    <a name="table4865996110948"></a>
    <table><thead align="left"><tr id="row3498648810948"><th class="cellrowborder" valign="top" width="19.689999999999998%" id="mcps1.1.5.1.1"><p id="p1533325610948"><a name="p1533325610948"></a><a name="p1533325610948"></a><strong id="a173ae121cc9e48328ca613e72f2a1504_5"><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a><a name="a173ae121cc9e48328ca613e72f2a1504_5"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.65%" id="mcps1.1.5.1.2"><p id="p58551667141645"><a name="p58551667141645"></a><a name="p58551667141645"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_5"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_5"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.669999999999998%" id="mcps1.1.5.1.3"><p id="p3403423310948"><a name="p3403423310948"></a><a name="p3403423310948"></a><strong id="b842352706143526_7"><a name="b842352706143526_7"></a><a name="b842352706143526_7"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.99%" id="mcps1.1.5.1.4"><p id="p530949010948"><a name="p530949010948"></a><a name="p530949010948"></a><strong id="b20601766145329_7"><a name="b20601766145329_7"></a><a name="b20601766145329_7"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61939585101142"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p20585353101142"><a name="p20585353101142"></a><a name="p20585353101142"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p47847589141645"><a name="p47847589141645"></a><a name="p47847589141645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p56800915101142"><a name="p56800915101142"></a><a name="p56800915101142"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p37471393101142"><a name="p37471393101142"></a><a name="p37471393101142"></a>ID of a role.</p>
    </td>
    </tr>
    <tr id="row66853790101157"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p64813205101157"><a name="p64813205101157"></a><a name="p64813205101157"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p32688602141645"><a name="p32688602141645"></a><a name="p32688602141645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p15378285101157"><a name="p15378285101157"></a><a name="p15378285101157"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p37681557101157"><a name="p37681557101157"></a><a name="p37681557101157"></a>Resource links of a role.</p>
    </td>
    </tr>
    <tr id="row5718865710123"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p4493586710123"><a name="p4493586710123"></a><a name="p4493586710123"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p39046523141645"><a name="p39046523141645"></a><a name="p39046523141645"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p1592658110123"><a name="p1592658110123"></a><a name="p1592658110123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p1498466710123"><a name="p1498466710123"></a><a name="p1498466710123"></a>Name of a role.</p>
    </td>
    </tr>
    <tr id="row62241948141653"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p44238071141653"><a name="p44238071141653"></a><a name="p44238071141653"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p49414957141653"><a name="p49414957141653"></a><a name="p49414957141653"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p24794027141653"><a name="p24794027141653"></a><a name="p24794027141653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p25158040141653"><a name="p25158040141653"></a><a name="p25158040141653"></a>ID of the domain to which a role belongs.</p>
    </td>
    </tr>
    <tr id="row1595755819282"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p138172182291"><a name="p138172182291"></a><a name="p138172182291"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p13817121812293"><a name="p13817121812293"></a><a name="p13817121812293"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p17817111817298"><a name="p17817111817298"></a><a name="p17817111817298"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p19817191816298"><a name="p19817191816298"></a><a name="p19817191816298"></a>Display mode of a role.</p>
    <a name="ul41008790111658"></a><a name="ul41008790111658"></a><ul id="ul41008790111658"><li><strong id="b38557376113117"><a name="b38557376113117"></a><a name="b38557376113117"></a>AX</strong>: A role is displayed at the domain layer.</li><li><strong id="b36139777113117"><a name="b36139777113117"></a><a name="b36139777113117"></a>XA</strong>: A role is displayed at the project layer.</li><li><strong id="b41640863113117"><a name="b41640863113117"></a><a name="b41640863113117"></a>AA</strong>: A role is displayed at both the domain and project layers.</li><li><strong id="b17466753113117"><a name="b17466753113117"></a><a name="b17466753113117"></a>XX</strong>: A role is not displayed at the domain or project layer.</li></ul>
    </td>
    </tr>
    <tr id="row67023479141653"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p60157466141653"><a name="p60157466141653"></a><a name="p60157466141653"></a>display_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p30596437141653"><a name="p30596437141653"></a><a name="p30596437141653"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p19598108141653"><a name="p19598108141653"></a><a name="p19598108141653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p55050582141653"><a name="p55050582141653"></a><a name="p55050582141653"></a>Displayed name of a role.</p>
    </td>
    </tr>
    <tr id="row3530547141653"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p5212430141653"><a name="p5212430141653"></a><a name="p5212430141653"></a>catalog</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p23753576141653"><a name="p23753576141653"></a><a name="p23753576141653"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p176754141653"><a name="p176754141653"></a><a name="p176754141653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p37402834141653"><a name="p37402834141653"></a><a name="p37402834141653"></a>Directory where a role locates.</p>
    </td>
    </tr>
    <tr id="row9480727141653"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p34698220141653"><a name="p34698220141653"></a><a name="p34698220141653"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p58736815141653"><a name="p58736815141653"></a><a name="p58736815141653"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p45413157141653"><a name="p45413157141653"></a><a name="p45413157141653"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p42066103141653"><a name="p42066103141653"></a><a name="p42066103141653"></a>Policy of a role.</p>
    </td>
    </tr>
    <tr id="row61388450141653"><td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.1 "><p id="p15390469141653"><a name="p15390469141653"></a><a name="p15390469141653"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.65%" headers="mcps1.1.5.1.2 "><p id="p7532843141653"><a name="p7532843141653"></a><a name="p7532843141653"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p46581224141653"><a name="p46581224141653"></a><a name="p46581224141653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.99%" headers="mcps1.1.5.1.4 "><p id="p11908964141653"><a name="p11908964141653"></a><a name="p11908964141653"></a>Description of a role.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
        "links": {
            "self": " www.example.com/v3/projects/3a4cd4d559d8492bbe7bd355643f9763/groups/728da352c017480f80b5a96beb15f0e6/roles",
            "previous": null,
            "next": null
        },
        "roles": [
            {
                "catalog": "BASE",
                "display_name": "Guest",
                "name": "readonly",
                "links": {
                    "self": " www.example.com/v3/roles/13d132b7856945788f6df7eb3ed5c35e"
                },
                "policy": {
                    "Version": "1.0",
                    "Statement": [
                        {
                            "Action": [
                                "*:*:Get*",
                                "*:*:List*"
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
                "domain_id": null,
                "type": "AA",
                "id": "13d132b7856945788f6df7eb3ed5c35e",
                "description": "Guest"
            },
            {
                "catalog": "BASE",
                "display_name": "Tenant Administrator",
                "name": "te_admin",
                "links": {
                    "self": " www.example.com/v3/roles/1def304b73f14e8eb8d1eb9bf8337ae6"
                },
                "policy": {
                    "Version": "1.0",
                    "Statement": [
                        {
                            "Action": [
                                "*"
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
                "domain_id": null,
                "type": "AA",
                "id": "1def304b73f14e8eb8d1eb9bf8337ae6",
                "description": "Tenant Administrator"
            }
        ]
    }
    ```


## **Status Codes**<a name="section5556784894735"></a>

<a name="en-us_topic_0032920307_table25927028"></a>
<table><thead align="left"><tr id="en-us_topic_0032920307_row10578662"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0032920307_p51565323"><a name="en-us_topic_0032920307_p51565323"></a><a name="en-us_topic_0032920307_p51565323"></a><strong id="b417103139635"><a name="b417103139635"></a><a name="b417103139635"></a>Status Code</strong></p>
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
<tr id="row61941807103648"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p51230500103648"><a name="p51230500103648"></a><a name="p51230500103648"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p56029858103648"><a name="p56029858103648"></a><a name="p56029858103648"></a>The server could not find the requested page.</p>
</td>
</tr>
</tbody>
</table>


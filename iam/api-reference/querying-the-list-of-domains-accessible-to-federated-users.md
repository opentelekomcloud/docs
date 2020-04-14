# Querying the List of Domains Accessible to Federated Users<a name="en-us_topic_0057845596"></a>

## Function Description<a name="section58789816165237"></a>

This interface is used to query the list of domains accessible to federated users.

## URI<a name="section52559452192324"></a>

-   URI format

    GET /v3/OS-FEDERATION/domains


## Request<a name="section37561902165237"></a>

-   Request header parameter description

    <a name="table6425434193643"></a>
    <table><thead align="left"><tr id="row58375964193643"><th class="cellrowborder" valign="top" width="21.42%" id="mcps1.1.5.1.1"><p id="p4016564193643"><a name="p4016564193643"></a><a name="p4016564193643"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.689999999999998%" id="mcps1.1.5.1.2"><p id="p56906283193643"><a name="p56906283193643"></a><a name="p56906283193643"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.89%" id="mcps1.1.5.1.3"><p id="p46006239193643"><a name="p46006239193643"></a><a name="p46006239193643"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.1.5.1.4"><p id="p35517879193643"><a name="p35517879193643"></a><a name="p35517879193643"></a><strong id="a76acf34e8e7b48948763ec1b460ad92f"><a name="a76acf34e8e7b48948763ec1b460ad92f"></a><a name="a76acf34e8e7b48948763ec1b460ad92f"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16486847193643"><td class="cellrowborder" valign="top" width="21.42%" headers="mcps1.1.5.1.1 "><p id="p30832629193643"><a name="p30832629193643"></a><a name="p30832629193643"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.689999999999998%" headers="mcps1.1.5.1.2 "><p id="p14415019193643"><a name="p14415019193643"></a><a name="p14415019193643"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.89%" headers="mcps1.1.5.1.3 "><p id="p26765861193643"><a name="p26765861193643"></a><a name="p26765861193643"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.5.1.4 "><p id="p50742315193643"><a name="p50742315193643"></a><a name="p50742315193643"></a>Unscoped token. For details, see <a href="obtaining-an-unscoped-token-in-federated-identity-authentication-mode-(sp-initiated).md">Obtaining an Unscoped Token in Federated Identity Authentication Mode (SP Initiated)</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The GET /v3/auth/domains interface is recommended. The response formats returned using the GET /v3/auth/domains and GET /v3/OS-FEDERATION/domains interfaces are the same. For details, see  [Querying the List of Domains Accessible to Users](querying-the-list-of-domains-accessible-to-users.md).  


-   Sample request

    ```
    GET /v3/OS-FEDERATION/domains
    ```


## Response<a name="section40971139165237"></a>

-   Response body parameter description

    <a name="table30327949165237"></a>
    <table><thead align="left"><tr id="row21947087165237"><th class="cellrowborder" valign="top" width="21.55%" id="mcps1.1.5.1.1"><p id="p32883631165237"><a name="p32883631165237"></a><a name="p32883631165237"></a><strong id="b33528600105430"><a name="b33528600105430"></a><a name="b33528600105430"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.82%" id="mcps1.1.5.1.2"><p id="p46328435165237"><a name="p46328435165237"></a><a name="p46328435165237"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.63%" id="mcps1.1.5.1.3"><p id="p61615748165237"><a name="p61615748165237"></a><a name="p61615748165237"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="40%" id="mcps1.1.5.1.4"><p id="p24819657165237"><a name="p24819657165237"></a><a name="p24819657165237"></a><strong id="b9974812105430"><a name="b9974812105430"></a><a name="b9974812105430"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64235178165237"><td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.1 "><p id="p35666961165237"><a name="p35666961165237"></a><a name="p35666961165237"></a>domains</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.82%" headers="mcps1.1.5.1.2 "><p id="p3342691165237"><a name="p3342691165237"></a><a name="p3342691165237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="p2322570165237"><a name="p2322570165237"></a><a name="p2322570165237"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.5.1.4 "><p id="p53910510165237"><a name="p53910510165237"></a><a name="p53910510165237"></a>List of domains.</p>
    </td>
    </tr>
    <tr id="row15432546165237"><td class="cellrowborder" valign="top" width="21.55%" headers="mcps1.1.5.1.1 "><p id="p42076715165237"><a name="p42076715165237"></a><a name="p42076715165237"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.82%" headers="mcps1.1.5.1.2 "><p id="p52770789165237"><a name="p52770789165237"></a><a name="p52770789165237"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.63%" headers="mcps1.1.5.1.3 "><p id="p46575544165237"><a name="p46575544165237"></a><a name="p46575544165237"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="40%" headers="mcps1.1.5.1.4 "><p id="p14522699165237"><a name="p14522699165237"></a><a name="p14522699165237"></a>Resource links of a domain.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Sample response

    ```
    {
      "domains": [
        {
          "links": {
            "self": "https://sample.domain.com/v3/domains/e31ac82d778b4d128cb6fed37fd72cdb"
          },
          "description": null,
          "name": "exampledomain",
          "enabled": true,
          "id": "e31ac82d778b4d128cb6fed37fd72cdb"
        }
      ],
      "links": {
        "self": "https://sample.domain.com/v3/OS-FEDERATION/domains",
        "previous": null,
        "next": null
      }
    }
    ```


## Status Codes<a name="section15537603165237"></a>

<a name="table50586344165237"></a>
<table><thead align="left"><tr id="row57508784165237"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p27699899165237"><a name="p27699899165237"></a><a name="p27699899165237"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p29099351165237"><a name="p29099351165237"></a><a name="p29099351165237"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row8237227165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p63235680165237"><a name="p63235680165237"></a><a name="p63235680165237"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p21816478165237"><a name="p21816478165237"></a><a name="p21816478165237"></a>The request is successful.</p>
</td>
</tr>
<tr id="row62130575165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p66520684165237"><a name="p66520684165237"></a><a name="p66520684165237"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p19466342165237"><a name="p19466342165237"></a><a name="p19466342165237"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row40979353165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p30993288165237"><a name="p30993288165237"></a><a name="p30993288165237"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p27428424165237"><a name="p27428424165237"></a><a name="p27428424165237"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row45529230165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p63989002165237"><a name="p63989002165237"></a><a name="p63989002165237"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p15726634165237"><a name="p15726634165237"></a><a name="p15726634165237"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row7321979165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p56209421165237"><a name="p56209421165237"></a><a name="p56209421165237"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p56669239165237"><a name="p56669239165237"></a><a name="p56669239165237"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row40261109165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p39924407165237"><a name="p39924407165237"></a><a name="p39924407165237"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p12651558165237"><a name="p12651558165237"></a><a name="p12651558165237"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row46755161165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p29071734165237"><a name="p29071734165237"></a><a name="p29071734165237"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p6000243165237"><a name="p6000243165237"></a><a name="p6000243165237"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row54002189165237"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p12101182165237"><a name="p12101182165237"></a><a name="p12101182165237"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p40671651165237"><a name="p40671651165237"></a><a name="p40671651165237"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>


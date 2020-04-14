# Querying the List of Projects Accessible to Federated Users<a name="en-us_topic_0057845595"></a>

## Function Description<a name="section5828421916512"></a>

This interface is used to query the list of projects accessible to federated users. The project list is used to obtain the scoped token in federated identity authentication mode.

## URI<a name="section826961192054"></a>

URI format

GET /v3/OS-FEDERATION/projects

## Request<a name="section4822038116512"></a>

-   Request header parameter description

    <a name="table1353674916512"></a>
    <table><thead align="left"><tr id="row2490362916512"><th class="cellrowborder" valign="top" width="20.44%" id="mcps1.1.5.1.1"><p id="p392808116512"><a name="p392808116512"></a><a name="p392808116512"></a><strong id="a6f95694edbbb43d8a152536754b86c82"><a name="a6f95694edbbb43d8a152536754b86c82"></a><a name="a6f95694edbbb43d8a152536754b86c82"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.9%" id="mcps1.1.5.1.2"><p id="p4973910816512"><a name="p4973910816512"></a><a name="p4973910816512"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_1"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.09%" id="mcps1.1.5.1.3"><p id="p233598516512"><a name="p233598516512"></a><a name="p233598516512"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_1"><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.57%" id="mcps1.1.5.1.4"><p id="p5499708616512"><a name="p5499708616512"></a><a name="p5499708616512"></a><strong id="a76acf34e8e7b48948763ec1b460ad92f"><a name="a76acf34e8e7b48948763ec1b460ad92f"></a><a name="a76acf34e8e7b48948763ec1b460ad92f"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2557896316512"><td class="cellrowborder" valign="top" width="20.44%" headers="mcps1.1.5.1.1 "><p id="p5863013716512"><a name="p5863013716512"></a><a name="p5863013716512"></a>X-Auth-Token</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.9%" headers="mcps1.1.5.1.2 "><p id="p5142066316512"><a name="p5142066316512"></a><a name="p5142066316512"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.1.5.1.3 "><p id="p432421416512"><a name="p432421416512"></a><a name="p432421416512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.57%" headers="mcps1.1.5.1.4 "><p id="p1471708616512"><a name="p1471708616512"></a><a name="p1471708616512"></a>Unscoped token. For details about how to obtain a token, see <a href="obtaining-an-unscoped-token-in-federated-identity-authentication-mode-(sp-initiated).md">Obtaining an Unscoped Token in Federated Identity Authentication Mode (SP Initiated)</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The GET /v3/auth/projects interface is recommended. The response formats returned using the GET /v3/auth/projects and GET /v3/OS-FEDERATION/projects interfaces are the same. For details, see  [Querying the List of Projects Accessible to Users](querying-the-list-of-projects-accessible-to-users.md).  


-   Sample request

    ```
    GET /v3/OS-FEDERATION/projects
    ```


## Response<a name="section6050485516512"></a>

-   Response body parameter description

    <a name="table13331867193912"></a>
    <table><thead align="left"><tr id="row24511618193912"><th class="cellrowborder" valign="top" width="20.62%" id="mcps1.1.5.1.1"><p id="p57442782193912"><a name="p57442782193912"></a><a name="p57442782193912"></a><strong id="b28097194105329"><a name="b28097194105329"></a><a name="b28097194105329"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.759999999999998%" id="mcps1.1.5.1.2"><p id="p22353756193912"><a name="p22353756193912"></a><a name="p22353756193912"></a><strong id="a105e6ed8c3de4c5a9dde97ae5a71071e_3"><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a><a name="a105e6ed8c3de4c5a9dde97ae5a71071e_3"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.360000000000003%" id="mcps1.1.5.1.3"><p id="p65823815193912"><a name="p65823815193912"></a><a name="p65823815193912"></a><strong id="a703d34a49a2f4162bc1a1a439f655f95_3"><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a><a name="a703d34a49a2f4162bc1a1a439f655f95_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.26%" id="mcps1.1.5.1.4"><p id="p30128774193912"><a name="p30128774193912"></a><a name="p30128774193912"></a><strong id="b28042497105329"><a name="b28042497105329"></a><a name="b28042497105329"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6434223193912"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p39284002193912"><a name="p39284002193912"></a><a name="p39284002193912"></a>projects</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.1.5.1.2 "><p id="p27887566193912"><a name="p27887566193912"></a><a name="p27887566193912"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.3 "><p id="p44300399193912"><a name="p44300399193912"></a><a name="p44300399193912"></a>array</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.1.5.1.4 "><p id="p31562605193912"><a name="p31562605193912"></a><a name="p31562605193912"></a>List of projects.</p>
    </td>
    </tr>
    <tr id="row28187440193912"><td class="cellrowborder" valign="top" width="20.62%" headers="mcps1.1.5.1.1 "><p id="p57908014193912"><a name="p57908014193912"></a><a name="p57908014193912"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.759999999999998%" headers="mcps1.1.5.1.2 "><p id="p60037521193912"><a name="p60037521193912"></a><a name="p60037521193912"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.360000000000003%" headers="mcps1.1.5.1.3 "><p id="p31201070193912"><a name="p31201070193912"></a><a name="p31201070193912"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.26%" headers="mcps1.1.5.1.4 "><p id="p44258731193912"><a name="p44258731193912"></a><a name="p44258731193912"></a>Resource links of a project.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Sample response

    ```
    {
      "links": {
        "self": "https://sample.domain.com/v3/OS-FEDERATION/projects",
        "previous": null,
        "next": null
      },
      "projects": [
        {
          "is_domain": false,
          "description": "",
          "links": {
            "self": "https://sample.domain.com/v3/projects/05cf683c351e43518618d9fa96a5efa9"
          },
          "enabled": true,
          "id": "05cf683c351e43518618d9fa96a5efa9",
          "parent_id": "e31ac82d778b4d128cb6fed37fd72cdb",
          "domain_id": "e31ac82d778b4d128cb6fed37fd72cdb",
          "name": "region_name"
        },
        {
          "is_domain": false,
          "description": "",
          "links": {
            "self": "https://sample.domain.com/v3/projects/32b56f108f87418e8219317beb0fff3c"
          },
          "enabled": true,
          "id": "32b56f108f87418e8219317beb0fff3c",
          "parent_id": "e31ac82d778b4d128cb6fed37fd72cdb",
          "domain_id": "e31ac82d778b4d128cb6fed37fd72cdb",
          "name": "MOS"   //Default project name of OBS
        }
      ]
    }
    ```


## Status Codes<a name="section3776874116512"></a>

<a name="table3936921516512"></a>
<table><thead align="left"><tr id="row6177659016512"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3784787616512"><a name="p3784787616512"></a><a name="p3784787616512"></a><strong id="b37151362163018"><a name="b37151362163018"></a><a name="b37151362163018"></a>Status Code</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p4577915216512"><a name="p4577915216512"></a><a name="p4577915216512"></a><strong id="b38470707163018"><a name="b38470707163018"></a><a name="b38470707163018"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1712379916512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4485049916512"><a name="p4485049916512"></a><a name="p4485049916512"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p901183616512"><a name="p901183616512"></a><a name="p901183616512"></a>The request is successful.</p>
</td>
</tr>
<tr id="row1399766516512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p6006904716512"><a name="p6006904716512"></a><a name="p6006904716512"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3375463816512"><a name="p3375463816512"></a><a name="p3375463816512"></a>The server failed to process the request.</p>
</td>
</tr>
<tr id="row3535628916512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p4528716416512"><a name="p4528716416512"></a><a name="p4528716416512"></a>401</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p4438164316512"><a name="p4438164316512"></a><a name="p4438164316512"></a>You must enter a username and password to access the requested page.</p>
</td>
</tr>
<tr id="row6389047016512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p774555116512"><a name="p774555116512"></a><a name="p774555116512"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2340985616512"><a name="p2340985616512"></a><a name="p2340985616512"></a>You are forbidden to access the requested page.</p>
</td>
</tr>
<tr id="row936211516512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2013387616512"><a name="p2013387616512"></a><a name="p2013387616512"></a>405</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p2023129816512"><a name="p2023129816512"></a><a name="p2023129816512"></a>You are not allowed to use the method specified in the request.</p>
</td>
</tr>
<tr id="row4786395916512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p5177548316512"><a name="p5177548316512"></a><a name="p5177548316512"></a>413</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3306455816512"><a name="p3306455816512"></a><a name="p3306455816512"></a>The request entity is too large.</p>
</td>
</tr>
<tr id="row2914557416512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1198130216512"><a name="p1198130216512"></a><a name="p1198130216512"></a>500</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3096138616512"><a name="p3096138616512"></a><a name="p3096138616512"></a>Failed to complete the request because of an internal service error.</p>
</td>
</tr>
<tr id="row1021702116512"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p2227238716512"><a name="p2227238716512"></a><a name="p2227238716512"></a>503</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p5923292916512"><a name="p5923292916512"></a><a name="p5923292916512"></a>Failed to complete the request because the service is unavailable.</p>
</td>
</tr>
</tbody>
</table>


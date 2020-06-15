# Querying a Specified API Version<a name="en-us_topic_0168602243"></a>

## Function<a name="s14614fd2e90249f2a00ff431b58d556b"></a>

This API is used to query a specified API version of CTS.

## URI<a name="s66c905ae94ad4a81896c5e6f0de880ee"></a>

GET/\{api\_version\}

For details about the parameters, see  [Table 1](#t2f4b2999b4784e78845eefcc5eefac90).

**Table  1**  Parameters in the URI

<a name="t2f4b2999b4784e78845eefcc5eefac90"></a>
<table><thead align="left"><tr id="rdc2ba009c5a44fda8c8932cd467426f7"><th class="cellrowborder" valign="top" width="19.99%" id="mcps1.2.4.1.1"><p id="aa0f370895eb54cec85ccb5085c6c6086"><a name="aa0f370895eb54cec85ccb5085c6c6086"></a><a name="aa0f370895eb54cec85ccb5085c6c6086"></a><strong id="b842352706115119"><a name="b842352706115119"></a><a name="b842352706115119"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.93%" id="mcps1.2.4.1.2"><p id="a17bc27d00f7e4f8c8972352347ecde1b"><a name="a17bc27d00f7e4f8c8972352347ecde1b"></a><a name="a17bc27d00f7e4f8c8972352347ecde1b"></a><strong id="b842352706115121"><a name="b842352706115121"></a><a name="b842352706115121"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="59.08%" id="mcps1.2.4.1.3"><p id="a438c4c360956438491022a235aa79ade"><a name="a438c4c360956438491022a235aa79ade"></a><a name="a438c4c360956438491022a235aa79ade"></a><strong id="b842352706115259"><a name="b842352706115259"></a><a name="b842352706115259"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2a3d66ff4fab47d8a77ab46284cc7f1a"><td class="cellrowborder" valign="top" width="19.99%" headers="mcps1.2.4.1.1 "><p id="ad1fb114c63814589bbb9bb78381a2266"><a name="ad1fb114c63814589bbb9bb78381a2266"></a><a name="ad1fb114c63814589bbb9bb78381a2266"></a>api_version</p>
</td>
<td class="cellrowborder" valign="top" width="20.93%" headers="mcps1.2.4.1.2 "><p id="a3c677c4ed84b4c71b79e725c41d3d554"><a name="a3c677c4ed84b4c71b79e725c41d3d554"></a><a name="a3c677c4ed84b4c71b79e725c41d3d554"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59.08%" headers="mcps1.2.4.1.3 "><p id="af4bea01a46bd4d22be26f3e25c347a20"><a name="af4bea01a46bd4d22be26f3e25c347a20"></a><a name="af4bea01a46bd4d22be26f3e25c347a20"></a>API version</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="s43e8ae7913c64b42b4089af6a4bb7c0e"></a>

None

## Response<a name="se4d7fb16a4304abba52627518b31ac64"></a>

-   Parameter description

    **Table  2**  Parameters in the request

    <a name="t263122336250459e9ec01ffec56ae110"></a>
    <table><thead align="left"><tr id="rb18c3fefdebb44d4ba0cbad406309d03"><th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.5.1.1"><p id="ac99751e3b99743be9b705df8725016d5"><a name="ac99751e3b99743be9b705df8725016d5"></a><a name="ac99751e3b99743be9b705df8725016d5"></a><strong id="b788689952"><a name="b788689952"></a><a name="b788689952"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="en-us_topic_0133184491_p543845610355"><a name="en-us_topic_0133184491_p543845610355"></a><a name="en-us_topic_0133184491_p543845610355"></a><strong id="b1141385166"><a name="b1141385166"></a><a name="b1141385166"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="a5c880227147543d98f2434c60f7732c2"><a name="a5c880227147543d98f2434c60f7732c2"></a><a name="a5c880227147543d98f2434c60f7732c2"></a><strong id="b842352706115123"><a name="b842352706115123"></a><a name="b842352706115123"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="en-us_topic_0133184491_p244212561357"><a name="en-us_topic_0133184491_p244212561357"></a><a name="en-us_topic_0133184491_p244212561357"></a><strong id="b1190327049"><a name="b1190327049"></a><a name="b1190327049"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r142682925e0b4a48acccff5421424035"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="abac252cf9780497eb83917cc6b446fda"><a name="abac252cf9780497eb83917cc6b446fda"></a><a name="abac252cf9780497eb83917cc6b446fda"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="ac05f072f2220464c824423f42e236e8f"><a name="ac05f072f2220464c824423f42e236e8f"></a><a name="ac05f072f2220464c824423f42e236e8f"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133184491_p444855610353"><a name="en-us_topic_0133184491_p444855610353"></a><a name="en-us_topic_0133184491_p444855610353"></a>Array</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133184491_p344911569354"><a name="en-us_topic_0133184491_p344911569354"></a><a name="en-us_topic_0133184491_p344911569354"></a>Specifies the list of all API versions.</p>
    </td>
    </tr>
    <tr id="r87b91e0d72cf434f898712c3c88b7f8b"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="aadd66af882714d0dba06a22bef915b13"><a name="aadd66af882714d0dba06a22bef915b13"></a><a name="aadd66af882714d0dba06a22bef915b13"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="a98b7dbe2700f4935ac19ec62f5305df9"><a name="a98b7dbe2700f4935ac19ec62f5305df9"></a><a name="a98b7dbe2700f4935ac19ec62f5305df9"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="a94f103f4c79f4bf78e57c7a5c2b53775"><a name="a94f103f4c79f4bf78e57c7a5c2b53775"></a><a name="a94f103f4c79f4bf78e57c7a5c2b53775"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133184491_p045585620357"><a name="en-us_topic_0133184491_p045585620357"></a><a name="en-us_topic_0133184491_p045585620357"></a>Specifies the version ID (version number), for example, v1.</p>
    </td>
    </tr>
    <tr id="r276c1d13c0bb4876aa41721ff95c41f6"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="a3aabde5277a54ddb98233f76d86d7171"><a name="a3aabde5277a54ddb98233f76d86d7171"></a><a name="a3aabde5277a54ddb98233f76d86d7171"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="add8b9996eee3446f87d74dbd29946b1b"><a name="add8b9996eee3446f87d74dbd29946b1b"></a><a name="add8b9996eee3446f87d74dbd29946b1b"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0133184491_p346325618353"><a name="en-us_topic_0133184491_p346325618353"></a><a name="en-us_topic_0133184491_p346325618353"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133184491_p746525619351"><a name="en-us_topic_0133184491_p746525619351"></a><a name="en-us_topic_0133184491_p746525619351"></a>Specifies the API URL.</p>
    </td>
    </tr>
    <tr id="row131913551711"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p16283354130"><a name="p16283354130"></a><a name="p16283354130"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p139117297139"><a name="p139117297139"></a><a name="p139117297139"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p13242332181317"><a name="p13242332181317"></a><a name="p13242332181317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p2269104581219"><a name="p2269104581219"></a><a name="p2269104581219"></a>Specifies the reference address of the current API version.</p>
    </td>
    </tr>
    <tr id="row5612123213170"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="p2139956101218"><a name="p2139956101218"></a><a name="p2139956101218"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="p1994102917139"><a name="p1994102917139"></a><a name="p1994102917139"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p824653211138"><a name="p824653211138"></a><a name="p824653211138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p513917563125"><a name="p513917563125"></a><a name="p513917563125"></a>Specifies the relationship between the current API version and the referenced address.</p>
    </td>
    </tr>
    <tr id="r9ce51fe931a144c3869af318434886cb"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="ae33082d4b436400e9879d0c779929a41"><a name="ae33082d4b436400e9879d0c779929a41"></a><a name="ae33082d4b436400e9879d0c779929a41"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133184491_p164706561359"><a name="en-us_topic_0133184491_p164706561359"></a><a name="en-us_topic_0133184491_p164706561359"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="ace33aa601e144b0c9fea118df489ca46"><a name="ace33aa601e144b0c9fea118df489ca46"></a><a name="ace33aa601e144b0c9fea118df489ca46"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="acbefcc854668470fad0139c50833333c"><a name="acbefcc854668470fad0139c50833333c"></a><a name="acbefcc854668470fad0139c50833333c"></a>If the APIs of this version support microversions, set this parameter to the supported maximum microversion. If the microversion is not supported, leave this parameter empty.</p>
    </td>
    </tr>
    <tr id="r47aefcb639c34c5b9424cbc20e3636bb"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0133184491_p647516561358"><a name="en-us_topic_0133184491_p647516561358"></a><a name="en-us_topic_0133184491_p647516561358"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133184491_p447812565352"><a name="en-us_topic_0133184491_p447812565352"></a><a name="en-us_topic_0133184491_p447812565352"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="a85867596c81c4645aaabd08e5b81165b"><a name="a85867596c81c4645aaabd08e5b81165b"></a><a name="a85867596c81c4645aaabd08e5b81165b"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="ac8a6589500da484fbcc14e244f496afe"><a name="ac8a6589500da484fbcc14e244f496afe"></a><a name="ac8a6589500da484fbcc14e244f496afe"></a>Specifies the version status. The options are as follows:</p>
    <p id="a6889c7d117df43bda353644adfe505ea"><a name="a6889c7d117df43bda353644adfe505ea"></a><a name="a6889c7d117df43bda353644adfe505ea"></a><strong id="b842352706192132"><a name="b842352706192132"></a><a name="b842352706192132"></a>CURRENT</strong>: indicates that the version is the primary version.</p>
    <p id="ab3a64fa2cb3b41b797e6122d0700d75d"><a name="ab3a64fa2cb3b41b797e6122d0700d75d"></a><a name="ab3a64fa2cb3b41b797e6122d0700d75d"></a><strong id="b842352706192150"><a name="b842352706192150"></a><a name="b842352706192150"></a>SUPPORTED</strong>: indicates that the version is an old version, but it is still supported.</p>
    <p id="af29a315255534a48aaf87dcd0118c9d8"><a name="af29a315255534a48aaf87dcd0118c9d8"></a><a name="af29a315255534a48aaf87dcd0118c9d8"></a><strong id="b84235270619220"><a name="b84235270619220"></a><a name="b84235270619220"></a>DEPRECATED</strong>: indicates that the version is a deprecated version, which may be deleted later.</p>
    </td>
    </tr>
    <tr id="ra0ae61f2decc4559aec48172eb70b51d"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="ae2d4298c05de4adfa2a5b41005171a5d"><a name="ae2d4298c05de4adfa2a5b41005171a5d"></a><a name="ae2d4298c05de4adfa2a5b41005171a5d"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="a9dd320bf902847be9254421018a06a42"><a name="a9dd320bf902847be9254421018a06a42"></a><a name="a9dd320bf902847be9254421018a06a42"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="a985e8249324e4106be76df87f1e2e820"><a name="a985e8249324e4106be76df87f1e2e820"></a><a name="a985e8249324e4106be76df87f1e2e820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="ab4745035d4014c3884e734939219603f"><a name="ab4745035d4014c3884e734939219603f"></a><a name="ab4745035d4014c3884e734939219603f"></a>Specifies the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
    </td>
    </tr>
    <tr id="r7e2fbeb893894eca92c1a1a920c9ad22"><td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.5.1.1 "><p id="ab5633a85365847acb6bdaabed082c8c8"><a name="ab5633a85365847acb6bdaabed082c8c8"></a><a name="ab5633a85365847acb6bdaabed082c8c8"></a>min_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0133184491_p14966566355"><a name="en-us_topic_0133184491_p14966566355"></a><a name="en-us_topic_0133184491_p14966566355"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="a7b50d389e8e2421fbcf50cded08baf59"><a name="a7b50d389e8e2421fbcf50cded08baf59"></a><a name="a7b50d389e8e2421fbcf50cded08baf59"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0133184491_p205014565351"><a name="en-us_topic_0133184491_p205014565351"></a><a name="en-us_topic_0133184491_p205014565351"></a>If the APIs of this version support microversions, set this parameter to the supported minimum microversion. If the microversion is not supported, leave this field empty.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "version": 
        {
          "id": "v1.0",
          "links": [
            {
              "href": "https://x.x.x.x/v1.0/",
              "rel": "self"
            }
          ],
          "min_version": "",
          "status": "CURRENT",
          "updated": "2018-09-30T00:00:00Z",
          "version": ""
        }
      ]
    }
    ```


## Returned Value<a name="s4d3f9f864ef240d5aede6b6c784671b8"></a>

-   Normal

    200

-   Abnormal

    **Table  3**  Return code for failed requests

    <a name="en-us_topic_0133184491_table46793998"></a>
    <table><thead align="left"><tr id="en-us_topic_0133184491_row65573909"><th class="cellrowborder" valign="top" width="61.839999999999996%" id="mcps1.2.3.1.1"><p id="en-us_topic_0133184491_p9886408"><a name="en-us_topic_0133184491_p9886408"></a><a name="en-us_topic_0133184491_p9886408"></a><strong id="b842352706112115"><a name="b842352706112115"></a><a name="b842352706112115"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.16%" id="mcps1.2.3.1.2"><p id="en-us_topic_0133184491_p62601592"><a name="en-us_topic_0133184491_p62601592"></a><a name="en-us_topic_0133184491_p62601592"></a><strong id="b1125561795"><a name="b1125561795"></a><a name="b1125561795"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0133184491_row37564172"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p22799085"><a name="en-us_topic_0133184491_p22799085"></a><a name="en-us_topic_0133184491_p22799085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p44643603"><a name="en-us_topic_0133184491_p44643603"></a><a name="en-us_topic_0133184491_p44643603"></a>Request error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row66248115"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p64497130"><a name="en-us_topic_0133184491_p64497130"></a><a name="en-us_topic_0133184491_p64497130"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p42202994"><a name="en-us_topic_0133184491_p42202994"></a><a name="en-us_topic_0133184491_p42202994"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row44282627"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p30123063"><a name="en-us_topic_0133184491_p30123063"></a><a name="en-us_topic_0133184491_p30123063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p15114764"><a name="en-us_topic_0133184491_p15114764"></a><a name="en-us_topic_0133184491_p15114764"></a>The request was forbidden.</p>
    </td>
    </tr>
    <tr id="row1385894717145"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="p6738773164846"><a name="p6738773164846"></a><a name="p6738773164846"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="p8969753164846"><a name="p8969753164846"></a><a name="p8969753164846"></a>The server failed to find the requested resource.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row1815156"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p12809933"><a name="en-us_topic_0133184491_p12809933"></a><a name="en-us_topic_0133184491_p12809933"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p10309404"><a name="en-us_topic_0133184491_p10309404"></a><a name="en-us_topic_0133184491_p10309404"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row25675773"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p66471715"><a name="en-us_topic_0133184491_p66471715"></a><a name="en-us_topic_0133184491_p66471715"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p5281111"><a name="en-us_topic_0133184491_p5281111"></a><a name="en-us_topic_0133184491_p5281111"></a>The number requests exceeded the upper limit.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row47530006"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p24725298"><a name="en-us_topic_0133184491_p24725298"></a><a name="en-us_topic_0133184491_p24725298"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0133184491_p39567352"><a name="en-us_topic_0133184491_p39567352"></a><a name="en-us_topic_0133184491_p39567352"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0133184491_row20561848"><td class="cellrowborder" valign="top" width="61.839999999999996%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0133184491_p54897010"><a name="en-us_topic_0133184491_p54897010"></a><a name="en-us_topic_0133184491_p54897010"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.16%" headers="mcps1.2.3.1.2 "><p id="a30ba56fc3d6d4269ab9eed7e32e91d0e"><a name="a30ba56fc3d6d4269ab9eed7e32e91d0e"></a><a name="a30ba56fc3d6d4269ab9eed7e32e91d0e"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



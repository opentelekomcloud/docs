# Querying a Specified API Version<a name="en-dc_topic_0055025312"></a>

## Function<a name="section109661156152112"></a>

This API is used to query a specified API version supported by Direct Connect.

## URI<a name="section11867232184814"></a>

GET /\{api\_version\}

## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

[Table 1](#table49902238182444)  lists the response parameters.

**Table  1**  Response parameters

<a name="table49902238182444"></a>
<table><thead align="left"><tr id="row27727643182444"><th class="cellrowborder" valign="top" width="21.529999999999998%" id="mcps1.2.4.1.1"><p id="p31346634182444"><a name="p31346634182444"></a><a name="p31346634182444"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.2.4.1.2"><p id="p56049421182444"><a name="p56049421182444"></a><a name="p56049421182444"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.010000000000005%" id="mcps1.2.4.1.3"><p id="p50789233182444"><a name="p50789233182444"></a><a name="p50789233182444"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39593523182444"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p1326331857"><a name="p1326331857"></a><a name="p1326331857"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p183219331352"><a name="p183219331352"></a><a name="p183219331352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p1232103319520"><a name="p1232103319520"></a><a name="p1232103319520"></a>Indicates the version number, for example, <strong id="b842352706151910"><a name="b842352706151910"></a><a name="b842352706151910"></a>v2.0</strong></p>
</td>
</tr>
<tr id="row64801111182444"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p13233311516"><a name="p13233311516"></a><a name="p13233311516"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p932153310512"><a name="p932153310512"></a><a name="p932153310512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p113219331057"><a name="p113219331057"></a><a name="p113219331057"></a>Indicates the API URL.</p>
</td>
</tr>
<tr id="row314332616201"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p124464144178"><a name="p124464144178"></a><a name="p124464144178"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p244781412174"><a name="p244781412174"></a><a name="p244781412174"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p144471814201718"><a name="p144471814201718"></a><a name="p144471814201718"></a>Indicates the reference address of the current API version.</p>
</td>
</tr>
<tr id="row342330162012"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p168331418121713"><a name="p168331418121713"></a><a name="p168331418121713"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p17833131818174"><a name="p17833131818174"></a><a name="p17833131818174"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p118332018191716"><a name="p118332018191716"></a><a name="p118332018191716"></a>Indicates the relationship between the current API version and the referenced address.</p>
</td>
</tr>
<tr id="row20716483182444"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p15325331257"><a name="p15325331257"></a><a name="p15325331257"></a>version</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p19321133251"><a name="p19321133251"></a><a name="p19321133251"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p93210331152"><a name="p93210331152"></a><a name="p93210331152"></a>Indicates the version. If APIs of this version support minor versions, set this parameter to the supported maximum minor version. If the minor versions are not supported, leave this parameter blank.</p>
</td>
</tr>
<tr id="row48951951182444"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p19326339519"><a name="p19326339519"></a><a name="p19326339519"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p1432193314519"><a name="p1432193314519"></a><a name="p1432193314519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p15331033950"><a name="p15331033950"></a><a name="p15331033950"></a>Indicates the version status. Possible values are as follows:</p>
<a name="ul597114391474"></a><a name="ul597114391474"></a><ul id="ul597114391474"><li><strong>CURRENT</strong>: indicates a primary version.</li><li><strong>SUPPORTED</strong>: indicates an old version but is still supported.</li><li><strong>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
</td>
</tr>
<tr id="row2329187257"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p18331633956"><a name="p18331633956"></a><a name="p18331633956"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p15331331459"><a name="p15331331459"></a><a name="p15331331459"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p133303319510"><a name="p133303319510"></a><a name="p133303319510"></a>Indicates the version release time, which must be the UTC time. For example, the release time of v1 is 2014-06-28T12:20:21Z.</p>
</td>
</tr>
<tr id="row4783956182444"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p833333852"><a name="p833333852"></a><a name="p833333852"></a>min_version</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="p7336331759"><a name="p7336331759"></a><a name="p7336331759"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.010000000000005%" headers="mcps1.2.4.1.3 "><p id="p1333933458"><a name="p1333933458"></a><a name="p1333933458"></a>If this API version supports microversions, the minimum microversion number is returned. If microversions are not supported, no value is returned.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section542210409508"></a>

-   Example request

    ```
    GET /v2.0
    ```

-   Example response

    ```
    {
      "version": {
        "id": "v2.0",
        "links": [
          {
            "href": "https://dcaas.***region.myhwclouds.com/v2.0",
            "rel": "self"
          }
        ],
        "updated": "2017-11-30T00:00:00Z",
        "status": "CURRENT",
        "version": "",
        "min_version": ""
      }
    }
    ```



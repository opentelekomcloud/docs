# Querying All API Versions<a name="en-dc_topic_0055025311"></a>

## Function<a name="section109661156152112"></a>

This API is used to query all API versions supported by Direct Connect.

## URI<a name="section11867232184814"></a>

GET /

## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

[Table 1](#table49902238182444)  lists the response parameters.

**Table  1**  Response parameters

<a name="table49902238182444"></a>
<table><thead align="left"><tr id="row27727643182444"><th class="cellrowborder" valign="top" width="25.277472252774725%" id="mcps1.2.4.1.1"><p id="p44979764154022"><a name="p44979764154022"></a><a name="p44979764154022"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.01749825017498%" id="mcps1.2.4.1.2"><p id="p19482271154022"><a name="p19482271154022"></a><a name="p19482271154022"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.7050294970503%" id="mcps1.2.4.1.3"><p id="p47904218154022"><a name="p47904218154022"></a><a name="p47904218154022"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row27455432182444"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p14315331153"><a name="p14315331153"></a><a name="p14315331153"></a>versions</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p183213310519"><a name="p183213310519"></a><a name="p183213310519"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p7328337520"><a name="p7328337520"></a><a name="p7328337520"></a>Indicates all API versions.</p>
</td>
</tr>
<tr id="row39593523182444"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p1326331857"><a name="p1326331857"></a><a name="p1326331857"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p183219331352"><a name="p183219331352"></a><a name="p183219331352"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p103293310511"><a name="p103293310511"></a><a name="p103293310511"></a>Indicates the version number, for example, <strong id="b842352706151910"><a name="b842352706151910"></a><a name="b842352706151910"></a>v2.0</strong></p>
</td>
</tr>
<tr id="row64801111182444"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p13233311516"><a name="p13233311516"></a><a name="p13233311516"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p932153310512"><a name="p932153310512"></a><a name="p932153310512"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p13211331354"><a name="p13211331354"></a><a name="p13211331354"></a>Indicates the API URL.</p>
</td>
</tr>
<tr id="row1144591413177"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p124464144178"><a name="p124464144178"></a><a name="p124464144178"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p244781412174"><a name="p244781412174"></a><a name="p244781412174"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p944741418176"><a name="p944741418176"></a><a name="p944741418176"></a>Indicates the reference address of the current API version.</p>
</td>
</tr>
<tr id="row1383361812179"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p168331418121713"><a name="p168331418121713"></a><a name="p168331418121713"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p17833131818174"><a name="p17833131818174"></a><a name="p17833131818174"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p188334182178"><a name="p188334182178"></a><a name="p188334182178"></a>Indicates the relationship between the current API version and the referenced address.</p>
</td>
</tr>
<tr id="row48951951182444"><td class="cellrowborder" valign="top" width="25.277472252774725%" headers="mcps1.2.4.1.1 "><p id="p19326339519"><a name="p19326339519"></a><a name="p19326339519"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.01749825017498%" headers="mcps1.2.4.1.2 "><p id="p1432193314519"><a name="p1432193314519"></a><a name="p1432193314519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.7050294970503%" headers="mcps1.2.4.1.3 "><p id="p9331331653"><a name="p9331331653"></a><a name="p9331331653"></a>Indicates the version status. Possible values are as follows:</p>
<a name="ul1936014510535"></a><a name="ul1936014510535"></a><ul id="ul1936014510535"><li><strong>CURRENT</strong>: indicates a primary version.</li><li><strong>SUPPORTED</strong>: indicates an old version but is still supported.</li><li><strong>DEPRECATED</strong>: indicates a deprecated version which may be deleted later.</li></ul>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section542210409508"></a>

-   Example request

    ```
    GET /
    ```

-   Example response

    ```
    {
     "versions": [
        {
          "status": "CURRENT",
          "id": "v2.0",
          "links":[
            {
              "href": "https://network.az0.dc0.domainname.com/v2.0","rel": "self"
             }
          ]
        }
      ]
    }
    ```



# Logging Out Of a Session<a name="EN-US_TOPIC_0220024732"></a>

## Function<a name="en-us_topic_0125376253_section488917100152"></a>

This API is used to return a temporary redirection, that is, a URL for logging out of the CAS, when you log out of the MapReduce Service system. This API can be used only by security clusters that support Kerberos authentication.

## URI<a name="en-us_topic_0125376253_sc26ed6caea3046cdafdef64b5012cbeb"></a>

-   Format

GET /web/v1/logout\_action

-   Parameter description

**Table  1**  URI parameter description

<a name="en-us_topic_0125376253_en-us_topic_0110839917_table45563202"></a>
<table><thead align="left"><tr id="en-us_topic_0125376253_en-us_topic_0110839917_row48520594"><th class="cellrowborder" valign="top" width="25.46%" id="mcps1.2.4.1.1"><p id="en-us_topic_0125376253_en-us_topic_0110839917_p37854043"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p37854043"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p37854043"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.46%" id="mcps1.2.4.1.2"><p id="en-us_topic_0125376253_en-us_topic_0110839917_p46278677"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p46278677"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p46278677"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="49.08%" id="mcps1.2.4.1.3"><p id="en-us_topic_0125376253_en-us_topic_0110839917_p48696066"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p48696066"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p48696066"></a><strong id="en-us_topic_0125376253_b842352706134712"><a name="en-us_topic_0125376253_b842352706134712"></a><a name="en-us_topic_0125376253_b842352706134712"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376253_en-us_topic_0110839917_row52067270"><td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0125376253_en-us_topic_0110839917_p56699371"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p56699371"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p56699371"></a>is_timeout_logout</p>
</td>
<td class="cellrowborder" valign="top" width="25.46%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0125376253_en-us_topic_0110839917_p29246361"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p29246361"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p29246361"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49.08%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0125376253_en-us_topic_0110839917_p9885251"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p9885251"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p9885251"></a>Whether to exit due to page timeout. This parameter is optional. Different audit logs are recorded in the background when a user logs out manually or exits due to timeout.</p>
<p id="en-us_topic_0125376253_en-us_topic_0110839917_p21858402"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p21858402"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p21858402"></a>Possible values are as follows:</p>
<p id="en-us_topic_0125376253_en-us_topic_0110839917_p62507891"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p62507891"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p62507891"></a><strong id="en-us_topic_0125376253_b842352706203838"><a name="en-us_topic_0125376253_b842352706203838"></a><a name="en-us_topic_0125376253_b842352706203838"></a>true</strong>: Logout due to timeout</p>
<p id="en-us_topic_0125376253_en-us_topic_0110839917_p25700113"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p25700113"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p25700113"></a><strong id="en-us_topic_0125376253_b84235270620395"><a name="en-us_topic_0125376253_b84235270620395"></a><a name="en-us_topic_0125376253_b84235270620395"></a>false</strong>: Manual logout</p>
<p id="en-us_topic_0125376253_en-us_topic_0110839917_p29974428"><a name="en-us_topic_0125376253_en-us_topic_0110839917_p29974428"></a><a name="en-us_topic_0125376253_en-us_topic_0110839917_p29974428"></a>The default value is <strong id="en-us_topic_0125376253_b2038714653203942"><a name="en-us_topic_0125376253_b2038714653203942"></a><a name="en-us_topic_0125376253_b2038714653203942"></a>false</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0125376253_sdf27c4a299d04c1baff23dbbc4269c9b"></a>

-   Example:

    ```
    GET /web/v1/logout_action?is_timeout_logout=null HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```

-   Parameter description

    None


## Response<a name="en-us_topic_0125376253_saf8a9f52782a466eacc8cd2dad480b24"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    ```

-   Parameter description

    None


## Status Code<a name="en-us_topic_0125376253_section2092982712508"></a>

<a name="en-us_topic_0125376253_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376253_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376253_p398115116158"><a name="en-us_topic_0125376253_p398115116158"></a><a name="en-us_topic_0125376253_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376253_p1798121191515"><a name="en-us_topic_0125376253_p1798121191515"></a><a name="en-us_topic_0125376253_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376253_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376253_p15667142018546"><a name="en-us_topic_0125376253_p15667142018546"></a><a name="en-us_topic_0125376253_p15667142018546"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376253_p23378286542"><a name="en-us_topic_0125376253_p23378286542"></a><a name="en-us_topic_0125376253_p23378286542"></a>The operation is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).


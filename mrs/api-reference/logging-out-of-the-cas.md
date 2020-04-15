# Logging Out of the CAS<a name="EN-US_TOPIC_0220024724"></a>

## Function<a name="en-us_topic_0125376206_section1818055918252"></a>

This API is used to destruct the CAS single sign-on \(SSO\) session of a client. This API can be used only by security clusters that support Kerberos authentication.

## URI<a name="en-us_topic_0125376206_sb749681635604c26a31130a87df6959b"></a>

POST /cas/logout

## Request<a name="en-us_topic_0125376206_section430111693012"></a>

-   Example:

    ```
    POST /cas/logout HTTP/1.1
    Host: example.com
    Content-Type: application/json
    Accept:application/json
    ```


-   Parameter description

    None


## Response<a name="en-us_topic_0125376206_s7386efa7409a4a2d8e27e696aaf97f0c"></a>

-   Example:

    ```
    HTTP/1.1 200 OK
    Data:Wed,02 May 2018 10:10:01 GMT
    Server: example-server
    Content-Type: application/json
    ```

-   Parameter description

    None


## Status Code<a name="en-us_topic_0125376206_section116110412358"></a>

<a name="en-us_topic_0125376206_table2979011121511"></a>
<table><thead align="left"><tr id="en-us_topic_0125376206_row3981161161515"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.3.1.1"><p id="en-us_topic_0125376206_p398115116158"><a name="en-us_topic_0125376206_p398115116158"></a><a name="en-us_topic_0125376206_p398115116158"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="83%" id="mcps1.1.3.1.2"><p id="en-us_topic_0125376206_p1798121191515"><a name="en-us_topic_0125376206_p1798121191515"></a><a name="en-us_topic_0125376206_p1798121191515"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0125376206_row69813112155"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0125376206_p698113117157"><a name="en-us_topic_0125376206_p698113117157"></a><a name="en-us_topic_0125376206_p698113117157"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="83%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0125376206_p7981131116153"><a name="en-us_topic_0125376206_p7981131116153"></a><a name="en-us_topic_0125376206_p7981131116153"></a>The logout is successful.</p>
</td>
</tr>
</tbody>
</table>

For details about error status codes, see  [Status Codes](status-codes.md).


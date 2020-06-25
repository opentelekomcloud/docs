# Deleting a Certificate<a name="EN-US_TOPIC_0096561586"></a>

## Function<a name="en-us_topic_0085859920_section2499709175535"></a>

This API is used to delete a specific certificate.

## URI<a name="en-us_topic_0085859920_section64362641175535"></a>

DELETE /v2.0/lbaas/certificates/\{certificate\_id\}

**Table  1**  Parameter description

<a name="table76017424715"></a>
<table><thead align="left"><tr id="row1462910423715"><th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.1"><p id="p862914421178"><a name="p862914421178"></a><a name="p862914421178"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.111111111111112%" id="mcps1.2.5.1.2"><p id="p62271176316"><a name="p62271176316"></a><a name="p62271176316"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p362914421274"><a name="p362914421274"></a><a name="p362914421274"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.58585858585859%" id="mcps1.2.5.1.4"><p id="p126291424718"><a name="p126291424718"></a><a name="p126291424718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row362914421378"><td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.1 "><p id="p46298424717"><a name="p46298424717"></a><a name="p46298424717"></a>certificate_id</p>
</td>
<td class="cellrowborder" valign="top" width="11.111111111111112%" headers="mcps1.2.5.1.2 "><p id="p36291421273"><a name="p36291421273"></a><a name="p36291421273"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p126292426712"><a name="p126292426712"></a><a name="p126292426712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.5.1.4 "><p id="p1762911427714"><a name="p1762911427714"></a><a name="p1762911427714"></a>Specifies the certificate ID.</p>
</td>
</tr>
</tbody>
</table>

## Constraints<a name="en-us_topic_0085859920_section35450812175535"></a>

If the target certificate is used by a listener, the certificate cannot be deleted, and 409 code will be displayed.

## Request<a name="en-us_topic_0085859920_section124704175535"></a>

-   Request parameters

    None


## Response<a name="en-us_topic_0085859920_section14041166175535"></a>

-   Response parameters

    None


## Example<a name="section593018453355"></a>

-   Example request: Deleting a certificate

    ```
    DELETE https://{Endpoint}/v2.0/lbaas/certificates/23ef9aad4ecb463580476d324a6c71af
    ```

-   Example response

    None


## Status Code<a name="en-us_topic_0049139664_section36936567"></a>

For details, see  [HTTP Status Codes for Enhanced Load Balancers](http-status-codes-for-enhanced-load-balancers.md).


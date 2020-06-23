# Token Authentication<a name="dds_api_0010"></a>

## Application Scenarios<a name="en-us_topic_0110967262_section50237402"></a>

If you use a token for authentication, you must obtain the user's token and add  **X-Auth-Token**  to the request message header of the service API when making an API call.

This section describes how to make an API call for token authentication.

## Invoking an API<a name="en-us_topic_0110967262_section49483440"></a>

1.  <a name="en-us_topic_0110967262_li14280177102918"></a>Obtain the following information:
    1.  To obtain the IAM endpoint and region name in the message body, see  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).
    2.  To obtain the project ID, see  [Obtaining a Project ID](obtaining-a-project-id.md).

2.  <a name="en-us_topic_0110967262_li109381224173013"></a>Send a POST https://_IAM__\_Endpoint_/v3/auth/tokens request to obtain the user token.

    **Table  1**  Header description

    <a name="en-us_topic_0110967262_table18389930"></a>
    <table><thead align="left"><tr id="en-us_topic_0110967262_row24749807"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0110967262_p58577354"><a name="en-us_topic_0110967262_p58577354"></a><a name="en-us_topic_0110967262_p58577354"></a><strong id="en-us_topic_0110967262_b842352706102328"><a name="en-us_topic_0110967262_b842352706102328"></a><a name="en-us_topic_0110967262_b842352706102328"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="24.25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0110967262_p47145209"><a name="en-us_topic_0110967262_p47145209"></a><a name="en-us_topic_0110967262_p47145209"></a><strong id="en-us_topic_0110967262_b84235270611143"><a name="en-us_topic_0110967262_b84235270611143"></a><a name="en-us_topic_0110967262_b84235270611143"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.45%" id="mcps1.2.5.1.3"><p id="en-us_topic_0110967262_p60665573"><a name="en-us_topic_0110967262_p60665573"></a><a name="en-us_topic_0110967262_p60665573"></a><strong id="en-us_topic_0110967262_b842352706102346"><a name="en-us_topic_0110967262_b842352706102346"></a><a name="en-us_topic_0110967262_b842352706102346"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.5.1.4"><p id="en-us_topic_0110967262_p14964341"><a name="en-us_topic_0110967262_p14964341"></a><a name="en-us_topic_0110967262_p14964341"></a><strong id="en-us_topic_0110967262_b842352706103845"><a name="en-us_topic_0110967262_b842352706103845"></a><a name="en-us_topic_0110967262_b842352706103845"></a>Example</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0110967262_row4152081"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0110967262_p774306"><a name="en-us_topic_0110967262_p774306"></a><a name="en-us_topic_0110967262_p774306"></a>Content-Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="24.25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0110967262_p62718864"><a name="en-us_topic_0110967262_p62718864"></a><a name="en-us_topic_0110967262_p62718864"></a>Specifies the MIME type of the request body.</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.45%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0110967262_p47063234"><a name="en-us_topic_0110967262_p47063234"></a><a name="en-us_topic_0110967262_p47063234"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0110967262_p54025633"><a name="en-us_topic_0110967262_p54025633"></a><a name="en-us_topic_0110967262_p54025633"></a>application/json</p>
    </td>
    </tr>
    </tbody>
    </table>

    An example request message is as follows:

    ```
    {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "username",
                        "password": "password",
                        "domain": {
                            "name": "domainname"
                        }
                    }
                }
            },
            "scope": {
                "project": {
                   "id": "project_id"
                 }
            }
        }
    }
    ```

    In the preceding command, replace parameter in italic with the actual values. For details, see the "Obtaining the User Token" section in the  _Identity and Access Management API Reference_.

    1.  **_IAM__\_Endpoint_**: Replace it with the IAM endpoint obtained in  [1](#en-us_topic_0110967262_li14280177102918).
    2.  **_username_**  and  **_password_**: Replace them respectively with the username and password of the IAM server.
    3.  **_\{project\_id\}_**: Replace it with the project ID obtained in  [1](#en-us_topic_0110967262_li14280177102918).

    After the request is successful, the value of  **X-Subject-Token**  in the header is the token value.

    ```
    X-Subject-Token:MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...
    ```

3.  Run the following command to set the token as an environment variable for subsequent operations:

    **export Token=_\{_**_X-Subject-Token_**_\}_**

    **_X-Subject-Token_**: Replace it with the token obtained in  [2](#en-us_topic_0110967262_li109381224173013). An example command is as follows:

    **export Token=MIIDkgYJKoZIhvcNAQcCoIIDgzCCA38CAQExDTALBglghkgBZQMEAgEwgXXXXX...**



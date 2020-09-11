# Deleting a VPN Resource Tag<a name="en_topic_0093011488"></a>

## **Function**<a name="en-us_topic_0103470568_section18353123911819"></a>

This interface is used to delete a VPN resource tag.

## URI<a name="en-us_topic_0103470568_section14354143910188"></a>

DELETE /v2.0/\{project\_id\}/ipsec-site-connections/\{resource\_id\}/tags/\{key\}

>![](/images/icon-note.gif) **NOTE:**   
>In the URI,  **project\_id** indicates the project ID, **resource\_id** indicates the target resource ID, and **key**  indicates the tag key to be deleted.  

## Request Message<a name="en-us_topic_0103470568_section1936363912184"></a>

None

## Response Message<a name="en-us_topic_0103470568_section13631839191813"></a>

None

## Example<a name="en-us_topic_0103470568_section1236413941815"></a>

-   Example Request

    ```
    DELETE /v2.0/{project_id}/ipsec-site-connections/{resource_id}/tags/{key}
    ```


-   Example Response

    None


## Returned Values<a name="section14121248103610"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


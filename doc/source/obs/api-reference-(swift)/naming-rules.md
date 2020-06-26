# Naming Rules<a name="obs_03_0009"></a>

If a request contains a container name or an object name, OBS \(compatible with OpenStack Swift\) starts to process the request only after checking that the name conforms to the specified naming rules.

## Account Naming Rules<a name="section41516642152937"></a>

-   Globally unique.
-   A string of 1 to 256 characters.

>![](/images/icon-note.gif) **NOTE:**   
>OBS \(compatible with OpenStack Swift\) uses the IDs of tenants created in the IAM system as account names.  

## Container Naming Rules<a name="section54815683"></a>

-   A string of 1 to 256 characters.
-   Can contain only case-sensitive letters, digits, periods \(.\), underscores \(\_\), and hyphens \(-\).
-   Uses the UTF-8 encoding format.

>![](/images/icon-note.gif) **NOTE:**   
>To ensure system security, in a container name, the types of characters that are prohibited by OBS \(compatible with OpenStack Swift\) are more than those prohibited by OpenStack Swift.  

## Object Naming Rules<a name="section23579102"></a>

-   A string of 1 to 1024 characters.
-   Can start with any character.
-   Uses the UTF-8 encoding format.
-   Cannot contain spaces, question marks \(?\), and double quotation marks \("\).
-   An object is named after an object key. Each object in a container must have a unique object key.

## Rules About Custom Metadata<a name="section29391483104815"></a>

-   The following rules apply to custom metadata of accounts, containers, and objects:
-   The value length of a custom metadata item cannot exceed 256 bytes.
-   The name of a custom metadata item cannot exceed 128 bytes.
-   The total length \(name and value\) of all custom metadata items cannot exceed 4096 bytes.
-   The number of custom metadata items cannot exceed 90.
-   The name of a custom metadata item can contain only letters, digits, and ASCII characters.
-   The value of a custom metadata item can be a UTF-8 character string.
-   The tab and space keys after the name of a custom metadata item are deleted by default.

>![](/images/icon-note.gif) **NOTE:**   
>In OpenStack Swift, the tab and space keys before and after the name of a custom metadata item are retained.  


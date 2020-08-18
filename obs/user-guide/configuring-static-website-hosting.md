# Configuring Static Website Hosting<a name="en-us_topic_0045853755"></a>

This section describes how to configure static website hosting for buckets and use bucket domain names to access static websites.

## Prerequisites<a name="section11221613153921"></a>

Web page files of the static website have been uploaded to a bucket.

If the web page files are in the Cold storage class, restore them first. For more information, see  [Restoring a Cold File Stored in OBS](restoring-a-cold-file-stored-in-obs.md).

>![](public_sys-resources/icon-notice.gif) **NOTICE:** 
>If the hosted static website needs to be accessed by anyone, authorize anonymous users the permission to access static website files in the bucket. The configuration of static website hosting takes effect within two minutes after the configuration.

## Procedure<a name="section11587693153957"></a>

1.  In the bucket list, click the bucket to be operated. The  **Overview**  page of the bucket is displayed.
2.  **Optional**: To ensure that a hosted static website can be accessed by all users, configure the object ACL or bucket policy as follows, so that all static website files in the bucket can be accessed publicly.

    Authorize anonymous users the permission to read files on the static website. For details, see  [Authorizing Access Permissions to Anonymous Users](authorizing-access-permissions-to-anonymous-users.md).

    If the bucket contains only static website files, configure the  **Public Read**  policy for the bucket so that all files in the bucket can be accessed publicly.

    1.  Choose  **Permissions**  \>  **Bucket Policies**.
    2.  In the  **Standard Bucket Policies**  area, select the  **Public Read**  policy for the bucket.
    3.  Click  **Public Read**. For details, see  [Figure 1](#fig15186794193556). In the confirmation dialog box that is displayed, click  **Yes**.

        **Figure  1**  Configuring the public read permission<a name="fig15186794193556"></a>  
        ![](figures/configuring-the-public-read-permission.png "configuring-the-public-read-permission")

3.  In the  **Basic Configurations**  area, click the  **Static Website Hosting**  label. The  **Static Website Hosting**  page is displayed.

    Alternatively, you can choose  **Basic Configurations**  \>  **Static Website Hosting**  from the navigation pane on the left.

4.  Click  **Configure Static Website Hosting**. The  **Configure Static Website Hosting**  dialog box is displayed.
5.  Enable it by turning on the status switch.
6.  Set  **Hosting By**  to  **Current bucket**. For details, see  [Figure 2](#fig1131112528711).

    **Figure  2**  Configuring static website hosting<a name="fig1131112528711"></a>  
    ![](figures/configuring-static-website-hosting.png "configuring-static-website-hosting")

7.  Set the values of  **Home Page**  and  **404 Error Page**.

    -   **Home Page**: specifies the default homepage of the static website. When OBS Console is used to configure static website hosting, only HTML web pages are supported. When SDKs are used to configure static website hosting, OBS does not have such a restriction but the  **Content-Type**  of objects must be specified.

        OBS only allows files such as  **index.html**  in the root directory of a bucket to function as the default homepage. That is to say, do not set the default homepage with a multi-level directory structure \(for example,  **/page/index.html**\).

    -   **404 Error Page**: specifies the error page returned when an error occurs during static website access. When OBS Console is used to configure static website hosting, only HTML, JPG, PNG, BMP, and WEBP files under the root directory are supported. When APIs or SDKs are used to configure static website hosting, OBS does not have such a restriction but the  **Content-Type**  of objects must be specified.

8.  **Optional**: In  **Redirection Rules**, configure redirection rules. Requests that comply with the redirection rules are redirected to the specific host or page.

    A redirection rule is compiled in the JSON or XML format. Each rule contains a  **Condition**  and a  **Redirect**. The parameters are described as follows:

    **Table  1**  Parameter description

    <a name="table59166151447"></a>
    <table><thead align="left"><tr id="row2916201574415"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p1091631511441"><a name="p1091631511441"></a><a name="p1091631511441"></a>Container</p>
    </th>
    <th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p6916111514447"><a name="p6916111514447"></a><a name="p6916111514447"></a>Key</p>
    </th>
    <th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.2.4.1.3"><p id="p3916111594412"><a name="p3916111594412"></a><a name="p3916111594412"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49161115194414"><td class="cellrowborder" rowspan="2" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p791616152446"><a name="p791616152446"></a><a name="p791616152446"></a>Condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p16916101534416"><a name="p16916101534416"></a><a name="p16916101534416"></a>KeyPrefixEquals</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p591681519441"><a name="p591681519441"></a><a name="p591681519441"></a>Object name prefix on which the redirection rule takes effect. When a request is sent for accessing an object, the redirection rule takes effect if the object name prefix matches the value specified for this parameter.</p>
    <p id="p58120199"><a name="p58120199"></a><a name="p58120199"></a>For example, to redirect the request for object <strong id="b4757156775"><a name="b4757156775"></a><a name="b4757156775"></a>ExamplePage.html</strong>, set the <strong id="b6131444151815"><a name="b6131444151815"></a><a name="b6131444151815"></a>KeyPrefixEquals</strong> to <strong id="b6763656177"><a name="b6763656177"></a><a name="b6763656177"></a>ExamplePage.html</strong>.</p>
    </td>
    </tr>
    <tr id="row189161115104413"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1791601516448"><a name="p1791601516448"></a><a name="p1791601516448"></a>HttpErrorCodeReturnedEquals</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11916171512441"><a name="p11916171512441"></a><a name="p11916171512441"></a>HTTP error codes upon which the redirection rule takes effect. The specified redirection is applied only when the error code returned equals the value specified for this parameter.</p>
    <p id="p40599109"><a name="p40599109"></a><a name="p40599109"></a>For example, if you want to redirect requests to <strong id="b9362122010"><a name="b9362122010"></a><a name="b9362122010"></a>NotFound.html</strong> when HTTP error code 404 is returned, set <strong id="b4424194512012"><a name="b4424194512012"></a><a name="b4424194512012"></a>HttpErrorCodeReturnedEquals</strong> to <strong id="b64812507207"><a name="b64812507207"></a><a name="b64812507207"></a>404</strong> in <strong id="b881723201"><a name="b881723201"></a><a name="b881723201"></a>Condition</strong>, and set <strong id="b168152162017"><a name="b168152162017"></a><a name="b168152162017"></a>ReplaceKeyWith</strong> to <strong id="b0810262017"><a name="b0810262017"></a><a name="b0810262017"></a>NotFound.html</strong> in <strong id="b198182132012"><a name="b198182132012"></a><a name="b198182132012"></a>Redirect</strong>.</p>
    </td>
    </tr>
    <tr id="row12916115134418"><td class="cellrowborder" rowspan="5" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p791671511442"><a name="p791671511442"></a><a name="p791671511442"></a>Redirect</p>
    </td>
    <td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p891613152448"><a name="p891613152448"></a><a name="p891613152448"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p3320144784713"><a name="p3320144784713"></a><a name="p3320144784713"></a>Protocol used for redirection The value can be <strong id="b12336184372115"><a name="b12336184372115"></a><a name="b12336184372115"></a>HTTP</strong> or <strong id="b15760124532113"><a name="b15760124532113"></a><a name="b15760124532113"></a>HTTPS</strong>. If this parameter is not specified, the default value <strong id="b125449352210"><a name="b125449352210"></a><a name="b125449352210"></a>HTTP</strong> is used.</p>
    </td>
    </tr>
    <tr id="row1091651554417"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1491691513447"><a name="p1491691513447"></a><a name="p1491691513447"></a>HostName</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p1691619151449"><a name="p1691619151449"></a><a name="p1691619151449"></a>Host name to which the redirection is pointed. If this parameter is not specified, the request is redirected to the host from which the original request is initiated.</p>
    </td>
    </tr>
    <tr id="row149161015184410"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p109167156447"><a name="p109167156447"></a><a name="p109167156447"></a>ReplaceKeyPrefixWith</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p119161715134413"><a name="p119161715134413"></a><a name="p119161715134413"></a>Object name prefix on which the redirection rule takes effect</p>
    </td>
    </tr>
    <tr id="row15916111519446"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1391611518441"><a name="p1391611518441"></a><a name="p1391611518441"></a>ReplaceKeyWith</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p891661574418"><a name="p891661574418"></a><a name="p891661574418"></a>Object name on which the redirection rule takes effect</p>
    </td>
    </tr>
    <tr id="row191651510442"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p391619155443"><a name="p391619155443"></a><a name="p391619155443"></a>HttpRedirectCode</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p2916131554417"><a name="p2916131554417"></a><a name="p2916131554417"></a>HTTP status code returned to the redirection request. The default value is <strong id="b495710404329"><a name="b495710404329"></a><a name="b495710404329"></a>301</strong>, indicating that requests are permanently redirected to the location specified by <strong id="b1032182516334"><a name="b1032182516334"></a><a name="b1032182516334"></a>Redirect</strong>. You can also set this parameter based on your service needs.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Example of setting a redirection rule**

    -   Example 1: All requests for objects prefixed with  **folder1/**  are automatically redirected to pages prefixed with  **target.html**  on host  **www.example.com**  using HTTPS.

        ```
        [
        	{
        	"Condition": {
        		"KeyPrefixEquals": "folder1/"
        		},
        	"Redirect":{
        		"Protocol": "HTTPS",
        		"HostName": "www.example.com",
        		"ReplaceKeyPrefixWith": "target.html"
        		}
        	}
        ]
        ```

    -   Example 2: All requests for objects prefixed with  **folder2/**  are automatically redirected to objects prefixed with  **folder/**  in the same bucket.

        ```
        [
        	{
        	"Condition": {
        		"KeyPrefixEquals": "folder2/"
        		},
        	"Redirect":{
        		"ReplaceKeyPrefixWith": "folder/"
        		}
        	}
        ]
        ```

    -   Example 3: All requests for objects prefixed with  **folder.html**  are automatically redirected to the  **folderdeleted.html**  object in the same bucket.

        ```
        [
        	"Condition": {
        		"KeyPrefixEquals": "folder.html"
        		},
        	"Redirect":{
        		"ReplaceKeyWith": "folderdeleted.html"
        		}
        	}
        ]
        ```

    -   Example 4: If the HTTP status code 404 is returned, the request is automatically redirected to the page prefixed with  **report-404/**  on host  **www.example.com**.

        For example, if you request the page  **ExamplePage.html**  but the HTTP 404 error is returned, the request will be redirected to the  **report-404/ExamplePage.html**  page on the  **www.example.com**. If the 404 redirection rule is not specified, the default 404 error page configured in the previous step is returned when the HTTP 404 error occurs.

        ```
        [
        	"Condition": {
        		"HttpErrorCodeReturnedEquals": "404"
        		},
        	"Redirect":{
        		"HostName": "www.example.com",
        		"ReplaceKeyPrefixWith": "report-404/"
        		}
        	}
        ]
        ```

9.  Click  **OK**.

    After the static website hosting is effective in OBS, you can access the static website by using the URL provided by OBS.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >In some conditions, you may need to clear the browser cache before the expected results are displayed.



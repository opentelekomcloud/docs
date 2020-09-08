# API Usage Guidelines<a name="cce_02_0344"></a>

Public cloud APIs comply with the RESTful API design principles. REST-based web services are organized into resources. Each resource is identified by one or more Uniform Resource Identifiers \(URIs\). An application accesses a resource based on the resource's Unified Resource Locator \(URL\). A URL is usually in the following format:  _https://Endpoint/uri_. In the URL,  _uri_  indicates the resource path, that is, the API access path.

Public cloud APIs use HTTPS as the transmission protocol. Requests/Responses are transmitted by using JSON messages, with media type represented by  **Application/json**.

-   The URL of APIs described in  [APIs](apis)  is in the format of  [https://Endpoint/uri](https://endpoint/uri). In the URL, uri indicates the resource path, that is, the API access path.
-   The URL of Kubernetes-native APIs described in  [Kubernetes APIs](kubernetes_apis)  is in the format of  **https://\{clusterid\}.Endpoint/uri**. In the URL, \{clusterid\} indicates a cluster ID, and uri indicates the resource path, that is, the API access path.
-   The URL of Kubernetes-native APIs is in the format of  **https://\{publicip\}:5443/uri**. In the URL,  **\{publicip\}**  indicates EIP of the cluster, and  **uri**  indicates the resource path, that is, the API access path following X-Auth-Token as a header or X-Remote-User as a header.

    Before using X-Remote-User as a header, obtain the required certificate in advance. Two types of certificates are supported:

    -   Self-owned certificate uploaded during cluster creation. For details, see  [Creating a VM Cluster](https://docs.otc.t-systems.com/en-us/usermanual2/cce/cce_01_0028.html).

        ![](figures/creating-a-vm-cluster.png)

    -   Cluster certificate generated and downloaded after cluster creation. For details, see  [Obtaining a Cluster Certificate](https://docs.otc.t-systems.com/en-us/usermanual2/cce/cce_01_0175.html).

        ![](figures/obtaining-a-cluster-certificate.png)



For details about how to use APIs, see  [API Usage Guidelines](https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328001.html?tag=API%20Documents).

>![](/images/icon-note.gif) **NOTE:**   
>CCE provides two methods to authenticate requests for calling an API: token and AK/SK. Select an authentication method based on actual requirements. If token-based authentication is used, you can call service APIs by using either of the following methods after obtaining a token:  
>-   Method 1: Add  **X-Auth-Token**  to the request header and set  **X-Auth-Token**  with the obtained IAM token.  
>-   Method 2: Add  **Authorization**  to the request header. The value of  **Authorization**  is  **Bearer $\{token\}**, and the value of  **$\{token\}**  is token obtained from IAM or from Kubernetes service account.  
>-   Method 3: Add  **X-Remote-User**  to the request header and specify user \***X-Remote-User: user**\*.  
>Method 3 requires that the CA root certificate must has been uploaded before you create a cluster on the CCE console. For details, see  [Cluster Management Permission Control](https://docs.otc.t-systems.com/en-us/usermanual2/cce/cce_01_0085.html).  


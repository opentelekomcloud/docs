# Obtaining a Project ID<a name="cce_02_0341"></a>

## Obtaining the Project ID by Calling an API<a name="section1691341861315"></a>

You can obtain the project ID by calling the API  [used to query project information based on the specified criteria](https://docs.otc.t-systems.com/en-us/api/iam/en-us_topic_0057845625.html).

The API used to obtain a project ID is  **GET https://**_\{Endpoint\}_**/v3/projects**, where  _\{Endpoint\}_  indicates the IAM endpoint. You can obtain the IAM endpoint from  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

The following is an example response. The value of  **id**  in the  **projects**  field is the project ID.

```
{
    "projects": [
        {
            "domain_id": "65382450e8f64ac0870cd180d14e684b",
            "is_domain": false,
            "parent_id": "65382450e8f64ac0870cd180d14e684b",
            "name": "eu-de",
            "description": "",
            "links": {
                "next": null,
                "previous": null,
                "self": "https://www.example.com/v3/projects/a4a5d4098fb4474fa22cd05f897d6b99"
            },
            "id": "a4a5d4098fb4474fa22cd05f897d6b99",
            "enabled": true
        }
    ],
    "links": {
        "next": null,
        "previous": null,
        "self": "https://www.example.com/v3/projects"
    }
}
```

## Obtaining a Project ID on the Console<a name="section59621329127"></a>

A project ID needs to be specified in the URLs of some APIs. Therefore, you need to obtain a project ID before calling such APIs. To obtain a project ID, perform the following operations:

1.  Sign up and log in to the management console.
2.  Click the username and select  **Basic Information**  from the drop-down list.
3.  On the  **Account Info**  page, click  **Manage**.

    On the  **My Credentials**  page, view project IDs in the project list.

    **Figure  1**  Viewing project IDs<a name="fig555610358190"></a>  
    ![](figures/viewing-project-ids.png "viewing-project-ids")



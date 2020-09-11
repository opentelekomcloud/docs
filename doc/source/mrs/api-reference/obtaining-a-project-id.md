# Obtaining a Project ID<a name="EN-US_TOPIC_0172602531"></a>

## Obtaining a Project ID from the Management Console<a name="section964292414404"></a>

A project ID \(**project\_id**\) is required for some URLs when an API is called. To obtain a project ID, perform the following operations:

1.  Log in to the management console.
2.  Click the username and choose  **My Credentials**  from the drop-down list.

    On the  **My Credentials**  page, view project IDs in the project list.


If there are multiple projects in one region, expand  **Region**  and view subproject IDs in the  **Project ID**  column.

## Obtaining a Project ID by Calling an API<a name="section199243176407"></a>

You can obtain the project ID by calling the IAM API used to query project information based on the specified criteria.

The API used to obtain a project ID is  **GET** **https://\{Endpoint\}/v3/projects**.  **\{Endpoint\}**  is the IAM endpoint and can be obtained from  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html). For details about API authentication, see  [Authentication](authentication.md).

The following is an example response. The value of  **id**  under  **projects**  is the project ID.

```
{
    "projects": [
        {
            "domain_id": "65382450e8f64ac0870cd180d14e684b",
            "is_domain": false,
            "parent_id": "65382450e8f64ac0870cd180d14e684b",
            "name": "cn-north-4",
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


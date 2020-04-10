# Identity Conversion Rule for Federated Users<a name="en-us_topic_0079620340"></a>

The identity conversion rule for federated users is displayed in a JSON file. You can modify it by modifying the JSON file. The JSON format is as follows:

```
[ 
        { 
            "remote": [ 
                { 
                   "<condition>" 
                } 
             ],
            "local": [ 
                { 
                  "<user> or <group> or <groups>" 
                } 
             ]             
          } 
       ]     
```

-   **remote**: indicates the information about a federated user in the IdP. This expression is a combination of assertion attributes and operators. The value of  **remote**  is determined based on the assertion.
-   **condition**: indicates the identity conversion rule that maps federated users to the cloud system. The following three conditions are supported:
    -   **empty**: unlimited. The condition is always valid and the returned value is the input attribute value. This value is used to replace the placeholder in the  **local**  block.
    -   **any\_one\_of**: The condition is valid only if the input attributes include any specified value, and a Boolean value is returned. The returned value cannot be used to replace the placeholder in the  **local**  block.
    -   **not\_any\_of**: The condition is valid only if the input attributes do not include any specified value, and a Boolean value is returned. The returned value cannot be used to replace the placeholder in the  **local**  block.

-   **local**: indicates the information about a federated user in the cloud system. This value can be a placeholder \{0..n\}. \{0\} indicates the first attribute of the user information in  **remote**. \{1\} indicates the second attribute of the user information in  **remote**.

## Examples of Identity Conversion Rule Conditions<a name="section14913494275"></a>

The following examples illustrate how to use the conditions \(**empty**,  **any\_one\_of**, and  **not\_any\_of**\) in an identity conversion rule.

-   The  **empty**  condition indicates that a character string value can be returned. This value is used to replace the placeholder \{0..n\} in the  **local**  block. The example is as follows:

    ```
    [ 
            { 
                "local": [ 
                    { 
                        "user": { 
                            "name": "{0} {1}" 
                        } 
                    }, 
                    { 
                        "group": { 
                            "name": "{2}" 
                        } 
                    } 
                ], 
                "remote": [ 
                    { 
                        "type": "FirstName" 
                    }, 
                    { 
                        "type": "LastName" 
                    }, 
                    { 
                        "type": "Group" 
                    } 
                ] 
            } 
        ]     
    ```

    The username of the federated user in the cloud system is "first attribute value of  **remote**+space+second attribute value of  **remote**", or  **FirstName LastName**. The belonged user group is the third attribute value of  **remote**, that is  **Group**. The  **Group**  attribute can have only one value.

    Assume that the cloud system receives the following assertion \(this example uses a simplified assertion structure\). The username of the federated user in the cloud system is John Smith. John Smith in the cloud system is attached to the  **admin**  user group.

    ```
    {FirstName: John} 
    {LastName: Smith} 
    {Groups: admin}
    ```

    If a federated user needs to belong to multiple user groups in the cloud system, the identity conversion rules are as follows:

    ```
    [  
            {  
                "local": [  
                    {  
                        "user": {  
                            "name": "{0} {1}"  
                        }  
                    },  
                    {  
                        "groups":  "{2}"  
                    }  
                ],  
                "remote": [  
                    {  
                        "type": "FirstName"  
                    },  
                    {  
                        "type": "LastName"  
                    },  
                    {  
                        "type": "Groups"  
                    }  
                ]  
            }  
        ]  
    ```

    The username of the federated user in the cloud system is "first attribute value of  **remote**+space+second attribute value of  **remote**", or  **FirstName LastName**. The user group of the federated user is the third attribute value of  **remote**, that is  **Groups**.

    Assume that the cloud system receives the following assertion, the username of the federated user in the cloud system is John Smith. John Smith belongs to the  **admin**  and  **manager**  user groups.

    ```
    {FirstName: John}  
    {LastName: Smith}  
    {Groups: [admin, manager]}
    ```

-   Unlike the  **empty**  condition, the returned values of the  **any one of**  and  **not any of**  conditions are Boolean values. These values cannot be used to replace the placeholder in the  **local**  block. In the following example, only the placeholder \{0\} exists and is replaced by the returned value of  **empty**  in the  **remote**  block. The value of  **group**  must be  **admin**.

    ```
    [ 
            { 
                "local": [ 
                    { 
                        "user": { 
                            "name": "{0}" 
                        } 
                    }, 
                    { 
                        "group": { 
                            "name": "admin" 
                        } 
                    } 
                ], 
                "remote": [ 
                    { 
                    "type": "UserName" 
                    }, 
                    { 
                        "type": "Groups", 
                        "any_one_of": [ 
                            "idp_admin" 
                        ] 
                    } 
                ] 
            } 
        ]     
    ```

    The username of the federated user in the cloud system is the first attribute value of  **remote**, that is  **UserName**. The user group of the federated user is  **admin**. This rule takes effect only for the users in the  **idp\_admin**  user group in the IdP.

    If a federated user needs to belong to multiple user groups in the cloud system, the identity conversion rules are as follows:

    ```
    [  
            {  
                "local": [  
                    {  
                        "user": {  
                            "name": "{0}"  
                        }  
                    },  
                    {  
                        "groups": "[\"admin\",\"manager\"]"  
                    }  
                ],  
                "remote": [  
                    {  
                    "type": "UserName"  
                    },  
                    {  
                        "type": "Groups",  
                        "any_one_of": [  
                            "idp_admin"  
                        ]  
                    }  
                ]  
            }  
        ]     
    ```

    The username of the federated user in the cloud system is the first attribute value of  **remote**, that is  **UserName**. The user groups of the federated user are  **admin**  and  **manager**. This rule takes effect only for the users in the  **idp\_admin**  user group in the IdP.

    -   Assume that the cloud system receives the following assertion. John Smith belongs to the  **idp\_admin**  user group and can therefore access the cloud system.

        ```
        {UserName: John Smith} 
        {Groups: [idp_user, idp_admin, idp_agency]}
        ```

    -   Assume that the cloud system receives the following assertion. John Smith does not belong to the  **idp\_admin**  user group, so this rule does not take effect for John Smith, and John Smith cannot access the cloud system.

        ```
        {UserName: John Smith} 
        {Groups: [idp_user, idp_agency]}
        ```


-   Condition including a regular expression: You can specify  **"regex": true**  in conditions to indicate that the system is calculating the result using a regular expression. 

    ```
    [ 
            { 
                "local": [ 
                    { 
                        "user": { 
                            "name": "{0}" 
                        } 
                    }, 
                    { 
                        "group": { 
                            "name": "admin" 
                        } 
                    } 
                ], 
                "remote": [ 
                    { 
                    "type": "UserName" 
                    }, 
                    { 
                        "type": "Groups", 
                        "any_one_of": [ 
                            ".*@mail.com$" 
                        ], 
                        "regex": true 
                    } 
                ] 
            } 
        ]     
    ```

    This rule takes effect for any user whose username starts with any value and ends with @mail.com. The username in the cloud system is  **UserName**, and the user group is  **admin**.

-   Condition combination: Multiple conditions are combined using the logical AND.

    ```
    [ 
            { 
                "local": [ 
                    { 
                        "user": { 
                            "name": "{0}" 
                        } 
                    }, 
                    { 
                        "group": { 
                            "name": "admin" 
                        } 
                    } 
                ], 
                "remote": [ 
                    { 
                    "type": "UserName" 
                    }, 
                    { 
                        "type": "Groups", 
                        "not_any_of": [ 
                            "idp_user" 
                        ] 
                    }, 
                    { 
                        "type": "Groups", 
                        "not_any_of": [ 
                            "idp_agent" 
                        ] 
                    } 
                ] 
            } 
        ]     
    ```

    This rule takes effect only for the federated users who do not belong to the  **idp\_user**  or  **idp\_agent**  user group in the IdP. The username of those users in the cloud system is  **UserName**, and their user group is  **admin**. The preceding rule is equivalent to the following:

    ```
    [ 
            { 
                "local": [ 
                    { 
                        "user": { 
                            "name": "{0}" 
                        } 
                    }, 
                    { 
                        "group": { 
                            "name": "admin" 
                        } 
                    } 
                ], 
                "remote": [ 
                    { 
                    "type": "UserName" 
                    }, 
                    { 
                        "type": "Groups", 
                        "not_any_of": [ 
                            "idp_user", 
                            "idp_agent" 
                        ] 
                    } 
                ] 
            } 
        ]     
    ```

-   Multiple rules

    If multiple rules are combined, the methods for generating usernames and user groups are different.

    The username in the first valid rule is used as  **UserName**. At least one user name rule among all of the rules must take effect, or the user will not be allowed to log in. The collection of the user group names in all valid rules is used as  **Groups**.

    Separating the configuration of usernames and user groups using multi-rule configuration makes it easier to read.

    ```
    [ 
        { 
            "local": [ 
                { 
                    "user": { 
                        "name": "{0}" 
                    } 
                } 
            ], 
            "remote": [ 
                { 
                    "type": "UserName" 
                } 
            ] 
        }, 
        { 
            "local": [ 
                { 
                    "group": { 
                        "name": "admin" 
                    } 
                } 
            ], 
            "remote": [ 
                { 
                    "type": "Groups", 
                    "any_one_of": [ 
                        "idp_admin" 
                    ] 
                } 
            ] 
        }
    ]
    ```

    This rule combination takes effect for the users in the  **idp\_admin**  user group. The username in the cloud system is  **UserName**, and the user group is  **admin**.

    Assume that the cloud system receives the following assertion. John Smith belongs to the  **idp\_admin**  user group, so this rule takes effect for John Smith. The username of the federated user in the cloud system is  **John Smith**, and its user group is  **admin**.

    ```
    {UserName: John Smith} 
    {Groups: [idp_user, idp_admin, idp_agency]}
    ```



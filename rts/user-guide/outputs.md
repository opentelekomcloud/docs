# Outputs<a name="EN-US_TOPIC_0076468587"></a>

Outputs are specified in the  **outputs**  field. This field is used to display the output of created resources. This field is optional. For example, the following code segment defines the IP address of an ECS instance. You can view the IP address from the response of a stack querying request.

```
outputs:
  instance_ip:
    description: The IP address of the deployed instance
    value: { get_attr: [my_instance, first_address] }
```

## Syntax<a name="section1573744018549"></a>

**outputs**  consists of three parts: output item, description, and value. If multiple output items are declared, use commas \(,\) to separate them. The following is an example code segment.

```
outputs:  
  ECSName:  
    description: The Name of the ECS instance newly created. 
    value: { get_attr: [server, name] }
  floating_ip:  
    description: The floating ip address of the server.  
    value: { get_attr: [floating_ip, floating_ip_address] }
```

In this command,

-   **ECSName**  and  **floating\_ip**  are both output items, which are unique in the template.
-   **description**: describes the meaning of  **ECSName**. This field is optional.
-   **value**: indicates the attribute value returned when the stack querying API is invoked, or the output value viewed on the management console. The  **value**  value can be obtained using internal functions, such as  **get\_attr**  in this example.


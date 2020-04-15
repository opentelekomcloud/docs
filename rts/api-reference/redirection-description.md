# Redirection Description<a name="EN-US_TOPIC_0084581281"></a>

## Redirect<a name="section152735214014"></a>

In the Heat API, the stack ID consists of  **stack\_name**  and  **stack\_id**. When the system calls APIs to access resources such as stacks, templates, events, and actions, if only  **stack\_name**  is specified, Heat queries the  **stack\_id**  value and returns a redirect response pointing to the correct URL. The following provides a request example:

```
GET /v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack
```

After redirection, the actual request is as follows:

```
Location: http://x.x.x.x:8004/v1/95d02433133a4c0a87ba6967474a2ad3/stacks/HeatStack/c89c4bb3-96cb-4a55-aafa-076a7939a306
```

## Redirect APIs<a name="section74276034111"></a>

The APIs used in the following topics support redirection. When calling the following APIs to access stacks or templates, you can specify only  **stack\_name**  or  **stack\_id**.

-   [Querying Details of a Stack](querying-details-of-a-stack.md)
-   [Querying Resources of a Stack](querying-resources-of-a-stack.md)
-   [Querying Events of a Stack](querying-events-of-a-stack.md)
-   [Querying a Stack Template](querying-a-stack-template.md)


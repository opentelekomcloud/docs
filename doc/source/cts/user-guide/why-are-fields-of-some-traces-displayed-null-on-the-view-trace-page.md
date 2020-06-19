# Why Are Fields of Some Traces Displayed Null on the View Trace Page?<a name="cts_faq_010"></a>

Fields  **resource\_IP**,  **code**,  **request**,  **response**, and  **message**  can be null. These fields are not mandatory for CTS.

-   **resource\_IP**: If the value of  **trace\_type**  is  **SystemAction**, the operation is triggered by the system. It is normal that the  **resource\_IP**  field is empty.
-   **request**,  **response**, and  **code**: These three fields indicate the request content, request result, and HTTP return code of an operation. In some cases, these fields are empty or have no service meaning. Therefore, they are left blank based on actual situations.
-   **message**: This is a reserved field. Additional information of other cloud services will be added in this field when necessary. It is normal that it is left blank.


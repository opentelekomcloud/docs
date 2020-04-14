# Constraints<a name="EN-US_TOPIC_0101431766"></a>

## Limitations<a name="section52552112318"></a>

-   RTS does not support snapshot-related APIs and the following operations: suspend, restore, discard, and adopt.
-   The Availability Zone \(AZ\) attribute cannot be updated in a stack life cycle.
-   Names of resources must be unique in the same nesting level.

## Specification Limitations<a name="section147011612163118"></a>

-   Each tenant can create a maximum of 100 stacks.
-   A maximum of 1000 resources can be created in a stack.
-   Each stack contains a maximum of 1000 operation logs.
-   A maximum of seven stacks can be nested together.
-   The maximum size of a decompressed template file is 512 KB.


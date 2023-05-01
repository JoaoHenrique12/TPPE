# Equivalence Partitioning

Involves dividing the input domain of a system or component into a set of equivalence
classes, where each class represents a distinct behavior of the system.
The goal of equivalence partitioning is to reduce the number of test cases needed
to cover all possible input scenarios while still ensuring that all relevant scenarios
are tested.

The basic idea behind equivalence partitioning is to group inputs into categories or 
partitions that are expected to behave in a similar way. Test cases can then be 
selected from each partition to represent the behavior of that partition.

## Example

Function validate\_password that takes a password string as input and returns True if the
password meets certain criteria and False otherwise. The criteria are:

- The password must be at least 8 characters long.
- The password must contain at least one uppercase letter and one lowercase letter.
- The password must contain at least one digit.

To apply equivalence partitioning to this function, we can divide the input domain of possible
passwords into three partitions:

- Valid passwords that meet all three criteria.
- Invalid passwords that fail only one criterion.
- Invalid passwords that fail multiple criteria.


We can then select a representative test case from each partition:

- A valid password that meets all three criteria, such as "Abc12345".
- An invalid password that fails only one criterion, such as "Abcdefgh".
- An invalid password that fails multiple criteria, such as "abc123".

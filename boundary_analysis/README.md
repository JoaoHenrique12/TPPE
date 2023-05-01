# Boundary Analysis

Boundary analysis is a software testing technique that focuses on testing the
boundaries or limits of input values to a software component or system. The purpose
of boundary analysis testing is to ensure that the software behaves correctly and 
produces the expected results when the input values are at the boundary or limit of
what the software can handle.

This technique typically involves the following steps:

- Identify the input values that define the boundaries of the software component or system. For example, if the component accepts integers as input, then the boundaries would be the minimum and maximum values that the component can accept.

- Define test cases that use input values that are at the boundaries of the software component or system. For example, if the software component can accept integers between 1 and 100, then the test cases would use the values 1, 100, and possibly other values close to the boundaries, such as 2 and 99.

- Execute the test cases and verify that the software behaves correctly and produces the expected results. For example, if the software component calculates the square root of an input value, then the test cases would verify that the component correctly handles the edge cases, such as calculating the square root of 1 and 100.

## Example

### CD Project Red

![Image Geralt Ther Rivia](https://dropsdejogos.uai.com.br/wp-content/uploads/sites/10/2020/05/the-witcher-950x534.jpg)

You are working as a developer for CD Projekt Red, the company behind the popular RPG
game, The Witcher 1. You have been tasked with testing two functions that are used to
reduce and sum a character's health in the game. The functions are called 
reduce\_health(character) and sum\_health(character), and they take the current 
character's health as input.

Your task is to use boundary analysis testing to write test cases for these functions,
to ensure that they behave correctly and predictably even in edge cases.

Here are the specifications for the functions:

#### reduce\_health(character)

This function is called whenever the character takes damage in the game. It takes the current character's health as input, and returns the new character's health after the damage is applied.

- The function should return 0 if the character's health drops to or below 0.
- The function should subtract the damage amount from the character's health if the damage does not exceed the character's current health value.

#### sum\_health(character)

This function is called whenever the character is healed in the game. It takes the current character's health and the amount of the healing as input,
and returns the new character's health after the healing is applied.

- The function should return the maximum health value (1000) if the healing would cause the character's health to exceed the maximum health value.
- The function should add the healing amount to the character's health if the healing does not exceed the maximum health value.

Your task is to write test cases for these functions that cover the boundary values 
and limits of the input values. Consider the following factors when defining your 
test cases:

- The minimum and maximum values for the character's health and damage/healing amounts.
- The behavior of the functions when the input values are at or near these boundaries or limits.
- Any other edge cases or corner cases that might be relevant.

Once you have written your test cases, you should run them using a testing framework like Pytest, and ensure that the functions behave correctly and predictably for all input values.

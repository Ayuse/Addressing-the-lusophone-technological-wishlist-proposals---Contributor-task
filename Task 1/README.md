## Addressing the Lusophone technological wishlist proposals - Task 1

### Objective of the task:
  Create a JavaScript script to manipulate a json object and print it in a human legible format.

### My approach:
  - get the _results_ element in which the data will be displayed
  - create a function `formatDate()` to transform the date into the required format by parsing the date parts manually to avoid timezone off-by-one errors e.g. September 13, 2021
  - loop over the provided input data, create and add each element of the data in a paragraph using safe DOM methods (`createElement` and `textContent`) to avoid XSS risks
  - append each of the paragraphs to the _results_ element

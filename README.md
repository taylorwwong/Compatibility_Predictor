# Compatibility_Predictor
<hr></hr>

## Handling input
The json file provided is formatted exactly the same as the sample data provided with the coding challenge. To access the data, the application calls upon the json python library. Here I use 3 separate lists (team, applicant names and applicant totals) to keep track of values pulled from the input file.

## Finding compatibility
To calculate the compatibility of the applicants, I take the mean value of the current team members' attributes. Specifically, intelligence and the feelings towards spicy food. Then I compare the applicant's values of intelligence and spicy food against the team's mean value. Here, we only care about the absolute value of the difference to measure the distance between the two values.

## Writing to output
Writing to output is done with f strings using the applicants' names and resulting score which were stored in lists. To write to the output file, we use the command json.dump() to format the output data into json.

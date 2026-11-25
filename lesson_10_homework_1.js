// ###### Exercise ########

// adding up numbers and caclulate average (like in Python exercise)

// define the required variables
let numbers = 0;   // how many numbers were entered (loop counter)
let sum = 0;       // the running total
let average = 0;   // the result

// take input from the user
let user_input = parseInt(prompt("Please enter a number: (negativ number stops input)"));

// do a while loop to run until the user input is < 0
while (user_input >= 0) {

  // add all positive numbers
  sum = sum + user_input;

  // increase loop counter
  numbers = numbers + 1;

  // take input again if the number is positive (inside while loop)
  user_input = parseInt(prompt("Please enter a number:"));

// end of loop
}

// calculate average
if (numbers > 0) {
  average = sum / numbers;
}

// output into console
console.log("Number of inputs: " , numbers, "Sum: ",sum, "Average: ", average);
console.log(`The sum of all inputs is: ${sum} !`);
console.log(`The average of all inputs is: ${average} !`);
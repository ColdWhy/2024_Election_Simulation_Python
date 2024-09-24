Requirements:
Python 3.x
tabulate library

How to run:
Run 2024 simulation.py to perform the simulation.
Optionally, run 2024 simulation logger.py to generate a log file of the results.

===================================================================================

This is a script that simulates the 2024 election using polling data and shows some averages and other probabilities.

It essentially focuses only on swing states. States deemed to be safe or likely are ignored, and their electoral votes are automatically handed to the candidate polling ahead.

In the end, it shows how many times each candidate won in all the simulations, how each state voted, and the Electoral College results.

It should be noted that this code transforms polling into the chance of a candidate winning. This is NOT AT ALL how odds work, and it's a TERRIBLE method. Under this logic, 
Trump has roughly a 30% chance of winning California, which is ridiculous. 
So why am I using this method? Well, even though it's useless for safe states, I think there's a case to be made for swing states, where the odds boil down to a toss-up 
and all polls are well within the margin of error. 
Pollsters have more sophisticated ways of determining the odds candidates have of winning a state, but I am not a pollster.

In each state election, a random number between 1 and 1000 is generated, and if it falls within a candidate's range, they receive that state's electoral votes. 
However, when you look at polling, you'll see that the percentages of candidates usually don't add up to 100%, so sometimes the random number may fall outside the range of 
either candidate. In this scenario, the program just tosses a coin and assigns the electoral votes to whichever candidate won the coin toss.

You can fiddle with the odds in each state and see how it affects the overall odds of either candidate winning. You may notice I commented on Wisconsin and Michigan 
with a line that would always give their electoral votes to the Democrats. This is because Harris is polling so far ahead in those states that I think her chances of 
winning are far greater than the percentages in the polls.

Don't take this as a prediction, but more as "this is what's likely to happen if the election took place TODAY." The opinions of undecided voters can change drastically 
in the span of a few months, and many people only inform themselves about the candidates in the weeks or days leading up to election day.

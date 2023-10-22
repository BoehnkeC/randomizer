# Random sets

#### How well are digits in a random set distributed? 

Consider the set `[012345]`, consisting of 6 digits. Each digit occurs once. This can be opposed with the set `[151718]`. The digit 1 occurs 3 times, lowering the randomization quality.

#### How unique are digits in a larger random set?

Consider the set `[012345, 123456, 234567]`. Although, most of the digits occur more than once, their position is shifted and the sets represent unique variations. Opposed to that is the set `[012345, 098765, 089765]`. Although, all the sets are intrisically unique, they share the same digits at the beginning and the end: 0 and 5. If we call the randomization function multiple times, repitition is expectable.

Execute `main.py` to create 10 million sets, consisting of 6 random digits.

![random_sets.png](images%2Frandom_sets.png)
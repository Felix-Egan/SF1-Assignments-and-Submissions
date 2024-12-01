# Mutation Testing Assignment
In this assignment, you need to upload mutant programs and solutions to one programming problem in Coding Cat. You will submit these files as part of another PR, and you will also need to review another student's work.

## Mutation Testing
Mutation testing is a technique used to evaluate the quality of software tests by intentionally introducing small errors (called mutations) into the program's code and checking whether the existing tests can detect these errors.

The idea is we want to create slightly buggy programs, so that when given a test suite, we find tests that work on correctly implemented code and the buggy implementations, as well as tests that only work on correct implementations.

## Task Overview
You need to create between 3 to 5 buggy implementations of your designated problem.

_________________________________________________________________________________________________________________________

# Example Problem: ordered_insert
Consider the problem ordered_insert, which is as follows:

    Write a function ordered_insert(lst, num) that takes two arguments:
    lst: A list of integers in ascending order.
    num: An integer to insert into the list.

    The function should return a new list with num inserted into the correct position so that the order is preserved.
    
Correct Implementation
    def ordered_insert(lst, num):
        '''
            Correct implementation
        '''
        for i in range(len(lst)):  # loop over the list
            if lst[i] > num:  # if we find an element of the list greater than num...
                lst.insert(i, num)  # we insert at this position
                return lst  # and return the list
        lst.append(num)  # if num is larger than all elements, add it at the end
        return lst
    
Buggy Implementations (Mutants)
Mutation 1: Change the Comparison Operator
    def mutation_1(lst, num):
        '''
            Simple mistake, change the comparison operator
        '''
        for i in range(len(lst)):
            if lst[i] < num:
                lst.insert(i, num)
                return lst
        return lst
    
Mutation 2: Insert at the Wrong Position (Off by One)
    def mutation_2(lst, num):
        '''
            Insert at the position (off by one)
        '''
        for i in range(len(lst)):
            if lst[i] > num:
                lst.insert(i + 1, num)  # Mutated to insert at an incorrect position
                return lst
        lst.append(num)
        return lst
    
Mutation 3: Incorrectly Modify the Loop Boundary
    def mutation_3(lst, num):
        '''
            Incorrectly modify loop boundary
        '''
        for i in range(len(lst)-1):  # Mutated loop limit
            if lst[i] > num:
                lst.insert(i, num)
                return lst
        lst.append(num)
        return lst
    
Mutation 4: Accidentally Use Wrong List Funtion
    def mutation_4(lst, num):
        '''
            Accidentally uses append instead of insert
        '''
        for i in range(len(lst)-1):
            if lst[i] > num:
                lst.append(num)  # Mutated: arguments swapped
                return lst
        lst.append(num)
        return lst
    
Mutation 5: Forgot a Return Statement
    def mutation_5(lst, num):
        '''
            Forgot a return statement
        '''
        for i in range(len(lst)-1):
            if lst[i] > num:
                lst.insert(i, num)
                return lst
        lst.append(num)
        # Missing return statement here
    
Specifications
Mutation testing (where users need to write comprehensive test suites) is an upcoming feature in Coding Cat. This gives future students a chance to practice writing test suites and thinking about testing more broadly.

However, for this feature to work, you need to follow closely these specifications:

You must write each mutation in its own file, named mutation_1.py, mutation_2.py, etc. Note that the functions in each file MUST be the same name as the name written in meta.json (and the same as the starter.py function name, solution.py function name, etc.). This is needed so Coding Cat knows how to call user code.
Mutation programs cannot crash tho!
For each mutation, please add a docstring with a simple description about why this mutation is buggy. This will eventually be shown to the user so they can confirm the bug they've found.
You must write a solution file as well, called solution.py. Again, this file must define a function with the same name in meta.json.
You must submit one PR with all these file changes. See the PR instructions from assignment 3 to refresh yourself on the process of creating a PR
Reviewing Your Partner's Submission
Like Assignment 3 when you made a problem, you will also have to review your partner's submission. Please check that they follow the instructions precisely and that they capture sufficiently subtle and common mutants.

Students who make PRs with mistakes in the specifications will lose points. Reviewers who fail to identify these errors will lose more points since your job is to verify your partner's work. I want everyone to get a 100 on this assignment, since that means the code works and we can add this feature without fixing additional errors.
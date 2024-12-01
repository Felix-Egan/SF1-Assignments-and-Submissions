# Coding Bat Question.py

def flatten_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

print(flatten_list(input('list:')))


# [
#     {
#         "input": [[1, [2, [[[3]]], [4, 5]], 6]],
#         "output": [1, 2, 3, 4, 5, 6]
#     },
#     {
#         "input": [[1, [2, [{"wait":"a second", "this":"is", "a":"Dictionary"}, [4, [5]]]]]],
#         "output": [1, 2, {"wait":"a second", "this":"is", "a":"Dictionary"}, 4, 5]
#     },
#     {
#         "input": [[1, [2, 3], {"Dictionary-ception":{"Dictionary":"Inside", "Another":"Dictionary"}}, [[[[4]]]]]],
#         "output": [1, 2, 3, {"Dictionary-ception":{"Dictionary":"Inside", "Another":"Dictionary"}}, 4]
#     },
#     {
#         "input": [[1, "a", [2, "b", [3, "c"]]]],
#         "output": [1, "a", 2, "b", 3, "c"]
#     },
#     {
#         "input": [[]],
#         "output": []
#     },
#     {
#         "input": [[{}]],
#         "output": [{}]
#     },
#     {
#         "input": [[[[[[{}, {}], {}], {}], {}], {}]],
#         "output": [{}, {}, {}, {}, {}, {}]
#     },
#     {
#         "input": [[[[[[[[[[[10], 9], 8], 7], 6], 5], 4], 3], 2], 1]],
#         "output": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#     },
#     {
#         "input": [["[", ["]", ["[", ["]", ["[", ["]", ["[", ["]", ["[", ["]"]]]]]]]]]]],
#         "output": ["[", "]", "[", "]", "[", "]", "[", "]", "[", "]"]
#     }
# ]




{
  "title": "Flatten List",
  "name": "flatten_list",
  "difficulty": "hard",
  "author": "Felix Egan",
  "category": "list-3"
}

# Description in Markdown format
"""
Title: Flatten List

Description:
Write a recursive function `flatten_list` that takes a nested list of arbitrary depth and returns a flattened list. The function should handle lists that contain other lists, integers, and/or other data types.

EXAMPLES:

Input: `[1, [2, 3, [4, 5]], 6]`
Output: `[1, 2, 3, 4, 5, 6]`

Input: `[1, "a", [2, "b", [3, "c"]]]`
Output: `[1, "a", 2, "b", 3, "c"]`
"""

# starter.py
"""
def flatten_list(lst) -> list:

"""
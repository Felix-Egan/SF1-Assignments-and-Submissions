if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        command_input = input().split()
        command = command_input[0]
        args = command_input[1:]
        if command == "print": print(lst)
        else:
            args_str = ', '.join(args)
            eval(f'lst.{command}({args_str})')     



def foo():
    print("function foo from module a")


def do_bar():
    import module_b
    module_b.bar()

do_bar()


if __name__ == '__main__':
    foo()

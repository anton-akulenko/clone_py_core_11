


def bar():
    print("function bar from module b")

def do_foo():
    import module_a
    module_a.foo()

do_foo()

if __name__ == '__main__':
    bar()

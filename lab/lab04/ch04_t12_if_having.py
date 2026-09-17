def using_control_once() -> str:
    if 2 < 10:
        return "Success #1"


def using_control_again() -> str:
    if not False:
        return "Success #2"


print(using_control_once())
print(using_control_again())

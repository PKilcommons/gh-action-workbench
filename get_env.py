import os


def main():
    env = os.getenv("HIVO_CI_OCI_TAG")
    print(env)
    print(repr(env))


main()

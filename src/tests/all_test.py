# Main test file. Must contain run of all other tests.
import os


def run_test_in_dir(dir: str):
    for name, type, _, _ in os.ilistdir(dir):
        if type == 0x4000:
            run_test_in_dir(dir + "/" + name)

        if type == 0x8000 and name.split(".")[-1] == "py" and name[:5] == "test_":
            print("running test " + dir + "/" + name)
            exec(open(dir + "/" + name).read())


if __name__ == "__main__":
    print("+++start testing+++")
    run_test_in_dir(".")
    print("+++end testing+++")

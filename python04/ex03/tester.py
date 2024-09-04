from new_student import Student


def main():
    """
    Test for ex03 new_student
    """
    student = Student(name="Edward", surname="agle")
    print(student)
    # try:
    #     student = Student(name="Edward", surname="agle", id="toto")
    #     print(student)
    # except TypeError as e:
    #     print("TypeError:", e)


if __name__ == "__main__":
    main()

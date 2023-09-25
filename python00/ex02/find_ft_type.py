def all_thing_is_obj(object: any) -> int:
    typeObject = type(object)
    if typeObject is list:
        print("List :", typeObject)
    elif typeObject is tuple:
        print("Tuple :", typeObject)
    elif typeObject is set:
        print("Set :", typeObject)
    elif typeObject is dict:
        print("Dict :", typeObject)
    elif typeObject is str:
        print(object, "is in the kitche :", typeObject)
    else:
        print("Type not found")
    return 42

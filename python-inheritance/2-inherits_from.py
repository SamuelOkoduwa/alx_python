#!usr/bin/python3
"""
 a function that returns True if the object is an instance of a class that inherited
"""
def inherits_from(obj, a_class):
    """
    the classes of object's type that hierarchy
    """
    for class_in_hierarchy in object_classes:
        if class_in_hierarchy is a_class:
            return False
        if issubclass(class_in_hierarchy, a_class):
            return True
        
    return True


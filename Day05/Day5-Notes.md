'''
                                                                                  Day 5
                                                                                  ___ _

Dictionsries
____________

--> dict is the key : value pair seperated by ":" andkeys are unique .

--> the place of keys we have to use immutable datatypes .
eg:
 details={"name" : "bharat",1 : "number"}
 print(details)

Methods
_______
1. keys()

--> used to get all keys from the dictionary.
    syntax : var_name.keys()

eg:
details = {"name":"bharat"
           "age":21
           "gender":"male"}
           print(details.keys())

2. values()

--> used to get all the values from the dictionary.
    syntax : var_name.values()

    eg:
    details = {"name":"bharat"
           "age":21
           "gender":"male"}
           print(details.values())

3. items()

--> used to get key.value pair from the dictionary.
    syntax : var_name.items()

    eg:
     details = {"name":"bharat"
           "age":21
           "gender":"male"}
           print(details.items())

    accessing the elements using the keys.

4. clear()

--> if we use the clear() method the dictionary will be empty.

details={"name":"bharat"
           "age":21
           "gender":"male"}
        details.clear()
        print(details)

5. update()
--> it updates or replaces the old value  or add the new element if it doesnt exist of the key with the new value. 

 eg:
 details={"name":"bharat"
           "age":21
           "gender":"male"}
        details.update({"name": "reddy"})
        details.update({"mobile":6302145799"})
        print(details)

Sets
____

--> set is a collection of unordered elements that are seperatesd by "," .

--> set is mutable.

--> can remove duplicate value by itself.

eg:
 go={1,2,3,4}
 print(go)

Methods
_______

1. union()(|)

--> used to combine the elements from both sets.
    syntax : set1.union(set2)
eg:
 go={1,2,3,4}
 so={5,6,7,3,4}
 print(go|so)
 print(go.union(so))

2. intersection() &

--> common elements from both sides .
    syntax : set1.interaction(set2)


eg:
 go={1,2,3,4}
 so={5,6,7,3,4}
 print(go & so)
 print(go.intersection(so))

3. symmetric diffrence() ^

--> all different elements from both sets.
    syntax : set1.symmetric_difference(set2).

eg:
 go={1,2,3,4}
 so={5,6,7,3,4}
 print(go ^ so)
 print(go.symmetric_diffrence(so))

4. add()
--> used to add new elements into set.

eg:
 go={1,2,3,4}
 go.add(5)
 print(go)

5.remove()
--> to delete the elements from set. 

eg:
 go={1,2,3,4}
 go.remove(3)
 print(go)

6.discard()
--> discard also removes the elements but if the element is not exist in the set, it just prints the set into output.

eg:
 go={1,2,3,4}
 go.discard(3)
 print(go)


    
    

































                          


















        

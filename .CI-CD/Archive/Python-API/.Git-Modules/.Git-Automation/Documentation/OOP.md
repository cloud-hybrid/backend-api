## Programming Paradigms - OOP ##

OOP introduces two fundamental types of inheritance: implementation (class) inheritance and
interface inheritance.7 Implementation inheritance defines an object's implementation in terms of
another object's implementation. In contrast, interface inheritance enforces only object interface
compatibility regardless, of implementation.

Hierarchical state machines introduce a third type of inheritance that is equally fundamental. We
call this behavioral inheritance . To understand why hierarchy introduces inheritance and how it
works, consider an empty (or transparent) substate nested within an arbitrary superstate. If such a
substate becomes active it behaves in exactly the same way as its superstate, that is, it inherits
the superstate's entire behavior. This is analogous to a subclass which does not introduce any new
attributes or methods. An instance of such a subclass is indistinguishable from its superclass
because, again, everything is inherited exactly.

This property of HSMs is fundamental because it requires only the differences from the superstate's
behavior to be defined. One observes that all OO design principles (for example, the Liskov
Substitution Principle) hold in HSM designs because one deals with inheritance in yet another form.
The concept of behavioral inheritance describes the “is-a” (“is-in”) relationship between substates
and superstates and should not be confused with inheritance of entire state models

The analogy between SOP and OOP goes further. Class instantiation and finalization is similar to
entering and exiting a state. In both cases special methods are invoked: constructors and destructors
for objects, entry and exit actions for states. Even the order of invocation of these methods is
the same: constructors are invoked starting from most remote ancestor classes (destructors are
invoked in reverse order), and entry actions are invoked starting from the topmost superstate (exit
actions are invoked in reverse order).

A final similarity between OOP and SOP lies in the way they are most efficiently implemented. Although polymorphism can be implemented in many ways, virtually all C++ compilers implement it in the same way: by using function pointers grouped into virtual tables. In view of the deep analogy between SOP and OOP, it is therefore not surprising that arguably the most efficient implementation of HSMs is also based on function pointers grouped into states. These simple state objects define both behavior and hierarchy but are not specific to any particular instance of a state machine. The same holds for virtual functions, which are characteristics of the whole class rather than specific to any particular object instance. For this reason we observe that state objects could (and probably should) be placed in v-tables and be supported as a native language feature.

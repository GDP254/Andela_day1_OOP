# Andela_day1_OOP
Sample real world problem with object oriented programming concepts applied for solution

The code represents a model of a vehicle in an upcoming video game.

ALl vehicles inherit from this CLASS. An instance of a vehicle for example: suzuki is an OBJECT. A suzuki, being a vehicle would INHERIT all properties and behaviours of one. When a vehicle is on it will make a sound but this sound will vary from vehicle to vehicle. POLYMORPHISM would allow for this to occur e.g. a suzuki will sound different to a tesla. 

When calling on a specific instance of a vehicle to make a sound we would not want to deal with looking for the audio file to be played caching it and doing so. Instead we would just call a function to achieve the desired behaviour, ABSTRACTING the functionality for a more managable implementation.

Given this information each instance of a vehicle can be seen to be a unique colleciton of data and behaviours. Both this data and behaviour can be hidden or ENCAPSULATED so as to ensure a consistent and stable instance.  
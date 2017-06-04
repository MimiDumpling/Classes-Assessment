"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   	A) Abstraction: Keeps details in only necessary places. Allows for
		for predictability. Keeps from too much "noise" building up in code.
		For example, base classes that are non-functioning within themselves, but
		provide attributes to subclasses.
	B) Encapsulation: Keeps all relevant details together. Classes that don't 
		need certain details won't have those details encapsulated with them.
	C) Polymorphism: Provides flexibility within a hierarchy. Not all components
		of a super class will be inherited by all sub classes. So, the sub 
		classes will take only attributes they need and not all attributes provided
		by the super class.


2. What is a class?
	A class is a part of object-oriented programming. A class is a type. For example,
	strings and lists are types of classes. A hierarchy of animals is similar to classes.
	For example, "Cat" is a subclass of the class "Mammal" which is a subclass of the 
	class "Animal."
		Example)
				# this is a super class named Animal. It takes objects.
				class Animal(object):
					# class attributes go here

				# this is a class named Mammal. It subclasses Animal.
				class Mammal(Animal):
					# class attributes go here
					# can inherit from Animal class

				# this is a class named Cat. It subclasses Mammal.
				class Cat(Mammal):
					# class attributes go here
					# can inherit from Mammal.


3. What is an instance attribute?
	After instantiation of a class (Ex. kitty = Animal()), instance attributes can be
	added (Ex. kitty.name = "Snowball"). An instance attribute can override a class 
	attribute. 
		Example)
				class Shirt(object):
					# class attribute
					style = "long-sleeved"

				# instantiation
				>>> short_sleeved = Shirt()

				# instance attribute overrides class attribute
				>>> short_sleeved.style = "short_sleeved"


4. What is a method?
	A method is similar to a function but it's defined inside of a class. They always
	have atleast one parameter called self and can refer to attributes.
		Example)
				class Shirt(object):
					style = "long-sleeved"

					# this is a method that announces if the shirt buttons
					def buttoned(self):
						return "Hi! I am a {style} shirt and I button".format(
							style)


5. What is an instance in object orientation?
	An instance in object orientation is when a class is called to make an instance
	of the class. This is called instantiation.
		Example)
				# creates a class called Shirt.
				class Shirt(object):
					# class attribute
					style = "long-sleeved"

				# instantiation creates an instance of Shirt called "short_sleeved"
				>>> short_sleeved = Shirt()


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   	A class attribute is defined within a class. An instance attribute can be made
   	outside of a class. An instance attribute can override a class attribute.
   		Example)
				class Shirt(object):
					# class attribute
					style = "long-sleeved"

				# instantiation
				>>> short_sleeved = Shirt()

				# instance attribute overrides class attribute
				>>> short_sleeved.style = "short_sleeved"

"""


# Parts 2 through 5:
# Create your classes and class methods

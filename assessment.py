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

class Student(object):
    """A base class for student information."""

    def __init__(self, first_name, last_name, address):
        """To do on instantiation."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class QuestionMixin(object):
    """A base class for questions on exams."""

    def __init__(self, question, correct_answer):
        """To do on instantiation."""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self, question):
        """Prints question to console and prompts user for answer"""

        user_answer = raw_input("{question} > ".format(question))
        
        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(QuestionMixin, object):
    """A base class for creating exams."""

    def __init__(self, name):
        """To do on instantiation."""
        self.name = name
        questions = []

    def add_question(self, question):
        """adds questions to Exam's list of questions"""
        
        # tried testing this. it isn't working...
        #QuestionMixin.__init__(question)

        # tried testing this. it isn't working...
        # NameError: global name 'questions' is not defined
        return questions.append(question)


    def administers(self):
        """ Administers the exam questions and returns tally of correct answers."""

        questions = get_questions()

        score = 0

        for question in questions:

            answer = ask_and_evaluate(question)

            if answer == True:
                score += 1
            else:
                score += 0

        number_of_questions = len(questions)
        final_score = float(score/number_of_questions)

        return final_score


class StudentExam(Student, QuestionMixin, Exam, object):
    """Stores a student's info, administers an exam, returns student's score for exam."""

    def __init__(self):
        """To do on instantiation."""
        # not sure what to put in here

    def take_test(self):
        """administers exam and assigns score."""

        # not sure if this is how to do this
        final_score = Exam.administers(self)

        print "Your score is: {final_score}.".format(final_score)


def example():
    """creates exam, adds questions to exam, creates student, administers exam"""

    # maybe this is a start?
    # exam = take_test()
    # student = Student()
    # questions = exam.add_question()

    # student_exam = StudentExam(student, exam)

    # take_test()


class Quiz(object):
    """gives student questions, return pass/fail based on score """

    # create an exam, but when scoring, if scores lower than 50% return fail
    # if scores are atleast 50%, return pass


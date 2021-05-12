# Interface Segragation Principle

"""
The Interface Segregation Principle states that “No client should be forced to depend on methods it does not use”.

Let’s say we are designing an application for different communication devices. 
We identify that a communication device is a device that would have one or many of these features – 
a) to make calls, 
b). send SMS and 
c). browse the Internet. 
So, we create an interface named CommunicationDevice and add the respective abstract methods for each of these features 
such that any implementing class would need to implement these methods.

Now say that we want to implement a traditional Landline phone. 
This also is a communication device, so we create a new class LandlinePhone using the same CommunicationDevice interface. 
This is exactly when we face the problem due to a large CommunicationDevice interface we created. In the class LanlinePhone, 
we implement the make_calls() method, 
but as we also inherit abstract methods send_sms() and browse_internet() we have to provide an implementation of these two abstract methods also in the LandlinePhone class 
even if these are not applicable to this class LandlinePhone. 
We can either throw an exception or just write pass in the implementation, but we still need to provide an implementation. 
"""

class CommunicationDevice:
    @abstractmethod
    def make_calls():
        pass

    @abstractmethod
    def send_sms():
        pass

    @abstractmethod
    def browse_internet():
        pass

class SmartPhone(CommunicationDevice):
    def make_calls():
        # implementation
        pass

    def make_calls():
        # implementation
        pass

    def browse_internet():
        # implementation
        pass

class LandlinePhoen(CommunicationDevice):
    def make_calls():
        # implementation
        pass

    def make_calls():
        # just pass or raise exception as this feature is not supported
        pass

    def browse_internet():
        # just pass or raise exception as this feature is not supported
        pass


"""
This can be corrected by following the Interface Segregation Principle as in the below example. 
Instead of creating a large interface, we create smaller role interfaces for each method. 
The respective classes would only use related interfaces. 
"""

from abc import ABCMeta, abstactmethod

class CallingDevice:
    @abstactmethod
    def make_calls():
        pass

class MessagingDevice:
    @abstactmethod
    def send_sms():
        pass

class InternetBrowsignDevice:
    @abstactmethod
    def browse_internet():
        pass

class SmartPhone(CallingDevice, MessagingDevice, InternetBrowsingDevice):
    def make_calls():
        # implementation
        pass

    def send_sms():
        # implementation
        pass

    def browse_internet():
        # implementation
        pass
    
class LandlinePhone(CallingDevice):
    def make_calls():
        # implementation
        pass
from contextlib import contextmanager


class just_some_exceptions():

    def __init__(self,elements):
        self.elements = elements

    def gimme(self,key):
        try:
            return self.elements[key]
        except (IndexError,KeyError):
            print(f"'{key}' nu exista ")
       
    def __enter__(self):
        return self

    def __exit__(self,_,__,___):
        del self.elements


with just_some_exceptions(['a','b']) as elements:
    elements.gimme(3)

@contextmanager
def just_some_exceptions(data):

    def gimme(key,elements=data):
        try:
            return elements[key]
        except (IndexError,KeyError):
            print(f"'{key}' nu exista ") 
    
    elements.gimme = gimme

    yield elements


with just_some_exceptions({}) as elements:
    elements.gimme(4)

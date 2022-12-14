from firebase import firebase
from abc import abstractclassmethod, ABC
from pprint import pprint


# abstractions
class AbstructPreson(ABC):
    def __init__(self, data):
        self._dump = data
        for name, value in data.items():
            setattr(self, name, value)
    
    @abstractclassmethod
    def get_all_values(self):
        pass
        
    @abstractclassmethod
    def push_dump(self, data):
        pass

    @abstractclassmethod
    def set_parameter(self, parameter_name, paramerter_value ):
        pass
    
    @abstractclassmethod
    def register_equivalent(self, person) -> int:
        pass
    
    @abstractclassmethod
    def signup_equivalent(self,person) -> int:
        pass

#realizations
class Person(AbstructPreson):
    def __init__(self, data):
        super().__init__(data)
    
    def push_dump(self, data : dict):
        self._dump = data
        for name, value in data.items():
            setattr(self, name, value)
    
    def set_parameter(self, parameter_name, paramerter_value ):
        setattr(self, parameter_name, paramerter_value)
    
    def get_all_values(self):
        return self._dump
    
    def register_equivalent(self, person : AbstructPreson):    
        if person.name == self.name:
            return 1
        
        elif person.email == self.email:
            return 2
        
        else:
            return 0

    def signup_equivalent(self, person : AbstructPreson) :
        if person.name != self.name and person.email != self.email:
            return 1
        
        elif person.password != self.password:
            return 2
        
        else:
            return 0


class AbstructRepository(ABC):
    def __init__(self, tocken : str=""):
        self.tocken = tocken
    
    @abstractclassmethod
    def write_person(self, person: Person):
        pass

    @abstractclassmethod
    def get_list_of_person(self):
        pass


class DataRepository(AbstructRepository):    
    default_user_directory = "\\Users"
    response_keys = []
    response_curent_user_id = ""
    
    
    def __init__(self, tocken = "https://animebase-5de39-default-rtdb.firebaseio.com"):
        super().__init__(tocken)
        self.base = firebase.FirebaseApplication(tocken, None)
        self.default_directory_name = tocken.split(".")[0].split('//')[1]

    def write_person(self, person):
        self.base.post(self.default_directory_name + self.default_user_directory, person.get_all_values())
        
    def get_list_of_person(self):
        self.response = self.base.get(self.default_directory_name + self.default_user_directory, '')
        self.response_keys = list(self.response.keys())
        return [Person(self.response[key]) for key,value in self.response.items()]

from  mlmodel.adapters.external_lib_adapter import lib_adapter
from mlmodel.core.history_data_interactor import HistoryDataInteractor

class validateinput:
    """
    class main in charge to validate data
    """
    @staticmethod
    def validate(lista:list):
        """
        function to validate values by pass list
        """
        print("Validate list of list")

        print("check if is a list")
        if not isinstance(lista, list):
            return False

        print("check if the sublist do not have 4 elementes")
        for sublist in lista:
            if not isinstance(sublist, list) or len(sublist) != 4:
                return False

            print("check if the elementes are not float")
            for item in sublist:
                if not (isinstance(item, float)):
                    return False
        return True



class mlflower:

    def __init__(self,list_data:list,name:str,save_data:bool) -> None:
        """
        load class to  validate data and adapter to connect at model
        """
        self._list_data=list_data
        self._lib_adapter=lib_adapter()
        self._checkdata=validateinput()
        self._save_data=save_data
        self._name = name
        self._history_data = HistoryDataInteractor()

    def save_register_data(self,data):
        """
        Save register data found using data recibe about ml
        """
        self._history_data.add_register(data=data, name=self._name)

    def exec_predictions(self):
        """
        Exec  prediction  using input values passing by init
        """
                
        validate_data = self._checkdata.validate(self._list_data)

        if(validate_data == False):
            raise ValueError("the payload data is wrong, please check it")
        
        response = self._lib_adapter.prediccions(value_inputs=self._list_data)

        if(self._save_data):
            self.save_register_data(response)
            

        
        return response

    
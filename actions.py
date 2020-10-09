# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class FormularioPedido(FormAction):
    def name(self):
        return "pedido_sushi"

    @staticmethod
    def required_slots(tracker):
       
        return["promocion_elegida", "modificaciones", "entrega_producto", "metodo_pago"]
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "promocion_elegida": [
                self.from_entity(entity="promocion_elegida"),
            ],
            "modificaciones": [
                self.from_text(intent="modificacion"),                
            ],
            "entrega_producto": [
                self.from_entity(entity="entrega_producto"),
                self.from_text(intent="destino"),
            ],
            "metodo_pago":[
                self.from_entity(entity="metodo_pago"),
            ],
        }

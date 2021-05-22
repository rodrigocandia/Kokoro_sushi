from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, logger, ConversationResumed
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class Formulario_Pedido(FormAction):
    def name(self):
        return "pedido_sushi"
    @staticmethod
    def required_slots(tracker):
        if tracker.get_slot("hacer_modificaciones")==True:
            return["promocion_elegida", "hacer_modificaciones", "modificaciones", "entrega_producto", "numero_telefono", "agregar_salsas","metodo_pago"]
        else:
            return["promocion_elegida", "hacer_modificaciones", "entrega_producto", "numero_telefono", "agregar_salsas", "metodo_pago"]
    
    def slot_mappings(self)-> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "promocion_elegida": [
                self.from_entity(entity="promocion_elegida"),
            ],
            "hacer_modificaciones": [ 
                self.from_intent(intent="verdadero", value=True),
                self.from_intent(intent="falso", value=False),                          
            ],
            "modificaciones": [
                self.from_text(intent="modificacion"), 
            ],
            "entrega_producto": [                
                self.from_text(intent="destino"),
                self.from_entity(entity="entrega_producto"),
            ],
            "numero_telefono":[
                self.from_text(intent="numero_telefono"),
            ],
            "agregar_salsas":[
                self.from_text(intent="agregar_salsas"),
            ],
            "metodo_pago":[
                self.from_entity(entity="metodo_pago"),
            ],
        }
    
    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker: Tracker,
        domain:Dict[Text, Any]) -> List[Dict]:
        return[]

class Formulario_Pizza(FormAction):
    def name(self):
        return "pedido_pizza"
    @staticmethod
    def required_slots(tracker):
        if tracker.get_slot("hacer_modificaciones")==True:
            return["promocion_elegida", "hacer_modificaciones", "modificaciones", "entrega_producto", "numero_telefono", "metodo_pago"]
        else:
            return["promocion_elegida", "hacer_modificaciones", "entrega_producto", "numero_telefono", "metodo_pago"]
    
    def slot_mappings(self)-> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "promocion_elegida": [
                self.from_entity(entity="promocion_elegida_pizza"),
            ],
            "hacer_modificaciones": [ 
                self.from_intent(intent="verdadero", value=True),
                self.from_intent(intent="falso", value=False),                          
            ],
            "modificaciones": [
                self.from_text(intent="modificacion"), 
            ],
            "entrega_producto": [                
                self.from_text(intent="destino"),
                self.from_entity(entity="entrega_producto"),
            ],
            "numero_telefono":[
                self.from_text(intent="numero_telefono"),
            ],
            "metodo_pago":[
                self.from_entity(entity="metodo_pago"),
            ],
        }
    
    def submit(
        self,
        dispatcher:CollectingDispatcher,
        tracker: Tracker,
        domain:Dict[Text, Any]) -> List[Dict]:
        return[]

class ActionPauseConversation(Action):
    """Pause a conversation"""

    def name(self):
        return "action_pause_conversation"

    async def run(self, dispatcher, tracker, domain) -> List[EventType]:
        logger.info(f"Pausing the conversation")

        return [ConversationPaused()]
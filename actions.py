# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType, ConversationPaused, logger, ConversationResumed
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class Formulario_Pedido(FormAction):
    def name(self):
        # horario_inicio = datetime.strptime("00:10:00", "%X").time()
        # horaio_salida = datetime.strptime("00:59:00", "%X").time()
        # hora_act = datetime.now().time()

        # if horaio_salida > horario_inicio:
        #     if hora_act > horario_inicio and hora_act < horaio_salida:
        #         return "pedido_final"
        #     else:
        #         dispatcher.utter_message(template="utter_greet")
        #         return []
        # else:
        #     if hora_act > horario_inicio or hora_act < horaio_salida:
        return "pedido_final"
            # else:
            #     dispatcher.utter_message(template="utter_greet")
            #     return []
        # return "pedido_final"
    @staticmethod
    def required_slots(tracker):
        if tracker.get_slot("hacer_modificaciones")==True:
            return["promocion_elegida", "hacer_modificaciones", "modificaciones", "entrega_producto", "metodo_pago"]
        else:
            return["promocion_elegida", "hacer_modificaciones", "entrega_producto", "metodo_pago"]
    
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

#class ActionResumeConversation(Action):

#    def name(self):
#        return "action_resume_conversation"

#    async def run(self, dispatcher, tracker, domain) -> List[EventType]:
#        logger.info(f"Resumed the conversation")
        
#        return [ConversationResumed()]

class ActionPauseConversation(Action):
    """Pause a conversation"""

    def name(self):
        return "action_pause_conversation"

    async def run(self, dispatcher, tracker, domain) -> List[EventType]:
        logger.info(f"Pausing the conversation")

        return [ConversationPaused()]
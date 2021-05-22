## en que puede ayudar el bot
* contribucion
  - utter_contribucion

## eliminar ingredientes
* eliminar_ingredientes
  - utter_eliminar_ingredientes

## fuera de alcance
* fuera_de_alcance
  - utter_fuera_de_alcance

## pedidos weones
* pedidos_locos
  - utter_pedidos_locos

## sushis veganos
* pregunta_sushi_veganos
  - utter_sushi_veganos

## saludar
* saludar
  - utter_greet

## sugerencia
* sugerencia
  - utter_sugerir

## say goodbye
* despedida
  - utter_goodbye

## say medios de pago
* medios_pago
  - utter_medios_pago

## preguntar por delivery
* entregas
  - utter_entregas

## horarios
* horario_atencion
  - utter_horarios

## bot challenge
* bot_challenge
  - utter_iamabot

## say_ubicacion_kokoro
* ubicados
  - utter_ubicados

## pedir pizza con saludo
* saludar
  - utter_greet
* pedir_pizza
  - utter_pedir_pizza
  - utter_pizza_kokoro
  - utter_pizza_Campestre

## pedir pizza
* pedir_pizza
  - utter_pedir_pizza
  - utter_pizza_kokoro
  - utter_pizza_Campestre

## historia buena pizza
* saludar
  - utter_greet
* pedir_pizza
  - utter_pedir_pizza
  - utter_pizza_kokoro
  - utter_pizza_Campestre
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia buena 3 pizza
* pedir_pizza
  - utter_pedir_pizza
  - utter_pizza_kokoro
  - utter_pizza_Campestre
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia buena 2 pizza
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 1 
* saludar
  - utter_greet
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* entregas
  - utter_entregas
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 2
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* pedidos_locos
  - utter_pedidos_locos
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 3
* saludar
  - utter_greet
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* medios_pago
  - utter_medios_pago
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 4
* seleccionar_pedido
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* ubicados
  - utter_ubicados
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 5
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* horario_atencion
  - utter_horarios
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 6
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* sugerencia
  - utter_sugerir
  - utter_continuar
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia para continuar
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* fuera_de_alcance
  - utter_continuacion
* confirmacion
  - pedido_pizza
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia pedido malo derivar persona
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
* inter_persona
  - utter_derivar_persona
  - action_pause_conversation
  - action_deactivate_form
  - form{"name":null}

## historia para volver a iniciar form
* seleccionar_pedido_pizza
  - pedido_pizza
  - form{"name":"pedido_pizza"}
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* negar
  - utter_reiniciar
  - action_restart
  - utter_nuevo_pedido
  - pedido_pizza
  - form{"name":"pedido_pizza"}
  - form{"name":null}
  - utter_slots_values_pizza
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

_______________________
## historia buena
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia_buena_directo_al_pedido
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia_buena_sin_saludo
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 1
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* entregas
  - utter_entregas
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 2
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* pedidos_locos
  - utter_pedidos_locos
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 3
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* medios_pago
  - utter_medios_pago
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 4
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* ubicados
  - utter_ubicados
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 5
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* horario_atencion
  - utter_horarios
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia con preguntas 6
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* sugerencia
  - utter_sugerir
  - utter_continuar
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia para continuar
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* fuera_de_alcance
  - utter_continuacion
* confirmacion
  - pedido_sushi
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

## historia pedido malo derivar persona
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
* inter_persona
  - utter_derivar_persona
  - action_pause_conversation
  - action_deactivate_form
  - form{"name":null}

## historia para volver a iniciar form
* saludar
  - utter_greet
* solicitar_pedido
  - utter_enviar_carta
  - utter_prom_2
  - utter_prom_3
  - utter_prom_4
  - utter_prom_fam
* seleccionar_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* negar
  - utter_reiniciar
  - action_restart
  - utter_nuevo_pedido
  - pedido_sushi
  - form{"name":"pedido_sushi"}
  - form{"name":null}
  - utter_slots_values
  - utter_confirmar_pedido
* confirmacion
  - utter_derivar_pedido
  - action_pause_conversation

# derivar persona
* inter_persona
  - utter_derivar_persona
  - action_pause_conversation

# pedir mas promociones
* mas_promociones
  - utter_mas_promociones
from ..model.mensajes_model import Mensaje
from flask import request, jsonify
class MensajesController:

    @classmethod
    def mostrar_mensaje(cls, mensaje_id):
        try:
            mensaje = Mensaje.obtener_mensaje_por_id(mensaje_id)

            if mensaje:
                mensaje_serializado = mensaje.serialize()
                return jsonify(mensaje_serializado), 200
            else:
                return {"mensaje": "Mensaje no encontrado"}, 404
        except Exception as e:
            print("Error en mostrar_mensaje:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    @classmethod
    def mostrar_mensajes_de_canal(cls, canal_id):
        try:
            # Consultar los mensajes del canal junto con la información del usuario
            mensajes = Mensaje.obtener_mensajes_de_canal(canal_id)
            
            # Si no hay mensajes en el canal, devolver un mensaje
            if not mensajes:
                return {"mensaje": "No hay mensajes en este canal"}, 200
            print(mensajes)
            # Serializar los mensajes y devolver la respuesta
            mensajes_serializados = [mensaje.serialize() for mensaje in mensajes]
            print("lo que retorna",mensajes_serializados)
            
            return jsonify(mensajes_serializados), 200
        except Exception as e:
            print("Error en mostrar_mensajes_de_canal:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    
    
    @classmethod
    def mostrar_mensajes_por_canal(cls, canal_id):
        try:
            mensajes = Mensaje.obtener_mensajes_por_canal(canal_id)
            mensajes_serializados = [mensaje.serialize() for mensaje in mensajes]
            return jsonify(mensajes_serializados), 200
        except Exception as e:
            print("Error en mostrar_mensajes_por_canal:", e)
            return {"mensaje": "Hubo un error en el servidor"}, 500

    # @classmethod
    # def crear_mensaje(cls):
    #     try:
    #         data = request.json

    #         mensaje = Mensaje(
    #             contenido=data.get('contenido', ''),
    #             id_usuario=data.get('id_usuario', None),
    #             id_canal=data.get('id_canal', None)
    #         )

    #         created_message = Mensaje.crear_mensaje(
    #             mensaje.contenido,
    #             mensaje.id_usuario,
    #             mensaje.id_canal
    #         )

    #         if created_message:
    #             return {'message': 'Mensaje creado con éxito'}, 201
    #         else:
    #             return {'message': 'No se pudo crear el mensaje'}, 500
    #     except Exception as e:
    #         print("Error en crear_mensaje:", e)
    #         return {'message': 'Hubo un error en el servidor'}, 500

    @classmethod
    def enviar_mensaje(cls):
        print("enviar_mensaje")
        data = request.json
        contenido = data.get('contenido')
        print("enviar_mensaje",contenido)
        id_usuario = data.get('id_usuario')
        print("enviar_mensaje", id_usuario)
        id_canal=data.get('id_canal')
        print("enviar_mensaje",id_canal)
        resul=Mensaje.crear_mensaje(contenido,id_usuario,id_canal)
        print(resul)
        if resul:
            return jsonify({'message': 'Mensaje enviado con éxito'}),200
        else:
            return jsonify({'message': 'Error al enviar el mensaje'}),500
    
    @classmethod
    def eliminar_mensaje(cls, mensaje_id):
        try:
            deleted_successfully = Mensaje.eliminar_mensaje(mensaje_id)

            if deleted_successfully:
                return {"message": "Mensaje eliminado correctamente"}, 204
            else:
                return {"message": "No se encontró el mensaje o hubo un problema al eliminarlo"}, 404
        except Exception as e:
            print("Error en eliminar_mensaje:", e)
            return {"message": "Hubo un error en el servidor"}, 500
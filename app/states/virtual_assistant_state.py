import reflex as rx
from typing import TypedDict
import asyncio


class Message(TypedDict):
    sender: str
    text: str


class VirtualAssistantState(rx.State):
    is_open: bool = False
    messages: list[Message] = []
    current_message: str = ""

    @rx.event
    def toggle_chat(self):
        self.is_open = not self.is_open
        if self.is_open and (not self.messages):
            self.messages = [
                {
                    "sender": "assistant",
                    "text": "Hello! How can I help you today? You can ask about services, pricing, or getting started.",
                }
            ]

    @rx.event
    async def send_message(self):
        if not self.current_message.strip():
            return
        user_message = self.current_message
        self.messages.append({"sender": "user", "text": user_message})
        self.current_message = ""
        yield
        await asyncio.sleep(1)
        response = self._get_bot_response(user_message)
        self.messages.append({"sender": "assistant", "text": response})

    def _get_bot_response(self, user_message: str) -> str:
        lower_message = user_message.lower()
        if "service" in lower_message:
            return "We offer Web Development, Graphic Design, and Digital Marketing. Check our services section for more!"
        elif "pricing" in lower_message or "plan" in lower_message:
            return "We have Basic, Medium, and Complete plans. You can see the details in the pricing section."
        elif "start" in lower_message or "tutorial" in lower_message:
            return "To get started, you can explore our tutorial page. It has videos and guides to help you out."
        elif (
            "miembros" in lower_message
            or "formulario" in lower_message
            or "análisis" in lower_message
        ):
            return "Claro, puedo ayudarte con eso. ¿Qué necesitas saber sobre la sección de miembros, el formulario o los análisis?"
        elif "hello" in lower_message or "hi" in lower_message:
            return "Hello there! How may I assist you?"
        else:
            return "I'm sorry, I don't understand that. Could you please rephrase? You can ask me about services, pricing, or our tutorial."
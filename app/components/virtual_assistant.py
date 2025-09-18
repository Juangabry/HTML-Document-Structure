import reflex as rx
from app.states.virtual_assistant_state import VirtualAssistantState


def chat_message(message: dict) -> rx.Component:
    is_user = message["sender"] == "user"
    return rx.el.div(
        rx.el.p(message["text"], class_name="text-sm"),
        class_name=rx.cond(
            is_user,
            "p-3 rounded-lg bg-blue-500 text-white self-end max-w-xs",
            "p-3 rounded-lg bg-gray-200 text-gray-800 self-start max-w-xs",
        ),
    )


def chat_window() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3("Virtual Assistant", class_name="font-bold text-lg text-gray-800"),
            rx.el.button(
                rx.icon("x", class_name="w-5 h-5"),
                on_click=VirtualAssistantState.toggle_chat,
                class_name="p-1 rounded-full hover:bg-gray-200",
            ),
            class_name="flex justify-between items-center p-4 border-b bg-white",
        ),
        rx.el.div(
            rx.foreach(VirtualAssistantState.messages, chat_message),
            class_name="flex-1 p-4 space-y-4 overflow-y-auto flex flex-col",
        ),
        rx.el.div(
            rx.el.input(
                placeholder="Type a message...",
                on_change=VirtualAssistantState.set_current_message,
                on_key_down=lambda e: rx.cond(
                    e == "Enter", VirtualAssistantState.send_message, rx.noop()
                ),
                class_name="flex-1 px-4 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500",
                default_value=VirtualAssistantState.current_message,
            ),
            rx.el.button(
                rx.icon("send", class_name="w-5 h-5"),
                on_click=VirtualAssistantState.send_message,
                class_name="p-3 rounded-full bg-blue-500 text-white hover:bg-blue-600 transition-colors",
            ),
            class_name="p-4 flex items-center gap-2 border-t bg-white",
        ),
        class_name="fixed bottom-24 right-5 w-80 h-[28rem] bg-gray-50 rounded-xl shadow-2xl border flex flex-col z-50",
    )


def virtual_assistant() -> rx.Component:
    return rx.el.div(
        rx.cond(VirtualAssistantState.is_open, chat_window()),
        rx.el.button(
            rx.icon(tag="message-circle", class_name="w-8 h-8"),
            on_click=VirtualAssistantState.toggle_chat,
            class_name="fixed bottom-5 right-5 p-4 bg-blue-500 text-white rounded-full shadow-lg hover:bg-blue-600 transition-transform hover:scale-110 z-50",
        ),
    )
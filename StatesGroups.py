from aiogram.dispatcher.filters.state import StatesGroup, State
class ClientStatesGroup(StatesGroup):
    name = State()
    desc = State()
    price = State()

class DeleteStatesGroup(StatesGroup):
    namee = State()
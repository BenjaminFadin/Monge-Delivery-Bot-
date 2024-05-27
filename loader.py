from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.postgresql import Database
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()


WEB_APP_URL = 'https://fadin.netlify.app/'

# engine = create_engine('postgresql://{}:{}@localhost:5432/{}'.format('postgres', 'Topson_2024', 'OrderEcommerseDB'))
# SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
# Base = declarative_base()




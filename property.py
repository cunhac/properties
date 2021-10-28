from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create import Lofts

engine = create_engine("sqlite:///loft_register.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()


def lofts_register(dic):
    #print(f'{dic["numbe"]}')
    #print(f'{dic["floor"]}')

    loft = Lofts(id=dic["id"], state=dic["state"], city=dic["city"], district=dic["district"],
                 address=dic["address"], number=float(dic["number"]), floor=float(dic["floor"]),
                 size_m2=float(dic["size_m2"]), garage=float(dic["garage"]), value=float(dic["value"]),
                 condominium=float(dic["condominium"]), iptu=float(dic["iptu"]), total_value=float(dic["total_value"]),
                 status=dic["status"])
    return loft








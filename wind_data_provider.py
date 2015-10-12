#coding=utf8
from WindPy import w
import datetime as DT

TODAY_DATE = DT.datetime.today().strftime(r'%Y-%m-%d')

class w_keeper:
    def __init__(self):
        w.start()

    def __del__(self):
        w.stop()

class WindProvider:
    W_KEEPER = w_keeper()

    def getLastPrice(self, code):
        rtn = w.wsq(str(code), "rt_latest")
        if rtn.ErrorCode == 0:
            return rtn.Data[0][0]
        return None

    def __getBaseInfo(self, code, info_type_str):
        rtn = w.wsd(code, info_type_str, TODAY_DATE, TODAY_DATE, "Fill=Previous")
        if rtn.ErrorCode == 0:
            return rtn.Data[0][0]
        return None

    def getOptionDirType(self, code):
        return self.__getBaseInfo(code, 'exe_mode')

    def getStrikePrice(self, code):
        return self.__getBaseInfo(code, 'exe_price')

    def getLastTradingDate(self, code):
        return self.__getBaseInfo(code, 'lasttradingdate')

    def getOptionRemainingDays(self, code):
        return self.__getBaseInfo(code, 'ptmday')


if __name__ == '__main__':
    indata = w.wsq("10000183.SH", "rt_latest")

    basedata = w.wsd("10000270.SH", """us_code,us_name,
                                    us_type,exe_mode,exe_type,exe_price,
                                    exe_ratio,ptmday,totaltm,startdate,
                                    lasttradingdate,exe_startdate,exe_enddate""",
                     TODAY_DATE, TODAY_DATE, "Fill=Previous")

    rtn = w.wsd("10000270.SH", "exe_ratio", TODAY_DATE, TODAY_DATE, "Fill=Previous")

    a = 1

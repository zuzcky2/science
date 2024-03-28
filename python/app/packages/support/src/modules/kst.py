from datetime import datetime
import pytz

class Kst(datetime):
    """
    한국 표준시(KST)를 사용하는 datetime 객체를 생성합니다.
    """

    def __new__(cls, *args, **kwargs):
        """
        새로운 Kst 객체를 생성합니다.

        Returns:
            Kst: 생성된 Kst 객체
        """
        timezone = pytz.timezone('Asia/Seoul')
        dt = datetime.now(tz=timezone)
        return super().__new__(cls, dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond,
                               tzinfo=timezone)

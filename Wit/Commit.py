from datetime import date


class Commit:
    def __init__(self,message):
        self._message = message
        self._hash_code = str(hash(message))[-6:]
        self._date = date.today()

    # def __str__(self):
    #     return f"hash code: {self._hash_code} \n message: {self._message} \n date: {self._date}"

    def to_dict(self):
        return {
            'message': self._message,
            'hash_code': self._hash_code,
            'date': str(self._date),
        }
    # @staticmethod
    # def from_dict(data):
    #     commit = Commit(data['message'])
    #     commit._hash_code = data['hash_code']
    #     commit._date = date.fromisoformat(data['date'])
    #     return commit
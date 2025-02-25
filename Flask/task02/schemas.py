from marshmallow import Schema, fields

class BookSchema(Schema):
    # id 필드는 dump_only=True 옵션이 설정되어 있습니다.
    # 이는 직렬화(서버 → 클라이언트) 시에만 포함되며,
    # 역직렬화(클라이언트 → 서버) 과정에서는 무시됨을 의미합니다.
    # 즉, 클라이언트에서 id 값을 입력할 수 없고, 서버가 관리합니다.
    id = fields.Int(dump_only=True)

    # title 필드는 문자열 타입이며, required=True로 지정되어 있습니다.
    # 이는 데이터를 역직렬화할 때 반드시 title 값을 제공해야 함을 의미합니다.
    title = fields.String(required=True)

    # author 필드도 문자열 타입이며, required=True 옵션이 설정되어 있습니다.
    # 따라서 데이터를 역직렬화할 때 author 값이 필수로 필요합니다.
    author = fields.String(required=True)

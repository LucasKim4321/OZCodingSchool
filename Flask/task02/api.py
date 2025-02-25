from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import BookSchema  # BookSchema: Marshmallow 스키마로, Book 데이터의 직렬화/역직렬화를 담당

# Blueprint 생성: URL 접두사와 설명을 지정합니다.
book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

# 전역 변수로 책 데이터를 저장하는 리스트를 선언합니다.
books = []

# '/' 엔드포인트에 대해 MethodView를 사용한 클래스 기반 뷰 정의 (전체 책 목록 조회 및 생성)
@book_blp.route('/')
class BookList(MethodView):
    # GET 메서드: 전체 책 목록을 반환합니다.
    @book_blp.response(200, BookSchema(many=True))
    def get(self):
        # books 리스트를 반환하면, BookSchema가 여러 항목(many=True)으로 직렬화함.
        return books

    # POST 메서드: 새로운 책 데이터를 생성합니다.
    @book_blp.arguments(BookSchema)
    @book_blp.response(201, BookSchema)
    def post(self, new_data):
        # 새로운 책의 id를 할당합니다.
        # 현재 저장된 책 수 + 1 을 id로 사용하여 자동 증가 효과를 냅니다.
        new_data['id'] = len(books) + 1
        
        # 새로운 책 데이터를 전역 books 리스트에 추가합니다.
        books.append(new_data)
        
        # 생성된 책 데이터를 반환합니다. HTTP 상태코드 201 (Created)로 응답.
        return new_data

# '/<int:book_id>' 엔드포인트에 대해 단일 책 데이터 조회, 수정, 삭제를 처리하는 클래스 기반 뷰 정의
@book_blp.route('/<int:book_id>')
class Book(MethodView):
    # GET 메서드: 특정 id의 책 정보를 조회합니다.
    @book_blp.response(200, BookSchema)
    def get(self, book_id):
        # books 리스트에서 해당 id를 가진 책을 찾습니다.
        book = next((book for book in books if book['id'] == book_id), None)
        
        # 책이 존재하지 않으면 404 에러 발생 (책을 찾지 못함)
        if book is None:
            abort(404, message="Book not found.")
        
        # 책 정보를 반환합니다.
        return book

    # PUT 메서드: 특정 id의 책 정보를 업데이트합니다.
    @book_blp.arguments(BookSchema)
    @book_blp.response(200, BookSchema)
    def put(self, new_data, book_id):
        # books 리스트에서 업데이트할 책을 찾습니다.
        book = next((book for book in books if book['id'] == book_id), None)
        
        # 찾지 못하면 404 에러 발생.
        if book is None:
            abort(404, message="Book not found.")
        
        # 기존 책 데이터에 새로운 데이터를 업데이트합니다.
        book.update(new_data)
        
        # 업데이트된 책 데이터를 반환합니다.
        return book

    # DELETE 메서드: 특정 id의 책 데이터를 삭제합니다.
    @book_blp.response(204)
    def delete(self, book_id):
        global books  # 전역 변수 books를 수정하기 위해 선언합니다.
        
        # 삭제할 책을 찾습니다.
        book = next((book for book in books if book['id'] == book_id), None)
        
        # 책을 찾지 못하면 404 에러 발생.
        if book is None:
            abort(404, message="Book not found.")
        
        # books 리스트에서 해당 id의 책을 제거합니다.
        books = [book for book in books if book['id'] != book_id]
        
        # 204 상태 코드는 'No Content'를 의미하며, 응답 본문은 비어있습니다.
        return ''

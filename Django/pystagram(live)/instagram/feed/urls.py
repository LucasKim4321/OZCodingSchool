

urlpatterns = [
]

#
# Feed API 설계
# - GET /posts/: 전체 게시물 조회(피드 보기)
# - POST /posts/: 게시물 생성
# - GET /posts/<int:post_id>/: 게시물 상세 조회
# - DELETE /posts/<int:post_id>/: 게시물 삭제
# - POST /posts/<int:post_id>/comments/: 댓글 작성
# - DELETE /comments/<int:comment_id>/: 댓글 삭제
# - POST /posts/<int:post_id>/likes/: 좋아요
# - DELETE /posts/<int:post_id>/likes/: 좋아요 취소
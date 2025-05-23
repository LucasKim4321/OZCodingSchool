# HTML(HyperText Markup Language)은 웹 페이지의 구조를 나타내는 마크업 언어입니다.

1. 웹 페이지의 구조는 HTML 요소(element)의 집합으로 이루어져 있습니다.
2. 요소는 여는 태그와 닫는 태그의 조합으로 이루어져 있습니다. 
    즉 여는 태그로 시작했다면, 반드시 닫는 태그로 닫아주어야 합니다. (몇 가지 예외는 존재 ex. input -> self closing tag)
<!-- 여는 태그 -->
<div>
<!-- 닫는 태그 -->
</div>

3. 여는 태그와 닫는 태그 사이에는 텍스트, 그리고 다른 요소를 포함시킬 수 있습니다.
<!-- 여는 태그와 닫는 태그 사이에 텍스트 넣기 -->
<div>여는 태그와 닫는 태그 사이에 이처럼 텍스트를 넣을 수 있습니다.</div>
<!-- 여는 태그와 닫는 태그 사이에 다른 요소 넣기 (자식 요소) -->
<div>
    <div></div>
    <div></div>
    <div></div>
</div>

<ul>
    <li>
        <div></div>
    </li>
    <li></li>
    <li></li>
    <li></li>
</ul>
<!-- 이때 감싸고 있는 요소를 부모 요소, 하위에 있는 요소를 자식 요소라고 부릅니다. -->
<!-- HTML이 계층 구조를 이루고 있다는 것을 이해하시면 됩니다. -->

<!-- HTML 요소의 종류는 매우 많습니다. 지금 당장 외우려고 하지 마세요. -->
<!-- 필요할 때 검색해서 사용하세요. -->

4. HTML 각 요소는 각기 사용할 수 있는 속성이 있습니다.
<!-- a요소는 href 속성을 사용해 연결할 링크를 지정할 수 있습니다. -->
<a href="https://ozcodingschool.com">오즈코딩스쿨</a>
<!-- img요소는 src 속성을 사용해 이미지의 경로를 입력합니다. -->
<img src="/IMG_7434.jpg">
<!-- HTML 요소의 속성도 다 외울 필요는 없습니다. -->

5. HTML 요소를 선택할 때는 선택자를 사용합니다.
<!-- id는 딱 하나만 지정 가능 -->
<div id="container">
<!-- #container -->

<!-- class는 여러 개의 요소를 지정할 수 있습니다. -->
<div class="child">
<div class="child">
<div class="child">
<div class="child">
<!-- .child -->

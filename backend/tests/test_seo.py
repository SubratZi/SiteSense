from auditor.seo import analyze_seo, SEOResult

def test_returns_seo_result():
    result = analyze_seo("<html></html>")
    assert isinstance(result,SEOResult)

def test_title_found():
    result = analyze_seo("<html><head><title>Hello World</title></head></html>")
    assert result.title == "Hello World"
    assert result.title_length == 11

def test_title_missing():
    result = analyze_seo("<html><head></head></html>")
    assert result.title is None
    assert result.title_length == 0

def test_title_empty_tag():
    result = analyze_seo("<html><head><title></title></head></html>")
    assert result.title is None

def test_meta_description_found():
    html= '<html><head><meta name="description" content = "A great page."></head></html>'
    result = analyze_seo(html)
    assert result.meta_description == "A great page."
    assert result.meta_description_length ==13

def test_meta_description_missing():
    result = analyze_seo("<html><head></head></html>")
    assert result.meta_description is None
    assert result.meta_description_length == 0

def test_meta_description_empty_content():
    html = '<html><head><meta name="description" content=""></head></html>'
    result = analyze_seo(html)
    assert result.meta_description is None

def test_meta_description_case_insensitive():
    html = '<html><head><meta name = "Description" content="Case test."></head></html>'
    result = analyze_seo(html)
    assert result.meta_description == "Case test."

def test_h1_count():
    html = "<html><body><h1>One</h1><h1>Two </h1></body></html>"
    result = analyze_seo(html)
    assert result.h1_count == 2

def test_h2_count():
    html = "<html><body><h2>A</h2><h2>B</h2><h2>C</h2></body></html>"
    result = analyze_seo(html)
    assert result.h2_count ==3

def test_no_headings():
    result= analyze_seo("<html><body><p>text</p></body></html>")
    assert result.h1_count == 0
    assert result.h2_count == 0

def test_word_count():
    html = "<html><body><p>one two three four five</p></body></html>"
    result = analyze_seo(html)
    assert result.word_count ==5

def test_word_count_strips_scripts():
    html = """
    <html><body>
        <p>real words here</p>
        <script>var x = 'not counted';</script>
        <style>.foo { color: red; } </style>
        </body></html>
        """
    result = analyze_seo(html)
    assert result.word_count ==3

def test_empty_html():
    result = analyze_seo("")
    assert result.title is None
    assert result.meta_description is None
    assert result.h1_count == 0
    assert result.word_count == 0
from auditor.images import analyze_images, ImageResult

def test_returns_image_result():
    result = analyze_images("<html></html>")
    assert isinstance(result, ImageResult)


def test_no_images():
    result = analyze_images("<html><body><p>Hello</p></body></html>")

    assert result.total_images == 0
    assert result.images_with_alt ==0 
    assert result.missing_alt == 0
    assert result.empty_alt == 0

def test_single_image_with_alt():
    html = '<img src="dog.jpg" alt="Dog">'
    result = analyze_images(html)

    assert result.total_images == 1
    assert result.images_with_alt ==1
    assert result.missing_alt ==0
    assert result.empty_alt ==0

def test_single_image_missing_alt():
    html = '<img src="dog.jpg">'

    result = analyze_images(html)

    assert result.total_images ==1
    assert result.images_with_alt ==0 
    assert result.missing_alt ==1
    assert result.empty_alt ==0

def test_single_image_empty_alt():
    html = '<img src="dog.jpg" alt ="">'

    result = analyze_images(html)

    assert result.total_images ==1
    assert result.images_with_alt ==0 
    assert result.missing_alt ==0
    assert result.empty_alt ==1

def test_whitespace_alt():
    html = '<img src="dog.jpg" alt="     ">'

    result = analyze_images(html)

    assert result.total_images ==1
    assert result.images_with_alt ==0 
    assert result.missing_alt ==0
    assert result.empty_alt ==1

def test_multiple_images():
    html = """
    <html>
        <body>
            <img src="1.jpg" alt="Dog">
            <img src="2.jpg">
            <img src="3.jpg" alt="">
            <img src="4.jpg" alt="Cat">
            <img src="5.jpg" alt="   ">
        </body>
    </html>
    """

    result = analyze_images(html)

    assert result.total_images ==5
    assert result.images_with_alt ==2 
    assert result.missing_alt ==1
    assert result.empty_alt ==2

def test_all_images_have_alt():
    html = """
    <img src="1.jpg" alt="One">
    <img src="2.jpg" alt="Two">
    <img src="3.jpg" alt="Three">
    """

    result = analyze_images(html)

    assert result.total_images == 3
    assert result.images_with_alt == 3
    assert result.missing_alt == 0
    assert result.empty_alt == 0

def test_all_images_missing_alt():
    html = """
    <img src="1.jpg">
    <img src="2.jpg">
    <img src="3.jpg">
    """

    result = analyze_images(html)

    assert result.total_images == 3
    assert result.images_with_alt == 0
    assert result.missing_alt == 3
    assert result.empty_alt == 0

def test_empty_html():
    result = analyze_images("")

    assert result.total_images == 0
    assert result.images_with_alt == 0
    assert result.missing_alt == 0
    assert result.empty_alt == 0
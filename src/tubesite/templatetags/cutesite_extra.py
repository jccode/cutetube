from django import template
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps as json_dumps

register = template.Library()


@register.filter
def duration(value):
    HOUR = 60 * 60
    h = None
    if value >= HOUR:
        h = value // HOUR
        value = value - HOUR
    (m, s) = (value // 60, value % 60)
    return "{}:{:02d}".format(m, s) if h is None else "{}:{:02d}:{:02d}".format(h, m, s)


@register.inclusion_tag('tubesite/_tags/pagination.html')
def pagination(paginator_list):
    """
    pagination
    ===========

    Definition:
    -------------
    number    (n)
    num_pages (np)

    Styles:
    --------
    s0:    <--  1   2   3   4   5   6    -->
    s1:    <--  1   2   3   4   5   6 ... 300 -->
    s2:    <--  1  ... 10  11  12  13  14  ... 300  -->
    s3:    <--  1  ... 295 296 297 298 299 300 -->

    Logic:
    -------
     style
      | np <= 7          = s0
      | np > 7
           | n <= 6      = s1
           | n > np - 6  = s3
           | otherwise   = s2

    :param paginator_list:
    :return:
    """
    num_pages = paginator_list.paginator.num_pages
    number = paginator_list.number

    if num_pages <= 7:
        page_indexes = range(1, num_pages + 1)
    else:
        if number <= 6:
            page_indexes = range(1, 7) + [0, num_pages]
        elif number > num_pages - 6:
            page_indexes = [1, 0] + range(num_pages - 5, num_pages + 1)
        else:
            page_indexes = [1, 0] + range(number - 2, number + 3) + [0, num_pages]
    return {"list": paginator_list, "page_indexes": page_indexes}



@register.filter
def json(data):
    """
    Safely JSON-encode an object.
    To protect against XSS attacks, HTML special characters (<, >, &) and unicode newlines
    are replaced by escaped unicode characters. Django does not escape these characters
    by default.
    Output of this method is not marked as HTML safe. If you use it inside an HTML
    attribute, it must be escaped like regular data:
    <div data-user="{{ data|json }}">
    If you use it inside a <script> tag, then the output does not need to be escaped,
    so you can mark it as safe:
    <script>
    var user = {{ data|json|safe }};
    </script>
    Escaped characters taken from Rails json_escape() helper:
    https://github.com/rails/rails/blob/v4.2.5/activesupport/lib/active_support/core_ext/string/output_safety.rb#L60-L113

    Refer: https://gist.github.com/amacneil/5af7cd0e934f5465b695
    """
    unsafe_chars = {
        '&': '\\u0026',
        '<': '\\u003c',
        '>': '\\u003e',
        '\u2028': '\\u2028',
        '\u2029': '\\u2029'}
    json_str = json_dumps(data, cls=DjangoJSONEncoder)

    for (c, d) in unsafe_chars.items():
        json_str = json_str.replace(c, d)

    return json_str

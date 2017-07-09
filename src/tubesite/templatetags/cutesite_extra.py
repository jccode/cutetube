from django import template


register = template.Library()


@register.filter
def duration(value):
    HOUR = 60 * 60
    h = None
    if value >= HOUR:
        h = value / HOUR
        value = value - HOUR
    (m, s) = (value / 60, value % 60)
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

#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html
    validation by checking whether every opening tag has a
    corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    tags = _extract_tags(html)
    if tags == []:
        if '<' in html or '>' in html:
            return False
        else:
            return True
    for i in range(len(tags)):
        if tags[i][1] != '/':
            stack.append(tags[i])
        else:
            if len(stack) == 0:
                return False
            if tags[i][1] == '/':
                if tags[i][2:-1] == stack[-1][1:-1]:
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False
    # HINT:
    # use the _extract_tags function below to generate a list of html
    # tags without any extra text;
    # then process these html tags using the balanced parentheses
    # algorithm from the class/book
    # the main difference between your code and the code from class will
    # be that you will have to keep track of not just the 3 types of
    # parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be
    used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the
    input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    output = []
    htmllist = html.split('<')
    # print(html.split('>')
    for i in range(len(htmllist)):
        if htmllist[i] == '':
            continue
        elif htmllist[i][-1] == '>':
            output.append('<' + htmllist[i])
        else:
            for j in range(len(htmllist[i])):
                if htmllist[i][j] == '>':
                    output.append('<' + htmllist[i][0:j + 1])
                else:
                    continue
            continue
    for i in range(len(output)):
        if '=' in output[i] or ' ' in output[i]:
            for j in range(len(output[i])):
                if output[i][j] == ' ':
                    output[i] = output[i][0:j] + '>'
                    break
    return output

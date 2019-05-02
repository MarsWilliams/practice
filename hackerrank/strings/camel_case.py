def camel_case(s: str) -> int:
    """
    Complete the camelcase function in the editor below. It must
    return the integer number of words in the input string.
    camelcase has the following parameter(s):
    s: the string to analyze
    Input Format
    A single line containing string s.
    Output Format
    Print the number of words in string s.
    """
    return sum(c.isupper() for c in s) + 1


print(camel_case('weHaveToGoHome'))

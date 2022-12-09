def solution(s):
    marked = {}
    answer = []
    for index, letter in enumerate(s):
        answer.append(index - marked[letter] if letter in marked else -1)
        marked[letter] = index
    return answer
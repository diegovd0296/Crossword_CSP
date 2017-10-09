

def modify_domain(domain,var,word,u_variables):


    for v in u_variables:
        if v[0][0] != var[0][0]:
            matches = set(var[1]) & set(v[1])

            for match in matches:
                new_domain = []
                if v[0] + "m" in domain:
                    [new_domain.append(w) for w in domain[v[0] + "m"] if
                     w[v[1].index(match)] == word[var[1].index(match)]]

                else:
                    [new_domain.append(w) for w in domain[str(len(v[1]))] if
                     w[v[1].index(match)] == word[var[1].index(match)]]

                domain[v[0] + "m"] = new_domain

    return domain

def check_restrictions(words,u_variables):
    """
    :param var: variable being analyzed
    :param a_variables: list of assigned variables
    :return: True if all restrictions are satisfied, False otherwise
    
    """


    # Find words that intersect with the variable that is being analyzed
    """
    for v in a_variables:
        if v[0][0][0] != var[0][0]:
            matches = list(set(var[1]) & set(v[0][1]))
            if matches:
                # Check that the current variable satisfies the restrictions
                for match in matches:
                    if v[1][v[0][1].index(match)] != var_value[var[1].index(match)]:
                        return False,map
    """
    for v in u_variables:
        if v[0] + "m" in words:
            if not words[v[0] + "m"]:
                return False

    return True


def Backtracking(a_variables,u_variables,words):
    """
    :param a_variables: list of tuples holding the name and absolute position of assigned variables
    :param u_variables: list of tuples holding the name and absolute position of unassigned variables
    :param words: dictionary with all the words to fill the crossword
    :param size: number of variables
    :return: 
    
    """
    domain_size = len(words)

    var = u_variables[-1]


    for word in words[str(len(var[1]))]:
        words = modify_domain(words,var, word,u_variables)
        if check_restrictions(words,u_variables):
            res = Backtracking(a_variables + [(var,word)],u_variables[:-1],words)
            if res != None:
                return res
        else:
            for i in range(len(words) - domain_size):
                words.popitem(-1)
            return None
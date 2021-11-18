import investpy

s_results = investpy.search_quotes(text='a', products=['stocks'], countries=['united states'], n_results=10)

s_res = map(lambda x :print(x), s_results)
list(s_res)

# print(s_results[0])

# len(s_results)
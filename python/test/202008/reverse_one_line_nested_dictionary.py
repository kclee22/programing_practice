from functools import reduce

def list_to_nested_dict(list0):
	return reduce(lambda x, y: {y:x}, list0)

def one_line_nested_dict_to_list(dict0):
	for k,v in dict0.items():
		stack = []
		stack.append(k)
		if not isinstance(v, dict):
			stack.append(v)
			return stack # End
		else:
			stack.extend(one_line_nested_dict_to_list(v)) # append v
		return stack

def answer(dict0):
    list0 = one_line_nested_dict_to_list(dict0)
    reversed_dict0 = list_to_nested_dict(list0)
    return reversed_dict0

if __name__ == '__main__':
    print(answer({'hired': {'be': {'to': {'deserve': 'I'}}}}))

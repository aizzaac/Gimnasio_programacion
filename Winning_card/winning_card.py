




import pytest

def winning_card(list_list):
  empty_list = []
  for sublist in list_list:
    for element in sublist:
      if element not in empty_list:
        empty_list.append(element)
      else:
        empty_list.remove(element)
  return -1 if not empty_list else max(empty_list)


class TestClass:
  def test_one(self):
    assert winning_card([[5,7,3,9,4,9,8,3,1], [1,2,2,4,4,1], [1,2,3]]) == 8, "La carta ganadora debe ser 8"
  def test_two(self):
    assert winning_card([[5, 5], [2, 2]]) == -1, "No hay carta ganadora, entonces -1"
unit_test = TestClass()

if __name__ == "__main__":
    pytest.main()

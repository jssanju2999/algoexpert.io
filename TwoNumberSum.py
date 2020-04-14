import unittest

def twoNumberSum(array, targetSum):
    array.sort()
	left=0
	right=len(array)-1
	while left<right:
		currSum=array[left]+array[right]
		if currSum==targetSum:
			return[array[left], array[right]]
		elif currSum<targetSum:
			left+=1
		elif currSum>targetSum:
			right-=1
    return[]

class TestProgram(unittest.TestCase):
    def test1(self):
        self.assertEqual(twoNumberSum([7, 2, 6, 4], 10), [4, 6])
    def test2(self):
        self.assertEqual(twoNumberSum([0, 0, 7, 20], 0), [0, 0])
    def test3(self):
        self.assertEqual(twoNumberSum([-1, 7, 8, 6], 6), [-1, 7])
    def test4(self):
        self.assertEqual(twoNumberSum([-5, -1, -4, -3, -2], -9), [-5, -4])
    def test5(self):
        self.assertEqual(twoNumberSum([7, 3], 10), [3, 7])

if __name__ == '__main__':
    unittest.main()
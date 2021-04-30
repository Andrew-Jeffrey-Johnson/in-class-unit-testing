import unittest
import calc

class testCaseAdd(unittest.TestCase):
	# Successful test
	def test_add(self):
		self.assertEqual(calc.add(5,4), 9)
	# Successful test
	def test_add_2(self):
		self.assertEqual(calc.add(10,2), 12)

	# Failed test
	def test_add_3(self):
		self.assertEqual(calc.add(1,1), 3)
	# Failed test
	def test_add_4(self):
		self.assertEqual(calc.add(5,8), 1)

	if __name__ == '__main__':
		unittest.main()

class testCaseSub(unittest.TestCase):
	# Successful test
	def test_sub(self):
		self.assertEqual(calc.sub(5,4), 1)
	# Successful test
	def test_sub_2(self):
		self.assertEqual(calc.sub(10,11), -1)

	# Failed test
	def test_sub_3(self):
		self.assertEqual(calc.sub(1,1), 3)
	# Failed test
	def test_sub_4(self):
		self.assertEqual(calc.sub(5,8), 1)

	if __name__ == '__main__':
		unittest.main()

class testCaseMul(unittest.TestCase):
	# Successful test
	def test_mul(self):
		self.assertEqual(calc.mul(5,4), 20)
	# Successful test
	def test_mul_2(self):
		self.assertEqual(calc.mul(10,2), 20)

	# Failed test
	def test_mul_3(self):
		self.assertEqual(calc.mul(1,1), 3)
	# Failed test
	def test_mul_4(self):
		self.assertEqual(calc.mul(5,8), 1)

	if __name__ == '__main__':
		unittest.main()

class testCaseDiv(unittest.TestCase):
	# Successful test
	def test_div(self):
		self.assertEqual(calc.div(5,4), 1.25)
	# Successful test
	def test_div_2(self):
		self.assertEqual(calc.div(10,5), 2)

	# Failed test
	def test_div_3(self):
		self.assertEqual(calc.div(1,1), 3)
	# Failed test
	def test_div_4(self):
		self.assertEqual(calc.div(5,8), 1)

	if __name__ == '__main__':
		unittest.main()
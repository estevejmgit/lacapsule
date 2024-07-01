const { addition, subtraction, multiplication } = require('./calc');

test('Addition - 5 + 6 = 11', () => {
  expect(addition(5, 6)).toBe(11);
});

test('Subtraction - 27 - 5 = 22', () => {
  expect(subtraction(27, 5)).toBe(22);
});


test('multiplication - 2 * 7  = 14', () => {
  expect(multiplication(2, 7)).toBe(144);
});

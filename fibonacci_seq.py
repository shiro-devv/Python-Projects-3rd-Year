class Result:
  def __init__(self, value=None, error=None):
    self.value, self.error = value, error

  def is_ok(self):
    return self.error is None

  def bind(self, fn):
    return self if not self.is_ok() else fn(self.value)

  def __repr__(self):
    if self.is_ok():
      return "Ok(" + str(self.value) + ")"
    return "Err(" + str(self.error) + ")"

class TailCall:
  def __init__(self, fn, *args):
    self.fn, self.args = fn, args


def tco(call):
  while isinstance(call, TailCall):
    call = call.fn(*call.args)
  return call


def fib_step(n, seq):
  if len(seq) >= n:
    return seq
  seq.append(seq[-1] + seq[-2])
  return TailCall(fib_step, n, seq)


def fib(n):
  if type(n) is not int:
    return Result(error="Sequence must be a number.")
  if n < 0:
    return Result(error="Sequence must be positive.")
  return Result(value=tco(TailCall(fib_step, n, [0, 1][:n])))


def read_input():
  try:
    return Result(value=int(input("Enter sequence: ")))
  except ValueError:
    return Result(error="Enter a valid number.")


if __name__ == "__main__":
  print(read_input().bind(fib))

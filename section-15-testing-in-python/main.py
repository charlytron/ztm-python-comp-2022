def bar_foo(num=0):
  try:
    if num:
      return int(num) + 5
    else:
      return 'please enter number, yo'
  except ValueError as err:
    return err
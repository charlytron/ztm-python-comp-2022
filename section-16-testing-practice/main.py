def do_things(num=0):
  try:
    if num:
      return int(num) + 5
    else:
      return 'Please use a number'
  except ValueError as err:
    return err
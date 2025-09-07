## CLI Eve

### Install package
```
pip install --editable .
```
The --editable option/flag omits the need to constantly uninstall and install the CLI for any updates to the ```cli()``` function

### (Optional) Uninstall if need (Already have eve downloaded)
```
pip uninstall eve
```

### Run Eve
```
eve
```
expected output:
```
Hello, world!
```

### Run Eve --name
Now with the adjustment there's a new --name option/flag, so you can replace the default case of 'world', with your or any name.
run the command:
```
eve --name Afsa
```
expected output:
```
Hello, Afsa!
```
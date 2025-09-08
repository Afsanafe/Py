## CLI Eve

### Install package
```
pip install -e .
```
or (these are the same commands)
```
pip install --editable .
```
The --editable/-e option/flag omits the need to constantly uninstall and install the CLI for any updates to the ```cli()``` function

### (Optional) Uninstall if need (Already have eve downloaded)
```
pip uninstall eve
```

### Run Eve
```
eve greet
```
expected output:
```
Hello, world!
```

### Run Eve --name
Now with the adjustment there's a new --name option/flag, so you can replace the default case of 'world', with your or any name.
run the command:
```
eve greet --name Afsa
```
expected output:
```
Hello, Afsa!
```

### New commands:
```
eve --config eve/.eve.yaml greet  
```

```
eve greet --name "ChatGPT" --no-shout
```

```
eve add --a 10 --b 4
```
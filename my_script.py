import subprocess
command = "reinvent -l sampling.log sampling.toml"
#command = "dir"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)
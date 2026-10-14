class log_operation:
    def __init__(self,filename,operation):
        self.filename = filename
        self.operation = operation 
    def __enter__(self):
        self.file =  open(self.filename, "a", encoding="utf-8")
        self.file.write(f"START {self.operation}\n")
        return self
    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.file.write(f"END {self.operation}\n")
        else:
            self.file.write(f"ERROR {self.operation}\n")
        self.file.close()
with log_operation("operation.log", "Data processing"):
    print("работа")

with log_operation("operation.log", "Data processing"):
    raise ValueError("сбой")
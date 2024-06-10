# wows_stats/conf/ReturnObj.py

class ReturnObj():
    def __init__(self, proc, obj):
        self.Process = str(proc)
        self.Fetched = len(obj)
        self.Success = 0
        self.Update = 0
        self.Exists = 0
        self.Error = 0

    def __str__(self):
        return f"{self.Process} Completed. Fetched: {self.Fetched}. Inserts: {self.Success}. Updates: {self.Update}. Exists: {self.Exists}. Errors: {self.Error}."

    def Merge(self, other):
        self.Fetched += other.Fetched 
        self.Success += other.Success
        self.Update += other.Update
        self.Exists += other.Exists
        self.Error += other.Error

    def Inc(self, ret):
        if ret == 'Success':
            self.Success += 1
        elif ret == 'Update':
            self.Update += 1
        elif ret == 'Exists':
            self.Exists += 1
        elif ret == 'Error':
            self.Error += 1
        elif ret == 'Fetched':
            self.Fetched += 1
class Information:
  def __init__(self,title,director,release,gener):
    self.title = title
    self.director = director
    self.release = release
    self.gener = gener
  def info(self):
    print(f"Movie name :{self.title}\nDirectore : {self.director}\nRelease : {self.release}\nGener : {self.gener}")
  def re(self):
    """ داله تغيير المخرج القديمه اللي عملتها انا"""
    if self.title == "Amirca":
      self.director = "u"
    elif self.title == "Sudan":
      self.director = "fuck"
    else:
      self.director = "wow"
  def udpat_dir(self,new_der):
    self.director = new_der

Movie1 = Information("Amirca","Isral",1830,"No hart")
Movie2 = Information("Sudan","Britsh",1956,"died")
Movie3 = Information("EA","Sony",2014,"Entertermant")
Movie1.info()
Movie2.info()
Movie3.info()
#تغيير المخرج
Movie1.udpat_dir("Omer chan")
Movie1.info()
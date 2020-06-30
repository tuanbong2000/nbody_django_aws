from django.db import models
import os
#from django.core.files import File
#from .create_data_output import create_output
#from .create_data_output import f

# Create your models here.
class Data(models.Model):
    title           = models.CharField(max_length=120) # max_length: required
    description     = models.TextField(blank=True, null=True)
    txt             = models.FileField(upload_to='data_files/', null=True)
    txt_info        = models.TextField(blank=True, null=True)
    
    def _str_(self):
        return self.title

    
    """
    def save(self):
        if self.txt != 0:
            # Open the file with read only permit
            #path_data = self.txt.url
            #path_data = "media/data_files/" + str(self.txt.open())
            f1 = open(path_data,'r')
            #f1 = open(self.txt.open(),'r')
            
            # The number of objects
            line = f1.readline()
            number_object=int(line[0])
#            self.txt_info =line+"\n"+ path_data+ "\n" + self.txt.url+ "\n"
            self.txt_info ="The number of objects: "+str(number_object)+"\n"
            
            #The initial time
            line = f1.readline()
            self.txt_info +="The initial time: "+line+"\n"

            for i in range(number_object):
                line = f1.readline()
                line_split=line.split()
                self.txt_info += "Planet %d: \t" %(i+1)
                self.txt_info += "m%d="%(i+1) +line_split[0]+"\t"
                self.txt_info += "p%d=("%(i+1) +line_split[1]+","+line_split[2]+","+line_split[3]+")""\t"
                self.txt_info += "v%d=("%(i+1) +line_split[4]+","+line_split[5]+","+line_split[6]+")""\n"
            
            #f1.close
            
            super().save()

def delete(self, *args, **kwargs):
        if self.txt != 0:
            self.txt.delete()
        super().delete(*args, **kwargs)

    

    def save(self):
        if self.txt != 0:
            
            # Open the file with read only permit
            #path_data_info= "/media/data_files/data_info.txt"
            f2 = open("media/data_files/data_info.txt","w")

            f2.write("hello")
            f2.close
            
            self.txt_info.save("data_info.txt", File(f2), save=True)
            
            
        super().save()




    def save(self):
        if self.txt != 0:
            
            # Open the file with read only permit
            #path_data_info= "/media/data_files/data_info.txt"
            f2 = open("media/data_files/data_info.txt","w")

            f2.write("hello")
            f2.close
            
            self.txt_info.save("data_info.txt", File(f2))
            self.save()
            
            
            super().save()

    def save(self):
        if self.txt != 0:
            
            # Open the file with read only permit
            path_data=self.txt.url
            path_data_info= "/media/data_files/data_info.txt"
            f1 = open('./'+path_data,'r')
            f2 = open(path_data_info,'w')

            # The number of objects
            line = f1.readline()
            number_object=int(line[0])
            f2.write("The number of object: "+str(number_object)+"\n")
            
            #The initial time
            line = f1.readline()
            f2.write("The initial time: "+line+"\n")
            
            for i in range(number_object):
                line = f1.readline()
                line_split=line.split()
                f2.write("Planet %d: \n" %(i+1))
                f2.write("m%d="%(i+1) +line_split[0]+"\n")
                f2.write("p%d=("%(i+1) +line_split[1]+","+line_split[2]+","+line_split[3]+")""\n")
                f2.write("v%d=("%(i+1) +line_split[4]+","+line_split[5]+","+line_split[6]+")""\n")
            
            f2.close
            f1.close
            
            self.txt_info.save(File(f2))
            
            
        super(Data, self).save()

    def create_data_info(self, *args, **kwargs):
        if args != 0:
            self.txt_info=args
        super(Data,self).create_data_info(*args, **kwargs)

    def create_data_output(self,commit=True):
        data = super(Data, self).save(commit=False)
        data.desciption = "abc" 

        if commit:
            data.save()
        return data
"""
    